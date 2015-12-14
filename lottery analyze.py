# -*- coding: utf-8 -*-
"""PROJECT : LOTTERY ANALYZE"""
def make_input(prize):  ####สร้างอินพุทเก็บเป็นลิสต์
    """Make input to dict and return."""
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
            
def compile_number(year, list_number, storage):#นับจำนวนครั้งที่ออก แล้วเก็บค่าเป็น dic
    """Return dict of number form compile number."""
    if year == "2010":
        count = 24
        for i in range(count):
            if list_number[i] not in storage:
                storage[list_number[i]] = 1
            else:
                storage[list_number[i]] += 1
        return storage
                
    elif year == "2011":
        count = 48
        for i in range(24, count):
            if list_number[i] not in storage:
                storage[list_number[i]] = 1
            else:
                storage[list_number[i]] += 1
        return storage
                
    elif year == "2012":
        count = 72
        for i in range(48, count):
            if list_number[i] not in storage:
                storage[list_number[i]] = 1
            else:
                storage[list_number[i]] += 1
        return storage
                
    elif year == "2013":
        count = 96
        for i in range(72, count):
            if list_number[i] not in storage:
                storage[list_number[i]] = 1
            else:
                storage[list_number[i]] += 1
        return storage
                
    elif year == "2014":
        count = 120
        for i in range(96, count):
            if list_number[i] not in storage:
                storage[list_number[i]] = 1
            else:
                storage[list_number[i]] += 1
        return storage

def lotto_two():#เก็บจำนวนครั้งของ 2 หลัก
    """Return dict of prize number by year."""
    lotto_two_2010 = compile_number("2010", make_input("2num"), dict())
    lotto_two_2011 = compile_number("2011", make_input("2num"), dict())
    lotto_two_2012 = compile_number("2012", make_input("2num"), dict())
    lotto_two_2013 = compile_number("2013", make_input("2num"), dict())
    lotto_two_2014 = compile_number("2014", make_input("2num"), dict())
    return lotto_two_2010, lotto_two_2011, lotto_two_2012, lotto_two_2013, lotto_two_2014

def lotto_three():#เก็บจำนวนครั้งของ 3 หลัก
    """Return dict of prize number by year."""
    for num in range(1, 5):
        if num == 1:
            lotto_three_2010 = compile_number("2010", make_input("3num1"), dict())
            lotto_three_2011 = compile_number("2011", make_input("3num1"), dict())
            lotto_three_2012 = compile_number("2012", make_input("3num1"), dict())
            lotto_three_2013 = compile_number("2013", make_input("3num1"), dict())
            lotto_three_2014 = compile_number("2014", make_input("3num1"), dict())
        elif num == 2:
            lotto_three_2010 = compile_number("2010", make_input("3num2"), lotto_three_2010)
            lotto_three_2011 = compile_number("2011", make_input("3num2"), lotto_three_2011)
            lotto_three_2012 = compile_number("2012", make_input("3num2"), lotto_three_2012)
            lotto_three_2013 = compile_number("2013", make_input("3num2"), lotto_three_2013)
            lotto_three_2014 = compile_number("2014", make_input("3num2"), lotto_three_2014)
        elif num == 3:
            lotto_three_2010 = compile_number("2010", make_input("3num3"), lotto_three_2010)
            lotto_three_2011 = compile_number("2011", make_input("3num3"), lotto_three_2011)
            lotto_three_2012 = compile_number("2012", make_input("3num3"), lotto_three_2012)
            lotto_three_2013 = compile_number("2013", make_input("3num3"), lotto_three_2013)
            lotto_three_2014 = compile_number("2014", make_input("3num3"), lotto_three_2014)
        elif num == 4:
            lotto_three_2010 = compile_number("2010", make_input("3num4"), lotto_three_2010)
            lotto_three_2011 = compile_number("2011", make_input("3num4"), lotto_three_2011)
            lotto_three_2012 = compile_number("2012", make_input("3num4"), lotto_three_2012)
            lotto_three_2013 = compile_number("2013", make_input("3num4"), lotto_three_2013)
            lotto_three_2014 = compile_number("2014", make_input("3num4"), lotto_three_2014)
        
    return lotto_three_2010, lotto_three_2011, lotto_three_2012, lotto_three_2013, lotto_three_2014

