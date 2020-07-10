# YOLO v3 : An Incremental Improvement

## 简介

yolo v3保留了先前的几种特征：

1. 划分grid cell预测。
2. 使用leaky ReLU。
3. end-to-end learning
4. batch normalization
5. multi-scale training

> 这里解释一下什么是端到端的训练。
>
> 在传统的学习方法中，一次学习的过程由很多独立的模块共同构成。各模块间的性能相互影响。学习时在每个模块间都需要做标注、反向传播。
>
> 而端对端的学习指（例如深度学习），神经网络的看成一整个模块，隐层的结果不单独分析。

## bounding box prediction

在YOLO9000中使用聚类来生成bbox，为每个bbox4个坐标。yolo2生成的5个anchorbox中，每个box预测5个坐标，$t_x,t_y,t_w,t_h,t_o$，此五个值均为偏移值。

$$b_x=\sigma(t_x)+c_x\\b_y=\sigma(t_y)+c_y\\b_w=p_we^{t_w}\\b_h=p_he^{t_h}$$

其中网格相对于图片的左上角坐标是$(c_x, c_y)$，边框的宽度和高度是$p_w,p_h$，$\sigma(x)$是Sigmoid激活函数，具体解释参考YOLO v2。

YOLO v3使用对数几率回归为每个bbox预测一个分数

## class prediction

每个box预测物体属于各个类别的概率。YOLO v3并没有沿用YOLO 9000的softmax方法，而是使用更简单的独立的逻辑分类器。并且使用二元交叉熵损失来训练分类器。

> 二元交叉熵损失函数：
>
> $$L=-[ylog\hat y+(1-y)log(1-\hat y)]$$

 