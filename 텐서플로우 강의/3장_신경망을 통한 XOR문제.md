# 텐서플로우딥러닝_Deep Learning

## 신경망을 통한 XOR문제 ( neural nets for XOR)

### 1) XOR using NN

![](https://i.ytimg.com/vi/kNPGXgzxoHw/maxresdefault.jpg)



- XOR의 속성
  - x1과 x2가 서로 다를 때만 그 결과가 1이고, 나머지 경우에는 0의 결과값을 가짐
  - 그래프로 표현했을 때 결과값 1과 0에 대해서 하나의 직선으로 정확히 나눌 수가 없음



#### 1. One logistic regression unit cannot seperate XOR

> XOR 문제는 단순히 하나의 모델로는 풀이가 불가능하다
>
> => 여러 개를 합치게 되면 가능하다

``` python
#xor 게이트
import tensorflow as tf
import numpy as np

x_data = np.arrary([[0, 0], [0, 1], [1, 0], [1, 1]], dtype = np.float32)
y_data = np.arrary([[0], [1], [1], [0]], dtype = np.float32)

X = tf.placeholder(tf.float32)
Y = tf.placeholder(tf.float32)

W = tf.Variable(tf.random_norma([2, 1]), name = 'weight')
b = tf.Variable(tf.random_norma([1]), name = 'bias') #θ

#Hypothesis using sigmoid: tf.div(1., 1. + tf.exp(tf.matmul(X,W)))
hypothesis = tf.sigmoid(tf.matmul(X, W)- b)
#cost/loss function
cost = -tf.reduce_mean(Y * tf.log(hypothesis) + (1 - Y) * tf.log(1-hypothesis))
train = tf.train.GradienDescentOptimizer(learning_rate = 0.1).minimize(cost)

#Accuracy computation
# True if hypothesis > 0.2 else False
predicted = tf.cast(hypothesis >0.2 dtype = tf.float32)
accuracy = tf.reduce_mean(tf.cast(tf.equal(predicted, Y), dtype = tf.float32))

#Launch graph
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    for step in range(10001):
        sess.run(train, feed_dict={X: x_data, Y: y_data})
        if step % 500 == 0:
            print("step :",step, "\ncost :", sess.run(cost, 				  feed_dict={X: x_data, Y: y_data}), "\nWeight 					 : \n", sess.run(W), "\nbias: \n", 							  sess.run(b))
            h, c, a = sess.run([hypothesis, predicted, 						accuracy], feed_dict = {X: x_data, Y: y_data})
            print("Hypothesis:\n", h, "\nCorrect:\n", c, 
                 "\nAccuracy: ", a)
```



- 결과

  ![](C:\Users\jdb96\AppData\Roaming\Typora\typora-user-images\image-20200304002843119.png)

  > 10000번까지 실행을 해도 cost나 weight나 bias의 경우에는 변화가 없음
  >
  > => 결과가 변함이 없기 때문에 학습을 제대로 할 수 없음
  >
  > => 하나의 퍼셉트론으로는 불가능하다

#### 2. Multiple logistic regression units

- 하나의 모델이 아닌 2개, 3개, 다수의 모델을 이용하면 가능하다

![](C:\Users\jdb96\AppData\Roaming\Typora\typora-user-images\image-20200304003118767.png)



![](C:\Users\jdb96\AppData\Roaming\Typora\typora-user-images\image-20200304003739396.png)

=> 3개의 모델을 활용하여 XOR 문제 해결



#### 1) XOR data set

![](C:\Users\jdb96\AppData\Roaming\Typora\typora-user-images\image-20200304003904253.png)

Y_모형은 -OR gate

y1 모형은 And gate

y2 모형은 -OR gate

