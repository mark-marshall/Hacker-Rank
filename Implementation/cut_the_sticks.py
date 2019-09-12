# https://www.hackerrank.com/challenges/cut-the-sticks/problem
def cutTheSticks(arr):
    num_sticks = []
    # nested recursive function
    def cut(arr):
        if not len(arr) == 0:
            num_sticks.append(len(arr))
            to_cut = min(arr)
            next_arr = []
            for stick in arr:
                new_height = stick - to_cut
                if new_height > 0:
                    next_arr.append(new_height)
            cut(next_arr)
    cut(arr)
    return num_sticks
