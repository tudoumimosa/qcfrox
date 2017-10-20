# coding: utf-8
fout = open('sample.csv','w')
fout.write("a,b,c\n")
fout.write("d,e,f\n")
fout.close()
get_ipython().magic('cat sample.csv')
import csv
for line in csv.reader(open('sample.csv')):
    print(line)
    
get_ipython().magic('ls ')
get_ipython().magic('cd qcf-workshop')
get_ipython().magic('ls ')
import stock.py
