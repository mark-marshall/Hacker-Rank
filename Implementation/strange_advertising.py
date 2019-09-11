# https://www.hackerrank.com/challenges/strange-advertising/problem
def viralAdvertising(n):
  people = 5
  cum_liked = 0
  for i in range (n):
    cum_liked += people // 2
    people = (people // 2) * 3
  return cum_liked
  