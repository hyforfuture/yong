import numpy as np 

def cal_f(x,y):
	return np.power((1-x),2)+100*np.power((y-np.power(x,2)),2)

def cal_dx(x,y):
	return 400*np.power(x,3)+(2-400*y)*x-2

def cal_dy(x,y):
	return 200*y-200*np.power(x,2)

def train_grad(max_iter=100000, step=0.001): # 梯度下降迭代主函数
	w = np.zeros((2,), dtype=np.float32) # 初始化求解数值从([0, 0])开始
	loss = 20 # 设置函数初值为20
	iter_count = 0
	while loss > 0.001 and iter_count < max_iter:
		err = np.zeros((2,), dtype=np.float32)
		err[0] = cal_dx(w[0],w[1]) # 计算x偏导数
		err[1] = cal_dy(w[0],w[1]) # 计算y偏导数
		for j in range(2):
			w[j] -= step * err[j] # 梯度下降迭代
		loss = cal_f(w[0], w[1]) # 最小值为0
		print("iter_count: ", iter_count, "the loss:", loss) # 每次迭代输出迭代序号和当前函数值
		iter_count += 1
	return w

if __name__ == '__main__': # main主程序

	w = train_grad() # 调用提督下降迭代祝函数
	print(w) # 显示w的值