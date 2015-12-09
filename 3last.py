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
def make_input():
        prize1 = csv_reader()
        prize2 = [row['3Last2'] for row in reader]
        #prize3 = [row['3Last3'] for row in reader]
        #prize4 = [row['3Last4'] for row in reader]
        print(prize1)
        #print(prize2)
        #print(prize3)
        #print(prize4)
make_input()
csv_reader()