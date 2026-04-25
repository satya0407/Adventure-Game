import random

playerClass = None
health = 100
experience = 1
experiencePoint = 0
toNextExperience = 50
enemyStrength = 0
strength = 0
magic = 0
archery = 0
armor = 0
armorProtect = 0
key = False
cellFinded = False
escaped = False
healthLost = 0
coin = 10
toShop = 5
toQuest = 10
roundCounter = 0
win = None

playerClass = input('Which class do you want to choose, the knight, the archer, the guardian, the prince, or the sorcerer?\n')
if playerClass == 'knight':
    strength = 10
    magic = 0
    archery = 0
    armor = 10
if playerClass == 'sorcerer':
    strength = 0
    magic = 10
    archery = 0
    armor = 10
if playerClass == 'archer':
    strength = 0
    magic = 0
    archery = 10
    armor = 10
if playerClass == 'guardian':
    strength = 7
    magic = 0
    archery = 0
    armor = 20
    coin = 20
if playerClass == 'prince':
    strength = 13
    magic = 0
    archery = 0
    armor = 0
    coin = 0

choice = ['explore', 'loot', 'enemy']
explore = ['You have find a door an you went to the next room,',
           'You have fallen down in a hole, and lost 10 HP.',
           'You have arrived to a hallway!',
           'You reached a dead end so you have to turn back!',
           'You have find a hole and you have crawled inside of it! You have arrived to a garden!']
loot = [f'You have find a chest and you find a sword in it, so you got plus one strength point!',
        f'You have find a spellbook in a shelf, so you get plus one magic point!',
        f'You have find a chest and you find an armor in it, so you got plus one armor point!',
        'You have find a chest and you find a medkit in it, so you got your health back!',
        'You have find a chest, and you have find a bow in it, so you got plus 1 archery point!',
        f'You have find a person in the castle and he given you ten coin!',
        f'You have traded with an other adventurer and got ten coin!']
enemy = ['Some knight have appeared in front of you, and you have to defeat them!',
         'Some archers have appeared in front of you, and you have to defeat them!',
         'Some guard have appeared in front of you, and you have to defeat them!',
         'Some sorcerer have appeared in front of you, and you have to defeat them!',
         'A prince have appeared in front of you, and you have to defeat him!']
enemyFightEnd = ['You have defeated your enemies, and you get out of the fight unharmed!',
                 f'You have defeated your enemies, but you have injured!']
quest = ['You have find the key to unlock the cell, and free your son!',
         'You have opened the cell and freed your son, but you have to escape from the castle!',
         f'Congratulation! You also known as the {playerClass} and your son have escaped from the castle!']

print(f'Welcome Adventurer!\nHere in the Kingdom of Hungary the life is really nice, I have to say.\nBut one day the king of the country stoled the son of the {playerClass} because he cannot pay the taxes to the king.\nAnd because of that the {playerClass} tried to have a revenge.\nSo he went to the castle, where the king hided his son and tried to free him.\nAnd this is where the adventure begins.\n')

