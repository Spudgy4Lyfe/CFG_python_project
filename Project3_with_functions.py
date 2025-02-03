import csv

# 1. read the data from the spreadsheet
# this function will read the data from the spreadsheet and return data in [{}{}] format


def read_data():
    data = []  # initialise empty list

    with open("sales.csv", "r") as sales_csv:
        spreadsheet = csv.DictReader(sales_csv)

        for row in spreadsheet:
            data.append(row)

    return data

# 2. collect all of the sales from each month into a single list


def sales_list():
    data = read_data()  #calling the read_data() function above to have access to the data from csv
    sales_list = []

    for row in data:
        sales_list.append(int(row["sales"]))

    return sales_list


# 3. output the total sales across all months


def total_sales(l):  # takes a list as parameter and then sums up all list's values to a total
    total = sum(l)
    return total


# 4. calculate the average


def average(l):  #takes a list as parameter and returns average of the lists' values; to check against eg sales_list()
    average = round((sum(l) / len(l)),2)
    return average

# 5. create a dict with months names + sales values - probably redundant but hey-ho!


def months_sales():
    data = read_data()  #reads data from csv
    sales = sales_list()  #creates a list of sales values
    months_list = []  #initialises empty list of months names

    for row in data:
        months_list.append(row["month"])  #appends months names to the months_list

    months_sales = dict(zip(months_list,sales))  #zips 2 lists together to create a dictionary of months names + sales values

    return months_sales

# 6. output months with highest and lowest sales; min = Feb : 1521, max = Jul : 7479


def max_min(d):  #takes dictionary as parameter, returns keys attached to highest/lowest value followed by the value

    return max(d, key=d.get), d[max(d, key=d.get)], min(d, key=d.get), d[min(d, key=d.get)]


# 7. function which outputs summary of the calculations in nice format


def run():

    print("Monthly sales' list: {}".format(sales_list()))
    print("Total sales across all months: {}".format(total_sales(sales_list())))
    print("Months with highest and lowest sales: {}".format(max_min(months_sales())))
    print("Average sales' value per month: {}".format(average(sales_list())))


run()
