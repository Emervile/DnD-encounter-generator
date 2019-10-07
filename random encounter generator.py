import random

creatures = ['1 Red Dragon', '20 Skeletons!', '13 Bandits', '15 Gnolls', '2 Wraiths', '10 Murlocks', '8 spiders', '3 werewolves', '3 elementals', '5 shadowhounds', '3 arcanians', 'Nothing!']
dice_number = ['1', '2-10', '11-20', '21-30', '31-40', '41-50', '51-60', '61-70', '71-80', '81-90', '90-99', '100']
encounter = list(zip(dice_number, creatures))

#print(encounter)

def rolling_encounter():
  roll = random.randint(1,100)
  print('Rolling encounter')
  print(roll)
  if roll == 1:
    return print('You have rolled a ' + str(roll) + ', now you must face ' + (creatures[0]) + '!')
  elif roll <= 10:
    return print('You have rolled a ' + str(roll) + ', now you must face ' + (creatures[1]) + '!')
  elif roll <= 20:
    return print('You have rolled a ' + str(roll) + ', now you must face ' + (creatures[2]) + '!')
  elif roll <= 30:
    return print('You have rolled a ' + str(roll) + ', now you must face ' + (creatures[3]) + '!')
  elif roll <= 40:
    return print('You have rolled a ' + str(roll) + ', now you must face ' + (creatures[4]) + '!')
  elif roll <= 50:
    return print('You have rolled a ' + str(roll) + ', now you must face ' + (creatures[5]) + '!')
  elif roll <= 60:
    return print('You have rolled a ' + str(roll) + ', now you must face ' + (creatures[6]) + '!')
  elif roll <= 70:
    return print('You have rolled a ' + str(roll) + ', now you must face ' + (creatures[7]) + '!')
  elif roll <= 80:
    return print('You have rolled a ' + str(roll) + ', now you must face ' + (creatures[8]) + '!')
  elif roll <= 90:
    return print('You have rolled a ' + str(roll) + ', now you must face ' + (creatures[9]) + '!')
  elif roll <= 99:
    return print('You have rolled a ' + str(roll) + ', now you must face ' + (creatures[10]) + '!')
  elif roll == 100:
    return print('You have rolled a ' + str(roll) + ', now you must face ' + (creatures[11]) + '!')

rolling_encounter()

