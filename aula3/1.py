if __name__ == '__main__':
    x,y,o,f = list(map(int,input().split())) + [lambda x,y,o: print(x+y if o == 1 else x-y)]
    f(x,y,o)