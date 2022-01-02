# Try to find out if a number you get from the user is perfect.
# A number is called a "perfect number" if the sum of its divisors is equal to itself.
# For example, 6 is a perfect number. (1 + 2 + 3 = 6)
def find_perfect_num():
    my_num = int(input("please enter a number, that you want to check whether it's a perfect number or not :"))
    div_nums_total = 0
    # div_nums_total = sum([i for i in range(1,my_num) if my_num % i == 0])
    for i in range(1, my_num):
        if my_num % i == 0:
            div_nums_total += i
        else:
            pass
    if div_nums_total == my_num:
        print("{} is a perfect number.".format(my_num))
    else:
        print("{} is not a perfect number.".format(my_num))

find_perfect_num()  # then we call the function
