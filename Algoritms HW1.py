#compute the sum of digits in all numbers from 1 to n
def sum_to_n(n):
    return (n * (n +1)) / 2


test_n = 4
print("The sum of digits is: ", int(sum_to_n(test_n)))


#find max number
number1 = int(input("Input number 1: "))
number2 = int(input("Input number 2: "))
number3 = int(input("Input number 3: "))

def find_max(n1, n2, n3):
    if n1 > n2 and n1 > n3:
        return n1
    if n2 > n1 and n2 > n3:
        return n2
    return n3


print("The max number is: ", find_max(number1, number2, number3))


#count the number of even an odd digits of the whole number
def count_evens_odds(n):
    evens = 0
    odds = 0

    while n != 0:
        current_digits = n % 10
        if current_digits % 2:
            odds += 1
        else:
            evens += 1

            return ["Number of even digits is: " + str(evens), "Number of odd digits is: " + str(odds)]


print(count_evens_odds(743679))