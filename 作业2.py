import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def computeCost(X, y, theta):
    inner = np.power((X*theta.T-y),2)
    return np.sum(inner) / (2 * len(X))

def gradientDescent(X, y, theta, alpha, iters):
    temp = np.matrix(np.zeros(theta.shape))
    parameters = int(theta.ravel().shape[1])
    cost = np.zeros(iters)
    
    for i in range(iters):
        error = (X * theta.T) - y
        
        for j in range(parameters):
            term = np.multiply(error, X[:,j])
            temp[0,j] = theta[0,j] - ((alpha / len(X)) * np.sum(term))
            
        theta = temp
        cost[i] = computeCost(X,y,theta)  # 填入一行代码，计算每次迭代的代价函数值
        # print(theta,end="    ")
        # print(cost[i])
    return theta, cost

print("My Student Number and Name are: YOUR_CODE ") #此处替换成你的学号和姓名
path =  'C:/Users/郝勇/Desktop/人工智能入门/WU_FILE_0/ai-hw4/hw4data1.txt'
data = pd.read_csv(path, header=None, names=['Population', 'Profit'])
# # print(data.head(1))
# # print(data.describe())
data.plot(kind='scatter', x='Population', y='Profit', figsize=(6,4))
# # plt.show()

data.insert(0, 'Ones', 1)
# # set X (training data) and y (target variable)
cols = data.shape[1]
X = data.iloc[:,0:cols-1]#X是所有行，去掉最后一列
y = data.iloc[:,cols-1:cols]#y是所有行，最后一列

X = np.matrix(X.values)
y = np.matrix(y.values)
theta = np.matrix(np.array([0,0]))

# print(computeCost(X, y, theta))

alpha = 0.01
iters = 1000

g, cost = gradientDescent(X, y, theta, alpha, iters)

# x = np.linspace(data.Population.min(), data.Population.max(), 100)
# f = g[0, 0] + (g[0, 1] * x)

# fig, ax = plt.subplots(figsize=(6,4))
# ax.plot(x, f, 'r', label='Prediction')
# ax.scatter(data.Population, data.Profit, label='Traning Data')
# ax.legend(loc=2)
# ax.set_xlabel('Population')
# ax.set_ylabel('Profit')
# ax.set_title('Predicted Profit vs. Population Size')
# # plt.show()

# print(g)

# fig, ax = plt.subplots(figsize=(6,4))
# ax.plot(np.arange(iters), cost, 'r')
# ax.set_xlabel('Iterations')
# ax.set_ylabel('Cost')
# ax.set_title('Error vs. Training Epoch')
# plt.show()

path =  'C:/Users/郝勇/Desktop/人工智能入门/WU_FILE_0/ai-hw4/hw4data2.txt'
data2 = pd.read_csv(path, header=None, names=['Size', 'Bedrooms', 'Price'])
# data2.head()

data2 = (data2 - data2.mean()) / data2.std()
# data2.head()

# # add ones column
data2.insert(0, 'Ones', 1)
# print(data2.values)
# # set X (training data) and y (target variable)
cols = data2.shape[1]

X2 = data2.iloc[:,0:cols-1]  # 从数据集中取得 X，参考之前的一元线性回归练习代码即可
# print(X2.values)
y2 = data2.iloc[:,cols-1:cols]  # 从数据集中取得 y

# # convert to matrices and initialize theta
X2 = np.matrix(X2.values)
y2 = np.matrix(y2.values)
theta2 = np.matrix(np.array([0,0,0]))

# # perform linear regression on the data set
g2, cost2 = gradientDescent(X2, y2, theta2, alpha, iters)

# # get the cost (error) of the model
# computeCost(X2, y2, g2)
# g2


# fig, ax = plt.subplots(figsize=(6,4))
# ax.plot(np.arange(iters), cost2, 'r')
# ax.set_xlabel('Iterations')
# ax.set_ylabel('Cost')
# ax.set_title('Error vs. Training Epoch')
# plt.show()


from sklearn import linear_model
model = linear_model.LinearRegression()
model.fit(X, y)


x = np.array(X[:, 1].A1)
f = model.predict(X).flatten()

# fig, ax = plt.subplots(figsize=(6,4))
# ax.plot(x, f, 'r', label='Prediction')
# ax.scatter(data.Population, data.Profit, label='Traning Data')
# ax.legend(loc=2)
# ax.set_xlabel('Population')
# ax.set_ylabel('Profit')
# ax.set_title('Predicted Profit vs. Population Size')
# plt.show()

# 正规方程
def normalEqn(X, y):
    theta = np.linalg.inv(X.T@X)@X.T@y#X.T@X等价于X.T.dot(X)
    return theta

final_theta2=normalEqn(X, y) #与批量梯度下降的theta的值略有差距
print(final_theta2)