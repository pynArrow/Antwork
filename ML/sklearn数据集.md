# dataset from scikit-learn



```python
from sklearn import datasets
```

下面简单介绍一下内置的小型标准数据集

## digit dataset

手写数字数据集，用于多分类任务

```python
digits = datasets.load_digits()
```

## iris dataset



## barset cancer dataset

乳腺癌数据集，用于二分类任务

## diabetes dataset

糖尿病数据集，用于回归任务

## boston dataset

波士顿房价数据集，用于回归任务

### 数据集简介

下表中给出了波士顿房价数据集的一些基本信息。

![TIM图片20200519095330](C:\Users\Administrator\Desktop\cs\ML\blog_image\sklearn\TIM图片20200519095330.png)

* 特征

  13维特征+1维类别标注

| 特征    | 特征解释                        | 数据类型 |
| ------- | ------------------------------- | -------- |
| CRIM    | 按城镇划分的人均犯罪率          |          |
| ZN      | 超过25000平方英尺的住宅用地比例 |          |
| INDUS   | 城镇非零售业务英亩比例          |          |
| CHAS    |                                 |          |
| NOX     |                                 |          |
| RM      |                                 |          |
| AGE     |                                 |          |
| DIS     |                                 |          |
| RAD     |                                 |          |
| TAX     |                                 |          |
| PTRATIO |                                 |          |
| B       |                                 |          |
| LSTAT   |                                 |          |
| MEDV    |                                 |          |

## linnerud dataset

体能训练数据集，用于多变量回归任务