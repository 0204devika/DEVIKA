def prime(n):
      if n<=1:                    # If the number is less than or equal to 1, it's not prime
          return False
      if n==2:
          return True
      if n%2==0:                  # Any other even number is not prime
          return False
      for i in range(3, int(n**0.5) + 1,2):   # If 'n' is divisible by any of these numbers, it's not prime
          if n % i == 0:
              return False
      return True                      # If no factors found, n is prim
while True:
    start=int(input("enter first number:"))
    end=int(input("enter last number:"))
    if start>=0 and end>=0 and start<=end: # Check for valid input where start is less than or equal to end, and both are non-negative
        break
    print("invalid input")
ans=[]                                 # List to store prime numbers
for i in range(start,end+1):
      if prime(i):
          ans.append(i)
print(ans)