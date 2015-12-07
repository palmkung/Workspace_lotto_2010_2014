import csv
with open("List_of_lotto_2010_2014 - Sheet1 (1).csv") as csvfile:
    reader = csv.DictReader(csvfile)
    
    prize = [row['3Last2'] for row in reader]
    year_10 = {}
    year_11 = {}
    year_12 = {}
    year_13 = {}
    year_14 = {}
    count = 24
    for num in range(count):
        if prize[num] not in year_10:
            year_10[prize[num]] = 1
        else: 
            year_10[prize[num]] += 1
    count = 48
    for num in range(24, count):
        if prize[num] not in year_11:
            year_11[prize[num]] = 1
        else: 
            year_11[prize[num]] += 1
            
    count = 72
    for num in range(48,count):
        if prize[num] not in year_12:
            year_12[prize[num]] = 1
        else: 
            year_12[prize[num]] += 1
            
    count = 96
    for num in range(72, count):
        if prize[num] not in year_13:
            year_13[prize[num]] = 1
        else: 
            year_13[prize[num]] += 1
            
    count = 120
    for num in range(96, count):
        if prize[num] not in year_14:
            year_14[prize[num]] = 1
        else: 
            year_14[prize[num]] += 1
    
    print(year_10)
    print(year_11)
    print(year_12)
    print(year_13)
    print(year_14)
