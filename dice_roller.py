import random 

def main():
  while True:    
    try:
      dice_rolls = int(input('Please choose the number of die: '))  
    except Exception as exc:      
      print(f'{exc} Please input a whole number, Only')
      continue
    break
  dice_sum =0
  for i in range(0,dice_rolls):
    roll = random.randint(1,6)
    dice_sum += roll
    if roll == 1:
      print(f'You rolled a {roll}! Critical fail')
    elif roll == 6:
      print(f'You rolled a {roll}! Critical success')      
    else:
      print(f'You rolled a {roll}')
  print(f'You have rolled a total of {dice_sum}')  

if __name__== "__main__":
  main()