# coding: UTF-8
import numpy as np
import matplotlib.pyplot as plt
from random import shuffle

plt.rcParams['font.sans-serif'] = ['SimHei']  # 显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 这两行需要手动设置

# 人口基数
PeopleBasic = 1000000
# 繁衍代数
generations = 10
# 遗传特征
K = 100


def normalGeneration(mu, sigma, N):
    return np.random.normal(mu, sigma, N)


def population_init(PeopleBasic, K, suan=1):
    return normalGeneration(K, 1, PeopleBasic)


def eliminate(population, rate):
    population = np.sort(population)
    length = len(population)
    new_length = int(rate * length)
    population = population[new_length:]
    shuffle(population)
    return population


def Offspring_diff(founder_count, mu=0, sigma=1):
    return normalGeneration(mu, sigma, founder_count)


def show(list):
    plt.hist(x=list,  # 指定绘图数据
             bins=100,  # 指定直方图中条块的个数
             color='steelblue',  # 指定直方图的填充色
             edgecolor='black'  # 指定直方图的边框色
             )
    # 添加x轴和y轴标签
    plt.xlabel('K')
    plt.ylabel(U"频数")
    # 添加标题
    plt.title('K')
    # 显示图形
    plt.show()


founder_lst = population_init(PeopleBasic, K, 1)
print(type(founder_lst))
founder_count = len(founder_lst)
show(founder_lst)
K_mean = np.mean(founder_lst)
print(K_mean)
K_mean_lst = np.zeros(generations)

for i in range(generations):
    founder_lst = eliminate(founder_lst, 0.1)
    founder_count = len(founder_lst)
    diff = Offspring_diff(founder_count, 0, 3)
    founder_lst = founder_lst + diff
    K_mean_lst[i] = np.mean(founder_lst)
    show(founder_lst)

print(K_mean_lst)
plt.plot(range(generations), K_mean_lst, color='red', linewidth=2.0, linestyle='--')
plt.show()
