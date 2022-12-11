import re
def CodelandUsernameValidation(strParam):
  pass_match = re.match('^[a-zA-Z]\w{2,23}[a-zA-Z0-9]$', strParam)
  return True if pass_match else False
