import csv
with open("List_of_lotto_2010_2014 - Sheet1.csv") as csvfile:
    reader = csv.DictReader(csvfile)
    table = [row['3Last1'] for row in reader]
    year = [row['Year'] for row in reader]
    dic1 = {}
    dic2 = {}
    dic3 = {}
    dic4 = {}
    dic5 = {}
    count = 0
    for i in table:
        if count <= 24:
            if i not in dic1:
                dic1[i] = 1
                count += 1
            else:
                dic1[i] += 1
                count += 1
        elif count <= 48:
            if i not in dic2:
                dic2[i] = 1
                count += 1
            else:
                dic2[i] += 1
                count += 1
        elif count <= 72:
            if i not in dic3:
                dic3[i] = 1
                count += 1
            else:
                dic3[i] += 1
                count += 1
        elif count <= 96:
            if i not in dic4:
                dic4[i] = 1
                count += 1
            else:
                dic4[i] += 1
                count += 1
        else:
            if i not in dic5:
                dic5[i] = 1
                count += 1
            else:
                dic5[i] += 1
                count += 1
    print(dic1)
    print(dic2)
    print(dic3)
    print(dic4)
    print(dic5)