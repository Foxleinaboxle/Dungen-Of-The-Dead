## Text Monster Game
## The goal of this game is to beat the monsters and claim the prize at the end of the dungeon.

# Map of the dungeon
# Feel free to adapt and design your own level. The whole map must be at least 3 floors and 15 rooms total, though.
floor0 = ['a large dimly lit hall', 'a sword', 'a room with a chest', 'a room with fountain', 'a room with 3 goblins', 'a stair case']
floor1 = ['a stair case', 'a room with an orc', 'a room with a chest', 'a spell tome', 'a sword', 'a stair well']
floor2 = ['a stair well', 'a magic sword', 'a sword', 'a room with a large undead', 'Dracoth the necromancer', 'a room full of loot and riches']
floors = [floor0, floor1, floor2]

# Items in the player's possession
inventory = []

# Player's current position in the dungeon
# The player starts in the first room on floor 0
currentFloor = 0
currentRoom = 0

# Keep track of whether the game is in progress or over (so we know when to stop the game loop)
gameState = 'ongoing'
print('''
█▀▄ █░█ █▄░█ █▀▀ █▀▀ █▀█ █▄░█   █▀█ █▀▀   ▀█▀ █░█ █▀▀   █▀▄ █▀▀ ▄▀█ █▀▄
█▄▀ █▄█ █░▀█ █▄█ ██▄ █▄█ █░▀█   █▄█ █▀░   ░█░ █▀█ ██▄   █▄▀ ██▄ █▀█ █▄▀''')

