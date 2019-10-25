# https://www.hackerrank.com/challenges/happy-ladybugs/problem
def happyLadybugs(b):
  # check if it's a single char
  if len(b) == 1:
    if b[0] == '_':
      return 'YES'
    else:
      return 'NO'
  unhappy = False
  blanks = False
  tally = {}
  for idx,bug in enumerate(b):
    # determine whether already happy
    # check if at start or end
    if idx == 0 and not (bug == b[idx+1]):
      unhappy = True
    elif idx == len(b) - 1 and not (bug == b[idx-1]):
      unhappy = True
    # otherwise check if same as one before or one after
    else:
      if not (bug == b[idx-1] or bug == b[idx+1]):
        unhappy = True
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
  if (available_pairs and blanks) or (not unhappy):
    return 'YES'
  else:
    return 'NO'
