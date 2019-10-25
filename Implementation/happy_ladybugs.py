# https://www.hackerrank.com/challenges/happy-ladybugs/problem
def happyLadybugs(b):
  # check if it's a single char
  if len(b) == 1:
    if b[0] == '_':
      return 'YES'
    else:
      return 'NO'
  happy = True
  blanks = False
  tally = {}
  for idx,bug in enumerate(b):
    # determine whether already happy
    # check if at start or end
    if idx == 0 and not (bug == b[idx+1]):
      happy = False
    elif idx == len(b) - 1 and not (bug == b[idx-1]):
      happy = False
    # otherwise check if same as one before or one after
    else:
      if not (bug == b[idx-1] or bug == b[idx+1]):
        happy = False
    # determine whether more than one of at least each ladybug
    # determine whether there's an empty space
    if bug == '_':
      blanks = True
    elif bug not in tally:
      tally[bug] = 'Unmatched'
    else:
      tally[bug] = 'Matched'
  available_pairs = not 'Unmatched' in tally.values()
  # check if criteria are met
  if happy or (available_pairs and blanks):
    return 'YES'
  else:
    return 'NO'
