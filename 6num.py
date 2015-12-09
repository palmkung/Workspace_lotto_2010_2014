import csv
with open("List_of_lotto_2010_2014 - Sheet1.csv") as csvfile:
    reader = csv.DictReader(csvfile)
    table = [row['JackPot'] for row in reader]
    digit1 = {"0":0,"1":0,"2":0,"3":0,"4":0,"5":0,"6":0,"7":0,"8":0,"9":0}
    digit2 = {"0":0,"1":0,"2":0,"3":0,"4":0,"5":0,"6":0,"7":0,"8":0,"9":0}
    digit3 = {"0":0,"1":0,"2":0,"3":0,"4":0,"5":0,"6":0,"7":0,"8":0,"9":0}
    digit4 = {"0":0,"1":0,"2":0,"3":0,"4":0,"5":0,"6":0,"7":0,"8":0,"9":0}
    digit5 = {"0":0,"1":0,"2":0,"3":0,"4":0,"5":0,"6":0,"7":0,"8":0,"9":0}
    digit6 = {"0":0,"1":0,"2":0,"3":0,"4":0,"5":0,"6":0,"7":0,"8":0,"9":0}
    
    for lotto in table:
        digit1[lotto[0]] += 1
        digit2[lotto[1]] += 1
        digit3[lotto[2]] += 1
        digit4[lotto[3]] += 1
        digit5[lotto[4]] += 1
        digit6[lotto[5]] += 1
        
    list_of_num = ["0","1","2","3","4","5","6","7","8","9"]
    list_of_times1 = []
    list_of_times2 = []
    list_of_times3 = []
    list_of_times4 = []
    list_of_times5 = []
    list_of_times6 = []

    for num in list_of_num:
        list_of_times1.append(digit1[num])
    for num in list_of_num:
        list_of_times2.append(digit2[num])
    for num in list_of_num:
        list_of_times3.append(digit3[num])
    for num in list_of_num:
        list_of_times4.append(digit4[num])
    for num in list_of_num:
        list_of_times5.append(digit5[num])
    for num in list_of_num:
        list_of_times6.append(digit6[num])
    
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
 
objects = list_of_num
y_pos = np.arange(len(objects))
performance = list_of_times1
 
plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.ylabel('Times')
plt.title('ww')

objects = list_of_num
y_pos = np.arange(len(objects))
performance = list_of_times2
 
plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.ylabel('Times')
plt.title('ww')

objects = list_of_num
y_pos = np.arange(len(objects))
performance = list_of_times3
 
plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.ylabel('Times')
plt.title('ww')

objects = list_of_num
y_pos = np.arange(len(objects))
performance = list_of_times4
 
plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.ylabel('Times')
plt.title('ww')

objects = list_of_num
y_pos = np.arange(len(objects))
performance = list_of_times5
 
plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.ylabel('Times')
plt.title('ww')

objects = list_of_num
y_pos = np.arange(len(objects))
performance = list_of_times6
 
plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.ylabel('Times')
plt.title('ww')

plt.show()
