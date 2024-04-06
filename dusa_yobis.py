size = int(input())

while True:
    yobi = int(input())
    if yobi < size:
        size += yobi
    else:
        print(size)
        break
