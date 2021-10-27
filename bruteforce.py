import csv


def loading_data(file):
    # reading *.csv file
    data = csv.DictReader(open(file))

    shares = []

    for row in data:

        share = [row['name'], float(row['price']), float(row['profit'])]
        shares.append(share)
        # if len(shares)>3:
        #     break

    # print(len(shares))
    search_best_profit(shares)


def search_best_profit(data):
    budget_max = 500
    best_shares = []

    # generating each unique permutation possible
    combinations = []
    if not combinations:
        starter_list = []
        combinations.append(starter_list)
    for item in data:
        sub_sets = [sub+[item] for sub in combinations]
        combinations.extend(sub_sets)

    # deleting empty list at index 0, to avoid iteration error in get price and
    # profit functions
    combinations.pop(0)

    # checking for each permutation if cost is under 500, then check if profits
    # is larger than actual best
    for shares in combinations:
        if get_price(shares) <= budget_max:
            if get_profits(shares) > get_profits(best_shares):
                best_shares = shares
    display_best(best_shares, get_price(best_shares))


def get_price(data):
    price = 0
    for share in data:
        price += share[1]
    return price


def get_profits(data):
    profits = 0
    for share in data:
        profits += share[2]
    return profits


def display_best(shares, budget):
    total_profit = 0
    for share in shares:
        print(share[0])
        total_profit += share[2]
    rendement = (total_profit / budget) * 100
    print('\n Cout : {} €.'.format(budget))
    print('\n Benefice total : {:.2f} €, rendement : {:.2f} %.'.format(
        total_profit, rendement))


if __name__ == '__main__':
    loading_data('shares.csv')
