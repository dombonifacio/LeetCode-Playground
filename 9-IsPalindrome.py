class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Use two-pointer method:
        
        arr = list(str(x))
        l, r = 0, len(arr) - 1
        
        # While the left pointer is not greater than the right pointer and both pointers hit the same index and none of the cases failed, then it is a palindrome

        while l < r:
            if arr[l] != arr[r]:
                print("it is not a palindrome")
                return False
            print("it is a palindrome")
             # If l and r pointer matches with each other in every loop, it is a palindrome
            return True

        

def main():
    sol = Solution()
    sol.isPalindrome(293)
        
if __name__ == "__main__":
    main()

        
        