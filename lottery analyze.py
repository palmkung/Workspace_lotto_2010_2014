# -*- coding: utf-8 -*-
def make_input(prize):  ####สร้างอินพุทเก็บเป็นลิสต์
    import csv
    with open("List_of_lotto_2010_2014 - Sheet1.csv") as csvfile:
        reader = csv.DictReader(csvfile)
        if prize == 'jackpot':
            prize_n = [row['JackPot'] for row in reader]
            return prize_n
        elif prize == '2num':
            prize_n = [row['2Last'] for row in reader]
            return prize_n
        elif prize == '3num1':
            prize_n = [row['3Last1'] for row in reader]
            return prize_n
        elif prize == '3num2':
            prize_n = [row['3Last2'] for row in reader]
            return prize_n
        elif prize == '3num3':
            prize_n = [row['3Last3'] for row in reader]
            return prize_n
        elif prize == '3num4':
            prize_n = [row['3Last1'] for row in reader]
            return prize_n
            
def compile_number(year, table, dic):
    if year == "2010":
        count = 24
        for i in range(count):
            #this 2Last_lotto in 2010      
            if table[i] not in dic:
                dic[table[i]] = 1
            else:
                dic[table[i]] += 1
        return dic
                
    elif year == "2011":
        count = 48
        for i in range(24, count):
            #this 2Last_lotto in 2011
            if table[i] not in dic:
                dic[table[i]] = 1
            else:
                dic[table[i]] += 1
        return dic
                
    elif year == "2012":
        count = 72
        for i in range(48, count):
            #this 2Last_lotto in 2012
            if table[i] not in dic:
                dic[table[i]] = 1
            else:
                dic[table[i]] += 1
        return dic
                
    elif year == "2013":
        count = 96
        for i in range(72, count):
            #this 2Last_lotto in 2013
            if table[i] not in dic:
                dic[table[i]] = 1
            else:
                dic[table[i]] += 1
        return dic
                
    elif year == "2014":
        count = 120
        for i in range(96, count):
            #this 2Last_lotto in 2014
            if table[i] not in dic:
                dic[table[i]] = 1
            else:
                dic[table[i]] += 1
        return dic
    
def lotto_two():
        dic_two_2010 = compile_number("2010", make_input("2num"), dict())
        dic_two_2011 = compile_number("2011", make_input("2num"), dict())
        dic_two_2012 = compile_number("2012", make_input("2num"), dict())
        dic_two_2013 = compile_number("2013", make_input("2num"), dict())
        dic_two_2014 = compile_number("2014", make_input("2num"), dict())
        
        
lotto_two()
def lotto_three():
    for num in range(1, 5):
        if num == 1:
            dic_two_2010 = compile_number("2010", make_input("3num1"), dict())
            dic_two_2011 = compile_number("2011", make_input("3num1"), dict())
            dic_two_2012 = compile_number("2012", make_input("3num1"), dict())
            dic_two_2013 = compile_number("2013", make_input("3num1"), dict())
            dic_two_2014 = compile_number("2014", make_input("3num1"), dict())
        elif num == 2:
            dic_two_2010 = compile_number("2010", make_input("3num2"), dic_two_2010)
            dic_two_2011 = compile_number("2011", make_input("3num2"), dic_two_2011)
            dic_two_2012 = compile_number("2012", make_input("3num2"), dic_two_2012)
            dic_two_2013 = compile_number("2013", make_input("3num2"), dic_two_2013)
            dic_two_2014 = compile_number("2014", make_input("3num2"), dic_two_2014)
        elif num == 3:
            dic_two_2010 = compile_number("2010", make_input("3num3"), dic_two_2010)
            dic_two_2011 = compile_number("2011", make_input("3num3"), dic_two_2011)
            dic_two_2012 = compile_number("2012", make_input("3num3"), dic_two_2012)
            dic_two_2013 = compile_number("2013", make_input("3num3"), dic_two_2013)
            dic_two_2014 = compile_number("2014", make_input("3num3"), dic_two_2014)
        elif num == 4:
            dic_two_2010 = compile_number("2010", make_input("3num4"), dic_two_2010)
            dic_two_2011 = compile_number("2011", make_input("3num4"), dic_two_2011)
            dic_two_2012 = compile_number("2012", make_input("3num4"), dic_two_2012)
            dic_two_2013 = compile_number("2013", make_input("3num4"), dic_two_2013)
            dic_two_2014 = compile_number("2014", make_input("3num4"), dic_two_2014)
        
    print(dic_two_2010)
lotto_three()
def lotto_six():
    digit1 = {"0":0,"1":0,"2":0,"3":0,"4":0,"5":0,"6":0,"7":0,"8":0,"9":0}
    digit2 = {"0":0,"1":0,"2":0,"3":0,"4":0,"5":0,"6":0,"7":0,"8":0,"9":0}
    digit3 = {"0":0,"1":0,"2":0,"3":0,"4":0,"5":0,"6":0,"7":0,"8":0,"9":0}
    digit4 = {"0":0,"1":0,"2":0,"3":0,"4":0,"5":0,"6":0,"7":0,"8":0,"9":0}
    digit5 = {"0":0,"1":0,"2":0,"3":0,"4":0,"5":0,"6":0,"7":0,"8":0,"9":0}
    digit6 = {"0":0,"1":0,"2":0,"3":0,"4":0,"5":0,"6":0,"7":0,"8":0,"9":0}
    jackpot = make_input("jackpot")
    for lotto in jackpot:
        digit1[lotto[0]] += 1
        digit2[lotto[1]] += 1
        digit3[lotto[2]] += 1
        digit4[lotto[3]] += 1
        digit5[lotto[4]] += 1
        digit6[lotto[5]] += 1
lotto_six()
def sort_numgraph():
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
##ตัวแปรที่ต้องแก้มี dic_two, table, i, dic