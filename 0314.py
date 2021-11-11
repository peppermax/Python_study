a=int(input('整数値a：'))
b=int(input('整数値b：'))
c = b != 0 and a % b
print(c, end='・・・')
if c:
  print('aはbで割り切れません。')
else:
  print('bが０またはaがbで割り切れます。')