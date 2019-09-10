# https://www.hackerrank.com/challenges/electronics-shop/problem
def getMoneySpent(keyboards, drives, b):
    # initalize variables
    cur_largest = -1
    cur_keyboard_idx = 0
    cur_drive_idx = 0
    # loop until all items have been examined
    while cur_drive_idx < len(drives):
        cur_value = keyboards[cur_keyboard_idx] + drives[cur_drive_idx]
        # check to see value is within budget and larger than cur_largest
        if cur_value <= b and cur_value > cur_largest:
            cur_largest = cur_value
        if cur_keyboard_idx < len(keyboards) - 1:
            cur_keyboard_idx += 1
        else:
            cur_keyboard_idx = 0
            cur_drive_idx += 1
    # return either -1 or largest calculated sum
    return cur_largest
    