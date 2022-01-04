def GCD():
    num_1=int(input("Please enter the first number :"))
    num_2 = int(input("Please enter the second number :"))
    if num_1>num_2:
        divisor_num=num_2
    else:
        divisor_num=num_1
    for i in range(1,divisor_num+1):
        if num_1 % i == 0 and num_2 % i == 0:
            biggest_divisor=i
    print("Your biggest divisor number is {}.".format(biggest_divisor))
    # if you want to use it for future programs you need it use return(....)

GCD()