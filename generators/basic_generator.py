'''
Generator function
'''
def countdown(n):
    print('Counting down from ', n)
    while n > 0 :
        yield n #emit a value
        n -=1
    print('Done')

def main():
    for x in countdown(5):
        print(x)
    
    c = countdown(2)
    it = c.__iter__()
    print(it)
    #print(it.__next__())

if __name__ == '__main__':
    main()