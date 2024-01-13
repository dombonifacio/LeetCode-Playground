class Solution:
    def maxProfit(self, prices) -> int:
        # current index has to be greater han the previous index to get max value
        # declare a max variable for maximized profit
        # change the max var 
        
        # loop through the array starting with [0], another loop for i + 1 until end

        # the stock on ith day must be greater than price[i] in order to chan
        max = 0
        

        # TODO:[7,1,5,3,6,4] -> output 6. Day 5, index 4
        # TODO: [7,6,4,3,1] -> output 0
        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                if prices[i] < prices[j]:
                    if prices[j] - prices[i] > max:
                        max = prices[j] - prices[i]
                    
           
        return max
                
        

def main():
    prices = [7,6,4,3,1]

    sol = Solution()
    solution = sol.maxProfit(prices)
    print(solution)
        
if __name__ == "__main__":
    main()



        