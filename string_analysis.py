def rev_str(s,p1,p2):
    l=list(s)                   # Convert the string to a list
    while p1<=p2:               # Swap the characters at positions p1 and p2
        l[p1],l[p2]=l[p2],l[p1]
        p1+=1
        p2-=1
    ans="".join(l)             # Convert the list back to a string
    return ans
def string_analyzer(s):
    vowels=['a','e','i','o','u','A','E','I','O','U']
    consonants=['B','C','D','F','G','H','J','K','L','M','N','P','Q','R','S','T','V','W','X','Y','Z','b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']
    digits=['0','1','2','3','4','5','6','7','8','9']
    special_chars=['!','@','#','$','%','^','&','*','(',')','<','>','~','-','_']
    count={'vowels':0,'consonants':0,'digits':0,'special_chars':0}             # Initialize a dictionary to count each category
    for ch in s:
        if ch in vowels:
            count['vowels']+=1
        elif ch in consonants:    
            count['consonants']+=1
        elif ch in digits:
            count['digits']+=1
        elif ch in special_chars:
            count['special_chars']+=1
    return count
def main():
    s=input("enter string:")
    print(string_analyzer(s))
    print(rev_str(s,0,len(s)-1))
main()
        
            
    
