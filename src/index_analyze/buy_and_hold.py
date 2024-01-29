# might need merge
def calc_shares(prices):
    return 1/prices

def sum_shares(shares):
    return shares.rolling(f"{365 * 5}d").sum()