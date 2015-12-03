# -*- coding: utf-8 -*-
import csv
with open("List_of_lotto_2010_2014 - Sheet1.csv") as csvfile:
    reader = csv.DictReader(csvfile)
    table = [row['2Last'] for row in reader]
    lis = []
    dic = {}
    dic2 = {}
    dic3 = {}
    dic4 = {}
    for i in table:
        if table.index(i) <= 24:
            
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1
        elif table.index(i) > 24 and table.index(i) <= 48:
            
            if i not in dic2:
                dic2[i] = 1
            else:
                dic2[i] += 1
        elif table.index(i) > 48 and table.index(i) <= 96:
            
            if i not in dic3:
                dic3[i] = 1
            else:
                dic3[i] += 1
        else:
            if i not in dic4:
                dic4[i] = 1
            else:
                dic4[i] += 1
    print(dic)
    print(dic2)
    print(dic3)
    print(dic4)
        
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
 
objects = dic.keys()
y_pos = np.arange(len(objects))
performance = dic.values()
 
plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.ylabel('Times')
plt.title('ww')
 
plt.show()
