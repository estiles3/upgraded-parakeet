def is_leap(year):
    leap = False
    
    # Write your logic here
    # print(year%4,year%100,year%400)
    if(year%4 == 0):
        if (year%100 == 0 and year %400 != 0):
            leap = False
        else:
            leap = True
    return leap

year = int(input())
print(is_leap(year))