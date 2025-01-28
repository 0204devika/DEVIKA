def bill_splitter(amount,people,tip_percent):             #this is the function that is used to calculate the total amount of meoney.
    total_amount=amount+(tip_percent/100 *amount)
    return total_amount/people
def main():
    amount=float(input("enter the total amount:"))
    people=int(input("enter the total number of people:"))
    tip_percent=int(input("enter the tip percentage:"))
    ans=bill_splitter(amount,people,tip_percent)
    print("amount each person has to pay is:",ans)
main()

    