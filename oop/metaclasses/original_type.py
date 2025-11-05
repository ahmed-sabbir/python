def main():
    name = 'Point'
    bases = (object,)
    methods = {
        "__init__": __init__,
        "move": move
    }
    Point = type(name, bases, methods)
    p = Point(1, 2)
    print(type(p))

def __init__(self, x, y):
    self.x = x
    self.y = y

def move(selff, dx, dy):
    self.x += dx
    self.y += dy

if __name__ == '__main__':
    main()