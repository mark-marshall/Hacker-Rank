# https://www.hackerrank.com/challenges/climbing-the-leaderboard/problem
def climbingLeaderboard(scores, alice):
  # initialize variables
  answer = []
  alice_idx = len(alice) - 1
  scores_idx = 0
  cur_rank = 1
  # logic loop
  while len(answer) < len(alice):
    if (scores_idx == len(scores) - 1) and (alice[alice_idx] < scores[scores_idx]):
        cur_rank += 1
        answer.append(cur_rank)
        alice_idx -= 1
    elif alice[alice_idx] > scores[scores_idx]:
      answer.append(cur_rank)
      alice_idx -= 1
    elif alice[alice_idx] < scores[scores_idx]:
      scores_idx += 1
      if scores[scores_idx] < scores[scores_idx - 1]:
        cur_rank += 1
    elif alice[alice_idx] == scores[scores_idx]:
      answer.append(cur_rank)
      alice_idx -= 1
  return reversed(answer)
