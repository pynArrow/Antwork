# CNN

[TOC]

## 卷积神经网络简介

* 特点
  * 将大数据量的图片降维成小数据量
  * 有效保留图片特征
* 应用领域
  * 人脸识别、自动驾驶、无人安防
* CNN解决的问题
  * 图像的数据量太大，导致成本很高，效率很低
  * 图像在数字化的过程中容易丢失特征
  * （其实就对应了两个特点）

下面具体看一下这两个问题

### 数据量大

图像是由很多像素构成的，每个像素又是由颜色构成的。一张彩色图，每一个像素都有RGB（即光学三原色）三个通道，用于表示颜色信息。所以，对于一张常见的1000\*1000清晰度的图片，就会含有1000\*1000\*3个数值需要计算，这显然是一个庞大的数据。

**为了解决此问题，CNN将大量参数降维成少量参数。**

需要说明的是，降维并不会影响结果。就比如将一张图像在一定范围内缩小，图像的特征仍然不会改变。

### 保留图像特征

![图像简单数字化无法保留图像特征](https://easy-ai.oss-cn-shanghai.aliyuncs.com/2019-06-12-tuxiangtx.png)

如果简单地将图像的特征01化，即有圆形的地方为1，其余地方为0。则对于特征相近的图像（比如平移），则数字化的矩阵会有很大区别。

**为解决此问题，CNN用视觉的方式保留图像特征，即模仿人的肉眼去提取、存留特征。**

## 人的视觉原理

深度学习的理论研究，很大程度上是对人视觉的模仿。

**人类视觉如何运作？**

![人类视觉原理1](https://easy-ai.oss-cn-shanghai.aliyuncs.com/2019-06-24-rennao.png)

首先摄入原始信号（即各种颜色的像素点），然后提取不同物体间的分界，接着识别图像的抽象（如几何形状），最后判断物体。

**对应成图像处理的步骤：读取图像并数值化、提取图像边缘、提取图像特征、图像分类。**

所以一个图像处理的思路是：构造多层的神经网络，较低层提取初级的图像特征，较高层进一步细化，最终在顶层实现图像的分类。

## CNN基本原理

* CNN三个基本组成部分
  * 卷积层：提取图像局部特征
  * 池化层：数据降维
  * 全连接层：输出结果

### 卷积层 

核心部分是一个卷积核，滑窗处理。大致思路是用一个卷积核来过滤图像的各个区域，**得到这些小区域的特征值**。

![卷积层运算过程](https://easy-ai.oss-cn-shanghai.aliyuncs.com/2019-06-19-juanji.gif)

具体计算过程为对应项相乘然后相加。

![img](http://file.elecfans.com/web1/M00/4F/88/pIYBAFreggeAF2KAAACFvnN48lU184.png)

(32\*32\*3->28\*28\*1)

在具体应用中，往往有多个卷积核，可以认为，每个卷积核代表了一种图像模式，**如果某个图像块与此卷积核卷积出的值大，则认为此图像块十分接近于此卷积核。**如果我们设计了6个卷积核，可以理解：我们认为这个图像上有6种底层纹理模式，也就是我们用6中基础模式就能描绘出一副图像。比如说垂直边缘、水平边缘等。

![img](http://file.elecfans.com/web1/M00/4F/88/pIYBAFreggeABvFBAAB6mlf9lJs981.png)

如果使用6个卷积核提取，最终得到6个特征图，叠加在一起就得到了卷积层。

![img](http://file.elecfans.com/web1/M00/4F/88/pIYBAFreggiAC8-aAACAg54bzYo475.png)

同时可以对卷积层继续进行卷积操作。注意每一个卷积核的深度和上一层的输入相等。经过连续的卷积不断提炼出高层次的特征，一步步将特征浓缩，得到高层次特征，最终达到分类效果。

可以发现，其实卷积层已经将图像缩小了一圈（如果不加边框），但是效果并不明显。

**在了解卷积的大致过程后，还有一些细节部分需要思考。**

* 卷积核每次滑动的步长stride
  * 步长如果太大，比如大于卷积核的长度，则会遗漏一些像素点，导致特征损失。
  * 步长如果太小，比如为1，则效率太低。
* 卷积对每个像素点是否平权
  * 由于滑窗的交集部分是计算了多次的，所以边缘的像素点计算次数少于中间的像素点。所以可能会丢失一部分边缘信息。
  * 解决方法是在图像外围加一圈0（或多圈），使得在不影响特征的情况下，增加边缘像素点的计算次数。

![img](http://file.elecfans.com/web1/M00/4F/88/pIYBAFregguAQ1DbAABCJCgZwDM770.png)

* 由于卷积的过程是多次叠加的，所以需要计算卷积过程中每一次的输入图尺寸，来设计卷积核。

  $h_{out}=\frac{h_{in}-Filter+2Pad}{Stride}+1$

  $w_{out}=\frac{w_{in}-Filter+2Pad}{Stride}+1$

* 权值共享

  * 同一卷积过程中，filter内的值不变，即对于每一时刻滑窗对应的矩阵，各个位置的参数对于结果的权重保持一致。

**前向传播和反向传播**

- 前向传播即是卷积的操作。（输入->输出）

本质是用输入层和卷积核去求解卷积结果。$w[i]$表示第i个卷积核。

![img](http://file.elecfans.com/web1/M00/4F/89/pIYBAFregg2ATy5SAAEQUsv9WF8019.png)

- 反向传播

本质是已知卷积结果，去更新$w$的过程。

![img](http://file.elecfans.com/web1/M00/4F/89/pIYBAFregg2ADWUXAAFXiJnclVI362.png)

**提取边缘特征**

- 为什么中间的卷积核可以提取垂直边缘？

![](https://img-blog.csdn.net/20171127205434674?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvaWNlX2FjdG9y/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

在颜色相近的区域，矩阵内的值相近，卷积计算的结果小，表现为暗色；在颜色区别明显的区域（可以认为是边缘），卷积计算结果大，表现为白色。

- 垂直边界和水平边界

一个物体的边界可以看成由许多小的垂直边缘和水平边缘组成。

![这里写图片描述](https://img-blog.csdn.net/20171127211757163?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvaWNlX2FjdG9y/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

**偏差值和激活函数**

* 卷积计算后还需加入偏差$b$，计算出新矩阵放入激活函数（Relu、Softmax、logistic等），作为卷积层的输出结果。

### 池化层（下采样）

池化层可以大大降低数据的维度，也可以有效避免过拟合。如下图(20\*20->2\*2)

![池化层过程](https://easy-ai.oss-cn-shanghai.aliyuncs.com/2019-06-19-chihua.gif)

池化的大致过程：选取输入图中某个区域的**最大值或均值**来代替整个区域。在一幅图像中提取最大值可能意味着提取了某些特定特征，如垂直边缘等。

![img](http://file.elecfans.com/web1/M00/4F/89/pIYBAFregg6AcomFAABVu_xqDok934.png)

### 全连接层

经过卷积层和池化层降维过的数据，全连接层才能”跑得动”，不然数据量太大，计算成本高，效率低下。

![全连接层](https://easy-ai.oss-cn-shanghai.aliyuncs.com/2019-06-19-quanlianjie.png)

典型的 CNN 并非只是上面提到的3层结构，而是多层结构，例如 LeNet-5 的结构就如下图所示：

**卷积层 – 池化层- 卷积层 – 池化层 – 卷积层 – 全连接层**

![LeNet-5网络结构](https://easy-ai.oss-cn-shanghai.aliyuncs.com/2019-06-19-lenet.png)

![img](http://file.elecfans.com/web1/M00/4F/89/pIYBAFreggyAFTuVAAEZZ59r0Cs173.png)

也就是说卷积和池化重复出现，避免一次池化降维太快，导致特征损失。

reference:

[卷积神经网络 – CNN](https://easyai.tech/ai-definition/cnn/)、[一文让你彻底了解卷积神经网络](https://blog.csdn.net/weixin_42451919/article/details/81381294)

