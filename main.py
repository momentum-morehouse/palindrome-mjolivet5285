import re

string = input('enter your string:')
house = re.sub(r'[^A-Za-z]','', string.lower())
if house == house[::-1]:
  print('String is Palindome')
else:
  print('String is not Palindome')