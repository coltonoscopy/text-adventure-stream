FARM_FIELD_OPTIONS = '''
You decide that the best course of action is to attack the humans
directly. You have landed in the center of a giant farm field and 
some humans have approached you. Do you?

1) Vaporize the humans.
2) Try to communicate to the humans.
3) Erase the humans' memories and move to a new area.
'''

VAPORIZE_HUMANS = '''
Using your latest in regex technology, you create a broken regex that
breaks down the entire planet of Earth, including their supply of peanut
butter, ruining your mission entirely.
'''

TALK_TO_FARMERS_OPTIONS = '''
You try to initiate a conversation with the local peanut farmers. How do you
guide the conversation?

1) You demand to speak to their leader.
2) Try to persuade the peanut farmers to board your ship.
3) Punch the farmer in his face, since that's your planetary greeting.
'''

TALK_TO_FARMERS_LEADER = '''
You demand to speak to the farmers' leader. Enraged at your brazen request,
the farmers gather their nearby pitchforks, surround you, and disable your
spaceship with their unanticipated technology. Your civilization will have to
seek out peanut butter another millenium.
'''

TALK_TO_FARMERS_PUNCH = '''
The farmer is impressed with your punch and takes you in as a peanut puncher.
You fall in love with the art of peanut punching and forget all about your
alien brethren, dooming them to a life devoid of peanuts.
'''

TALK_TO_FARMERS_VICTORY = '''
You successfully persuade the peanut farmers to board your ship. Sensing this
will be an easy task henceforth, you embark on a worldwide peanut farmer
gathering expedition and steal all of the Earth's peanut farming talent,
thus ridding the Earth of peanuts and granting your species infinite peanut
agricultural prowess.
'''

BECOME_DOG_CHOICE = '''
Upon landing, you see a furry creature playing with an earthling from a distance.
What do you do, amongst supposedly three choices?

1) Become the furry creature playing with the earthling.
2) Approach the earthling and ask to phone home.
3) Fly to a new location.
'''

NEW_LOCATION = '''
After erasing the humans' memories, you decide to fly to a second new location.
You find yourself in the sand and see water waving around and see an earthling
playing with the sand. You approach her and ask for the nearest peanut butter
source. She happily gives you a peanut butter jar full of energy. You walk out
of the beach, unsure what to do next. Do you?

1) Go back and build a sandcastle.
2) Ask the girl why they like peanut butter so much.
3)
'''

SANDCASTLE = '''
You decide to construct a sandcastle. While doing so, you see a man running
faster than light across the beach. What do you do?

1) Trip him with a stick.
2) Ignore the man running faster than light and step into the water.
3) 
'''

TRIP_STICK = '''
After Chuck Norris trips on the stick, it flies away and hits a forgotten
casette player from the late 1980s. You hear the words: "Never gonna give you
up, never gonna let you down, never gonna turn around and desert you"--and
you realize that humanity really is worthy of keeping peanut butter.
'''

PEANUT_BUTTER_GIRL = '''
You ask the girl why she loves peanut butter so much. She gives you a peanut
butter and jelly sandwich. You understand that humans had it right all along
and decide to eat the peanut butter instead of using it for intergalactic travel.
Yum!
'''

STEP_INTO_WATER = '''
As soon as you set foot into the water, you realize a long-suppressed fact
about yourself: you're actually Spongebob! You commit to a live under the
sea, living in your pineapple, and forget all about peanut butter's
existence.
'''

SECRET_DOG_ENDING = '''
You transform completely into the dog, forgetting that you can't shapeshift
for an extended period of time, and you forget all about your mission. You
lose all your memories and grow fond of humans and realize that they are
actually quite nice. To top it off, you get peanut treats every day!
'''

BECOME_ET_ENDING = '''
You approach the earthling and crudely ask if you can phone home. The human
awkwardly obliges by transporting you in his bike basket. With your alien
powers and lack of patience, you imbue the bicycle with levitation and fly
across the moon; however, your impatience leads to boredom and then fatigue,
causing you to forget you're levitating, bringing the bike crashing back to
earth and wiping both of you out in gruesome form.
'''

BECOME_DOG_VICTORY = '''
Once you have shapeshifted into a dog, you eat all of the peanut butter in the
world, but since you are an alien, you have simply stored it, not digested it,
and bring it back to your alien overlords.
'''

def attack_narrative():
    farm_choice = int(input(FARM_FIELD_OPTIONS))
    if farm_choice == 1:
        print(VAPORIZE_HUMANS)
        # vaporize the humans
    elif farm_choice == 2:
        # communicate with humans
        communicate_option = int(input(TALK_TO_FARMERS_OPTIONS))

        if communicate_option == 1:
            print(TALK_TO_FARMERS_LEADER)
        elif communicate_option == 2:
            # victory
            print(TALK_TO_FARMERS_VICTORY)
        else:
            pass
    else:
        # dog option
        dog_option = int(input(BECOME_DOG_CHOICE))

        if dog_option == 1:
            print(BECOME_DOG_VICTORY)
        elif dog_option == 2:
            print(BECOME_ET_ENDING)
        elif dog_option == 3:
            new_location = int(input(NEW_LOCATION))

            if new_location == 1:
                sandcastle = int(input(SANDCASTLE))

                if sandcastle == 1:
                    print(TRIP_STICK)
                elif sandcastle == 2:
                    # spongebob ending
                    print(STEP_INTO_WATER)
            elif new_location == 2:
                print(PEANUT_BUTTER_GIRL)
        elif dog_option == 4:
            # secret choice
            print(SECRET_DOG_ENDING)
        