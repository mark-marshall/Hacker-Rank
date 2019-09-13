# Luhn algorithm
def checksum(cardNum):
    A = 0
    B = 0
    numStr = str(cardNum)
    for idx, num in enumerate(reversed(numStr)):
        # check if num is at even idx
        if idx % 2 == 0:
            # increment A
            A += int(num)
        # check if num is at odd idx
        elif not (idx % 2 == 0):
            # multiply by 2
            holding_num = int(num) * 2
            final_num = holding_num
            # check whether holding_num is double digits
            # and add digits together if so
            if final_num > 9:
                final_num = 0
                for dig in str(holding_num):
                    final_num += int(dig)
            # increment B
            B+= final_num
    # apply checksum rules using A and B
    if (A + B) % 10 == 0:
        return 'Yes'
    else:
        return 'No'
