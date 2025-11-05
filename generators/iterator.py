class Countdown(object):
    def __init__(self,start):
        self.start = start

    def __iter__(self):
        n = self.start
        while n > 0:
            yield n
            n -=1


c = Countdown(5)
for x in c:
    print(x)

print('--------------------')


c=Countdown(2)
for x in c:
    print(x)