def fizzbuzz(n):
    if n%3==0 and n%5==0:        #check if number is divisible by 3 and 5
        return "FizzBuzz"
    elif n%3==0:                  #check if number is divisible by 3
        return "Fizz"             
    elif n%5==0:                  #check if number is divisible by 5
        return "Buzz"
    else:
        return n                  #if number is not divisible by 3 and 5, return number itself
def main():
    for i in range(1, 101):
        print(fizzbuzz(i))
main()