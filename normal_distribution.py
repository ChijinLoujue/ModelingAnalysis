from scipy.stats import norm
import numpy as np
import matplotlib.pyplot as plt

# mu = 0  # 均值
# sigma = 1  # 标准差
# x = np.arange(-5, 5, 0.1)  # 从-5到5 ，步长是 0.1 产生数据
# y = norm.pdf(x, mu, sigma)
# # x 的意思 大概是 横坐标 ，求出来的y是
# plt.plot(x, y)  # 画折线图
# plt.xlabel('x')  # 设置x轴名字
# plt.ylabel('density')  # 设置y轴名字
# plt.show()  # 输出图像

N = 100000
n = 100
mu = 0
sigma = 1
lst1 = np.random.normal(mu, sigma, N)
lst2 = [0] * n
d = 8.00 / n
x_n = range(n)
x_N = range(N)
# plt.plot(x_N, lst1)
# plt.show()
for i in x_N:
    if i % 1000 == 0:
        print(i / 1000, '\n')
    for j in x_n:
        if lst1[i] <= d * (j + 1) - 4:
            lst2[j] += 1
            break

plt.plot(x_n, lst2)
plt.show()

pipfreeze > requirements.txt
