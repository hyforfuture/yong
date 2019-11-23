import pymysql
import tkinter as tk
from tkinter import filedialog
import csv
from faker import Faker
def proc(list):
    f=Faker()
    for i in range(len(list)):
        if list[i]=='':
            list[i]=f.first_name()

host_name=input("host_name:")
usr_name=input("usr_name:")
password=input("password:")
db_name=input("db_name:")
db = pymysql.connect(host_name, usr_name, password, db_name,autocommit=True)
cursor = db.cursor()
 
root = tk.Tk()
root.withdraw() 
file_path = filedialog.askopenfilename()
i=0
with open(file_path, 'r') as fe:
    dialect = csv.Sniffer().sniff(fe.read(1024), delimiters=";,")
    fe.seek(0)
    f = csv.reader(fe, dialect)
    for line in f:
        if i==0:
            table_name=input("table_name:")
            proc(line)
            sql='CREATE TABLE %s (`%s` text);' % (table_name,"` text,\n`".join(line))
            cursor.execute(sql)
            i=1
            continue
        value_list = list(map(lambda x: "'%s'" % x, line))
        cursor.execute('INSERT INTO %s VALUES(%s)' % (table_name, ','.join(value_list)))
        
db.commit()
db.close()