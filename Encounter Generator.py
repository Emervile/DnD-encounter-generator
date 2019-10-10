import random
#character generator
race = ['Dragonborn', 'Dwarf', 'Elf', 'Gnome', 'Half Elf', 'Half Orc', 'Halfling', 'Human', 'Tiefling', 'Changeling', 'Eladrin', 'Genasi']
classes = ['Paladin', 'Ranger', 'Rogue', 'Wizard', 'Warlock', 'Sorcerer', 'Cleric', 'Druid', 'Psion', 'Arteficer', 'Warlord', 'Fighter']
creature = ['10 Bunnies', '3 Bandits', '2 Wizards', '4 Gnolls', 'An Evil Warlock', '4 Skeletons', '3 Wolves', 'A Driad', '3 Wraiths', '5 Zombies', 'A Warewolf', 'A Giant']
magic_item = ['A Wooden Sword', 'A Great Axe', 'A Chaos Wand', 'Giant Stength Gloves', 'Wand of Fireballs', 'A staff of the Ram', 'A Revolver', 'An Enchanted Bow', 'A Thunder Hammer', 'A Vampiric Dagger', 'A Vorpal Sword', 'Crown Render']
random_character = []
random_creature = []
random_magic_item = []
def random_character_generator():
  roll = random.randint(1,10)
  random_character.append(race[roll -1])
  rolla = random.randint(1,10)
  random_character.append(classes[rolla -1])
  rollb = random.randint(1,10)
  random_creature.append(creature[rollb -1])
  rollc = random.randint(1,10)
  random_magic_item.append(magic_item[rollc -1])
  return 'Your new character is a', random_character, 'who must fight ', random_creature, 'with ', random_magic_item

print(random_character_generator())
