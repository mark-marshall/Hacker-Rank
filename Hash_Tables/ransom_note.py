# https://www.hackerrank.com/challenges/ctci-ransom-note/problem
def checkMagazine(magazine, note):
    hash_table = {}
    for mag_word in magazine:
        if mag_word in hash_table:
            hash_table[mag_word] += 1
        else:
            hash_table[mag_word] = 1
    for note_word in note:
        if note_word in hash_table and hash_table[note_word]:
            hash_table[note_word] -= 1
        else:
            return "No"
    return "Yes"
     