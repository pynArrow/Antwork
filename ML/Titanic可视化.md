## 背景

在20世纪初，由英国白星轮船公司耗资7500万英镑打造的当时世界上最大的豪华客轮“泰坦尼克”号，曾被称作为“永不沉没的船”和“梦幻之船”这艘豪轮在她的处女之航中，就因撞上冰山而在大西洋沉没。百年来，关于“泰坦尼克”号沉没的原因，一直是人们津津乐道的话题。

时至今日，Titanic号上的各位成员身份信息已经被整理成了数据集，可以用于机器学习的分类任务。在用此数据集训练之前，我们先对其部分特征可视化，以期对此数据集有个更宏观的了解。

## 数据来源

数据来源：[泰坦尼克号数据集](https://www.kesci.com/home/dataset/58a940107159a710d916aefb)

## 可视化结果

话不多说先上图

* **存活率**

<img src="C:\Users\Administrator\Desktop\cs\ML\blog_image\titanic\TIM图片20200512170502.png" alt="TIM图片20200512170502" style="zoom:67%;" />

* **男女比例**

<img src="C:\Users\Administrator\Desktop\cs\ML\blog_image\titanic\TIM图片20200512170516.png" alt="TIM图片20200512170516" style="zoom:67%;" />

* **男女成员存活率**

<img src="C:\Users\Administrator\Desktop\cs\ML\blog_image\titanic\TIM图片20200512170934.png" alt="TIM图片20200512170934" style="zoom:67%;" />

* **各阶级人数**

<img src="C:\Users\Administrator\Desktop\cs\ML\blog_image\titanic\TIM图片20200512170938.png" alt="TIM图片20200512170938" style="zoom:67%;" />

* **各阶级成员存活率**

<img src="C:\Users\Administrator\Desktop\cs\ML\blog_image\titanic\TIM图片20200512170941.png" alt="TIM图片20200512170941" style="zoom:67%;" />

* **全体成员年龄分布**

<img src="C:\Users\Administrator\Desktop\cs\ML\blog_image\titanic\TIM图片20200512170945.png" alt="TIM图片20200512170945" style="zoom:67%;" />

* **各年龄段存活率**

<img src="C:\Users\Administrator\Desktop\cs\ML\blog_image\titanic\TIM图片20200512170950.png" alt="TIM图片20200512170950" style="zoom:67%;" />

## 可视化代码

### 使用的模块

```python
import matplotlib.pyplot as plt
import csv        				  #数据集是csv格式
import seaborn as sns			  #刚刚发掘的可视化神器
```

### 数据特征

![img](https://pic2.zhimg.com/80/v2-737b06ac20f01aed28fde1be98df2989_720w.png)

本次只选取了部分特征分析

### 完整代码

```python
import matplotlib.pyplot as plt
import csv
import seaborn as sns

def show_pie(class1, class2, label1, label2):
    plt.figure(figsize=(6,6))
    labels = [label1, label2]
    colors = ['yellowgreen', 'lightblue']
    size = [class1, class2]
    explode = (0,0.1)
    plt.pie(size,
            explode=explode,
            labels=labels,
            colors=colors,
            autopct='%2.2f%%',
            shadow=False)
    plt.axis('equal')
    plt.legend()
    plt.show()

def show_bar(class1, class2, label1, label2, ylabel='', class3=[], label3=[], color3=[]):
    label_list = [label1,label2]+label3
    class_list = [class1,class2]+class3
    colors = ['lightgreen','lightblue']+color3
    plt.bar(range(len(class_list)), class_list, 
                                    color=colors,
                                    tick_label=label_list)
    plt.ylabel(ylabel)
    plt.show()

def show_histogram(data):
    sns.distplot(data,color='b')
    plt.show()

if __name__ == '__main__':
    filename = r'D:\VS-Code-python\ML_algorithm\titanic_train.csv'
    with open(filename, 'r') as f:
        csvreader = csv.reader(f)
        csvreader.__next__()
        lines = list(csvreader)
        all = len(lines)
        survived = 0
        male = 0
        male_survive = 0
        class_1st = 0
        class_2nd = 0
        class_3rd = 0
        class_1st_survive = 0
        class_2nd_survive = 0
        class_3rd_survive = 0
        age = []
        age_survive = []
        for line in lines:
            #存活人数
            survived += 1 if int(line[1]) else 0
            #男性人数
            male += 1 if line[4] == 'male' else 0
            #存活男性
            male_survive += 1 if int(line[1]) and line[4] == 'male' else 0
            #各阶级人数
            class_1st += 1 if line[2] == '1' else 0
            class_2nd += 1 if line[2] == '2' else 0
            class_3rd += 1 if line[2] == '3' else 0
            #各阶级存活人数
            class_1st_survive += 1 if line[2] == '1' and int(line[1]) else 0
            class_2nd_survive += 1 if line[2] == '2' and int(line[1]) else 0
            class_3rd_survive += 1 if line[2] == '3' and int(line[1]) else 0
            #统计年龄
            if line[5] != '':
                age.append(int(float(line[5])))
                if int(line[1]):
                    age_survive.append(int(float(line[5])))

        #存活率饼图
        show_pie(survived,all-survived,'survived','died')
        #男女比例
        show_pie(male,all-male,'male','female')
        #男女存活率
        show_bar(male_survive/male,(survived-male_survive)/(all-male),'male_survive','female_survive')
        #各阶级人数
        show_bar(class_1st,class_2nd,'first_class','second_class','numbers',
                        class3=[class_3rd],
                        label3=['third_class'],
                        color3=['yellow'])
        #各阶级存活率
        show_bar(class_1st_survive/class_1st,class_2nd_survive/class_2nd,'first_class','second_class','survive_rate',
                        class3=[class_3rd_survive/class_3rd],
                        label3=['third_class'],
                        color3=['yellow'])
        #年龄分布
        show_histogram(age)
        #各年龄段存活率
        show_histogram(age_survive)        
```

