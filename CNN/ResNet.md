# Deep Residual Learning for Image Recognition——ResNet



## 残差（residual）

残差是ResNet的核心概念。残差，不同于偏差（bias）、方差（variance），是指预测结果与真实值之间的差异。偏差指预测结果与真实值的差异，这与残差的概念很类似，但是偏差是由模型拟合度不足导致，而残差是模型确定的。一般而言，残差应当是随机分布的，没有明显的模式和异常值。

## Residual Module

首先解释一个概念：恒等映射（identical mapping）。恒等映射即集合中的元素与自身一一对应。

Residual Module的结构图如下，x为浅层的输出，$F（x）$是经过两层变换后的结果，$H(x)=F(x)+x$是深层的输出

![TIM图片20200624234940](C:\Users\Administrator\Desktop\cs\ML\blog_image\ResNet\TIM图片20200624234940.png)

## short connection



reference:

[回归模型偏差&方差&残差](https://zhuanlan.zhihu.com/p/50214504)