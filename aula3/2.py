if __name__ == '__main__':
    f, f2 = lambda x: print(f"Maior valor: {max(x[0], x[1])}"), lambda x: print(f"Menor valor: {min(x[0], x[1])}")
    [f(list((map(int, input().split())))) for x in range(2)] + [f2(list((map(int, input().split()))))]


