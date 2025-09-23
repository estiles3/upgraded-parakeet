if __name__ == '__main__':
    ourlist = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        ourlist.append([name,score])
    ourlist.sort( key=lambda x:x[1] )
    results = []
    win = min(ourlist, key= lambda x:x[1] )
    # print(win)
    for x in ourlist:
        if (x[1] > win[1]):
            secondvalue = x[1]
            break
    for x in ourlist:
        if(x[1] > win[1] and secondvalue == x[1]):
            results.append(x)
        if (secondvalue < x[1]):
            break
    results.sort(key=lambda x:x[0])
    for x in results:
        print(x[0])