# 텐서플로우딥러닝_Deep Learning

## 신경망을 통한 XOR문제 ( neural nets for XOR)_실습테스트

### 인공신경망 실습

#### 1) XOR data set

![](C:\Users\jdb96\AppData\Roaming\Typora\typora-user-images\image-20200304222946693.png)



```python
#xor 게이트
import tensorflow as tf
import numpy as np

x_data = np.arrary([[0, 0], [0, 1], [1, 0], [1, 1]], dtype = np.float32)
y_data = np.arrary([[0], [1], [1], [0]], dtype = np.float32)

X = tf.placeholder(tf.float32)
Y = tf.placeholder(tf.float32)

W1 = tf.Variable(tf.random_norma([2, 2]), name = 'weight1')
#두개가 들어가기 때문에 [2,2]
b1 = tf.Variable(tf.random_norma([2]), name = 'bias1') #θ
layer1 = tf.sigmoid(tf.matmul(X, W1) + b1)

W2 = tf.Variable(tf.random_norma([2, 1]), name = 'weight2')
b2 = tf.Variable(tf.random_norma([1]), name = 'bias2') #θ
hypothesis = tf.sigmoid(tf.matmul(layer1, W2)- b2)
#앞에서 가져왔던 layer1을 입력값으로 가져오기

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
    for step in range(10001):#만번 돌리기
        sess.run(train, feed_dict={X: x_data, Y: y_data})
        if step % 500 == 0:#500번마다 확인
            print("step :",step, "\ncost :", sess.run(cost, 				  feed_dict={X: x_data, Y: y_data}), "\nWeight 					 : \n", sess.run([W1, W2]), "\nbias: \n", 						sess.run([b1, b2]))
            h, c, a = sess.run([hypothesis, predicted, 						accuracy], feed_dict = {X: x_data, Y: y_data})
            print("Hypothesis:\n", h, "\nCorrect:\n", c, 
                 "\nAccuracy: ", a)
```



- 결과

<img src="C:\Users\jdb96\AppData\Roaming\Typora\typora-user-images\image-20200304223514144.png" style="zoom:200%;" />

correct에서 0 1 1 0 이 나와야하는데 1 1 1 1이 나왔기 때문에 Accuracy가 0.5임

![](C:\Users\jdb96\AppData\Roaming\Typora\typora-user-images\image-20200304223636587.png)

7000번 돌렸을 때  cost도 줄어들고 Accuracy도 증가

![image-20200304223704541](C:\Users\jdb96\AppData\Roaming\Typora\typora-user-images\image-20200304223704541.png)

10000번 돌렸을 때 cost값이 급격하게 줄어들었으며, Accuracy 100% 달성



#### 실습2

``` python
#XOR 게이트

#xor 게이트
import tensorflow as tf
import numpy as np

x_data = np.arrary([[0, 0], [0, 1], [1, 0], [1, 1]], dtype = np.float32)
y_data = np.arrary([[0], [1], [1], [0]], dtype = np.float32)

X = tf.placeholder(tf.float32)
Y = tf.placeholder(tf.float32)

W1 = tf.Variable(tf.random_norma([2, 7]), name = 'weight1')
#7개 퍼셉트론 [2,7]
b1 = tf.Variable(tf.random_norma([7]), name = 'bias1') #θ
layer1 = tf.sigmoid(tf.matmul(X, W1) + b1)

W2 = tf.Variable(tf.random_norma([7, 1]), name = 'weight2')
#7개 입력받고, 출력은 1개
b2 = tf.Variable(tf.random_norma([1]), name = 'bias2') #θ
hypothesis = tf.sigmoid(tf.matmul(layer1, W2)- b2)
#앞에서 가져왔던 layer1을 입력값으로 가져오기

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
    for step in range(10001):#만번 돌리기
        sess.run(train, feed_dict={X: x_data, Y: y_data})
        if step % 500 == 0:#500번마다 확인
            print("step :",step, "\ncost :", sess.run(cost, 				  feed_dict={X: x_data, Y: y_data}), "\nWeight 					 : \n", sess.run([W1, W2]), "\nbias: \n", 						sess.run([b1, b2]))
            h, c, a = sess.run([hypothesis, predicted, 						accuracy], feed_dict = {X: x_data, Y: y_data})
            print("Hypothesis:\n", h, "\nCorrect:\n", c, 
                 "\nAccuracy: ", a)
```

![image-20200304223958068](C:\Users\jdb96\AppData\Roaming\Typora\typora-user-images\image-20200304223958068.png)



![image-20200304224045668](D:\lecture\텐서플로우 강의\image-20200304224045668.png)

가중치 w1, w2 값이 7개씩 있음

