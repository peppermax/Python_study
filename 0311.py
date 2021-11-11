n=int(input('整数値：'))
if n == 0:
  print('その値は０です。')
elif n >= -9 and n <= 9:
  print('その値は１桁です。')
else:
  print('その値は２桁です。')