class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Use two-pointer method:
        
        if x < 0:
            return False
        arr = str(x)
        l, r = 0, len(arr) - 1
        
        # While the left pointer is not greater than the right pointer and both pointers hit the same index and none of the cases failed, then it is a palindrome

        while l < r:
            if arr[l] != arr[r]:
                print("it is not a palindrome")
                return False
            l+=1
            r-=1
        return True
           

        

def main():
    sol = Solution()
    sol.isPalindrome(121)
        
if __name__ == "__main__":
    main()

        
        