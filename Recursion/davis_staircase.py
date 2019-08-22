# https://www.hackerrank.com/challenges/ctci-recursive-staircase/problem
def stepPerms(n):
    c = [0] * (n+1)
    def stepPermsCalc(n,c):
        if n < 0:
            return 0
        elif n <= 1:
            return 1
        elif c[n]:
            return c[n]
        else:
            c[n] = stepPermsCalc(n-1,c) + stepPermsCalc(n-2,c) + stepPermsCalc(n-3,c)
            return c[n]
    return stepPermsCalc(n,c)