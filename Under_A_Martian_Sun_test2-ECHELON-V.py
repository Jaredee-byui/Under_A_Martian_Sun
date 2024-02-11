
#caution: long code ahead
print(" ")
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
        aware_water = False
        break

    elif choice_one.lower() == "talk":
        print(f'''
    It has been awhile since you were able to really use your silver tongue, nothing like the fear of death to make you barter.
Wearily, you apprach the leader of the caravan. "{character_name.capitalize()}? I didn't think I'd ever see you again.
The guild isn't too happy with you after that little sweet-water stunt.
Ordinarilly, I would have my guards put you in cuffs and we'd drag you to the nearest guild house, but not today. 
A large lake just appeared south of Utopia City near Crimson Gulch, the guild needs us there immediately to stake out the water.
Instead of cuffing you, I'll give you this warning. The guild doesn't know much about the situation but they won't let a flea like you interfere.
Keep walking and pretend you never saw us." ''')
        aware_water = True
        break

    else:
        print(" ")
        print("Perhaps you should rephrase that.")
        print(" ")
    
#scenario wrap up and scene transition

if character_alive:
    if aware_water:
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
Upon arriving at Hank's office, you find him typing at his desk. " Ah, {character_name.capitalize()}, good take a seat. 
I just got some news before you walked in, have you heard about the lake that just appeared south of Utopia?" 
The reports are saying that the thing just appeared over night. You got a new contract in the works but I can't give it to you just yet.
Go get a drink and report back here in half an hour. The client should have all the details forwarded to me by then.''')
        talk_to_hank = True
        break

    elif choice_two.lower() == "drink":
        print(" ")
        print(''' 
    You really should report to Hank soon, of course you DID just complete such a long walk in the dunes. Maybe you'll get a drink first.
Besides, Hank's probably asleep in his office right now anyway. The lazy old coot.''')
        talk_to_hank = False
        break

    else:
        print(" ")
        print("Sorry, maybe you should rephrase that.")

#scene II at the rusted strut
print(" ")

print('''
    You arrive at the Rusted Strut. The Rusted Strut was one of the earliest bars established on Mars and has seen better days.
Looking around the bar you see a few people. Running the bar is JUDY, a stern faced but wise minded woman. 
She's the daughter of the original owner, Carl. Sitting in the corner, you see a strange looking OLD MAN with wild white hair and a flowing beard.
A few OTHERs sit at the booths and stools, but none of them mind you any attention.''')

while True: 
    bar_talk = input("Who would you like to talk to? ")
    
    if bar_talk.lower() == "old man":
        print(" ")
        print('''
    You decide to appraoch the old man sitting in the corner. As you appraoch you can see in the dim light of booth that his face is deeply
tanned and weathered by many harsh years on Mars. He might be a first generation colonist by the look of it. As you get closer, the old man
raises his head and looks at you. "Ah, another stranger come to hear my tale of shimmering blue water upon a red planet" he says.  ''')
        print(" ")
        print(''' 
    The old man tells you a fantastic tale of an ancient prophesy that must soon come to fruition. "Soon the waters of Mars will
flow once more. The red desert will bloom and men will be free to spread across the planet. I saw it all in vision".
What an eccentric performance. ''')
        talk_to_man = True

    elif bar_talk.lower() == "judy":
        print(" ")
        print('''
    You decide to talk to Judy and grab a drink. As you approach the counter, she looks up from cleaning an old glass. "Long time no see stranger"
She remarks. She pours you up a glass of the usual, a tall glass of water with a slice of lemon. Water is king on Mars. As you sip from your drink,
Judy asks you a question. "So have you heard the news about that lake? I figured someone who's in the sand box all day might know about it." ''')

        if aware_water and talk_to_hank and talk_to_man:
            print(" ")
            print("You tell her only what you heard from Hank. A large lake appeared to the south and everybody wants it.")
            print(" ")
            print(''' 
    Strange stuff, that old man in the corner came in rambling about it about an hour ago. He hasn't told me a word since.
Maybe you can pester him for some info if he's still sober enough. Even if those rumors are exaggerting, 
an entire lake of water doesn't just appear. Especially not on a place like Mars. I think something's going on. ''')
        
            print(" ")
            print('''
    You tell Judy about the old man and the strange prophecy.
"Huh. That is interesting. I wonder where he got that all from. By the looks of him, he's been on this rock for awhile. Maybe the Gamma rays
cooked his brain". Well, I got a communique from Hank while you were talkin to your friend over there, he say's to get up to his office. Pronto".''')
            break

        elif (aware_water or talk_to_hank) and talk_to_man:
            print(" ")
            print("You tell her about the encounter with the water guild caravan you had several days ago.")
            print(" ")
            print(''' 
    Strange stuff, that old man in the corner came in rambling about it about an hour ago. He hasn't told me a word since.
Maybe you can pester him for some info if he's still sober enough. I know the guild well enough, they don't just send an enitre caravan
on a wild goose chase. I think something's going on. ''')
            
            print(" ")
            print('''
    You tell Judy about the old man and the strange prophecy. 
"Huh. That is interesting. I wonder where he got that all from. By the looks of him, he's been on this rock for awhile. Maybe the Gamma rays
cooked his brain". Well, I got a communique from Hank while you were talkin to your friend over there, he say's to get up to his office. Pronto".''')
            break
        
        elif aware_water:
            print(" ")
            print('''
    Strange stuff, that old man in the corner came in rambling about it about an hour ago. He hasn't told me a word since.
Maybe you can pester him for some info if he's still sober enough. Even if those rumors are exaggerting, 
an entire lake of water doesn't just appear. Especially not on a place like Mars. I think something's going on.''')

        else:
            print(" ")
            print("You tell her this is the first you've heard about it.")
            print(" ")
            print(''' 
    Strange stuff, that old man in the corner came in rambling about it about an hour ago. Said that a lake has appeared in the south, and
that more will appear in time as the "ancient prophecies" come to fruition. He hasn't told me a word since.
Maybe you can pester him for some info if he's still sober enough. Even if those rumors are exaggerating, 
an entire lake of water doesn't just appear. Especially not on a place like Mars. I think something's going on. ''')
            aware_water = True
        

        
    elif bar_talk.lower() == "others":
        print(" ")
        print('''
You talk to several of the bar's occupants. The topic of conversation ranges from talking about the weather to talking about water. ''')

    else:
        print(" ")
        print("I'm sorry, try again.")


print(" ")
print("If you're reading this then you have completed chapter one. Congrats.")
exit()

#code grave yard

#    elif bar_talk.lower() == "old man":
#        print(" ")
#        print('''
#    You decide to appraoch the old man sitting in the corner. As you appraoch you can see in the dim light of booth that his face is deeply
#tanned and weathered by many harsh years on Mars. He might be a first generation colonist by the look of it. As you get closer, the old man
#raises his head and looks at you. "Ah, another stranger come to hear my tale of shimmering blue water upon a red planet" he says.  ''')
#        print(" ")
#        print(''' 
#    The old man tells you a fantastic tale of an ancient prophesy that must soon come to fruition. "Soon the waters of Mars will
#flow once more. The red desert will bloom and men will be free to spread across the planet. I saw it all in vision".
#What an eccentric performance. ''')
#        talk_to_man = True


#        elif character == "unaware_water":
#            print(" ")
#            print('''
#    Strange stuff, that old man in the corner came in rambling about it about an hour ago. He hasn't told me a word since.
#Maybe you can pester him for some info if he's still sober enough. I know the guild well enough, they don't just send an enitre caravan
#on a wild goose chase. I think something's going on..''')
