import numpy as np
import pickle
import argparse

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    
    parser.add_argument('-mode',
                        default="test",
                        dest='MODE',
                        help='input mode train/test')
    parser.add_argument('-k',
                        default="100",
                        dest='K_value',
                        help='input k')
                        
    args = parser.parse_args()

    mode = args.MODE
    
    K = int(args.K_value)
    
    print("K:",K,'\n')

    if(mode == "train"):
        
        x_train = np.load("imdb/x_train.npy")
        y_train = np.load("imdb/y_train.npy")
        train_size = len(x_train)
        #print("train_size:",train_size)
        
        TB = [[[0 for i in range(2)]for j in range(2)] for k in range(K+1)] 
       
        for article, label in zip(x_train, y_train):
            for k in range(1,K+1):
                TB[k][k in article][label]+=1
                # if(k in article):
                #     TB[k][1][label]+=1
                # else:
                #     TB[k][0][label]+=1
                    
        #print(TB,'\n')
        
        with open(str(K)+'table.pickle', 'wb') as Ktable_file:
            pickle.dump(TB,Ktable_file)
            
    else:        

        with open(str(K)+'table.pickle', 'rb') as Ktable_file:
            Ktable = pickle.load(Ktable_file)
                
        x_test = np.load("imdb/x_test.npy")
        y_test = np.load("imdb/y_test.npy")

        test_size = len(x_test)
        
        t_bad = [0 for i in range(K+1)]
        t_good = [0 for i in range(K+1)]
        t_Nappear = [0 for i in range(K+1)]
        t_appear = [0 for i in range(K+1)]
        
        for i in range(1,K+1):
            t_bad[i] = (Ktable[i][0][0] + Ktable[i][1][0] )/ test_size
            t_good[i] = (Ktable[i][0][1] + Ktable[i][1][1] )/ test_size
            t_Nappear[i] = (Ktable[i][0][0] + Ktable[i][0][1] )/ test_size
            t_appear[i] = (Ktable[i][1][0] + Ktable[i][1][1] )/ test_size
            
            Ktable[i][0][0] /= t_bad[i] * test_size
            Ktable[i][0][1] /= t_good[i] * test_size
            Ktable[i][1][0] /= t_bad[i] * test_size
            Ktable[i][1][1] /= t_good[i] * test_size
        
            #t_bad[i] /= test_size
            #t_good[i] /= test_size
            #t_Nappear[i] /= test_size
            #t_appear[i] /=  test_size
            
        pridict_y = [[0 for i in range (2)]for j in range(test_size)]
        pridict_label = [0 for i in range(test_size)]
        
        for i,articleTest in enumerate(x_test):
            neg_p = 1
            pos_p = 1
            for k in range(1,K+1):
                if(k in articleTest):
                    neg_p *= Ktable[k][1][0] / t_appear[k]
                    pos_p *= Ktable[k][1][1] / t_appear[k] 
                else:
                    neg_p *= Ktable[k][0][0] / t_Nappear[k]
                    pos_p *= Ktable[k][0][1] / t_Nappear[k] 
            neg_p *= 0.5
            pos_p *= 0.5
            pridict_y[i][0] = neg_p
            pridict_y[i][1] = pos_p
            if(neg_p > pos_p):
                pridict_label[i] = 0
            else:
                pridict_label[i] = 1

        TP = 0
        FP = 0
        TN = 0
        FN = 0
        for pridict,y in zip(pridict_label,y_test):
            if(pridict == y):
                if(pridict == 1):
                    TP += 1
                else:
                    TN += 1
            else:
                if(pridict == 1):
                    FP += 1
                else:
                    FN += 1

        accuracy = (TP+TN) / test_size
        precision = TP / (TP+FP)
        recall = TP / (TP+FN)
        
        print("TP:",TP)
        print("FP:",FP)
        print("TN:",TN)
        print("FN:",FN,'\n')
        
        print("accuracy",accuracy)
        print("precision",precision)
        print("recall",recall)
    
    
    
    
    
    
    
        
        
