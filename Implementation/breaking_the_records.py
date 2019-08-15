# https://www.hackerrank.com/challenges/breaking-best-and-worst-records/problem
def breakingRecords(scores):
    # lists with highest, lowest
    records = [scores[0],scores[0]]
    breaks = [0,0]
    for score in scores:
        if score < records[1]:
            records[1] = score
            breaks[1] += 1
        elif score > records[0]:
            records[0] = score
            breaks[0] += 1
    return breaks
