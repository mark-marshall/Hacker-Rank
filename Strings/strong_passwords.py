# https://www.hackerrank.com/challenges/strong-password/problem
def minimumNumber(n, password):
  unmet_rules = 0
  regex_rules = ["[0-9]","[a-z]","[A-Z]","[!@#$%^&*()\-+]"]
  for rule in regex_rules:
    if not re.findall(rule,password):
        unmet_rules += 1
  if len(password) + unmet_rules < 6:
    return 6 - len(password)
  else:
    return unmet_rules