def lotto_six():#เก็บจำนวนครั้งของรางวัลที่หนึ่ง
    """Return dict of prize number by each number in prize."""
    digit1 = {"0":0,"1":0,"2":0,"3":0,"4":0,"5":0,"6":0,"7":0,"8":0,"9":0}
    digit2 = {"0":0,"1":0,"2":0,"3":0,"4":0,"5":0,"6":0,"7":0,"8":0,"9":0}
    digit3 = {"0":0,"1":0,"2":0,"3":0,"4":0,"5":0,"6":0,"7":0,"8":0,"9":0}
    digit4 = {"0":0,"1":0,"2":0,"3":0,"4":0,"5":0,"6":0,"7":0,"8":0,"9":0}
    digit5 = {"0":0,"1":0,"2":0,"3":0,"4":0,"5":0,"6":0,"7":0,"8":0,"9":0}
    digit6 = {"0":0,"1":0,"2":0,"3":0,"4":0,"5":0,"6":0,"7":0,"8":0,"9":0}
    jackpot = make_input("jackpot")
    for lotto in jackpot:
        print(jackpot)
        digit1[lotto[0]] += 1
        digit2[lotto[1]] += 1
        digit3[lotto[2]] += 1
        digit4[lotto[3]] += 1
        digit5[lotto[4]] += 1
        digit6[lotto[5]] += 1
    return digit1, digit2, digit3, digit4, digit5, digit6

def make_graphlotto(number, times):#นำข้อมูลมาแสดงกราฟ
    """Make graph from input number and times."""
    import matplotlib.pyplot as plt; plt.rcdefaults()
    import numpy as np
    import matplotlib.pyplot as plt
    import random
    color_random = "#%06x" % random.randint(0, 0xFFFFFF)
    objects = number
    y_pos = np.arange(1, len(objects)*2, 2)
    performance = times
 
    plt.bar(y_pos, performance, align='center', alpha=0.5, color=color_random)
    plt.subplots_adjust(hspace=10)
    plt.xticks(y_pos, objects)
    plt.tick_params(axis='x', labelsize=7)
    plt.ylabel('Times')
    plt.title('amount of prize number')
    
    plt.show()

def graph2lotto():#แสดงกราฟรางวัล 2หลัก 
    """Print graph of 2 number lottery."""
    two_lotto_2010, two_lotto_2011, two_lotto_2012, two_lotto_2013, two_lotto_2014 = lotto_two()
    make_graphlotto(two_lotto_2010.keys(), two_lotto_2010.values())####เนื่องจากcanopy แสดงกราฟได้ทีละครั้ง เวลาจะแสดงผลกราฟจึงต้องแสดงทีละฟังก์ชั่น T__T
    make_graphlotto(two_lotto_2011.keys(), two_lotto_2011.values())####ถ้่าแสดงรวมกราฟทุกอันจะรวมเป็นหนึ่งแล้วทำให้ข้อมูลอาจเห็นไม่ครบได้
    make_graphlotto(two_lotto_2012.keys(), two_lotto_2012.values())
    make_graphlotto(two_lotto_2013.keys(), two_lotto_2013.values())
    make_graphlotto(two_lotto_2014.keys(), two_lotto_2014.values())
graph2lotto()

def graph3lotto():#แสดงกราฟรางวัล 3หลัก
    """Print graph of 3 number lottery."""
    three_lotto_2010, three_lotto_2011, three_lotto_2012, three_lotto_2013, three_lotto_2014 = lotto_three()
    make_graphlotto(three_lotto_2010.keys(), three_lotto_2010.values())
    make_graphlotto(three_lotto_2011.keys(), three_lotto_2011.values())
    make_graphlotto(three_lotto_2012.keys(), three_lotto_2012.values())
    make_graphlotto(three_lotto_2013.keys(), three_lotto_2013.values())
    make_graphlotto(three_lotto_2014.keys(), three_lotto_2014.values())

graph3lotto()

def graph6lotto():#แสดงกราฟรางวัลที่หนึ่ง
    """Separate each number in 6 number lottery and print graph of 6 number lottery."""
    digit1, digit2, digit3, digit4, digit5,digit6 = lotto_six()
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

    make_graphlotto(list_of_num, list_of_times1)
    make_graphlotto(list_of_num, list_of_times2)
    make_graphlotto(list_of_num, list_of_times3)
    make_graphlotto(list_of_num, list_of_times4)
    make_graphlotto(list_of_num, list_of_times5)
    make_graphlotto(list_of_num, list_of_times6)
graph6lotto()
