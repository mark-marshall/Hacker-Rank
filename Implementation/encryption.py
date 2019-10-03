# https://www.hackerrank.com/challenges/encryption/problem
def encryption(s):
  # remove all whitespace
  arrS = list(s.replace(" ",""))
  # calculate rows and columns
  rows = math.floor(math.sqrt(len(arrS)))
  cols = math.ceil(math.sqrt(len(arrS)))
  # create array of arrays
  encryptAtt = []
  cur_num = 0
  cur_arr = 0
  for char in arrS:
    if cur_num == 0:
      encryptAtt.append([char])
      cur_num += 1
    elif cur_num == cols - 1:
      encryptAtt[cur_arr].append(char)
      cur_num = 0
      cur_arr += 1
    else:
      encryptAtt[cur_arr].append(char)
      cur_num += 1
  # create final encrypted s
  num_arrs = len(encryptAtt)
  cur_arr = 0
  cur_idx = 0
  encryptS = ''
  while True:
    if cur_arr == num_arrs:
      cur_arr = 0
      cur_idx += 1
      encryptS += " "
    elif cur_idx < len(encryptAtt[cur_arr]):
      encryptS += encryptAtt[cur_arr][cur_idx]
      cur_arr += 1
    elif cur_idx < rows:
      cur_arr = 0
      cur_idx += 1
      encryptS += " "
    else:
      break
  # remove final space after last letter and print
  return(encryptS.rstrip())
  