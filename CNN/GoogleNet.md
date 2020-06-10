# GoogLeNet

之所以名为“GoogLeNet”而非“GoogleNet”，据说是为了向早期的LeNet致敬。

[TOC]

## 简介

GoogLeNet首次出现在ILVRC 2014的比赛中，以较大的优势获得当年第一名，top-5错误率6.67%。当年的网络通常被称为Inception V1。

* 优点

1. 控制了计算量和参数量。既减少了计算资源的消耗，还简化了模型，从而控制了学习的数据量。

2. 具有非常好的分类性能。一方面使用了更深的模型。另一方面除去了最后的全连接层，用全局平均池化层来代替。还有就是使用InceptionModule提高了参数的利用效率。

## Inception v1

### Inception Module

这一部分借鉴了Network ln Network（NIN）的思想。简单来说，InceptionModule是一个小网络，通过增加分支结构，级联（concatenation）形成大网络。

* NIN

通常CNN中的同一通道的卷积核参数是共享的，只能提取一类特征，而NIN中的MLOConv具有更强的能力，可以输出通道间的组合信息。MLPConv基本等效于普通卷积层后再连接1*1的卷积和ReLU激活函数。

> 1*1卷积就是组合各通道信息的过程。可以提高网络表达能力，也可以升维或降维。

![img](https://img-blog.csdn.net/20170612110417837?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvbWFyc2poYW8=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

* Inception Module

第一个分支使用1*1卷积。第二个分支先使用了1\*1卷积，然后连接3\*3卷积，相当于进行了两次特征变换。第三个分支类似，先是1\*1的卷积，然后连接5\*5卷积。最后一个分支则是3\*3最大池化后直接使用1\*1卷积。最后再将四个分支级联。这种方式可以增加网络对于不同尺度的适应性。

### 稀疏结构

Inception Net的主要目标就是找到最优的稀疏结构单元Inception Module。这个稀疏结构基于Hebbian原理，将相关性高的节点连接在一起。

> Hebbian原理：突触前神经元向突触后神经元的持续重复的刺激可以导致突触传递效能的增加。简单来说就是当神经元*A*的轴突与神经元*B*很近并参与了对*B*的重复持续的兴奋时，这两个神经元或其中一个便会发生某些生长过程或代谢变化，致使*A*作为能使*B*兴奋的细胞之一，它的效能增强了。

临近数据比如相邻两层的数据相关性较高，因此由卷积操作连接在一起；同一层、同一区域、不同通道的数据相关性同样很高，而1*1的卷积可以很自然地把各通道的特征连接在一起，所以Inception Module中多次运用1\*1的卷积核。由此构建出Inception Module的稀疏结构。

### Inception Net网络结构

![img](https://img-blog.csdn.net/20170612110458444?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvbWFyc2poYW8=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

我们希望靠后的Inception可以捕获更高阶的抽象特征，因此靠后Inception中3\*3和5*5两个大面积的卷积核占比增加（大面积意味着大感受野），从而捕获更大面积的特征。

### 辅助分类节点

Inception Net除了最后一层之外，中间节点的分类效果也很好，所以在网络中增加了辅助分类节点，将中间某一层的输出用于分类。最后将所有分类结果（softmax值）加权求和得到最终分类结果。同时使得反向传播时增加了额外的正则化，可以增强训练结果。

### 整体网络

以下是网络结构图：

![img](https://img-blog.csdn.net/20170612110614351?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvbWFyc2poYW8=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

## Inception v2

Inception借鉴了VGGNet的思路，用多个小卷积核代替大卷积核。网络用两个3\*3的卷积代替了5*5的卷积核，既降低了参数量，又减轻了过拟合。

### BN（Batch Normalization）

在网络中，BN对每一个mini-batch数据的内部进行标准化（normalization），是输出规范化到N（0,1）的正态分布，减少了内部神经元分布的改变。

> BN的论文指出，传统的深度神经网络在训练时，每一层的输入的分布都在变化，导致训练变得困难，我们只能使用一个很小的学习速率解决这个问题。而对每一层使用BN之后，我们就可以有效地解决这个问题，学习速率可以增大很多倍，达到之前的准确率所需要的迭代次数只有1/14，训练时间大大缩短。而达到之前的准确率后，可以继续训练，并最终取得远超于Inception V1模型的性能——top-5错误率4.8%，已经优于人眼水平。因为BN某种意义上还起到了正则化的作用，所以可以减少或者取消Dropout，简化网络结构。



## Inception v3

### Factorization into smallconvolutions

将较大的二维卷积拆成两个较小的一维卷积，比如将5\*5拆分成5\*1和1\*5。好处有：

1. 减少了大量参数，加快计算，减轻过拟合。
2. 增加了一层非线性扩展模型表达能力。论文中指出，这种非对称的卷积结构拆分，其结果比对称地拆为几个相同的小卷积核效果更明显，可以处理更多、更丰富的空间特征，增加特征多样性。

![img](https://img-blog.csdn.net/20170612110651403?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvbWFyc2poYW8=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)



## Inception v4



reference：

[赫布理论](https://blog.csdn.net/qq_31374615/article/details/48623221)

[深度学习经典卷积神经网络之GoogLeNet（Google Inception Net）](https://blog.csdn.net/marsjhao/article/details/73088850)