try:
    v = int(input("Enter price :"))
    r = 100 / v
    # Code
except ValueError:
    print("Sorry! Invalid number. Please try again!")
# except ZeroDivisionError:
#     print("Sorry! Enter non-zero as input!")
except Exception as ex:
    print("Error :", ex)


print('The End')



