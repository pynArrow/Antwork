# KNN——K-Nearest Neighbor

## 简介

KNN，最邻近分类算法通过测量不同特征值之间的距离来进行分类，即每个样本都可以用最接近的k个邻居来预测。通常，在分类任务中可使用“投票法”，即选择这k个实例中出现最多的标记类别作为预测结果；在回归任务中可使用“平均法”，即将这k个实例的实值输出标记的平均值作为预测结果；还可基于距离远近进行加权平均或加权投票，距离越近的实例权重越大。

<img src="https://img-blog.csdn.net/20180703172639433?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3NpbmF0XzMwMzUzMjU5/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70" alt="这里写图片描述" style="zoom: 33%;" />

* **优点**

1. 简单有效，复杂度低
2. 重新训练代价低
3. 适合类域交叉样本

* **缺点**

1. 惰性学习

   > 与急切学习相对应，KNN没有显示地学习过程，也就是说没有训练阶段

2. 类别分类不标准化

3. 可解释性不强

4. 计算量大

   > 新样本需要与数据集中每个数据进行距离计算，复杂度O（n）。

5. 不均衡性

   > 样本容量大的类对测试集的影响更明显。可以引入权值来改进。
   >
   > <img src="https://img-blog.csdn.net/20180915131206466?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3BlbmdqdW5sZWU=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70" alt="img" style="zoom: 50%;" />

* **基本思路**

对于任意n维输入向量，对应于特征空间中的一个点，输出为该特征向量所对应的类别标签或预测值。

* **具体流程**

1. 计算已知类别数据集中的点与当前点之间的距离
2. 按距离递增排序
3. 选取当前距离最小的k个点
4. 统计前k个点所在类别的频率
5. 返回k个点的最高频率

## 基本原理

* **距离度量**

一般使用欧式距离：

$$Lp(x_i,x_j)=(∑_{l=1}^n|x^{(l)}_i−x^{(l)}_j|^p)^{\frac1p}$$

* **k值的选择**

> 近似误差：理解为对训练集的训练误差。当近似误差较小的时候，会出现过拟合的现象，对现有训练集能有很好地预测，但在测试样本上会有较大偏差。
>
> 估计误差：理解为对测试集的测试误差。估计误差小的模型就是较优的模型。

当选择较小的k值时，学习的近似误差会减小（边界情况），但是学习的估计误差会增大，很容易受到噪声的影响，产生过拟合；当选择较大的k值时，可以减少估计误差，但会增大近似误差，意味着整体模型变简单。

* **交叉验证法cross validation**

**k-fold cross validation**：k折交叉验证。将数据集分成k份，每次取出一份作为测试集，分别计算MSE后取平均。

* **特征的预处理**

**量化**：如果样本中存在非数值的特征，需要量化为数值，然后再映射到特征空间中。

**归一化**：样本中不同特征的尺度不同，所以对距离计算的影响不一样，所以进行归一化处理，使得各特征的尺度相当。



**reference**：

[机器学习之KNN最邻近分类算法]([https://blog.csdn.net/pengjunlee/article/details/82713047?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522158855105619724839250020%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fall.57662%2522%257D&request_id=158855105619724839250020&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~first_rank_v2~rank_v25-1](https://blog.csdn.net/pengjunlee/article/details/82713047?ops_request_misc=%7B%22request%5Fid%22%3A%22158855105619724839250020%22%2C%22scm%22%3A%2220140713.130102334.pc%5Fall.57662%22%7D&request_id=158855105619724839250020&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~first_rank_v2~rank_v25-1))