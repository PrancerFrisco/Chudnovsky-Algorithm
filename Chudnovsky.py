from mpmath import mp, mpf
from math import factorial
from time import time

print("Chudnovsky algorithm")





# THE FUNCTION
def chudnovsky(digits):
    mp.dps = digits + 10  # extra precision
    C = mpf(426880) * (mpf(10005) ** mpf(0.5))
    L = mpf(13591409)
    M = mpf(1)
    X = mpf(1)
    K = mpf(-6)
    a1 = mpf(0)
    a2 = mpf(0)
    for q in range(digits):
        e = (M * L) / X
        a1 += e
        if a1 == a2:  # if the value of a1 is the same as it was before the latest a1 += e. i.e, the value added is so small that it doesn't get computed
            break  # stops summation
        a2 += e  # updates the variable a2 AFTER checking if a1 == a2
        L += mpf(545140134)
        X *= mpf(-262537412640768000)
        K += 12
        M *= (mpf(K)**mpf(3) - mpf(16)*mpf(K)) / (mpf(q+1)**mpf(3))


    print()
    return str(C * a1 ** -1)[:-10]  # cuts off extra potentially inaccurate digits








# GET USER INPUT
while True: # loops until an integer is entered
    try:
        user_input = int(input("\nHow many digits?: "))
        break # this only get executed if the user types a valid integer
    except ValueError: # if the user types in something that cant be interpreted as an integer
            print("Enter an integer")




# PRINT RESULTS
start_time = time()
print(BetterChudnovsky(user_input))
print()
print(f"Elapsed time: [{time() - start_time}s]") # outputs elapsed time
