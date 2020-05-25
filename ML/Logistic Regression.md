# Logistic Regression

## 简介

对数几率回归，也称为逻辑回归，虽然名为“回归”，但实际上是分类学习方法。

* **优点**

1. 不仅可以预测类别，还可以得到近似概率，对许多需要利用概率辅助决策的任务很有用。

2. 直接对分类可能性建模，无需考虑数据分布的问题。

3. 对率函数任意阶可导，有很好的数学性质

* **缺点**

1. 特征空间较大时，性能表现不好
2. 容易欠拟合，一般准确率不高
3. 只适用线性可分问题

## 基本原理

* **分类函数**

考虑二分类任务，输出类别标记为$\{0, 1\}$，要将线性回归模型产生的预测值$z$转换为0/1值，可以使用**单位越阶函数**，即

$$y = \begin{cases} 0 & \text{z<0} \\ 0.5& \text{z=0} \\ 1& \text{z>0} \end{cases}$$

但是单位越阶函数并非连续可微，因此不能作为**联系函数**。于是改用**对数几率函数**，也称**sigmoid函数**，即

$$y=\frac 1 {1+e^{-z}}$$

* **从概率的角度思考**

以sigmoid函数为联系函数带入到线性模型中，变化为

$$ln\frac y{1-y}=w^Tx+b$$

在这个模型中，将$y$视作样本分类为正的可能，则$1-y$为反例的可能，两者的比值即为**“几率”**，再取对数即为所谓对数几率。

故可将上式重写为

$$ln\frac{p(y=1|x)}{p(y=0|x)}=w^Tx+b$$

同时有$p(y=1|x)=\frac {e^{-(w^tx+b)}}{1+e^{-(w^tx+b)}}$、$p(y=0|x)=\frac {1}{1+e^{-(w^tx+b)}}$。

* **损失函数**

为了回归学习出参数$w$和$b$，需要选择合适的损失函数，先直接给出对数几率回归中使用的损失函数，即**对数损失**：

$$L=-[yln\hat y+(1-y)ln(1-\hat y)]$$

> 对数损失是从**最大似然函数**取对数导出的，最大似然函数即
>
> $$l(\theta)=\prod_{i=1}^mp(y=1|x_i)^{y_i}p(y=0|x_i)^{1-y_i}$$

当类别y取不同值的时候，此函数总是只有一项发挥作用，可以理解为分段函数：

![\begin{eqnarray}L=\begin{cases}-\log(\hat y), &y=1\cr -\log(1-\hat y), &y=0 \end{cases}\end{eqnarray}](https://www.zhihu.com/equation?tex=%5Cbegin%7Beqnarray%7DL%3D%5Cbegin%7Bcases%7D-%5Clog%28%5Chat+y%29%2C+%26y%3D1%5Ccr+-%5Clog%281-%5Chat+y%29%2C+%26y%3D0+%5Cend%7Bcases%7D%5Cend%7Beqnarray%7D)

而由于$\hat y$和$1-\hat y$的值均在0-1之间，故取对数后加负号，使结果为正。此时$\hat y$越接近1，损失函数越小。

* **梯度下降**

学习任务为：$(w^*, b^*)=argmin_{w,b}\ L$，用链式法则分别求$L$对$w$和$b$的导数，即

$$\frac{\partial L}{\partial w}=\frac{\partial L}{\partial \hat y}\frac{\partial \hat y}{\partial z}\frac{\partial z}{\partial w}=(\hat y-y)*x$$

$$\frac{\partial L}{\partial b}=\frac{\partial L}{\partial \hat y}\frac{\partial \hat y}{\partial z}\frac{\partial z}{\partial b}=\hat y-y$$

* **过拟合**

先上图，从左到右分别为欠拟合、适当拟合、过拟合。

![这里写图片描述](https://img-blog.csdn.net/20170409111252143?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvY29kZV9jYXE=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

可以使用**正则化方法**，对于容易过拟合的特征进行惩罚，即在损失函数中额外加上该特征的惩罚项：

![[公式]](https://www.zhihu.com/equation?tex=%5Ctilde%7BJ%7D%5Cleft%28+w%3BX%2Cy+%5Cright%29+%3DJ+%5Cleft%28+w%3BX%2Cy+%5Cright%29%2B%5Calpha%5COmega%5Cleft%28+w+%5Cright%29)



**reference**：

[对数几率回归（Logistic Regression）总结](https://blog.csdn.net/code_caq/article/details/69803476?ops_request_misc=%7B%22request%5Fid%22%3A%22158882313319724845048725%22%2C%22scm%22%3A%2220140713.130102334..%22%7D&request_id=158882313319724845048725&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~baidu_landing_v2~default-2)

[对数几率回归 —— Logistic Regression](https://blog.csdn.net/hellozhxy/article/details/80885899?ops_request_misc=&request_id=&biz_id=102&utm_medium=distribute.pc_search_result.none-task-blog-2~all~sobaiduweb~default-1)