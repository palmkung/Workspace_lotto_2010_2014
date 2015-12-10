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