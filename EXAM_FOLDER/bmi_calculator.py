def bmi_cal(weight,height):
    return weight/height**2               #this is the formula of bmi
def main():
    weight=float(input("enter the weight:"))
    height=float(input("enter the height:"))
    bmi=bmi_cal(weight,height)
    if bmi<=12:
      print("underweight")                
    if bmi>12 and bmi<25:
      print("normal")
    if bmi>25:
      print("overweight")
    if bmi>50:
      print("obese")
main()
