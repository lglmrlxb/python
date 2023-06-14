import numpy as np

"""参考网址 https://blog.csdn.net/qq_53582111/article/details/122055963"""
a = np.array([[1, 2, 3, 0], [4, 5, 6, 7], [12, 32, 9, 223]]

             )
print(a)  # 输出数组的排列
print(a.shape)  # 输出数组的形状  可以设置形状  类似分段一般
print(a.ndim)  # 输出数组的维度

b = np.arange(10)  # 等差数组的创建
v = np.arange(0, 10, 2)  # [开始数值，结束数值（不含），步数]
print(b)
print(v)
print(a.dtype)  # 数据类型
print(a.size)  # 总元素个数
print(a.itemsize)  # 占用空间 单位字节
print(np.zeros((4, 3)))  # 输出1.的排列组合
print(2)
print(np.ones_like(np.zeros((4, 3))))

print(3)
print(np.eye(4))
print(4)
print(np.identity(3))
print("开根号")
print(np.sqrt(a))  # 开根号
print("绝对值")
print(np.abs(a))  # 绝对值

print('第二题')
array1 = np.array(range(24))
print(array1)
array1[4] = 1
print(array1)
print(6)
array1.shape = 2, 3, 4  # [2段 ，3行  ，4列]
print(array1)
print(array1.shape)

print('第三题')
array3 = np.arange(0, 16)
array3.shape = 4, 4
print(array3)
print('第二行第一列为：', array3[1][0], '\n第三行第二列为', array3[2][1])
print('第一行为:', array3[1, :])
print('第二行为:', array3[2, :])
print('第二列为:', array3[:, 1])
print('第三列为:', array3[:, 2])
print(array3)
print(array3[2, 2], array3[1, 3])

print('第七题')
number7 = np.array([[1, 1],
                    [2, 3],
                    [4, 2]])
print(number7)
print("每一列的和", number7.sum(axis=0))
print("每一行的和", number7.sum(axis=1))
temp1 = number7[1]
temp1.shape = 1, 2
print("计算第一行所有列的和", np.sum(temp1, axis=0))
print("计算矩阵中所有元素的最大值", number7.max())
print("计算第二列的最大", number7[:, 1].max())
print("计算第二行的最大值", number7[1].max())
print("计算每一行的最大值", np.max(number7, axis=1))
print("计算每一列的最大值", np.max(number7, axis=0))
print("每一列的最大值对应该列中的索引", np.argmax(number7, axis=0))
print("每一行的最大值对应该列中的索引", np.argmax(number7[1]))
