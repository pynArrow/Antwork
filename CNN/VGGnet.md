# VGGNet——Visual Geometry Group

[TOC]

## 简介

2014年，牛津大学计算机视觉组和Google DeepMind公司的研究员一起研发出了新的深度卷积神经网络：VGGNet，并取得了ILSVRC2014比赛分类项目的第二名（第一名是GoogLeNet，也是同年提出的）和定位项目的第一名。

VGGNet可以看成是加深版的AlexNet，5层卷积层、3层全连接层、softmax层，层与层时间使用max-pooling，激活函数均为ReLU。

### 主要贡献

1. 使用多个小卷积核构成的卷积层代替较大的卷积层，两个3x3卷积核的堆叠相对于5x5卷积核的视野，三个3x3卷积核的堆叠相当于7x7卷积核的视野。一方面减少参数，另一方面相当于进行了更多的非线性映射，可以增加拟合能力。

   ![img](http://5b0988e595225.cdn.sohucs.com/images/20180105/b852b036ad6c4515ba57183e0e272bad.jpeg)

2. 小池化核，相较于AlexNet的的3x3的池化核，VGG全部采用2x2的池化核。

3. 更多的卷积核使特征图的通道数更多，特征提取更全面。第一层通道数为64，后面每层均翻倍，最多到512个通道。

4. 测试阶段不使用全连接层。而替换为三个卷积层，从而使得不再局限于固定尺寸的输入，可以接受任意宽或高。具体如下图。

![img](https://static.oschina.net/uploads/space/2018/0314/023015_rDZR_876354.png)

## 基本原理

### 预处理

每一个像素减去均值。

### 数据增强

VGGNet使用Multi-Scale的方法做数据增强，将原始图像缩放到不同尺寸S，然后再随机裁切224x224的图片，可以很好地扩充数据量，防止过拟合。

### 参数初始化

虽然网络的层数加深了，但是VGGNet比AlexNet收敛更快。这是因为VGGNet在特定的层使用了预训练的数据进行参数的初始化。

对于较浅的网络，则可以直接使用随机数随机初始化；对于较深的网络，则使用前面已经训练好的较浅网络中的参数值对前几层的卷积层和最后的全连接层进行初始化。

## 网络结构

### 整体架构

VGGNet的整体架构如图，六中网络结构使用不同数量的卷积核：

![img](https://static.oschina.net/uploads/space/2018/0314/023044_X49R_876354.png)

每种网络结构都延续了AlexNet的架构设计，5卷积层、3全连接层，区别就在于每一层所使用的卷积核数量、尺寸不同。根据层数的不同，又分别称作VGGNet16，VGGNet19等。值得一提的是，虽然网络从11层增加到19层，但是参数并没有很明显的增加，这是因为参数主要集中在全连接层。

以VGGNet16为例：

![img](https://static.oschina.net/uploads/space/2018/0314/023055_OLcQ_876354.png)

### 前五层卷积层

卷积层使用的卷积核均为3x3，stride为1，padding为1。池化层使用最大池化，size2x2，stride为2。

五层的卷积核数量：2$\rightarrow$2$\rightarrow$3$\rightarrow$3$\rightarrow$3。

卷积层深度：64$\rightarrow$128$\rightarrow$256$\rightarrow$512$\rightarrow$512。

特征图尺寸：224$\rightarrow$112$\rightarrow$56$\rightarrow$28$\rightarrow$14$\rightarrow$7。

### 后三层全连接层

同AlexNet。

![img](https://static.oschina.net/uploads/space/2018/0314/023111_GG9k_876354.png)

## 模型评估

论文作者对A、A-LRN、B、C、D、E共6种网络结构进行评估，错误率如下：

![img](https://static.oschina.net/uploads/space/2018/0314/023135_0OwO_876354.png)

简单分析表格：

1. 在总层数为11层时，LRN层并没有带来性能的提升，相反还使错误率提升了。
2. 随着网络层数的增加，分类的性能明显提升。而VGG19相较于VGG16提升并不明显，所以一般使用VGG16。

reference:

[大话CNN经典模型：VGGNet](https://my.oschina.net/u/876354/blog/1634322)