# https://www.hackerrank.com/challenges/compare-the-triplets/problem
def compareTriplets(a, b):
    score = [0,0]
    for idx, alice_comparator in enumerate(a):
        if alice_comparator > b[idx]:
            score[0] += 1
        elif alice_comparator < b[idx]:
            score[1] += 1
    return score
