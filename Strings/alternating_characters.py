# https://www.hackerrank.com/challenges/alternating-characters/problem
def alternatingCharacters(s):
    deletions = 0
    for idx,char in enumerate(s):
        if (not idx == (len(s) - 1)) and (char == s[idx + 1]):
            deletions += 1
    return deletions
