def factorial_using_loop(n):
    if n<0:                              # Edge case: Factorial is not defined for negative numbers
        return "Factorial does not exist for negative numbers"
    if n == 0:                           #Edge case: Factorial of zero is one
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i                  #multiply the result with current value i.
    return result
def main():
    n=int(input("enter the number:"))
    print(factorial_using_loop(n))
main()
    