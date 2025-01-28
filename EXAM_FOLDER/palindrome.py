def palindrome(s,p1,p2):
    while p1<=p2:
        if s[p1]!=s[p2]:     #if characters at index p1 and p2 are not equal, then it is not a palindrome, return false
            return False
        p1+=1                #move p1 forward and p2 backward to check next pair of characters
        p2-=1
    return True              #if all characters matched return true
def is_pal(s):
    return palindrome(s,0,len(s)-1)     #call palindrome function with p1 as starting index and p2 as last index
def main():
    t=int(input("enter testcases:"))     #get number of testcases from user
    for _ in range(t):
        s=input("enter string:")
        if(is_pal(s)):
            print("yes")
        else:
            print("no")
main()
