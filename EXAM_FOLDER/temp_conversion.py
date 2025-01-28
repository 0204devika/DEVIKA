#f=9/5*c+32
#k=c+273.15
#c=k-273.15
#c=(f-32)*5/9

def temp_conv_cel_fah(cel,fah):
    return 9/5*cel+32
def temp_conv_fah_cel(fah,cel):
    return (fah-32)*5/9
def temp_conv_cel_kel(cel,kel):
    return cel+273.15
def temp_conv_kel_cel(kel,cel):
    return kel-273.15
def temp_conv_fah_kel(fah,kel):
    return (fah-32)*5/9+273.15
def temp_conv_kel_fah(kel,fah):
    return (kel-273.15)*9/5+32
def main():
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")
    print("4. Kelvin to Celsius")
    print("5. Fahrenheit to Kelvin")
    print("6. Kelvin to Fahrenheit")
    choice=int(input("Enter your choice: "))
    if choice==1:
        cel=float(input("Enter temperature in Celsius: "))
        fah=temp_conv_cel_fah(cel,0)
        print(f"{cel}°C is equal to {fah}°F")
    elif choice==2:
        fah=float(input("Enter temperature in Fahrenheit: "))
        cel=temp_conv_fah_cel(fah,0)
        print(f"{fah}°F is equal to {cel}°C")
    elif choice==3:
        cel=float(input("Enter temperature in Celsius: "))
        kel=temp_conv_cel_kel(cel,0)
        print(f"{cel}°C is equal to {kel}°K")
    elif choice==4:
        kel=float(input("Enter temperature in Kelvin: "))
        cel=temp_conv_kel_cel(kel,0)
        print(f"{kel}°K is equal to {cel}°C")
    elif choice==5:
        fah=float(input("Enter temperature in Fahrenheit: "))
        kel=temp_conv_fah_kel(fah,0)
        print(f"{fah}°F is equal to {kel}°K")
    elif choice==6:
        kel=float(input("Enter temperature in Kelvin: "))
        fah=temp_conv_kel_fah(kel,0)
        print(f"{kel}°K is equal to {fah}°F")
    else:
        print("Invalid choice")
main()
    