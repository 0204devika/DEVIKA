def main():
    n=int(input("enter the number:"))      #input of number for which table will be printed
    rng=int(input("enter the range:"))     #input of range upto which table will be printed
    for i in range(1,rng+1):
        print(f"{n}x{i}={n*i}")
main()