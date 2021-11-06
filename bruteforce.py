import csv
from glob import glob


def loading_data(file):
    """
    loading function
    :param file: csv file name to analyse
    :return: None, call knapsack function
    """

    # reading *.csv file
    data = csv.DictReader(open(file))

    shares = []

    for row in data:
        if float(row['price']) > 0 and float(row['profit']) > 0:
            price = float(row['price'])
            profit = price * float(row['profit']) / 100
            share = [row['name'], price, profit]
            shares.append(share)

    search_best_profit(shares, 500)


def search_best_profit(data, max_budget):
    """
    function to find the best shares combination
    :param data: list of shares : [name, price, profit]
    :param max_budget: int, max value to spend.
    :return: None, call display_best function
    """

    budget_max = max_budget
    best_shares = []

    # generating each unique combinations possible
    combinations = []

    # need an empty list in combinations for starting the powerset
    if not combinations:
        starter_list = []
        combinations.append(starter_list)

    # creating for each share a copy of each combinations already in the list,
    # and adding the new share on every copy. Then add those new combinations
    # to the list
    for item in data:
        sub_sets = [sub + [item] for sub in combinations]
        combinations.extend(sub_sets)

    # deleting empty list at index 0, to avoid iteration error in get price and
    # profit functions
    combinations.pop(0)

    # checking for each combinations if cost is under 500, then check if
    # profits is larger than actual best
    for shares in combinations:
        if get_price(shares) <= budget_max:
            if get_profits(shares) > get_profits(best_shares):
                best_shares = shares
    display_best(best_shares, get_price(best_shares))


def get_price(data):
    """
    function to get the total cost of a set of shares
    :param data: list of shares : [name, price, profit]
    :return: float
    """

    price = 0
    for share in data:
        price += share[1]
    return price


def get_profits(data):
    """
    Function to get profits form a set of shares
    :param data: list of shares : [name, price, profit]
    :return: float
    """

    profits = 0
    for share in data:
        profits += share[2]
    return profits


def display_best(shares, budget):
    """
    function to display the best shares combination, their total cost, and
    their profits
    :param shares: list of shares : [name, price, profit]
    :param budget: float, total cost of the shares
    :return:  None, print the results
    """

    total_profit = 0
    for share in shares:
        print(share[0])
        total_profit += share[2]
    rendement = (total_profit / budget) * 100
    print('\n Cout : {} €.'.format(budget))
    print('\n Benefice total : {:.2f} €,'
          ' rendement : {:.2f} %.'.format(total_profit, rendement))


# time for :
# 20 shares :   2.54s    cost :     498.00€,    profits :     99.08€

def main():
    """
    Main function, user choose which file to analyse.
    :return: None, call loading_data function
    """

    csv_files = glob("csv_files/*.csv")

    for index, file in enumerate(csv_files):
        print(index, file[10:])

    sel = int(input("Entrez l'index du fichier à analyser : "))
    loading_data(csv_files[sel])


if __name__ == '__main__':
    main()
