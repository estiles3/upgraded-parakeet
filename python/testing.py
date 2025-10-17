with open('my_file.txt', 'w') as f:
    number = int(input())
    f.write(str(number//2)+"\n")
    for x in range(0,number,2):
        f.write(str(x)+"\n")
    f.write("2")