import csv


def loading_data(file):
    # reading *.csv file
    data = csv.DictReader(open(file))

    shares = []
    for row in data:
        share = [row['name'], float(row['price']), float(row['profit'])]
        shares.append(share)


def knapsack(data):
    return




if __name__ == '__main__':
    loading_data('shares.csv')
