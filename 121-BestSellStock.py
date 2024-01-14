class Solution:
    def maxProfit(self, prices) -> int:
        # current index has to be greater han the previous index to get max value
        # declare a max variable for maximized profit
        # change the max var 
        
        # loop through the array starting with [0], another loop for i + 1 until end

        # the stock on ith day must be greater than price[i] in order to chan
        profit = 0
        

        # TODO:[7,1,5,3,6,4] -> output 6. Day 5, index 4
        # TODO: [7,6,4,3,1] -> output 0
        # TODO: [3,10,4,12] -> output 9
        
        l = 0
        r = l + 1

        profit = 0
        max_price = max(prices)
        
        for i in range(len(prices)):
            # get the max val of the array
            # check if the nums being compared is larger than the max
            # 
            if prices[i] > max_price:
                profit = prices[i] - 

                    
           
        return max_price
                
        

def main():
    prices = [7,6,4,3,1]

    sol = Solution()
    solution = sol.maxProfit(prices)
    print(solution)
        
if __name__ == "__main__":
    main()



        