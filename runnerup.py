if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    # arr.sort(key=lambda x:x)
    ourlist = sorted(list(arr))
    win = max(ourlist)
    # runner = min(ourlist)
    # for x in ourlist:
    #     if (x>win):
    #         runner = win
    #         win = x
    #     elif (x > runner and x != win):
    #         runner = x
    while (ourlist[-1] == win):
        ourlist.pop(-1)
        
    print (ourlist[-1])