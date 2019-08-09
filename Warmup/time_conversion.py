# https://www.hackerrank.com/challenges/time-conversion/problem
def timeConversion(s):
  time_arr = s.split(':')
  # handle case for 12:00:00 AM - 1:00:00 AM
  if s[8] == "A" and (int(s[0]), int(s[1])) == (1,2):
    updated_hours = "00"
    time_arr[0] = updated_hours
  # handle PMs
  if s[8] == "P" and (int(s[0]), int(s[1])) != (1,2):
    updated_hours = str(int(time_arr[0]) + 12)
    time_arr[0] = updated_hours
  # remove the AM/PM suffix
  removed_suffix = time_arr[2][0] + time_arr[2][1]
  # assemble new string
  converted_time = f"{time_arr[0]}:{time_arr[1]}:{removed_suffix}"
  return(converted_time)
