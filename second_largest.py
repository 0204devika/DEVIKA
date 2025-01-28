def second_largest(arr):
    if len(arr) < 2:       # If there are fewer than 2 elements, return None since a second largest element doesn't exist
        return None
    else:
        max_n=float('-inf')          # Initialize max and second_max with negative infinity
        second_max_n=float('-inf')
        for i in range(len(arr)):
            if arr[i]>max_n:           # If current element is greater than the max found so far
                second_max_n=max_n      # Update second max to previous max
                max_n=arr[i]            # Update max to current element
            elif arr[i]>second_max_n and arr[i]!=max_n:  # Update second max if current element is greater than it but not equal to max
                second_max_n = arr[i]
                second_max_n=arr[i]
    return second_max_n 
def main():
    arr=list(map(int,input("enter the list of numbers:").split()))
    print(second_largest(arr))
main()
