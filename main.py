from random import randint
switch = True

def roll_dice():
  return randint(1,6)

def main():
  global switch 
  #agar bisa merubah variabel dari dalam function. Tapi hanya function ini saja yang bisa merubah
  #function lain juga harus menerapkan "global" untuk variabelnya agar bisa dirubah
  
  print('Type 1 if you want to roll the dice')
  print('Type 2 if you want to quit')

  try:
    option = int(input('Enter your option: '))
  except ValueError:
    print('That is not an option')
    return
  
  if option == 1:
    print(f'You got {roll_dice()}!')
  elif option == 2:
    switch = False
  else:
    print('That is not an option')

while switch:
  main()