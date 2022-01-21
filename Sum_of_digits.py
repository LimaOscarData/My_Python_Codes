# Write a function to find the sum of the digits of a number in Python?
def sum_of_digits():
    my_input=input("Please enter a number that you want to sum :")
    try:
        int(my_input)
    except ValueError :
        print("Please enter only numbers !")
    else:
        print(sum([int(i) for i in my_input]))
        # my_total=0
        # for i in my_input:
        #     my_total+=int(i)
        # print(my_total)

sum_of_digits()
# Please enter a number that you want to sum :123456
# 21
# Please enter a number that you want to sum :a123456
# Please enter only numbers !
# Please enter a number that you want to sum :-----
# Please enter only numbers !

