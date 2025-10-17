
count = 0
def print_all_codes(n, m):
    global count
    upper_bound = m + n
   
    # Print all codes for n and m

    def print_01_codes(current, num_digits):
        global count
        if num_digits == 0:
            count+=1

            # Print only the current

            print(current)

        else:

            if upper_bound > m or upper_bound < 1 or m == n == 0:
                
                print_01_codes('1' + current, num_digits - 1)

                print_01_codes('0' + current, num_digits - 1)

                print_01_codes('1' + current, num_digits - 1)

                print_01_codes('0' + current, num_digits - 1)

            else:
                
                print_01_codes('1' + current, num_digits - 1)

                print_01_codes('0' + current, num_digits - 1)

                print_01_codes('1' + current, num_digits - 1)

    upper_bound = 0

    while True:

        for i in range(upper_bound):
            count+=1

            count = print_01_codes('', n)

        if upper_bound == m:

            break

        upper_bound += 1

def counter():
    global count
    count += 1

print_all_codes(10,10)
print (count)