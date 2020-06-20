# GoogLeNet

GoogLeNet首次出现在ILVRC 2014的比赛中，以较大的优势获得当年第一名，top-5错误率6.67%。当年的网络通常被称为Inception V1。

之所以名为“GoogLeNet”而非“GoogleNet”，据说是为了向LeNet致敬。在本文中，先是详细介绍一下GoogLeNet v1中的基本思想，然后简介后续改进工作中做的主要贡献，重复的内容不再提及。

* 优点

1. 控制了计算量和参数量。既减少了计算资源的消耗，还简化了模型，从而控制了学习的数据量。

2. 具有非常好的分类性能。一方面使用了更深的模型。另一方面除去了最后的全连接层，用全局平均池化层来代替。还有就是使用InceptionModule提高了参数的利用效率。

[TOC]

## GoogLeNet v1

### Inception Module

这一部分借鉴了Network ln Network（NIN）的思想。简单来说，InceptionModule是一个小网络，通过增加分支结构，级联（concatenation）形成大网络。

* NIN

通常CNN中的同一通道的卷积核参数是共享的，只能提取一类特征，而NIN中的MLOConv具有更强的能力，可以输出通道间的组合信息。MLPConv基本等效于普通卷积层后再连接1*1的卷积和ReLU激活函数。

> 1*1卷积就是组合各通道信息的过程。可以提高网络表达能力，也可以升维或降维。

![img](https://img-blog.csdn.net/20170612110417837?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvbWFyc2poYW8=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

* Inception Module

第一个分支使用1*1卷积。第二个分支先使用了1\*1卷积，然后连接3\*3卷积，相当于进行了两次特征变换。第三个分支类似，先是1\*1的卷积，然后连接5\*5卷积。最后一个分支则是3\*3最大池化后直接使用1\*1卷积。最后再将四个分支级联。这种方式可以增加网络对于不同尺度的适应性。

### Filter Concatenation

注意到在各个分支结束后，有一个Filter Contenation的结构，其实就是把各分支结果在图像深度上叠加。这里需要注意的是，各分支的输出特征图尺寸是相同的，也就是说各分支的卷积核（因为尺寸不同）需要添加不同的padding和stride。

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

## GoogLeNet v2

Inception借鉴了VGGNet的思路，用多个小卷积核代替大卷积核。网络用两个3\*3的卷积代替了5*5的卷积核，既降低了参数量，又减轻了过拟合。

### BN（Batch Normalization）

在网络中，BN对每一个mini-batch数据的内部进行标准化（normalization），使输出规范化到N（0,1）的正态分布，减少了内部神经元分布的改变。

> 论文指出，传统的深度神经网络在训练时，每一层的输入的分布都在变化，导致训练变得困难，我们只能使用一个很小的学习速率解决这个问题。而对每一层使用BN之后，我们就可以有效地解决这个问题，学习速率可以增大很多倍，达到之前的准确率所需要的迭代次数只有1/14，训练时间大大缩短。而达到之前的准确率后，可以继续训练，并最终取得远超于Inception V1模型的性能——top-5错误率4.8%，已经优于人眼水平。因为BN某种意义上还起到了正则化的作用，所以可以减少或者取消Dropout，简化网络结构。

BN可以使网络使用更大的学习率，不用担心参数初始化的影响，还可以忽略原数据的分布规律，从而使得dropout变得非必须。

## GoogLeNet v3

### Factorization into smallconvolutions

将较大的二维卷积拆成两个较小的一维卷积，比如将3\*3拆分成3\*1和1\*3。这样做的好处有：

1. 减少了大量参数，加快计算，减轻过拟合。
2. 增加了一层非线性扩展模型表达能力。论文中指出，这种非对称的卷积结构拆分，其结果比对称地拆为几个相同的小卷积核效果更明显，可以处理更多、更丰富的空间特征，增加特征多样性。

事实上，任意n\*n的卷积都可以通过1\*n和n\*1的卷积的先后进行来替代。不过，论文中说明：这种分解方法在网络的前期效果并不好，而在feature map尺寸在12-20左右时，才能表现更好。

![img](https://img-blog.csdn.net/20170612110651403?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvbWFyc2poYW8=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

### Effificient Grid Size Reduction

一般来说，CNN使图片尺寸不断缩小，深度不断增大。尺寸缩小有两种方法：

1. 先池化后卷积
2. 先卷积后池化

![TIM图片20200620153046](C:\Users\Administrator\Desktop\cs\ML\blog_image\GoogLeNet\TIM图片20200620153046.jpg)

然而对于方法一，在池化的过程中会损失一些特征，导致表达瓶颈；方法二是正常的思路，但是先卷积会使得计算量大于第一种方法。GoogLeNet使用如下结构来权衡两种方法，即分别并行执行，再合并。

![TIM图片20200620153447](C:\Users\Administrator\Desktop\cs\ML\blog_image\GoogLeNet\TIM图片20200620153447.jpg)

### 整体结构

![TIM图片20200620153627](C:\Users\Administrator\Desktop\cs\ML\blog_image\GoogLeNet\TIM图片20200620153627.jpg)

表中Figure 5指Inception v2中借助VGGNet思路改进后的结构。

![TIM图片20200620153807](C:\Users\Administrator\Desktop\cs\ML\blog_image\GoogLeNet\TIM图片20200620153807.png)

表中Figure 6表示借助刚才提到的分解（factorization）的方法改进的结构。

![TIM图片20200620153942](C:\Users\Administrator\Desktop\cs\ML\blog_image\GoogLeNet\TIM图片20200620153942.png)

表中Figure 7借鉴了NININ的思想。

![TIM图片20200620154153](C:\Users\Administrator\Desktop\cs\ML\blog_image\GoogLeNet\TIM图片20200620154153.jpg)

## GoogLeNet v4

v4主要借鉴了ResNet，引入残差连接（Residual Connection），得到得到Inception-ResNet-v1，Inception-ResNet-v2，Inception-v4三种网络结构。

### Inception v4

整体结构如下：



![TIM图片20200620155841](C:\Users\Administrator\Desktop\cs\ML\blog_image\GoogLeNet\TIM图片20200620155841.png)

### Inception-ResNet

通过引入residual connection，把Inception和ResNet结合起来。

* residual connection

ResNet中提出的rc。

![TIM图片20200620180247](C:\Users\Administrator\Desktop\cs\ML\blog_image\GoogLeNet\TIM图片20200620180247.png)

作者重新研究了下residual connection的作用，指出residual connection并不会明显提升模型精度，而是会加快训练收敛。

residual connection与inception结合后是如下图的结构。论文中添加了一个scale操作，也就是乘以一个很小的缩放系数，通常使用0.1。

![TIM图片20200620180558](C:\Users\Administrator\Desktop\cs\ML\blog_image\GoogLeNet\TIM图片20200620180558.jpg)

reference：

[赫布理论](https://blog.csdn.net/qq_31374615/article/details/48623221)

[深度学习经典卷积神经网络之GoogLeNet（Google Inception Net）](https://blog.csdn.net/marsjhao/article/details/73088850)

[CNN经典模型之GoogLeNet](https://zhuanlan.zhihu.com/p/76446136)