while win == None:
    if toQuest == 0:
        if key == False:
            print(quest[0])
            key = True
        elif cellFinded == False:
            print(quest[1])
            cellFinded = True
        else:
            print(quest[2])
            escaped = True
            win = True
        toQuest = 10
        tell = input('Can we continue our adventure?')

    while toShop == 0:
        print(f'Welcome to my shop {playerClass}!\nYou can buy here everything you want!\nYou have {coin} coin.\nAnd your health is {health}!\nThe medkit(It can heal you back to 100 HP), and the price of it is 5 coin!\nThe sword(It can give you plus 1 sterngth point), and the price of it is 5 coin!\nThe spellbook(It can give you plus 1 magic point), and the price of it is 5 coin!\nThe bow(It can give you plus 1 archery point), and the price of it is 5 coin!\nAnd the armor(It can give you plus 1 armor point), and the price of it is 5 coin!\nIf you do not want to buy something you can tell me that you want to leave!')
        wanted = input('So what do you want? ')
        if wanted == 'medkit' and coin >= 5:
            health = 100
            coin -= 5
            print(f'Your have 100 HP again, but you gave me 5 coin! So you have {coin} coin!')
        elif wanted == 'sword' and coin >= 5:
            strength += 1
            coin -= 5
            print(f'Your have got 1 plus strength point, but you gave me 5 coin! Your strength is {strength}. So you have {coin} coin!')
        elif wanted == 'spellbook' and coin >= 5:
            magic += 1
            coin -= 5
            print(f'Your have got 1 plus magic point, but you gave me 5 coin! Your magic is {magic}. So you have {coin} coin!')
        elif wanted == 'armor' and coin >= 5:
            armor += 1
            coin -= 5
            print(f'Your have got 1 plus armor point, but you gave me 5 coin! Your armor is {armor}. So you have {coin} coin!')
        elif wanted == 'bow' and coin >= 5:
            archery += 1
            coin -= 5
            print(f'Your have got 1 plus archery point, but you gave me 5 coin! Your archery is {archery}. So you have {coin} coin!')
        elif wanted == 'leave':
            toShop = 5
            print(f'Good bye, {playerClass}!')
        elif coin < 5:
            print(f'Sorry, but you only have {coin} coin!')
            toShop = 5
            print(f'Good bye, {playerClass}!')


    num1 = random.randint(0, 2)
    if num1 == 0:
        num2 = random.randint(0, 4)
        print(explore[num2])
        if num2 == 1:
            health = health - 10
    elif num1 == 1:
        num2 = random.randint(0, 6)
        if num2 == 0:
            strength += 1
            print(loot[num2])
            print(f'So your strength is {strength}.')
        elif num2 == 1:
            magic += 1
            print(loot[num2])
            print(f'So your magic is {magic}.')
        elif num2 == 2:
            armor += 1
            print(loot[num2])
            print(f'So your armor is {armor}.')
        elif num2 == 3:
            print(loot[num2])
            health = 100
        elif num2 == 4:
            archery += 1
            print(loot[num2])
            print(f'So your archery is {archery}.')
        else:
            coin += 10
            print(loot[num2])
            print(f'So you have got {coin} coin.')
    elif num1 == 2:
        num2 = random.randint(0, 4)
        print(enemy[num2])
        if roundCounter <= 10:
            enemyStrength = random.randint(10, 12)
            if strength >= magic and strength >= archery:
                if strength >= enemyStrength:
                    print(enemyFightEnd[0])
                else:
                    num3 = random.randint(10, 50)
                    healthLost = num3
                    armorProtect = 1 * armor / 100
                    healthLost = healthLost - armorProtect
                    health = health - healthLost
                    print(enemyFightEnd[1])
                    print(f'Now you only have {health} HP.')
            elif magic >= strength and magic >= archery:
                if magic >= enemyStrength:
                    print(enemyFightEnd[0])
                else:
                    num3 = random.randint(10, 50)
                    healthLost = num3
                    armorProtect = 1 * armor / 100
                    healthLost = healthLost - armorProtect
                    health = health - healthLost
                    print(enemyFightEnd[1])
                    print(f'Now you only have {health} HP.')
            else:
                if archery >= enemyStrength:
                    print(enemyFightEnd[0])
                else:
                    num3 = random.randint(10, 50)
                    healthLost = num3
                    armorProtect = 1 * armor / 100
                    healthLost = healthLost - armorProtect
                    health = health - healthLost
                    print(enemyFightEnd[1])
                    print(f'Now you only have {health} HP.')
        elif roundCounter > 10 and roundCounter <= 20:
            enemyStrength = random.randint(15, 17)
            if strength >= magic and strength >= archery:
                if strength >= enemyStrength:
                    print(enemyFightEnd[0])
                else:
                    num3 = random.randint(10, 50)
                    healthLost = num3
                    armorProtect = 1 * armor / 100
                    healthLost = healthLost - armorProtect
                    health = health - healthLost
                    print(enemyFightEnd[1])
                    print(f'Now you only have {health} HP.')
            elif magic >= strength and magic >= archery:
                if magic >= enemyStrength:
                    print(enemyFightEnd[0])
                else:
                    num3 = random.randint(10, 50)
                    healthLost = num3
                    armorProtect = 1 * armor / 100
                    healthLost = healthLost - armorProtect
                    health = health - healthLost
                    print(enemyFightEnd[1])
                    print(f'Now you only have {health} HP.')
            else:
                if archery >= enemyStrength:
                    print(enemyFightEnd[0])
                else:
                    num3 = random.randint(10, 50)
                    healthLost = num3
                    armorProtect = 1 * armor / 100
                    healthLost = healthLost - armorProtect
                    health = health - healthLost
                    print(enemyFightEnd[1])
                    print(f'Now you only have {health} HP.')
        elif roundCounter > 20:
            enemyStrength = random.randint(20, 22)
            if strength >= magic and strength >= archery:
                if strength >= enemyStrength:
                    print(enemyFightEnd[0])
                else:
                    num3 = random.randint(10, 50)
                    healthLost = num3
                    armorProtect = 1 * armor / 100
                    healthLost = healthLost - armorProtect
                    health = health - healthLost
                    print(enemyFightEnd[1])
                    print(f'Now you only have {health} HP.')
            elif magic >= strength and magic >= archery:
                if magic >= enemyStrength:
                    print(enemyFightEnd[0])
                else:
                    num3 = random.randint(10, 50)
                    healthLost = num3
                    armorProtect = 1 * armor / 100
                    healthLost = healthLost - armorProtect
                    health = health - healthLost
                    print(enemyFightEnd[1])
                    print(f'Now you only have {health} HP.')
            else:
                if archery >= enemyStrength:
                    print(enemyFightEnd[0])
                else:
                    num3 = random.randint(10, 50)
                    healthLost = num3
                    armorProtect = 1 * armor / 100
                    healthLost = healthLost - armorProtect
                    health = health - healthLost
                    print(enemyFightEnd[1])
                    print(f'Now you only have {health} HP.')
        experiencePoint += 25
        toNextExperience -= 25
        if toNextExperience == 0:
            experience += 1
            experiencePoint = 0
            toNextExperience = 50
            armor += 1
            strength += 1
            magic += 1
            archery += 1
            print(f'Your stats are {strength} strength, {armor} armor, {magic} magic, {archery} archery.\nYour experience level is {experience}.')

    if health <= 0:
        win = False
        print(f'The {playerClass} have died in this journey!')

    toShop -= 1
    toQuest -= 1
    roundCounter += 1
    tell = input('Can we continue our journey?')

if win == True:
    print(f'After the escape from the castle of the king. The {playerClass}, and his son have returned to their family and lived a happy life after that.\nThis is where our adventure ends, but I hope we will meet again!\nThe End!')
else:
    print(f'After the death of the {playerClass}, the king gave the son of the {playerClass} back to his family at a cost of 200 coin!\nBut after that they have no money and lived in poor condition, and in sadness!\nThis is where our adventure ends, but I hope we will meet again!\nThe End!')
