def grep(pattern, file):
    with open(file) as f:
        for line in f:
            if pattern in line:
                yield line

for line in grep('IBM', '../data/portfolio.csv'):
    print(line)

print('-------------------------------\n')


'''
  Using generator expressions instead of list comprehensions can save memory.
'''
with open('../data/portfolio.csv') as f:
    ibm = (line for line in f if 'IBM' in line)  # <--- this is the generator exppression
    for line in ibm:
        print(line)
