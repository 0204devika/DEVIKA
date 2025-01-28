def bank_loan_eligibility(salary,age,credit_score):
    min_salary=30000             # this the eligibilty that user should have, to get the loan.
    min_age=22
    min_credit_score=650
    if salary<min_salary:
        return "Loan is rejected, because of the Insufficient salary"
    if age<min_age:
        return "Loan is rejected, because of the age"
    if credit_score<min_credit_score:
        return "Loan is rejected, because of the less credit score"
    else:
        return "Congratulations!!!, you loan is approved"
def main():
    salary=int(input("enter salary:"))
    age=int(input("enter age:"))
    credit_score=int(input("enter credit score:"))
    print(bank_loan_eligibility(salary,age,credit_score))
main()