import numpy as np
import argparse
from scipy.special import comb
import matplotlib.pyplot as plt 
import random
import math

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('-mode',
                        default="test",
                        dest='MODE',
                        help='input mode 1/2')
                        
    parser.add_argument('-p',
                        default="0.2",
                        dest='Simulator_P',
                        help='input Simulator p ,default=0.2 ')                        

    args = parser.parse_args()


    if(args.MODE == "1"):
        print("<3-1>\n")
        
        p = np.array( [i/10 for i in range(11)] )
        prior1 = np.array( [ 1/11 for i in range (11) ] )
        prior2 = np.array([ 0.01, 0.01, 0.05, 0.08, 0.15, 0.4, 0.15, 0.08, 0.05, 0.01, 0.01 ])
        likelihood = comb(10,2)* np.power(p,2)*np.power(1-p,8)
        posterior1 = likelihood * prior1 / (prior1 * likelihood).sum()
        posterior2 = likelihood * prior2 / (prior2 * likelihood).sum()
        
        print("likelihood:",likelihood)
        print("MLE: p = ",p[likelihood.argmax()],'\n')
        print("prior1:",prior1)
        print("posterior1:",posterior1)
        print("MAP: p = ",p[posterior1.argmax()],'\n')
        print("prior2:",prior2)
        print("posterior2:",posterior2)
        print("MAP: p = ",p[posterior2.argmax()],'\n')
        
        x = p
        
        y = prior1
        plt.bar(x, y, width = 0.08)
        plt.title('prior1')
        plt.xlabel('Prior probability distribution of p ')
        plt.ylabel('p')
        plt.show()
        
        y = prior2
        plt.bar(x, y, width = 0.08)
        plt.title('prior2')
        plt.xlabel('Prior probability distribution of p ')
        plt.ylabel('p')
        plt.show()
        
        y = likelihood
        plt.bar(x, y, width = 0.08)
        plt.title('Likelihood')
        plt.xlabel('Prior probability distribution of p ')
        plt.ylabel('Likelihood')
        plt.show()
        
        y = posterior1
        plt.bar(x, y, width = 0.08)
        plt.title('Prior1:')
        plt.xlabel('Prior probability distribution of p ')
        plt.ylabel('Posterior')
        plt.show()

        y = posterior2
        plt.bar(x, y, width = 0.08)
        plt.title('Prior2')
        plt.xlabel('Prior probability distribution of p ')
        plt.ylabel('Posterior')
        plt.show()

    elif(args.MODE == "2"):
        print("<3-2>\n")
        
        class Simulator():
            def __init__(self, p):
                self.p = p

            def tossing(self):
                pos_num = 0
                for i in range(10):
                    toss = random.random()
                    if(toss<=p):
                        coin = 1
                        pos_num += 1
                    else:
                        coin = 0
                        
                return pos_num
                
        p = float(args.Simulator_P)
        simulator = Simulator(p)
        
        round = 50
        check_point = 10
        
        p_distribution = np.array( [i/10 for i in range(11)] )
        prior = np.array( [ 1/11 for i in range (11) ] )
        posterior_list = []
        entropy_list = []
        likelihood = np.ones(11)
        for i in range(1,round+1):
            pos_num = simulator.tossing()
            likelihood *= comb(10,pos_num)* np.power(p_distribution,pos_num)*np.power(1-p_distribution,10-pos_num)            
            posterior = likelihood * prior / (prior * likelihood).sum()
            entropy = - (posterior * np.log2(posterior + 0.00000000000001)).sum()
            entropy_list.append(entropy)
            
            if(i%check_point == 0):
                posterior_list.append(list(posterior))
        
        #plot posterior_list
        for i in range( int(round/check_point) ):
            x = p_distribution
            y = posterior_list[i]
            plt.title('3-(2):Observation'+ str((i+1)*10)+ " Posterior")
            plt.xlabel('Prior probability distribution of p')
            plt.ylabel('Posterior')
            plt.bar(x, y, width = 0.08)    
            plt.show()

        #plot entropy
        x = [i for i in range(1,round+1)]
        y = entropy_list
        plt.title('Bonus:Entropy of posterior')
        plt.xlabel('Observations')
        plt.ylabel('Entropy')
        plt.plot(x, y)
        plt.show()
        #print(x,'\n',y)
      
    else:
        print("please input your mode,use -mode 1/2, 1=<3-1>, 2=<3-2>")
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    