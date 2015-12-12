import csv
def lotto_two():
    '''
    This is output of 2Last in 2010-2014
    '''
    with open("lotto2010_2014.csv") as csvfile:
        reader = csv.DictReader(csvfile)
        table = [row['2Last'] for row in reader]
        print(table)
        print(len(table))
        dic_two_2010 = {}
        dic_two_2011 = {}
        dic_two_2012 = {}
        dic_two_2013 = {}
        dic_two_2014 = {}
        
        count = 24
        for i in range(count):
            #this 2Last_lotto in 2010      
            if table[i] not in dic_two_2010:
                dic_two_2010[table[i]] = 1
            else:
                dic_two_2010[table[i]] += 1

        count = 48
        for i in range(24, count):
            #this 2Last_lotto in 2011
            if table[i] not in dic_two_2011:
                dic_two_2011[table[i]] = 1
            else:
                dic_two_2011[table[i]] += 1

        count = 72
        for i in range(48, count):
            #this 2Last_lotto in 2012
            if table[i] not in dic_two_2012:
                dic_two_2012[table[i]] = 1
            else:
                dic_two_2012[table[i]] += 1

        count = 96
        for i in range(72, count):
            #this 2Last_lotto in 2013
            if table[i] not in dic_two_2013:
                dic_two_2013[table[i]] = 1
            else:
                dic_two_2013[table[i]] += 1
        count = 120
        for i in range(96, count):
            #this 2Last_lotto in 2014
            if table[i] not in dic_two_2014:
                dic_two_2014[table[i]] = 1
            else:
                dic_two_2014[table[i]] += 1
                    
    print("This 2Last_lotto in 2010" + str(dic_two_2010))
    print("This 2Last_lotto in 2011" + str(dic_two_2011))
    print("This 2Last_lotto in 2012" + str(dic_two_2012))
    print("This 2Last_lotto in 2013" + str(dic_two_2013))
    print("This 2Last_lotto in 2014" + str(dic_two_2014))

lotto_two()

def make_num(prize, dic):
    count = 24
    for num in range(count):
        if prize[num] not in year_10:
            dic[prize[num]] = 1
        else: 
            dic[prize[num]] += 1
    count = 48
    for num in range(24, count):
        if prize[num] not in year_11:
            dic[prize[num]] = 1
        else: 
            dic[prize[num]] += 1
            
    count = 72
    for num in range(48,count):
        if prize[num] not in year_12:
            dic[prize[num]] = 1
        else: 
            dic[prize[num]] += 1
            
    count = 96
    for num in range(72, count):
        if prize[num] not in year_13:
            dic[prize[num]] = 1
        else: 
            dic[prize[num]] += 1
            
    count = 120
    for num in range(96, count):
        if prize[num] not in year_14:
            dic[prize[num]] = 1
        else: 
            dic[prize[num]] += 1
            
make_num()

def make_3():
    import csv
    with open("List_of_lotto_2010_2014 - Sheet1.csv") as csvfile:
        reader = csv.DictReader(csvfile)
        prize = [row['3Last2'] for row in reader]
    for i in range(1, 4):
        if i == '1':
            year_10 = make_num(prize, dict())
            year_11 = make_num(prize, dict())
            year_12 = make_num(prize, dict())
            year_13 = make_num(prize, dict())
            year_14 = make_num(prize, dict())
        elif i == '2':
            year_10 = make_num(prize, year_10)
            year_11 = make_num(prize, year_11)
            year_12 = make_num(prize, year_12)
            year_13 = make_num(prize, year_13)
            year_14 = make_num(prize, year_14)
    print(year_10)
make_3()

def jackpot():
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
jackpot()