UNDERCOVER_OPTIONS = '''
You decide to go undercover on Planet Earth as a human. Where do you decide
to go first?

1) Harvard University
2) Visit the circus.
3)
'''

VISIT_CIRCUS = '''
    
'''

HARVARD_OPTION = '''
You end up in a CS50 lecture and end up being in the algorithms demo. You then
understand that CS50 is better than any peanut butter. You film the lecture
and send it to your overlords, who then use CS to create a new power source.
'''

def undercover_narrative():
    undercover_option = int(input(UNDERCOVER_OPTIONS))

    if undercover_option == 1:
        print(HARVARD_OPTION)