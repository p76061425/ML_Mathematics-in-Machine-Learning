# <center> Mathematics in Machine Learning </center>
* __Naïve Bayes Classifier__
* __Bayesian Estimation__

## Usage

### naive_bayes_classifier.py
```sh
$ python3 naive_bayes_classifier.py [-h] 
```

| optional Options | Description |
| ---              | --- |
| -h --help       | show this help message and exit |
|  -mode MODE  | input mode train/test |
|  -k K_VALUE  | input k |


### bayesian_estimation.py
```sh
$ python3 bayesian_estimation.py [-h] 
```
| optional Options | Description |
| ---              | --- |
| -h --help       | show this help message and exit |
|  -mode MODE    | input mode 1/2 |
|  -p SIMULATOR_P | input Simulator p ,default=0.2 |

## Naïve Bayes Classifier
Use the IMDB dataset to predict that a comment is positive or negative. (The format of the dataset is shown in the following figure.) Try to use top-K (K=100, 1000, or 10000) frequent words to train the Naive Bayes Classifier and report the corresponding accuracy, precision, and recall for different K values.

![](https://i.imgur.com/Er98zxT.png) </br>
![](https://i.imgur.com/yji0MX4.png) </br>
![](https://i.imgur.com/DWuAfL2.png) </br>

---

## Bayesian Estimation
Assume ten coins with unknown but the same probability of head or tail are used for tossing. Each observation is composed of the tossing results of these ten coins. Let 𝑝 be the probability of tossing a head, and the probability of 𝒏 heads for the ten coins follows the binomial distribution</br>
![](https://i.imgur.com/BEyTvCH.png)

Assume the prior probability distribution of 𝑝 is discrete and 𝑝 can be one of 11 kinds of values, i.e. 0.0, 0.1, 0.2,..., 1.0. Each observation can be used to update the belief of 𝑝.

(1) Assume the distribution of the prior is
(a) [1/11, 1/11, ..., 1/11] 
(b) [0.01, 0.01, 0.05, 0.08, 0.15, 0.4, 0.15, 0.08, 0.05, 0.01, 0.01]
Write a code to draw the bar graph of prior, likelihood and posterior after an observation of ten coins with two heads and eight tails. Then print the estimation result of 𝑝 using MLE (Maximum likelihood Estimation) and MAP (Maximum a Posteriori Estimation) respectively

![](https://i.imgur.com/m3dpiIs.png)
![](https://i.imgur.com/9T7x9kB.png)
![](https://i.imgur.com/4kwotcG.png)
![](https://i.imgur.com/QTgo4jX.png)
![](https://i.imgur.com/dt6AJg5.png)
![](https://i.imgur.com/NvRM9GE.png)

(2) Write a simulator of tossing the ten coins 50 times. Visualize the posterior bar graph every 10 observations
 
![](https://i.imgur.com/JEaHbBH.png)
![](https://i.imgur.com/CCQuQOd.png)
![](https://i.imgur.com/RFH57mk.png)
![](https://i.imgur.com/M9dIndR.png)
![](https://i.imgur.com/QV4gjb4.png)
![](https://i.imgur.com/u51AFza.png)

Bonus: Draw the line graph of entropy of posterior and explain the trend of the curve

 ![](https://i.imgur.com/aqcqwNN.png)
可以看到隨著Observation變多，entropy的值也會隨著下降。


