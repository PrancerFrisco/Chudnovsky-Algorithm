from mpmath import mp, mpf, sqrt
from numpy import power
from time import time

print("Chudnovsky algorithm")


# THE FUNCTION
def chudnovsky(digits):
    mp.dps = digits + 10  # extra precision
    C = mpf(426880) * sqrt(10005)
    L = mpf(13591409)
    M = mpf(1)
    X = mpf(1)
    K = mpf(-6)
    a1 = mpf(0)

    L_const = 545140134
    X_const = -262537412640768000
    for q in range(digits):
        e = (M * L) / X
        if a1 + e == a1:  # if the value of a1 is the same as it was before the latest a1 += e. i.e, the value added is so small that it doesn't get computed
            result = f"after {q} iterations: {str(C * a1 ** -1)[:digits+1]}" # cuts off extra potentially inaccurate digits
            mp.dps = 10
            return result
        a1 += e
        L += L_const
        X *= X_const
        K += 12
        M_operation = (power(K, 3) - 16*K) / (q+1)**3
        M *= M_operation
    result = str(C * a1 ** -1)[:digits+1] # incase it doesn't break out of the previous loop
    mp.dps = 10
    return result





# GET USER INPUT
while True: # loops until an integer is entered
    try:
        user_input = int(input("\nHow many digits?: "))
        break # this only get executed if the user types a valid integer
    except ValueError: # if the user types in something that cant be interpreted as an integer
            print("Enter an integer")


start = time()
print()
print(chudnovsky(user_input))
print()
print(f"Elapsed time: [{time() - start}s]")
