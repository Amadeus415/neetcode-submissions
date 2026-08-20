class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        lowest = prices[0]
        output = 0
        for i in range(len(prices)):
            num = prices[i]
            if num < lowest:
                lowest = num
                continue
                

            # save greatest diff
            if (num - lowest) > output:
                output = (num - lowest)

        return output