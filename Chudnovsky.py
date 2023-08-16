from mpmath import mp, mpf
from math import factorial
from time import time

print("Chudnovsky algorithm")





# THE FUNCTION
def chudnovsky(digits):  # however many digits here is how many digits are guaranteed correct
    mp.dps = digits + 10 # extra precision
    C = mpf(426880) * (mpf(10005) ** mpf(0.5))
    a1 = mpf(0)
    a2 = mpf(0)

    for q in range(digits):
        e = mpf(factorial(6 * q)) / mpf((factorial(3 * q)) * mpf((factorial(q)) ** mpf(3))) * (mpf(545140134) * mpf(q) + mpf(13591409)) / (mpf(-262537412640768000) ** mpf(q))
        a1 += e
        if a1 == a2: # if the value of a1 is the same as it was before the latest a1 += e. i.e, the value added is so small that it doesn't get computed
            break # stops summation
        a2 += e # updates the variable a2 AFTER checking if a1 == a2

    print()
    return str(C * a1 ** -1)[:-10]  # cuts off extra potentially inaccurate digits










# GET USER INPUT
while True: # loops until an integer is entered
    try:
        user_input = int(input("\nHow many digits?: "))
        break # this only get executed if the user types a valid integer
    except ValueError: # if the user types in something that cant be interpreted as a integer
            print("Enter an integer")






# PRINT OUT RESULT
start_time = time() # starts stopwatch
print(chudnovsky(user_input))
print()
print(f"Elapsed time: [{time() - start_time}s]") # outputs elapsed time






# HOW LONG IT TOOK MY LAPTOP TO RUN FOR DIFFERENT AMOUNTS OF DIGITS
#5000 = 1s
#10000 = 5s
#15000 = 12s
#20000 = 30s
#25000 = 60s
#30000 = 100s
#35000 = 266s
