def password_strength_checker(s):
    if len(s)<8:             #if password length is less than 8, it is not a strong password
        return "Password should contain atleast 8 characters"
    if not any(c.isupper() for c in s):      #check if password contains anu upper case letters
        return "password should have at least one uppercase letter"
    if not any(c.islower() for c in s):       #check if password contains any lower case letters
        return "password should have at least one lowercase letter"
    if not any(c.isdigit() for c in s):       #check if password contains any number
        return "password should have at least one digit"
    if not any(c in "!@#$%^&*()-+" for c in s):  #ch3ck if password contains any special character or not
        return "password should have at least one special character"
    else:
        return "password is strong"          
def main():
    s = input("Enter your password: ")
    print(password_strength_checker(s))
main()