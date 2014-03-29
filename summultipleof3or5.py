#Multiples of 3 and 5
#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
#The sum of these multiples is 23.
#
#Find the sum of all the multiples of 3 or 5 below 1000.


def multiple3or5(num):
    if num % 3 == 0:
        return True
    elif num % 5 == 0:
        return True
    else:
        return False


def sum_multiples_of_3or5(max_num):
    total = 0
    for i in range(1, max_num + 1):
        if multiple3or5(i):
            print("multiple: ", i)
            total += i
    print("Sum: ", total)


sum_multiples_of_3or5(9)
sum_multiples_of_3or5(999)
