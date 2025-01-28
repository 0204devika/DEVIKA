def odd_and_even_separator(arr):
    odd=[]               #list created to add odd elements
    even=[]              #list created to add even elements 
    for i in arr:
        if i%2==0:       # check if number is divisible by 2 and add it into even list
            even.append(i)
        else:
            odd.append(i)  
    return f"odd list is: {odd} and even list is: {even}"
def main():
    arr=list(map(int,input("enter the list of numbers:").split()))       #input of the list
    print(odd_and_even_separator(arr))
main()