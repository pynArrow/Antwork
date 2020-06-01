# 常见神经网络

简单学习、记录几种常见的神经网络。

## Perceptron感知机

- **感知机模型**

感知机学习旨在求出将训练数据进行线性划分的分离超平面，为此，导入基于误分类的损失函数，利用梯度下降法对损失函数进行极小化，求得感知机模型。输入特征向量，输出为实例的类别。

输入空间到输出空间对应如下函数：

$$f(x)=\begin{cases}1& \text{w*x+b>=0}\\-1& \text{w*x+b<0}\end{cases}$$

这里很容易看出**误分类数据**满足$y_i*(wx_i+b)<0$。所以误分类点到超平面S的总距离为：$$-\frac 1 {||w||}\Sigma y_i*(wx_i+b)$$

我们可以确定损失函数为：$L(w,b)=-\Sigma y_i*(wx_i+b)$。（$||w||$为定值）

在梯度下降极小化损失函数的过程中，随机选取一个误分类点，更新$w、b$，并迭代直到没有误分类点。损失函数的梯度：

![img](https://upload-images.jianshu.io/upload_images/4736919-905f6e79401da648.png-xyz?imageMogr2/auto-orient/strip|imageView2/2/w/272/format/webp)

$w、b$的更新：

![img](https://upload-images.jianshu.io/upload_images/4736919-1307c5fb001d9fe2.png-xyz?imageMogr2/auto-orient/strip|imageView2/2/w/202/format/webp)

需要注意的是当训练集线性不可分的时候，感知机不收敛，迭代结果会发生震荡，这时需要用到核函数。

## 误差逆传播算法

## RBF(Radial Basis Function)径向基函数

* **简介**

RBF是一种单隐层前馈神经网络，用**径向基函数**作为隐层神经元激活函数，而输出层则是对隐层神经元输出的线性组合。径向基函数是某种沿径向对称的标量函数，常用的有**高斯径向基函数**：

$$\rho(x, c_i)=e^{-\beta||x-c_i||^2}$$

其中$||x-c_i||$为欧式距离，相应的RBF网络可表示为：

$$\varphi(x)=\Sigma_{i=1}^mw_i\rho(x, c_i)$$

* **流程**

1. 确定神经元中心$c_i$，常用的方式包括随机采样、聚类等
2. 用BP（back propagation）算法等来确定参数$w_i$和$b_i$

## ART(Adaptive Resonance Theory)自适应谐振理论



## SOM(Self-Organizing Map)自组织映射

## Cascade-Correlation级联相关网络

## Elman网络

## Boltzmann机



**reference**：

《机器学习》——周志华