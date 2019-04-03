PEANUT_BUTTER_JAR_OPTIONS = '''
In an effort to infiltrate Planet Earth in the most clandestine way
possible, you decide to transform yourself into a sentient peanut butter
jar. What do you do from here?

1) Modify your flavor profile to taste absolutely horrendous.
2) Join the circus as "The Most Sentient Peanut Butter Jar in the World".
3) Look at the jelly jar beside you.
4) Create the ultimate Peanut Butter Hamburger.
'''

TASTE_TERRIBLE = '''
As the humans realize this peanut butter has turned, they scramble to create
fresh peanut butter. As they do, you learn the recipe to create as MUCH
peanut butter as we need.
'''

JOIN_CIRCUS = '''

'''

JELLY_JAR = '''
You try to talk to the jelly jar beside you. Turns out that it's a cursed
woman, and the two of you fall in love. You decide to abandon your peanut
butter mission in the name of love.
'''

PEANUT_BUTTER_BURGER = '''
You create the ultimate Peanut Burger Hamburger. The President finds out
about these great hamburgers and decides to eat one. He takes one big bite
and shouts, "WHAT A GREAT HAMBERDER!" Little did he know that you were now
able to gain control of his body... what do you see there? Is that the
nuclear football?
'''

def peanut_butter_jar_narrative():
    jar_option = int(input(PEANUT_BUTTER_JAR_OPTIONS))

    if jar_option == 1:
        print(TASTE_TERRIBLE)
    elif jar_option == 2:
        pass
    elif jar_option == 3:
        print(JELLY_JAR)
    elif jar_option == 4:
        print(PEANUT_BUTTER_BURGER)