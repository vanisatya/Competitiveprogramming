def get_max_profit(stock_prices):

    # Calculate the max profit
      
    if len(stock_prices) < 2:
        raise ValueError('Minimum of 2 prices are required to calculate profit')
    min_price  = stock_prices[0]
    max_profit = stock_prices[1] - stock_prices[0]
    for current_time in xrange(1, len(stock_prices)):
        current_price = stock_prices[current_time]
        current_profit = current_price - min_price
        max_profit = max(max_profit, current_profit)
        min_price  = min(min_price, current_price)

    return max_profit
