import csv

def read_portfolio(filename, *, errors='warn'): # the * forces the argument following it to be named, the callers have to use portfolio_cost('Data/portfolio.csv', errors='warn')
    '''
    Read a CSV file with name,date,shares,price into a list.
    '''
    if errors not in {'warn', 'silent', 'raise'} : 
        raise ValueError ("Errors must be one of 'warn', 'silent, 'raise'")

    portfolio = []
    with open(filename, 'r') as f:
        rows = csv.reader(f)
        headers = next(rows) # skip the header row
        for rowNumber,row in enumerate(rows, start=1):
            try: 
                row[2] = int(row[2])
                row[3] = float(row[3])
            except ValueError as err: # don't catch errors that you cannot recover from, i.e. FileNotFoundError. Here ValueError is recoverable
                if errors == 'warn':
                    print('Row: ',rowNumber,'Bad row: ', row)
                    print('Row: ',rowNumber,'Reason: ', err)
                elif errors =='raise':
                    raise   # Reraises the last exception
                else:
                    pass    # Ignore
                continue    # Skips to the next line
            # record = tuple(row)
            record = {
                "name" : row[0],
                "date" : row[1],
                "shares" : row[2],
                "price" : row[3]
            }
            portfolio.append(record)
    return portfolio


portfolio = read_portfolio('Data/portfolio4.csv', errors='warn')
print(portfolio)

total = 0.0
for holding in portfolio:
    total += holding['shares'] * holding['price']
print('Total cost: ', total)