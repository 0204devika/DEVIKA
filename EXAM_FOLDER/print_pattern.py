def print_pattern(n):
    for i in range(1, n + 1):
        print('*' * i)
def main():
    n=int(input("enter n:"))               # Get the number of rows from the user
    print("pattern is:")
    print_pattern(n)
    print("reverse pattern is:")
    for i in range(n,0,-1):              # Loop from n to 1 to print the reverse pattern
        print('*' * i)  
main()
   
