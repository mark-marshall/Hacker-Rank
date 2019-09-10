# https://www.hackerrank.com/challenges/bon-appetit/problem
def bonAppetit(bill, k, b):
    actual = 0
    for idx,item_value in enumerate(bill):
        if not idx == k:
            actual += item_value
    actual //= 2
    if not actual == b:
        print(b - actual)
    else:
        print("Bon Appetit")
        