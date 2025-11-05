class Manager(object):
    def __enter__(self):
        print('Entering')
        return 'some value'
    
    def __exit__(self, ty, val, tb):
        print("Exting")
        print(ty,val,tb)


def main():
    m = Manager()
    with m: # the context manager drives the with statement
        print('Manage me!!')

    with m as val: # as qualifier is driven by the return statement of __enter__ function
        print('val=', val)


if __name__ == '__main__':
    main()