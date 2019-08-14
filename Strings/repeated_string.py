# https://www.hackerrank.com/challenges/repeated-string/problem
import re
def repeatedString(s, n):
  if not re.findall(r"[^a]", s):
    return n
  else:
    whole_nums = n // len(s)
    remainder = n % len(s)
    num_as = len(re.findall(r"a", s))
    num_as_in_remainder = len(re.findall(r"a",s[:remainder]))
    return (whole_nums * num_as) + num_as_in_remainder
    