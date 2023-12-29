# report.py
#
# Exercise 2.4
import csv

def read_portfolio(filename):
    # reads a file into a list of tuples
    portfolio = []
    with open(filename,'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            holding = (row[0], int(row[1]), float(row[2]))
            portfolio.append(holding)
    return portfolio

def calc_pcost(portfolio):
    total = 0.0
    for name, shares, price in portfolio:
        total += shares*price
    return total

fn='Data/portfolio.csv'
fn2='Data/prices.csv'

def read_portfolio2(filename):
    # reads a file into a list of dicts
    portfolio2 = []
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
#            name, shares, price = row.split(',')
#            print(name, shares, price)
#            print(row)            
            #insert into dict, then append to list            
            dict = {
                'name' : row[0], 
                'shares' : int(row[1]), 
                'price' : float(row[2])
            }
            portfolio2.append(dict)

    return portfolio2


def read_prices(filename):
    # read prices file into dict
    prices = {}
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        for row in rows:
#            print(row)
            try:
                prices[row[0]] = float(row[1])
            except IndexError:
                pass

    return prices

def read_pr2(filename):
    #read prices file into dict
    d = {}
    with open(filename) as f:
        rows = csv.reader(f)
        
#        data = next(rows)
#        a, b = list(data)
#        d[a] = b
#        print(d)

        for data in rows:
            try:
                data = next(rows)
                a, b = list(data)
                d[a] = b
                #print(d)

            except StopIteration:
                pass

    print(d)
    return d
        

pt = read_portfolio2(fn)
pr = read_prices(fn2)

tc = 0.0
for s in pt:
    tc += s['shares'] * s['price']
print('TC =', tc)

tv = 0.0
for s in pt:
    tv += s['shares']*pr[s['name']]

print('CV is =', tv)
print("PnL is:", round(tv - tc,2))

