def prob18():
    a=range(14)
    a.reverse()
    for row in a:
        for item in range(row+1):
            actual[row][item]=max(actual[row+1][item],actual[row+1][item+1])+actual[row][item]
            print(actual[row][item])
