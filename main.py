Student: Mathias Thorkild Liendgaard 

#Imports
import random
import numpy as np



# Functions
def simulate_customers():
    studentArrive = np.random.poisson(studentLambda)
    i=0
    payingStudent = 0
    while i != studentArrive:
        buy = random.randint (0,1)
        if buy == 1:
          payingStudent += 1
          i += 1
        else:
            i += 1
    print(f"There are {i} students at university and {payingStudent} bought something from the cafeteria")
    return payingStudent


def purchases(buyers , inventories):
    j=0
    sales = []
    soldItems = []
    while j != buyers:
        itemsBought = random.choices(items, weights=[2,1,2], k=random.randint(1,len(items)))
        j += 1
        for t in itemsBought:
            index = items.index(t)
            if inventories[index] > 0:
                sales.append(prices[index])
                soldItems.append(index)
                inventories[index] = inventories[index]-1
            # if inventories[index] == 0:
                # print(f"We are sold out of {index}, and lost a sale")
    return sum(sales), sales, soldItems


def generate_report(money, soldItems):
    profit = money - sum(costs)
    print(20*"---")
    print("---Super Fancy Sales Report---")
    print(f"We sold {(len(soldItems))} items: {soldItems.count(0)} sandwiches, {soldItems.count(1)} salads and {soldItems.count(2)} cakes")
    print(f"Total revenue for the day is: {money}")
    print(f"We have {inventories[0]} sandwices, {inventories[1]} salads and {inventories[2]} cakes leftover")
    print(f"The total costs of the food is {sum(costs)}")
    print(f"Which results in a profit of: {profit}")

def average_sales(nRuns, q):
    averageSales = []
    for i in range(nRuns):
        inventories = [0, 0, q]
        customers = simulate_customers()
        income, sales = purchases(customers, inventories)
        expense = sum(costs)
        profit = (income-expense)
        averageSales.append(profit)

    average= sum(averageSales)/len(averageSales)
    return average


# Main Programme
# for q in range(370, 430, 10):
items = ["Sandwich", "Salad", "Cake"]
prices = [65, 45, 50]
inventories = [400, 200, 400]
costs = [(prices[0]/2)*inventories[0], (prices[1]/2)*inventories[1], (prices[2]/2)*inventories[2]]
studentLambda = 1000


payingStudent = simulate_customers()
sumsales, sales, solditems = purchases(payingStudent , inventories)

generate_report(sumsales, solditems)

#Using the average sales funciton and the for loop in the main programme, i found the optimal quantity of each food type

#optimal sandwiches is 400 with 1000 customers 
#optimal salads is 200 with 1000 customers
#optimal cakes is 400 with 1000 customers
    # profit = average_sales(1000, q)
    # print(f"{q}: {profit}")
