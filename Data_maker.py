
from faker import Faker
from faker import Factory

f=open("C:/Users/郝勇/Desktop/4.csv","w+")
faker=Faker()
gender=("Male","Female")
dept_name=("CS","AI","EE","DS","CV","BU","EN")
inid=1180001
#f.write("%s,%s,%s,%s,%s\n" %("id","name","gender","dept_name","grade"))
for i in range(20):
	f.write("%s,%s,%s,%s,%s\n" %(
		inid+i,
		faker.first_name(),
		gender[faker.random_int(0,1)],
		dept_name[faker.random_int(0,6)],
		faker.random_int(2016,2019))
	)
f.close()
