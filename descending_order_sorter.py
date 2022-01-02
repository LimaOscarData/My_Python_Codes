def desc_order_sorter():
    user_value = int(input("please enter a number that you want to order as upper element :"))
    # I will use the list comprehension technique
    my_list = sorted([i for i in range(1, user_value+1)], reverse=True)
    print(my_list)

desc_order_sorter()   # lets call the function