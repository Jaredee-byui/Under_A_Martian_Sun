print("Under a Martian Sun by Jared Ellis")

print(" ")

character_name = input("What is your name? ")

print(" ")

print('''NARRATOR: You are a traveling water merchant on the planet Mars. 
Years of harsh living, and less than honest dealing, have landed you in trouble more times than you can count.
While traveling the road from Utopia City to Olympus Station, you spot an approaching caravan.
You recognize instantly the banners of the Inter-regional water guild, they recently bought a less-than-clean aquafer from you.
It appears you've gotten in trouble once again, possibly for the last time.''')

print(" ")

character_alive = True
# I decided to space out the variables in this section of code to make reading through it easier on the eyes.
while True:

    choice_one = input('''
    Time is of the essence, you are armed well enough to survive the occasional bandit but not FIGHT an entire caravan.
A large outcropping of rocks is approaxametly three meters to the southeast of you, they could HIDE you well enough.
Alternatively, you could attempt to TALK your way out of this FIGHT, you have done it before. What will you do? ''')
    print(" ")
        
    if choice_one.lower() == "fight":
        print('''
    You ready your rifle and open fire on the approaching caravan. The first man in the caravan crumples to the Martian dust.
All at once a deadly hailstorm of bullets and energy beams return to your position. ''')
        character_alive = False
        break 
        
    elif choice_one.lower() == "hide":
        print('''
    You decide to exercise the better part of valor and scramble to the rock face. 
Hidden in the shadows of the Martian afternoon is a large crevice, just large enough to fit you and your gear.
From the mouth of the cavern you see the caravan walk onwards towards Utopia City.
They never even notice the faint tracks only meters away.''')
        character = "unware_water"
        break

    elif choice_one.lower() == "talk":
        print(f'''
    It has been awhile since you were able to really use your silver tongue, nothing like the fear of death to make you barter.
Wearily, you apprach the leader of the caravan. "{character_name}? I didn't think I'd ever see you again.
The guild isn't too happy with you after that little sweet-water stunt.
Ordinarilly, I would have my guards put you in cuffs and we'd drag you to the nearest guild house, but not today. 
A large lake just appeared south of Utopia City near Crimson Gulch, the guild needs us there immediately to stake out the water.
Instead of cuffing you, I'll give you this warning. The guild doesn't know much about the situation but they won't let a flea like you interfere.
Keep walking and pretend you never saw us." ''')
        character = "aware_water"
        break

    else:
        print(" ")
        print("Perhaps you should rephrase that.")
        print(" ")
    
#scenario wrap up and scene transition

if character_alive:
    if character == "aware_water":
        print(" ")
        print('''
The news of a new lake appearing is interesting, unfortunately you don't have time to investigate. 
You need to get to Olympus Station. Maybe somebody there might know more about the situation.''')
    else:
        print(" ")
        print(''' 
After hiding for several more minutes you extract yourself from the rockface. 
The caravan is nowhere to be seen. Not wanting to risk any more confrontations, you hurry to reach Olympus Station.''')
else:
    print(" ")
    print("You are dead. Your sun bleached bones lie in the harsh Martian Sun.")
    exit()

#act II olympus station


if character_alive:
    print(''' 
    After many days of traveling you arrive at Olympus Station. Olympus Station was one of the first stations established on Mars back in the 40's.
Olympus was never built with luxury in mind, it was established as an ore processing facility and has since grown into a glorified shanty town.
Most of the well-to-do citizens of Mars moved to the bright, shining new city of Utopia City 20 years ago. Everybody who stayed was either too
broke or too stubborn to leave. Home sweet home.''')
    print(" ")
    while True:
        choice_two = input('''
    You need to meet with your courier contractor, HANK. Hank's office is in the south spire on level two. 
Alternatively, you could go get a DRINK at your favorite watering hole. The Rusted Strut is in the old extension zone on sub level 3.
Where do you want to go? ''')
        if choice_two.lower() == "hank":
            print(" ")
            print(f'''
    You head to the south spire and summon a lift. The ride up to Hank's office is slow and uneventful. 
The grimey windows of the station reveal a look at the ever present red-surface of mars. 
Upon arriving at Hank's office, you find him typing at his desk. " Ah, {character_name}, good take a seat. 
I just got some news before you walked in, have you heard about the lake that just appeared south of Utopia?" 
The reports are saying that the thing just appeared over night. You got a new contract in the works but I can't give it to you just yet.
Go get a drink and report back here in half an hour. The client should have all the details forwarded to me by then.''')
            break
        elif choice_two.lower() == "drink":
            print(" ")
            print(''' 
    You really should report to Hank soon, of course you DID just complete such a long walk in the dunes. Maybe you'll get a drink first.
Besides, Hank's probably asleep in his office right now anyway. The lazy old coot.''')
            break
        else:
            print(" ")
            print("Sorry, maybe you should rephrase that.")

#scene II at the rusted strut
