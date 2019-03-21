class Solution:
    def maxProfit(prices):
        lowest_num = min(prices[0:len(prices)-1])
        index = prices.index(lowest_num)
        prices = prices[index:len(prices)]
        highest_num = max(prices)
        answer = highest_num - lowest_num
        print(highest_num, lowest_num)


    maxProfit([2, 4,1])