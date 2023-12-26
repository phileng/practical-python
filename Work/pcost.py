# pcost.py
#
# Exercise 1.27
# read portfolio.csv, calc cost to buy all shares
totalcost = 0.0

f = open('Data/portfolio.csv', 'rt')
headers = next(f).split(',')
#print (headers)

for line in f:
    row = line.split(',')
    # extract each share's quantity * price and sum it up    
    # print (row[0], row[1], row[2])
    totalcost = totalcost + (int(row[1]) * float(row[2]))

print ("cost to buy:", totalcost)


f.close()
