import csv


def loading_data(file):
    # reading *.csv file
    data = csv.DictReader(open(file))

    shares = []
    for row in data:
        share = ([row['name'], float(row['price']),
                  float(row['profit']) * float(row['price'])])
        shares.append(share)


def knapsack(data):
    name = []

    #weight
    price = []

    #value
    profits = []

    limit = 500

    for share in data:
        name.append(share[0])
        price.append(share[1])
        profits.append(share[2])





if __name__ == '__main__':
    loading_data('shares.csv')