input('*poof* (A shadowy figure now stands before you) Greetings Adventurer, I see that you have found my castle leave now or face your INEVITABLE DEMISE!! MWAHAHAHAHAHAHA... *poof* (and with a cloud of smoke the figure vanishes)')
print('*ping* (The ominous warning does not deter you. You steel your nerves and enter the castle through the large wooden doors infront of you. )')
print('_______________________________')
print(' ')
while gameState == 'ongoing':
  # Describe the room the player is in
  if currentFloor == 0:
    floor = floor0
  elif currentFloor == 1:
    floor = floor1
  else:
    floor = floor2
  room = floor[currentRoom]
  print(' ')
  print(('<-['), room, (']->'))
  print(' ')
  print('Room:', currentRoom)
  print( 'Floor:', currentFloor)
  print("Bag", inventory)
  print('_______________________________')
  # You need to handle describing the other cases..

  # Get command from the player
  choice = input('What action would you like to take? ')

  # Respond to command
  if choice == 'help':
    # Help: display all commands
    # Note that the "pass" keyword in Python is a placeholder for lines where the interpreter would normally expect to see code. If control flow reaches the line with "pass", the interpreter "passes" over the line (i.e. does nothing).
    print('your comands are; Left, Right, Up, Down, Grab, Fight, Enter')

  elif choice == 'left':
    Monster=floors[currentFloor][currentRoom]
    if currentRoom == 0:
      print('*ping* (There is nothing here but the wall of the room)')
    elif Monster == 'a room with an orc':
      print('*ping* (You atempted to sneak past the monster(s) and failed. By the way the monster(s) thought you were delicious.) ')
      gameState = 'GameOver'
    else:
      print('You have left the room, now before you is... ')
      currentRoom= currentRoom -1
    pass 
  elif choice == 'right':
        # if floor[currentRoom] has a monster in it they die
    Monster=floors[currentFloor][currentRoom]
    if Monster == 'a room with 3 goblins':
      print('*ping* (You atempted to sneak past the monster(s) and failed. By the way the monster(s) thought you were delicious.) ')
      gameState = 'GameOver'
    elif Monster == 'a room with a large undead':
      print('*ping* (You atempted to sneak past the monster(s) and failed. By the way the monster(s) thought you were delicious.) ')
      gameState = 'GameOver'
    elif Monster == 'Dracoth the necromancer':
      print('*ping* (You atempted to sneak Dracoth the necromancer and failed. He caught you and turned you into one of his many undead solders) ')
      gameState = 'GameOver'
    elif  currentRoom==5:
      print('*ping* (There is nothing here but the wall of the room)')
  
    else:
      print('*ping* (You have left the room, now before you is... )')
      currentRoom = currentRoom + 1
    pass
  elif choice == 'up':
    # Player wants to go upstairs
    if room == floor0[5] or room == floor1[0]:
      print('*ping* (You ascend the stair case, now before you is... )')
      currentFloor = currentFloor +1
    else:
      print('*ping* (There is nothing above you except the ceiling. )')
  elif choice == 'down':
    # Player wants to go downstairs
    if room == floor1[5] or room == floor2[0]:
      print('*ping* (You descend the stair well, now before you is... )')
      currentFloor = currentFloor -1
    else:
      print('*ping* (There is nothing below you except the cold stone floor. )')
  elif choice == 'grab':
    # Player wants to grab item from the room'
    
    Item= floors[currentFloor][currentRoom]
    if Item == 'a sword':
      print('*ping* (Sword was added to your bag)')
      inventory.append('Sword')
      floors[currentFloor][currentRoom] = 'a dimly lit room'
    elif Item == 'a magic sword':
      print('*ping* (Hero Sword was added to your bag)')
      inventory.append('Hero Sword')
      floors[currentFloor][currentRoom] = 'a room with a pedastal'
    
    elif Item == 'a spell tome':
      print('*ping* (Spell Tome was added to your bag)')
      inventory.append('Spell Tome')
      floors[currentFloor][currentRoom] = 'a room with a pedastal'
    elif Item == 'a room with a chest':
      print('*ping* (As you open the chest, it opens on its own and awakens into a mimic, eating you whole in one bite...)')
      gameState = 'GameOver'
    elif Item == "a room full of loot and riches":
      print('*ping* (You sucessfully defeated Dracoth the necromancer and claimed the treasure)')
      gameState = 'won'
    else:
      print('*ping* (This room contains nothing of value)')

    
  elif choice == 'fight':
    # Player wants to fight monster in the room
    Monster=floors[currentFloor][currentRoom]
    if inventory == ["Sword"] and room == floor0[4] or room==floor1[1]:
      print('*ping* (You and the monster(s) fought ruthlessly. In the end you came out victorious, but not unscathed your trusty sword is no longer usable...) ')
      inventory.remove("Sword")
      floors[currentFloor][currentRoom] = 'a room with body(s) on the floor'
    elif inventory == ['Spell Tome', 'Hero Sword', 'Sword'] and room==floor2[3]:
      print('*ping* (You and the monster(s) fought ruthlessly. In the end you came out victorious, but not unscathed your trusty sword is no longer usable...) ')
      inventory.remove("Sword")
      floors[currentFloor][currentRoom] = 'a room with body(s) on the floor'
    
    elif inventory == ['Spell Tome', 'Hero Sword'] and room == floor2[4]:
      print('Ah. Adventurer you have done well to make it this far but, defeating me will not be as easy. Prepare for your DOOM... ')
      print(' ')
      print('*ping* (You and Dracoth the necromancer fought a rigorous and bloody battle. Just when it seemed like you were about to reach your end, you cast the banishing spell. And sent Dracoth to the ethereal plain, never to be seen again...) ')
      floors[currentFloor][currentRoom] = 'a large destroyed throne room with a mystirous portal in the middle.'
    else:
      print('*ping* (You atempted to fight the monster(s) and failed. Now you have become but one of many zombies under Dracoth the necromancers controll... ')
      gameState = 'GameOver'
 
      #This is the DLC
      
  elif choice == 'enter':
    portal = floors[currentFloor][currentRoom]
    if portal == 'a large destroyed throne room with a mystirous portal in the middle.':
      print('*ping* (You enter through the portal fearfull of what is on the other side. As you do it closes behind you they only way back is forward...)')
      lv0 = ['a peacefull field', 'a sword', 'a ruin with a chest', 'a village ruin', 'a field with 4 Daemons', 'a mysterious gateway']
      lv1 = ['a mysterious gateway', 'a field with an undead daemon horde', 'a ruin with a chest', 'a village ruin', 'a sword', 'a mysterious gateway']
      lv2 = ['a mysterious gateway', 'a village ruin', 'a sword', 'a field with a large undead Daemon', 'Dracoth the necromancer', "a stone hendge that holds an ancient relic"]
      demen = [lv0, lv1, lv2]
      gameState = 'DLC'
      currentLv = 0
      currentArea =0
      while gameState == 'DLC':
  # Describe the room the player is in
        if currentLv == 0:
          lv = lv0
        elif currentLv == 1:
          lv = lv1
        else:
          lv = lv2
        Area = lv[currentArea]
        print(' ')
        print(('<-['), Area, (']->'))
        print(' ')
        print('Area:', currentArea)
        print( 'Lv:', currentLv)
        print("Bag", inventory)
        print('_______________________________')
        choice = input('What action would you like to take? ')
                # Respond to command
        if choice == 'help':
          # Help: display all commands
          # Note that the "pass" keyword in Python is a placeholder for lines where the interpreter would normally expect to see code. If control flow reaches the line with "pass", the interpreter "passes" over the line (i.e. does nothing).
          print('your comands are; Left, Right, Through, Back, Grab, Fight, Enter')
      
        elif choice == 'left':
          Daemon=demen[currentLv][currentArea]
          if currentArea == 0:
            print('*ping* (The field seems to stretch on for eternity you dare not continue less you get lost)')
          elif Daemon == 'a field with an undead daemon horde':
            print('*ping* (You atempted to sneak past the Daemon(s) and failed. By the way the Daemon(s) thought you were delicious.) ')
            gameState = 'loss'
          else:
            print('You continue through the field, now before you is... ')
            currentArea= currentArea -1
          pass 
        elif choice == 'right':
              # if floor[currentRoom] has a monster in it they die
          Daemon=demen[currentLv][currentArea]
          if Daemon == 'a field with 4 Daemons':
            print('*ping* (You atempted to sneak past the Daemon(s) and failed. By the way the Daemon(s) thought you were delicious.) ')
            gameState = 'loss'
          elif Daemon == 'a field with a large undead Daemon':
            print('*ping* (You atempted to sneak past the Daemon(s) and failed. By the way the Daemon(s) thought you were delicious.) ')
            gameState = 'loss'
          elif Daemon == 'Dracoth the necromancer':
            print('*ping* (You atempted to sneak Dracoth the necromancer and failed. He caught you and turned you into one of his many undead solders) ')
            gameState = 'loss'
          elif  currentArea==5:
            print('*ping* (The field seems to stretch on for eternity you dare not continue less you get lost)')
          else:
            print('You continue through the field, now before you is... ')
            currentArea = currentArea + 1
        elif choice == 'through':
          # Player wants to go upstairs
          if Area == lv0[5] or Area == lv1[0]:
            print('*ping* (You enter the gateway, now before you is... )')
            currentLv = currentLv +1
          else:
            print('*ping* (There is no gateway to the next relm here. )')
        elif choice == 'back':
          # Player wants to go downstairs
          if Area == lv1[5] or Area == lv2[0]:
            print('*ping* (You descend the stair well, now before you is... )')
            currentLv = currentLv -1
          else:
            print('*ping* (There is no gateway to the previous relm here. )')
        elif choice == 'grab':
          # Player wants to grab item from the room'
          
          Item= demen[currentLv][currentArea]
          if Item == 'a sword':
            print('*ping* (Sword was added to your bag)')
            inventory.append('Sword')
            demen[currentLv][currentArea] = 'a small ruin'
          elif Item == 'a spell tome':
            print('*ping* (Spell Tome was added to your bag)')
            inventory.append('Spell Tome')
            demen[currentLv][currentArea] = 'a field with a pedastal'
          elif Item == 'a ruin with a chest':
            print('*ping* (As you open the chest, it opens on its own and awakens into a mimic, eating you whole in one bite...)')
            gameState = 'loss'
          elif Item == "a stone hendge that holds an ancient relic":
            print('*ping* (You sucessfully concured the plain and claimed the treasure)')
            gameState = 'victory'
          else:
            print('*ping* (This room contains nothing of value)')
      
          
        elif choice == 'fight':
          # Player wants to fight monster in the room
          Daemon=demen[currentLv][currentArea]
          if inventory == ['Spell Tome', 'Hero Sword', 'Sword'] and Area == lv0[4] or Area==lv1[1]:
            print('*ping* (You and the Daemon(s) fought ruthlessly. In the end you came out victorious, but not unscathed your trusty sword is no longer usable...) ')
            inventory.remove("Sword")
            demen[currentLv][currentArea] = 'a field with body(s) in the grass'
          elif inventory == ['Spell Tome', 'Hero Sword', 'Sword'] and Area==lv2[3]:
            print('*ping* (You and the Daemon(s) fought ruthlessly. In the end you came out victorious, but not unscathed your trusty sword is no longer usable...) ')
            inventory.remove("Sword")
            demen[currentLv][currentArea] = 'a field with body(s) in the grass'
          
          elif inventory == ['Spell Tome', 'Hero Sword'] and Area == lv2[4]:
            print('Ah. Adventurer you have come to face me yet again. This time it will be diferent. This time YOU WILL DIE!!!')
            print(' ')
            print('*ping* (You and Dracoth the necromancer fight a battle to the death. You defeated him once you know you can do it again, you cast a several spells to soften him up then rush twords him to land the final blow. Destroying any of his minions in your way when you finally reach him, you land the blow to end all blows scatering his remains around the ruin, the dead is done and Dracoth is no more...) ')
            print(' ')
            demen[currentLv][currentArea] = 'a large battle devastated ruin with the remains of Dracoth the necromancer'
          else:
            print('*ping* (You atempted to fight the Daemon(s) and failed. Now you have become but one of many zombies under Dracoth the necromancers controll... ')
            gameState = 'loss'
       
        
        else:
          print('Command not recognized. Type "help" to see all commands.')
      
      if gameState == 'victory':
        print('After defeating Dracoth the necromancer you touch the relic and return to your world. Then you head home knowing the evil of this world and the other has been eliminated... *ping* (You beat the game... Restart to play again)')
      elif gameState == 'loss':
        print('*ping* (You perished in combat. Restart the game to play again)')
      
        #end of DLC
  
  else:
    print('Command not recognized. Type "help" to see all commands.')

if gameState == 'won':
  print('You may have defeated me this time adventurer but I will be back... *ping* (You beat the game... Restart to play again)')
else:
  print('*ping* (You perished in combat. Restart the game to play again)')