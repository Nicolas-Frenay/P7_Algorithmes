from csv import DictReader


def loading_data(file):
    # reading *.csv file
    data = DictReader(open(file))

    shares = []
    for row in data:
        price = float(row['price'])
        profit = price * float(row['profit'])/100
        # price*100 to only deal with int, profit *1000 to deal with int, and
        # to avoid rounding errors.
        share = [row['name'], int(price*100), int(profit*1000)]
        shares.append(share)
    knapsack(shares, 500)


def knapsack(data, max_budget):
    #values
    profits = []
    #weight
    prices = []
    #limit, *100 for avoiding index error with float noumbers
    budget = max_budget*100
    shares= []
    best_shares = []

    for share in data:
        if share[1] > 0:
            shares.append(share)
            profits.append(abs(share[2]))
            prices.append(abs(share[1]))


    # knapsack algo
    n = len(profits)
    table = [[0 for _ in range(budget + 1)] for _ in range(n + 1)]

    for i in range(n + 1):
        for j in range(budget + 1):
            if i == 0 or j == 0:
                table[i][j] = 0
            elif prices[i - 1] <= j:
                table[i][j] = max(profits[i - 1]
                                  + table[i - 1][j - prices[i - 1]],
                                  table[i - 1][j])
            else:
                table[i][j] = table[i - 1][j]

    result = table[n][budget]

    # getting shares
    for i in range(n, 0, -1):
        if result <= 0:
            break
        if result == table[i-1][budget]:
            continue
        else:
            best_shares.append(shares[i-1])
            result = result - profits[i-1]
            budget = budget - prices[i-1]

    display_best(best_shares, get_price(best_shares))


def get_price(data):
    price = 0
    for share in data:
        price += share[1]
    return price/100


def display_best(shares, budget):
    total_profit = 0
    for share in shares:
        print(share[0])
        total_profit += share[2]/1000
    rendement = (total_profit / budget)*100
    print('\n Cout : {} €.'.format(budget))
    print('\n Benefice total : {:.2f} €, rendement : {:.2f} %.'.format(
        total_profit, rendement))

# time for 20 shares : 0.63s, dataset1 : 29.9s, dataset2 : 17.7s
if __name__ == '__main__':
    loading_data('dataset1_Python+P7.csv')
    # loading_data('shares.csv')
