* HOG
* SIFT
* CNN
  * LeNet
  * AlexNet
  * ZF Net
  * GoogLeNet
  * VGG Net
  * ResNet

候选区

![img](https://img-blog.csdn.net/20180502184712966)

* R-CNN
  * 2014
  * 1. selective search选出候选框
    2. 每个候选框分别卷积，提取特征
    3. 把卷积后的特征放到SVM分类器
  * 1. 候选框没有共享神经网络
    2. 分类用SVM，很麻烦
    3. 费时

* SPP-net
  * 在R-CNN基础上加了特殊的pooling层，把不同尺寸的图池化成大小一致
* Fast R-CNN
  * 2015
  * 1. 不用selective search，先卷积，加快了速度
    2. 在特征图上找对应原始图像上的框
    3. RoI Pooling
    4. 回归加分类
  * 选框费时
* Faster R-CNN
  * 2015
  * 1. 卷积
    2. 对特征图RPN操作，产生候选框
       1. 二分类，删去不是物体的选框
       2. 回归计算loss
    3. RoI Pooling
    4. n分类
* R-FCN

基于深度学习

* YOLO
* SSD
* DenseBox
* RRC
* Deformable CNN

