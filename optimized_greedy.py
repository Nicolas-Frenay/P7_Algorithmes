from csv import DictReader
from glob import glob
from operator import itemgetter


def loading_data(file):
    """
    loading function
    :param file: csv file name to analyse
    :return: None, call knapsack function
    """

    # reading *.csv file
    data = DictReader(open(file))

    shares = []

    # Cleaning data at this step, if a share have an incoherent price or
    # profit value, it's not included.

    for row in data:
        if float(row['price']) > 0 and float(row['profit']) > 0:
            ratio = float(row['profit'])
            price = float(row['price'])
            # profit : absolute benefit from a share
            profit = (price * ratio)/100
            share = [row['name'], price, ratio, profit]
            shares.append(share)
    knapsack(shares, 500)


def knapsack(data, max_budget):
    """
    function that calculate the best set of shares for maximizing profits.
    :param data: list extract from csv file : [name, price, ratio, profit]
    :param max_budget: int, max value to spend.
    :return: None, call display_best function
    """
    budget = max_budget
    capacity = 0
    remain = max_budget
    best_shares = []

    # sorting shares by percentage
    shares = sorted(data, key=itemgetter(2), reverse=True)

    i = 0
    while capacity < budget:
        if shares[i][1] < remain:
            best_shares.append(shares[i])
            capacity += shares[i][1]
            remain -= shares[i][1]
        i += 1
        # security, in case of very short data set, to avoid indexing error.
        if i == len(shares):
            break

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
        total_profit += share[3]
    rendement = (total_profit / budget)*100
    print('\n Cout : {:.2f} €.'.format(budget))
    print('\n Benefice total : {:.2f} €,'
          ' rendement : {:.2f} %.'.format(total_profit, rendement))


# time for :
# 20 shares :   0.041s   cost :     498.00€,    profits :     97,48€,
# dataset1 :    0.053s   cost :     499.94€,     profits :   198.51€,
# dataset2 :    0.048s   cost :     499.98€,     profits :   197.77€.


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