layer1 역시 7개의 입력값

![image-20200304224147087](C:\Users\jdb96\AppData\Roaming\Typora\typora-user-images\image-20200304224147087.png)

![image-20200304224157910](C:\Users\jdb96\AppData\Roaming\Typora\typora-user-images\image-20200304224157910.png)

layer가 하나임에도 불구하고 그 안에 들어가든 히든 레이어가 많기 때문에 가능..



#### 실습 3

```python
#XOR 게이트

#xor 게이트
import tensorflow as tf
import numpy as np

x_data = np.arrary([[0, 0], [0, 1], [1, 0], [1, 1]], dtype = np.float32)
y_data = np.arrary([[0], [1], [1], [0]], dtype = np.float32)

X = tf.placeholder(tf.float32)
Y = tf.placeholder(tf.float32)

W1 = tf.Variable(tf.random_norma([2, 3]), name = 'weight1')
#입력값은 2개 모델은 3개
b1 = tf.Variable(tf.random_norma([3]), name = 'bias1') #θ
layer1 = tf.sigmoid(tf.matmul(X, W1) + b1)

W2 = tf.Variable(tf.random_norma([3, 3]), name = 'weight2')
#3개 입력받고, 출력은 3개
b2 = tf.Variable(tf.random_norma([3]), name = 'bias2') #θ
layer2 =  tf.sigmoid(tf.matmul(layer1, W2) + b2)

W3 = tf.Variable(tf.random_norma([3, 1]), name = 'weight3')
#3개 입력받고, 출력은 1개
b3 = tf.Variable(tf.random_norma([1]), name = 'bias3')
hypothesis = tf.sigmoid(tf.matmul(layer2, W3)+ b3)
#앞에서 가져왔던 layer1을 입력값으로 가져오기

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
    for step in range(10001):#만번 돌리기
        sess.run(train, feed_dict={X: x_data, Y: y_data})
        if step % 500 == 0:#500번마다 확인
            print("step :",step, "\ncost :", sess.run(cost, 				  feed_dict={X: x_data, Y: y_data}), "\nWeight 					 : \n", sess.run([W1, W2, W3]), "\nbias: \n", 						sess.run([b1, b2, b3]))
            h, c, a = sess.run([hypothesis, predicted, 						accuracy], feed_dict = {X: x_data, Y: y_data})
            print("Hypothesis:\n", h, "\nCorrect:\n", c, 
                 "\nAccuracy: ", a)
```

- 결과값

![image-20200304224511814](C:\Users\jdb96\AppData\Roaming\Typora\typora-user-images\image-20200304224511814.png)

 만 번을 돌렸을 때 cost가 아주 낮은 것을 확인할 수 있음.



#### Wide NN for XOR

- 두 개의 모델 사이의 연결선을 증가시킴

``` python
W1 = tf.Variable(tf.random_norma([2, 10]), name = 'weight1')
b1 = tf.Variable(tf.random_norma([10]), name = 'bias1')
layer1 = tf.sigmoid(tf.matmul(X, W1) + b1)

W2 = tf.Variable(tf.random_norma([10, 1]), name = 'weight2')
b2 = tf.Variable(tf.random_norma([1]), name = 'bias2')
hypothesis = tf.sigmoid(tf.matmul(layer1, W2)+ b2)
```



![image-20200304224904327](C:\Users\jdb96\AppData\Roaming\Typora\typora-user-images\image-20200304224904327.png)



#### Deep NN for XOR

- Layer를 더 깊게 만들어서 예측율을 높이는 또 다른 방법

![image-20200304224913300](C:\Users\jdb96\AppData\Roaming\Typora\typora-user-images\image-20200304224913300.png)

``` python
W1 = tf.Variable(tf.random_norma([2, 10]), name = 'weight1')
b1 = tf.Variable(tf.random_norma([10]), name = 'bias1')
layer1 = tf.sigmoid(tf.matmul(X, W1) + b1)

W2 = tf.Variable(tf.random_norma([10, 10]), name = 'weight2')
b2 = tf.Variable(tf.random_norma([10]), name = 'bias2')
layer2 = tf.sigmoid(tf.matmul(layer1, W2) + b2)

W3 = tf.Variable(tf.random_norma([10, 10]), name = 'weight3')
b3 = tf.Variable(tf.random_norma([10]), name = 'bias3')
layer3 = tf.sigmoid(tf.matmul(layer2, W3) + b3)

W4 = tf.Variable(tf.random_norma([10, 1]), name = 'weight4')
b4 = tf.Variable(tf.random_norma([1]), name = 'bias4')
hypothesis = tf.sigmoid(tf.matmul(layer3, W4)+ b4)
```

