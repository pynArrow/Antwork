import tensorflow.examples.tutorials.mnist.input_data as input_data
import tensorflow as tf
import tensorflow.contrib.slim as slim
import math

KEEP_PROB = 0.5
LEARNING_RATE = 0.005
BATCH_SIZE = 5000
EPOCHES = 21
CKPT_PATH = './ckpt/test-model.ckpt'

class Lenet:
    def __init__(self):
        #将二进制数据划分出图片
        self.raw_input_image = tf.placeholder(tf.float32, [None, 784])
        self.input_images = tf.reshape(self.raw_input_image, [-1, 28, 28, 1])
        self.raw_input_label = tf.placeholder("float", [None, 10])
        self.input_labels = tf.cast(self.raw_input_label,tf.int32)
        #dropout值
        self.dropout = KEEP_PROB

        with tf.variable_scope("Lenet") as scope:
            self.train_digits = self.construct_net(True)
            scope.reuse_variables()
            self.pred_digits = self.construct_net(False)

        self.prediction = tf.argmax(self.pred_digits, 1)
        #tf.argmax返回列表最大值的索引值
        #tf.equal判断两个参数相等
        #pred_digits是属于各类别的概率列表
        self.correct_prediction = tf.equal(tf.argmax(self.pred_digits, 1), tf.argmax(self.input_labels, 1))
        #cast将corret_prediction转换为float类型
        #reduce_mean计算平均値，由于二值化了，也就相当于1的占比（正确分类的占比）
        self.train_accuracy = tf.reduce_mean(tf.cast(self.correct_prediction, "float"))


        #设置损失函数
        self.loss = slim.losses.softmax_cross_entropy(self.train_digits, self.input_labels)
        #设置学习率
        self.lr = LEARNING_RATE
        #adam优化寻找全局最优点，最小化loss
        self.train_op = tf.train.AdamOptimizer(self.lr).minimize(self.loss)


    #生成网络
    def construct_net(self,is_trained = True):
        #给slim.conv2d函数设置默认值
        with slim.arg_scope([slim.conv2d], padding='VALID',
                            weights_initializer=tf.truncated_normal_initializer(stddev=0.01),
                            weights_regularizer=slim.l2_regularizer(0.0005)):
            net = slim.conv2d(self.input_images,6,[5,5],1,padding='SAME',scope='conv1')
            net = slim.max_pool2d(net, [2, 2], scope='pool2')
            net = slim.conv2d(net,16,[5,5],1,scope='conv3') 
            net = slim.max_pool2d(net, [2, 2], scope='pool4')
            net = slim.conv2d(net,120,[5,5],1,scope='conv5')
            #将输入扁平化至二维，第一个维度不变
            #[batch_size, ..., ...]->[batch_size, -1]
            net = slim.flatten(net, scope='flat6')
            net = slim.fully_connected(net, 84, scope='fc7')
            #dropout
            net = slim.dropout(net, self.dropout,is_training=is_trained, scope='dropout8')
            digits = slim.fully_connected(net, 10, scope='fc9')
        return digits

def main():
    #导入数据集，二值化
    mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)
    
    #开启会话
    sess = tf.Session()

    print("train data size:", mnist.train.num_examples)
    print("validating data size:", mnist.validation.num_examples)
    print("test data size:", mnist.test.num_examples)

    #导入参数
    batch_size = BATCH_SIZE
    lenet = Lenet()
    epoches = EPOCHES
    ckpt_path = CKPT_PATH

    sess.run(tf.initialize_all_variables())
    saver = tf.train.Saver()
    saver.restore(sess, ckpt_path)

    for epoch in range(epoches):
        #随机划分batch, batch = (batch_image, batch_label)
        #先用先前的网络计算accuracy然后训练
        if epoch == 10:
            global LEARNING_RATE
            LEARNING_RATE /= 10

        for batch in range(math.ceil(mnist.train.num_examples/batch_size)):

            image_batch, label_batch = mnist.train.next_batch(batch_size)

            train_accuracy = sess.run(lenet.train_accuracy,feed_dict={
                lenet.raw_input_image: image_batch,lenet.raw_input_label: label_batch
            })
            test_accuracy = sess.run(lenet.train_accuracy,feed_dict={
                lenet.raw_input_image: mnist.test.images,lenet.raw_input_label: mnist.test.labels
            })
            print("epoch %d, batch %d, training accuracy %g, test accuracy %g" % (epoch , batch, train_accuracy, test_accuracy))
            #
            sess.run(lenet.train_op,feed_dict={lenet.raw_input_image: image_batch,lenet.raw_input_label: label_batch})

    save_path = saver.save(sess, ckpt_path)


if __name__ == '__main__':
    main()


