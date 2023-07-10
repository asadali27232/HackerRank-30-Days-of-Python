if __name__ == '__main__':
    n = int(input().strip())
    n = "{0:b}".format(int(n))

    arr = n.split('0')
    print(len(max(arr)))