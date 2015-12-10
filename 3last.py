# -*- coding: utf-8 -*-
def make_input(prize):
    import csv
    with open("List_of_lotto_2010_2014 - Sheet1.csv") as csvfile:
        reader = csv.DictReader(csvfile)
        if prize == 'jackpot':
            prize_n = [row['3Last1'] for row in reader]
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
        print(dic_two_2010)
        
        

lotto_two()

##ตัวแปรที่ต้องแก้มี dic_two, table, i