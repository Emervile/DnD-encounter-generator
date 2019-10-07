import random

loot = ['10 pounds of coal', '5 vials of Minor Healing', '4 daggers', 'a ring of Spell Storage', 'a wand of Fireball', '50 gold coins', 'a Quicksilver long sword', '25 fire arrows',
        'a staff of Turn Undead', '5 Clockwork Bombs', '6 poitions of Greater Healing', 'a Astral Dimond']
dice_number = ['1', '2-10', '11-20', '21-30', '31-40', '41-50', '51-60', '61-70', '71-80', '81-90', '90-99', '100']
encounter = list(zip(dice_number, loot))

def rolling_encounter():
  roll = random.randint(1,100)
  print('Rolling for LOOT!')
  print(roll)
  if roll == 1:
    return print('You have rolled a ' + str(roll) + ', in the chest you find ' + (loot[0]) + '!')
  elif roll <= 10:
    return print('You have rolled a ' + str(roll) + ', in the chest you find ' + (loot[1]) + '!')
  elif roll <= 20:
    return print('You have rolled a ' + str(roll) + ', in the chest you find ' + (loot[2]) + '!')
  elif roll <= 30:
    return print('You have rolled a ' + str(roll) + ', in the chest you find ' + (loot[3]) + '!')
  elif roll <= 40:
    return print('You have rolled a ' + str(roll) + ', in the chest you find ' + (loot[4]) + '!')
  elif roll <= 50:
    return print('You have rolled a ' + str(roll) + ', in the chest you find ' + (loot[5]) + '!')
  elif roll <= 60:
    return print('You have rolled a ' + str(roll) + ', in the chest you find ' + (loot[6]) + '!')
  elif roll <= 70:
    return print('You have rolled a ' + str(roll) + ', in the chest you find ' + (loot[7]) + '!')
  elif roll <= 80:
    return print('You have rolled a ' + str(roll) + ', in the chest you find ' + (loot[8]) + '!')
  elif roll <= 90:
    return print('You have rolled a ' + str(roll) + ', in the chest you find ' + (loot[9]) + '!')
  elif roll <= 99:
    return print('You have rolled a ' + str(roll) + ', in the chest you find ' + (loot[10]) + '!')
  elif roll == 100:
    return print('You have rolled a ' + str(roll) + ', in the chest you find ' + (loot[11]) + '!')

rolling_encounter()
