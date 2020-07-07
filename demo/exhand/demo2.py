try:
    v = int(input("Enter price :"))
    r = 100 / v
    # Code
except ValueError:
    print("Sorry! Invalid number. Please try again!")
except ZeroDivisionError:
    print("Sorry! Enter non-zero as input!")

print('The End')



