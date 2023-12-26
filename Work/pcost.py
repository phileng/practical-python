# pcost.py
#
# Exercise 1.27
import sys
import os

def portfolio_cost(filename):
    print("entering def")
# read portfolio.csv, calc cost to buy all shares
    totalcost = 0.0
    print(filename)
#    f = open('Data/portfolio.csv', 'rt')
    f = open(filename, 'rt')
    headers = next(f).split(',')
#print (headers)

    for line in f:
        row = line.split(',')
    # extract each share's quantity * price and sum it up    
    # print (row[0], row[1], row[2])
        try:
            totalcost = totalcost + (int(row[1]) * float(row[2]))
        except ValueError:
            print("couldnt parse", line)

    print ("inside def Total cost:", totalcost)
    f.close()

print(sys.argv)
print(os.getcwd())

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = '/Users/phileng/src/1)python/practical-python/Work/Data/portfolio.csv'
print(filename)

portfolio_cost(filename)
#print('outside def Total cost:', cost)
