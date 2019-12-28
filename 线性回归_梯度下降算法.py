#一个用于解决线性回归的梯度下降算法，使用sklearn提供的数据集作为样本，进行测试

import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets

iter_num=10000#迭代次数上限制
alpha=5#迭代步长
error_rate=1e-2#代价阈值


def computeCost(X,theta,y):
	temp=np.power((np.dot(X,theta.T)-y),2)
	return (np.sum(temp)/(2*len(X)))


#批量梯度下降算法
def BGD(X,theta,y,iter_num=iter_num,alpha=alpha,error_rate=error_rate):
	temp=np.zeros(theta.shape)
	cost=[]
	parameter=theta.shape[1]
	# print(theta)
	for i in range(iter_num):
		if(i%100==0):
			print('=',end='')
		error=(np.dot(X,theta.T)-y)
		for j in range(parameter-1):
			temp[0,j]=theta[0,j]-alpha*np.sum(np.multiply(X[:,j],error))/len(X)
		# temp[0,0]=theta[0,0]-alpha*np.sum(np.multiply(X[:,0],error))/len(X)
		theta=temp
		cost.append(computeCost(X,theta,y))
		# print(i,end="           ")
		# print(cost[i])
		if(cost[i]<error_rate):
			break
	return theta,cost



#随机梯度下降算法
def SGD(X,theta,y,iter_num=iter_num,alpha=alpha,error_rate=error_rate):
	temp=np.zeros(theta.shape)
	cost=[]
	# print(theta)
	for i in range(iter_num):
		rand_i=np.random.randint(X.shape[0])
		error=(np.dot(X[rand_i],theta.T)-y[rand_i])
		temp=theta-alpha*sum(np.multiply(X,error))
		theta=temp
		cost.append(computeCost(X,theta,y))
		if(cost[i]<error_rate):
			break
	return theta,cost

#小批量梯度下降算法
def MBGD(X,theta,y,iter_num=iter_num,alpha=alpha,error_rate=error_rate):
	temp=np.zeros(theta.shape)
	cost=[]
	parameter=theta.shape[1]
	batch_size=10
	# print(theta)
	for i in range(iter_num):
		if(i%100==0):
			print('=',end='')
		rand_i=np.random.choice(range(len(X)),batch_size)
		sample=np.array(X[rand_i,:]).reshape(batch_size,-1)
		target=np.array(y[rand_i,:]).reshape(batch_size,-1)
		error=(np.dot(sample,theta.T)-target)
		for j in range(parameter-1):
			temp[0,j]=theta[0,j]-alpha*np.sum(np.multiply(sample[:,j],error))/len(X)
		# temp[0,0]=theta[0,0]-alpha*np.sum(np.multiply(X[:,0],error))/len(X)
		theta=temp
		cost.append(computeCost(X,theta,y))
		# print(i,end="           ")
		# print(cost[i])
		if(cost[i]<error_rate):
			break
	return theta,cost

def predict(X,theta):
	return np.dot(X,theta.T)

'''载入波士顿房价数据'''

X,y = datasets.load_diabetes(return_X_y=True)
y=y.reshape(-1,1)

'''获取自变量数据的形状'''
theta=np.zeros(X.shape[1]).reshape(1,-1)
# theta=np.array([-0.09651627,0.12904406,-0.05825913,0.007411,0.00407647,0.13200498,0.08190729,0.01922284,0.01252504,0.00311486,0.09080688,0.0455587,-0.33963799]).reshape(1,X.shape[1])
# theta=np.array([-0.0639322,0.1300011,-0.03736517,0.00385068,0.00209666,0.07047141,0.06196949,0.0130796,0.0032656,0.00145702,0.04774843,0.04867805,-0.19360267]).reshape(X.shape[1])
# print(theta.shape)
# print(computeCost(X,theta,y))
theta,cost=MBGD(X,theta,y)
plt.plot(range(iter_num),cost)
plt.show()
print(predict(X[29,:],theta))
print(y[29,:])
# print(theta)
print(computeCost(X,theta,y))

# error=(np.dot(X[rand_i],theta.T)-y[rand_i])