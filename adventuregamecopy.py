Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:23:07) [MSC v.1927 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> ...

# Posessions/other variables
pencil = False
ruler = False
protractor = False
whistle = False
textbook = False
usb = False
umbrella = False
pin = False
backpack = False
mystery = False
firstzombie = False
secondzombie = False


# Beginning of game
# Player Information
name = input('Hi! What is your name? ')
print(f"Nice to meet you, {name}! \n\nWhat type of student are you?\n\n[1] Jock \n[2]Band kid \n[3] Nerd \n[4] Student council kid\n [4] Wallflower\n\n")
choice0 = int(input('Enter your choice: '))
print(f'\nYou chose [{choice0}].\n\n')
if choice0 == 1:
  intelligence = 40
  strength = 100
  speed = 80
  health = 100
  print('JOCK\nYour Statistics:\nIntelligence: 50\nStrength: 100\nSpeed: 80\nHealth: 100')
elif choice0 == 2:
  intelligence = 70
  strength = 60
  speed = 70
  health = 100
  print('BAND KID\nYour Statistics:\nIntelligence: 70\nStrength: 60\nSpeed: 70\nHealth: 100')
elif choice0 == 3:
  intelligence = 100
  strength = 60
  speed = 60
  health = 100
  print('NERD \nYour Statistics:\nIntelligence: 100\nStrength: 50\nSpeed: 60\nHealth: 100')
elif choice0 == 4:
  intelligence = 80
  strength = 50
  speed = 80
  health = 100
  print('STUDENT COUNCIL KID\n Your Statistics:\nIntelligence: 80\nStrength: 60\nSpeed: 80\nHealth: 100')
elif choice0 == 5:
  intelligence = 80
  strength = 80
  speed = 80
  health = 100
  mystery = True
  print('WALLFLOWER \nYour Statistics:\nIntelligence: 90\nStrength: 40\nSpeed: 40\nHealth: 80')

grade = int(input('What grade are you in?'))
print(f'\nYou chose [{grade}].\n\n')
if grade == 9:
  print('You are a niner. Ew.\nIntelligence - 10\nStrength -10\nSpeed + 20\nHealth + 10\n\n')
  intelligence = intelligence - 10
  strength = strength - 10
  speed = speed + 20
  health = health + 10
  niner = True
elif grade == 10:
  print('You are a sophomore. \nIntelligence + 0\nStrength +10\nSpeed + 10\nHealth + 5\n\n')
  strength = strength + 10
  speed = speed + 10
  health = health + 5
elif grade == 11:
  print('You are a junior. \nIntelligence + 10\nStrength + 20\nSpeed + 0\nHealth + 10\n\n')
  strength = strength + 20
  health = health + 10
  intelligence =intelligence + 10
elif grade == 12:
	print('You are a senior. \nIntelligence + 20\nStrength + 20\nSpeed - 10\nHealth + 0\n\n')
	intelligence = intelligence + 20
	strength = strength + 20
	speed = speed - 10
# Display beginning stats
print(f'Your starting stats are: \nIntelligence: {intelligence} \nStrength: {strength} \nSpeed: {speed} \nHealth: {health}') 

print("Now that we have everything sorted out, let's get started, shall we?\n. \n. \n. \n. \n. \n. \n.")

# Introductory dialogue
print('St. Robert CHS. 2047. Last period.')
print(f"\nYou are in math class as you watch the clock tick. 'Ten minutes until 3:00. I just have to get through two minutes 5 times,' you think.\n \nMath is tedious. Your teacher is going on and on about some test review and as you feel your eyelids getting heavier and heavier as you slowly start to drift to sleep... \n \n'{name}!' your teacher yells. You are startled awake by the shrill voice of your teacher. '{name},' your teacher says, 'Since you were obviously paying your undivided attention to class- what is the answer to question 6?' \n\nBefore you have a chance to answer, a horrifying shriek coming from the hallway pierces the air. \n\n'EEEEEEEEEEEEK!' You recognize it as the Vice Principal, Mrs. Morris. \n\nFollowing the commotion, your class begins to murmur and some students get out of their seats to see what happened. \n\n'Hey, {name}, I'll bet you $20 that Mrs. Morris broke her nail or something stupid like that,' your best friend, Henry, snickers as he carves his initials into the desk beside you. \n\n'Shut up, man,' you reply. 'What if something bad happened to her?'\n\nHenry looks at you judgingly.'Since when did you care what happened to teachers?'\n\nAs you open your mouth to defend yourself, the group of students who went to check the commotion run screaming back. Their hysterical voices are inseperable from each other but, in your attempt to decipher their frantic message, you hear three words that stand out.\n\nZOMBIES.\n\nHERE.\n\nRUN.\n\n\n\nUh oh.\n.\n.\n.\nST. ROBERT: MISSION ZOMBIE\nBONNIE TANG\nICS3U1b\n.\n.\n.")

# Gameplay
# First decision
print('Your fight or flight instincts instantly kick in. You look around at the chaos around you and you notice that Henry is nowhere to be found. So much for best friends.\n You continue to scan your surroundings for something to defend yourself with and you see a pencil, a ruler, and a protractor. Which do you pick up?\n\n[1] PENCIL\n\n[2] RULER\n\n[3] PROTRACTOR\n\n')

# Choice 1
choice1 = int(input('Enter your choice: '))

# If statements choice 1
if choice1 == 1:
  print('\nYou put the pencil into your pocket and the sharpened tip pricks your leg through your uniform pants. \nHEALTH -10')
  health = health - 10
  pencil = True
elif choice1 == 2:
  print('\nYou put the ruler in your pocket. It barely fits.\n')
  ruler = True
elif choice1 == 3:
  print('\nYou put the protractor into your pocket.\n')
  protractor = True


# Zombie 1
print(f'\nYou chose [{choice1}].\n')
print(f"You walk out of your now deserted math classroom and peak your head out to see if the coast is clear. You don't see any zombies so you leave and walk towards the stairs that lead to exit in the main lobby. \n\nAs you walk down the hallway towards the french office, you hear somebody your name.\n\n'{name}...{name}...{name}!'\n\nYou whip your head in the direction of whoever was calling you and you see your gym teacher... but ZOMBIFIED!\n\nYou're so stupidifed at the sight of the 60 year old man who used to yell at you to run faster with grey skin and rolled over eyes that you fail to realize how he has just started running toward you. He's too quick so you can't hide. You have to fight your gym teacher.")
# If statements1
# Pencil
if pencil == True:
  print('You take out the pencil you took from your pocket. When the zombie gets close enough, where do you stab?\n\n[1] THIGH\n\n[2] FACE\n\n[3] ARM \n\n[4] CHEST\n\n[5] FOOT\n')
# Choice 1.1
  choice1_1 = int(input('Enter your choice: '))
  if choice1_1 == 4:
    print('You stab him in the chest with the sharp end of your pencil and you hit his heart. He yells and falls to the ground in pain. You rip his rotting limbs off to make sure he can not get back up.\n\nSTRENGTH +20')
    strength = strength + 20
    input('Press ENTER to continue.')
  elif choice1_1 == 2:
    print('You stab him in the face with the sharp end of your pencil. The pencil goes through his right eye socket and goes into his rotting brain. He immediately falls to the ground. He seizes for a bit but soon after, he dies. Efficient!\n\nINTELLIGENCE +20')
    intelligence = intelligence + 20
    input('Press ENTER to continue.')
  else:
    print('\nYou stab him with the sharp end of your pencil but you do not hit anything important. The pain makes him even more irritated and he grabs your left arm and rips your hand off. You scream and fall to the ground. He punches you in the head and you are knocked out. He bites you and you become a zombie.\nHEALTH -{health}\nHealth = 0\n\n')
    input('YOU ARE DEAD. GO BACK TO START.')
  print('\n\nAs you are about to continue down the hallway, you see a whistle on the ground hanging from the neck of the dead zombie. Do you pick it up?\n\n[1] Yes\n\n[2] No\n')
  # Choice 1.1.1
  choice1_11 = int(input('Enter your choice: '))
  print(f'\nYou chose [{choice1_11}].\n')
  if choice1_11 == 1:
    whistle = True
    print('\nYou pick up the whistle.\n')
  else:
    print('\nYou leave the whistle.\n')

# Ruler
elif ruler == True:
  print('You take out the ruler you took from your pocket. Your zombie gym teacher runs toward you. Where do you stab him?\n\n[1] Eye \n[2] Chest')
  # Choice 1.2
  choice1_2 = int(input('Enter your choice: '))
  print(f'\nYou chose [{choice1_2}].\n')
  if choice1_2 == 1:
    print('You stab him in the eye with your ruler. It is difficult but you manage to poke through his eye. You do not manage to kill him but the pain scares him away.\n')
    if speed >= 90 or speed == 90:
      print('You chase the zombie down and grab his neck. He is impaired by his damaged eye and you manage to knock him out. You rip his limbs off just to be safe.)
      input('Press ENTER to continue.')
      print('\n\nAs you are about to continue down the hallway, you see that the gym teacher dropped his whistle in his hurry to run away. Do you pick it up?\n\n[1] Yes\n[2] No')
      # Choice 1.2.1
      choice1_21 = int(input('Enter your choice: '))
      if choice1_21 == 1:
        whistle = True
        print('\nYou pick up the whistle.\n')
      else:
        print('\nYou leave the whistle.\n')
    else:
      print('You try to chase him down but you are not fast enough. He gets away.\n')
      firstzombie = True
  elif choice1_2 == 2:
    print('You stab him in the chest with your ruler. The ruler is too blunt to do any real damage and the attempt irritates the zombie. He takes the ruler from your hand and hits you across the face. As you stagger back, he grabs you and punches your head. You are knocked out. He bites you and you become a zombie.\nHEALTH -{health}\nHealth = 0\n\n')
    input('YOU ARE DEAD. GO BACK TO START.')
# Protractor
elif protractor == True:
  if strength == 120:
    print('You take out the protractor from your pocket and attempt to stab him in the eye with it. It does not work; why would you choose a weapon with a round edge? \nLucky for you, your big muscles save the day! You throw the protractor away and punch the zombie in the face. He howls in pain and staggers back. You take your fingers and stick them straight through his eye sockets. You use your other hand to hold his head still while you repeatedly poke him in the face with your fingers. He falls to the ground, seizing for a bit, but eventually dying. Who needs tools when you can bench 315?')
    input('Press ENTER to continue.')
    print('\n\nAs you are about to continue down the hallway, you see a whistle on the ground hanging from the neck of the dead zombie. Do you pick it up?\n\n[1] Yes\n\n[2] No\n')
    # Choice 1.1.1
    choice1_11 = int(input('Enter your choice: '))
    print(f'\nYou chose [{choice1_11}].\n')
    if choice1_11 == 1:
      whistle = True
      print('\nYou pick up the whistle.\n')
    else:
      print('\nYou leave the whistle.\n')
  else:
    print('You take out the protractor you took from your pocket. The zombie comes running toward you and you try to stab it in the eye. It does not work; why would you choose something with a round edge as a weapon? The zombie becomes more irritated and flings the protractor out of your hand. He attacks you and you fall the the ground. You are knocked out. He bites you and you become a zombie.HEALTH -{health}\nHealth = 0\n\n')
    input('YOU ARE DEAD. GO BACK TO START.')

# Second decision
print('You continue down the hallway and turn right towards the balcony. The majority of the school seems to be abandoned already. In the corner of your eye, you see an open locker. You approach it and you see some things that may help you on your quest. The thing that first catches your eye is a gigantic biology textbook. There is also a small USB stick hanging from the side of a jacket. You also spot an umbrella hanging beside the jacket. \nWhich one do you take?\n\n[1] Textbook\n\n[2] USB stick \n\n[3] Umbrella\n')
# Choice 2
choice2 = int(input('Enter your choice: '))

# If statements choice 2
if choice2 == 1:
  print('\nYou grab the textbook. You have nowhere to store it so you hold it in your arms.')
  textbook == True
elif choice2 == 2:
  print('\nYou detach the USB stick from the lanyard and put it into your pocket.')
  if pencil == true:
    print('It fits nicely in the same pocket as the pencil.')
  elif ruler == true: 
    print('It does not fit in the same pocket as your ruler so you place it into the other pocket.')
  usb = True
elif choice2 == 3:
  print('\nYou pick up the umbrella. You have nowhere to store it so you hold it in your hand.')
  umbrella = True

# Third decision
print('You start walking toward the stairs again. On the wall, you see the water fountain. You are reminded of the existence of water and your throat feels extra dry. Do you take a swig?\n\n[1] Yes\n[2] No')
water = int(input('Enter your choice: )
if water == 1:
  health = health - 50
  print(f'You take nice, long drink of water. It tastes a bit funny and your stomach starts to feel weird. The water must have been contaminated! \nHEALTH -50\nHEALTH: {health}')
else:
  print('You decide not to drink the water. Who knows what it could be contaminated with?\n\n')
# Zombie 2
print("You keep walking towards the stairs. When you reach the doors, you see that there is another zombie inside the stairwell. It seems distracted by something outside the window; you may be able to sneak past it. \nDo you go inside?\n\n[1] Yes \n\n[2] No\n")

# Choice 2.1
choice2_1 = int(input('Enter your choice: '))

# If statements 2.1
if choice2_1 == 1:
  print("You enter the stairwell quietly. You recognize the zombie as your biology teacher. Darn, she was really nice. You continue moving towards the stairs and look out the window. You see that she is distracted by a bunch of helicopters in the sky.'Hopefully they're here to help us,' you think to yourself.")
  if textbook == True:
    if intelligence >= 100 or intelligence = 100:
      print("You are at the stairs beginning to descend when you lose your grip on the textook you are holding. You had too much stuff! It drops on the floor with a 'BANG!'. The zombie is immediately notified of your presence. She whips her head around at you and, before she is able to attack, she recognizes you. \n\n'{name}...{name}! Y-you... star... student...' she moans. 'Pop... quiz! Monomer... of... peptide... called... what...?'\n\n'Tha's too easy! Amino acids, of course!' you answer.\n\nShe smiles at you, satisfied, and returns to her state of distraction. Who says being smart is uncool?')
      intelligence = intelligence + 10
    else:
      print("You are at the stairs and beginning to descend when you lose your grip on the textbook you are holding. You had too much stuff! It drops on the floor with a loud 'BANG!' The zombie is immediately notified of your presence. She runs toward you with a scream and you lose your balance. You fall backwards off of the stairs and hit your head. You are knocked unconscious because of the impact and get eaten. \nHEALTH -{health}\nHealth = 0\n\n")      
      input('YOU ARE DEAD. GO BACK TO START.')
  elif umbrella == True:
    print('You are at the stairs and beginning to descend when you lose your grip on the umbrella. Your heart skips a beat but you manage to hook its handle onto your finger before it drops onto the ground. You look at the zombie and it is as distracted as ever. You breathe a sigh of relief and quietly make it down the stairs.')
    speed = speed + 10
  else:
    print('You make it to the stairs and slowly descend as to not alert the zombie. You make it to the bottom in one peace and you breathe out a sigh of relief.')
  print('Before you head out of the stairwell, you spot a shiny metal pin with the St. Robert CHS symbol on it. You pick it up and head out into the main hallway.')
  pin = True
elif choice2_1 == 2:
  if grade == 9:
    print('You chicken out and head back in the direction that you came from. You realize that you are still fairly new to the school and freak out. You are lost and begin wandering around. All of a sudden, you hear a zombie 
# if niner, you get lost and die
  print('You chicken out and head back in the direction that you came from. You remember that there is another staircase, right beside the french office. You go down that one instead; there are no zombies. You take a left at the bottom of the stairs and arrive at the main hallway.)

# Main lobby doors

# Henry

# Third zombie and zombie from previous fights

# Final

# Outcomes(Question of remembering situation), use while/loop for health
