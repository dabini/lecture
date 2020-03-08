# 텐서플로우딥러닝_Deep Learning

## Tensorboard

### Droptout과 앙상블



#### 1) Overfitting

> 학습하고자 하는 학습데이터와 검증을 하고자 하는 valuation 데이터가 있을 때,  완벽하게 이를 나누는 hyperplane의 경우 overfitting이 나올 수 있음.

#### ![image-20200308195416935](C:\Users\jdb96\AppData\Roaming\Typora\typora-user-images\image-20200308195416935.png)

![image-20200308195652068](C:\Users\jdb96\AppData\Roaming\Typora\typora-user-images\image-20200308195652068.png)

​																				=> 너무나 학습을 과도하게 한 모습

#### 2) Overfitting in NN

![image-20200308195809574](C:\Users\jdb96\AppData\Roaming\Typora\typora-user-images\image-20200308195809574.png)

layer의 개수가 어느 이상으로 증가하게 되면 train error는 낮아지지만, test에러가 증가하게 됨.



#### 3) Solutions for overfitting

- 더 많은 학습 데이터
- Feature을 줄여주는 방법
  - 실제로 모형에 들어가는 변수의 개수를 10개에서 15개 내외로만 사용하고, 그 이상의 변수들을 사용하지 않음.
  - Neural network에서는 feature의 개수를 줄이는 것을 고려할 필요가 없음
- Regularization(정교화)



#### 4) Regularization

- weight을 너무 크게 주지 마라

  ![image-20200308200213671](C:\Users\jdb96\AppData\Roaming\Typora\typora-user-images\image-20200308200213671.png)

  상대적으로 w값이 커지면 하이퍼플랜이 더 복잡해짐.

![image-20200308200330075](C:\Users\jdb96\AppData\Roaming\Typora\typora-user-images\image-20200308200330075.png)

​	cost function의 값을 정교화의 strength만큼 높여주자..



#### 5) Dropout 

> A Simple Way to Prevent Neural Networks from Overfitting

Neural Network에서는 dropout이라는 방법 사용

![image-20200308200530346](C:\Users\jdb96\AppData\Roaming\Typora\typora-user-images\image-20200308200530346.png)

![image-20200308200622974](C:\Users\jdb96\AppData\Roaming\Typora\typora-user-images\image-20200308200622974.png)



#### 6) TensorFlow implementation

```python
Dropout_rate = tf.placeholder("float")
_L1 = etf.nn.relu(tf.add(Tf.matmul(X, W1), B1))
L1 = tf.nn.dropout(_L1, dropout_rate)

TRAIN:
    Sess.run(optimizer, feed_dict ={X:batch_xs, Y: batch_ys, dropout_rate: 0.5})

EVALUATION:
    Print"Accuracy", accuracy.eval({X:mnist.test.images, Y:batch_ys, mnist.test.labels, dropout_rate : 1 })
```

