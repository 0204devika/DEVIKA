def leap_year(n):
    if n%4==0 and (n%100!=0):              #check if number is divisible by 4 and not divisible by 100
        return True
    elif n%400==0:                         #check is number is divisible by 400(for century years)
        return True
    else:
        return False                       #if above conditions are not met,the year is not leapp year, return false
def main():
    t=int(input("enter number of test cases:"))         #testcases, it allows users to check multiple years
    for _ in range(t):
        n=int(input("enter year:"))
        if leap_year(n):
            print(n,"is a leap year")
        else:
            print(n,"is not a leap year")
main()
