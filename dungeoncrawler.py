#generative room game
#by Ben Kulp

print"""
    ___                                    
   /   \_   _ _ __   __ _  ___  ___  _ __  
  / /\ / | | | '_ \ / _` |/ _ \/ _ \| '_ \ 
 / /_//| |_| | | | | (_| |  __/ (_) | | | |
/___,'  \__,_|_| |_|\__, |\___|\___/|_| |_|
                    |___/                  
   ___                   _           
  / __\ __ __ ___      _| | ___ _ __ 
 / / | '__/ _` \ \ /\ / / |/ _ \ '__|
/ /__| | | (_| |\ V  V /| |  __/ |   
\____/_|  \__,_| \_/\_/ |_|\___|_|   
"""

#initiating variables
player = 0
charcter = 0
weapon = 0
hp = 0
dmg = 0
score = 0
mhp = 0
mdmg = 0
chance = 0
x = 0
rnumber = 0
snumber = 0
enumber = 0
monster_name = 0

#creates function that returns a random number from input range
def roll(dice):
	dice = randrange(dice)
	return dice
	
	

#imports
from random import randrange

#creates character for use later
while player == 0:
	character = raw_input("Enter a character name: ")
	w = raw_input("Choose a weapon \n1. Axe \n2. Sword\n3. Dagger\n4. Mace\n:")
	try: 
		w = int(w)
		if w == 1:
			weapon = "Axe"
			dmg = roll(6) + roll(6)
		elif w == 2:
			weapon = "Sword"
			dmg = roll(4) + roll(4) + roll (4)
		elif w == 3:
			weapon = "Dagger"
			dmg = (roll(3) + 1) + (roll(3) + 1) * 2
		else:
			weapon = "Mace"
			dmg = roll(12) + 1
	except ValueError:
		print "This is not going well for you. In the future, pick a number."
	hp = (roll(6) + roll(6) + roll(6) + roll(6)) * 2
	print "Name: %s" % character 
	print "Weapon: %s - %d damage" % (weapon, dmg)
	print "Hit Points: %d" % hp
	value = raw_input("Keep or re-start?\n1. Keep \n2. Re-start\n: ")
	try:
		value = int(value)
		if value == 1:
			player = 1
		else:
			player = 0
	except ValueError:
		print "Really?!  Numbers, please type numbers."

#lists initializations
monster_display = ["Orc", "Goblin", "Ogre", "Hobgoblin"]


potion_choice = ["hp regen", "dmg plus", "Poison"]

room_adjectives = [
"brick-walled", "cavernous", "dark and musty", "dim and musty", 
"huge", "tiny", "small", "damp", "well-lit", "dimly-lit", 
"musty", "dank", "dark", "wood-panelled"
]

next_sentence =["There are bits of bone and detritus on the floor which you can't help but step on as you walk.",
"It smells strongly of cat urine. You hold back the urge to puke.",
"You can hear the sound of rats somewhere nearby and notice their droppings on the floor.",
"Lichen cover the walls and deaden the echo of your footsteps.",
"Light filters in through a hole in the ceiling.",
"Insect husks crunch under your feet as you walk.",
"You're certain you can hear voices coming from the next room, but as you approach they quiet.",
"You feel as if you are being watched and the hairs on the back of your neck stand at attention.",
"The temperature here is warm, a little too warm and you begin to sweat.",
"The floor is sticky, with what you cannot tell.",
"The room is completely silent.  You need to leave quickly, you can feel your nerves fraying.",
"There are bloody footsteps leading to a dead body, you search it but find nothing useful.",
"On the floor you see the skull of an unknown animal.",
"The walls in the room are crumbling away, you need to leave before one of them collapses.",
"You hear your footsteps echoed back strangely, nothing in the room seems to account for this."
"There are strange goat noises coming from behind the walls. It is unnerving.",
"There is a chill in the air, it is noticeably colder here.",
"Dust covers every surface, nobody has been in this room for ages."]

exit_options = ["east", "west", "south", "north", "south", "east", "north", "west", "east", "south", "west", "north"]

monster_des = ["it does not look friendly", 
"it gnashes its teeth at you.",
"it roars in anger and charges.",
"it is clearly injured.",
"it has huge fangs.",
"it glares at you from across the room.",
"you tremble with fear as it bellows a battle cry and charges at you.",
"it eyes you suspiciously from afar.",
"you can smell its breath from where you stand, which is kind of impressive.",
"drool spills from its lips, it clearly wants to eat you.",
"it is reading a book, quietly.", 
"its back is turned.",
"it really, really stinks.  Don't these things bathe?"]
#sets death handling


def died(x):
	print"""
__  __               ____  _          __
\ \/ /___  __  __   / __ \(_)__  ____/ /
 \  / __ \/ / / /  / / / / / _ \/ __  / 
 / / /_/ / /_/ /  / /_/ / /  __/ /_/ /  
/_/\____/\__,_/  /_____/_/\___/\__,_/   
                                        
	"""
	print "final score: ", score
	exit()

#creates functions that modify score, hp, dmg, mhp, and mdmg
def score_mod(x):
	global score 
	score = score + x
	return score

def hp_mod(x):
	global hp
	hp = hp + x
	return hp
	
def dmg_mod(x):
	global dmg
	dmg = dmg + x
	return dmg
	
def mhp_mod(x):
	global mhp
	mhp = mhp + x
	return mhp
	
def mdmg_mod(x):
	global mdmg
	mdmg = mdmg + x
	return mdmg

#defines all the possible death messages
death = ["You trip on your own feet, not only is it embarrassing, but you hit your head on a rock and die.", 
"You step on a hidden panel and spears shoot out from the walls.  You are impaled and die.", 
"A chittering roar erupts from the room, before you even understand what is happening you are bitten to death by rats.", 
"A large chunk of the ceiling comes loose and falls, you are stuck on the head and die instantly.",
"You fall into a pit with spikes. How you managed to not see the pit is sort of amazing.",
"You trip, skinning your knee. You don't even notice the infection that kills you three hours later.",]

#creates function that displays random death message when called.  
def death_message(x):
	dnumber = randrange(5)
	x = death[dnumber]
	print x
	died(1)

#defines the possible monsters and assigns appropriate bonuses based on random outcome	
def monster(x):
	global mhp
	global mdmg
	mhp = randrange(3,7)
	mdmg = randrange(0,2)
	mnumber = roll(3)
	mdnumber = roll(12)
	global monster_name
	monster_name = monster_display[mnumber]
	if mnumber == 0:
		mhp_mod(10)
		mdmg_mod(4)
	elif mnumber == 1:
		mhp_mod(4)
		mdmg_mod(1)
	elif mnumber == 2:
		mhp_mod(20)
		mdmg_mod(10)
	else:
		mhp_mod(3)
		mdmg_mod(2)
	print "A %s appears, %s" % (monster_display[mnumber], monster_des[mdnumber])
	print "Monster hp: %d" % mhp
	print "Monster dmg: %d" % mdmg
	monster_response = int(raw_input("What do you do?\n1. Flee\n2. Fight\n:"))
	if monster_response == 1:
		score_mod(-5)
		room_advance(1)
	else:
		score_mod(20)
		battle(1)

#defines the various potion outcomes	
def object(x):
	print "You see something on the ground,"
	pnumber = roll(4)
	score_mod(randrange(10,15))
	if pnumber == 0:
		print "it is a health potion and you drink it."
		hp_mod(10)
		print "You now have %d hit points." % hp
		raw_input(">press enter to continue<")
		room_advance(1)
	if pnumber == 1:
		print "it is a damage plus potion and you drink it."
		dmg_mod(2)
		print "You now deal %d damage." % dmg
		raw_input(">press enter to continue<")
		room_advance(1)
	if pnumber == 2:
		print "It is a poison potion so you don't drink it."
		raw_input(">press enter to continue<")
		room_advance(1)
	else:
		unmarked(1)

#defines what happens when an unmarked bottle is found		
def unmarked(x):
	print "The potion is unmarked, do you drink it?"
	pdecision = raw_input("1. Yes\n2. No: ")
	try:
		pdecision = int(pdecision)
	except ValueError:
		"The potion is poison, you die wishing you could type numbers."
		died(1)
	if pdecision == 1:
		score_mod(randrange(25,50))
		x = roll(2)
		if x == 1:
			print "You probably shouldn't drink random things off the ground."
			print "That was poison and you die and it is really painful."
			score_mod(randrange(25,50))
			died(1)
		else:
			print "You got really lucky, that was a health potion."
			print "you gain 10 hp."
			hp_mod(10)
			score_mod(randrange(50,100))
			print "current hp: %d" % hp
			raw_input(">press enter to continue<")
			room_advance(1)
	else:
		print "You put the potion down."
		raw_input(">press enter to continue<")
		room_advance(1)
		
#function that executes battle between player and monster
def battle(x):
	global hp
	global mhp
	global dmg
	global mdmg
	global score
	while hp > 0 and mhp > 0:
		mhp_mod(-dmg)
		print "%s attacks, doing %d damage. The %s has %d hit points left" % (character, dmg, monster_name, mhp)
		if mhp <= 0:
			print "the %s dies" % monster_name
			score_mod(randrange(90,115))
			print "current score: %d" % score
			room_advance(1)
		hp_mod(-mdmg)
		print "The %s attacks, hitting %s for %d damage. You have %d hit points left." % (monster_name, character, mdmg, hp)
		if hp <= 0:
			print "you were killed by the %s" % monster_name
			died(1)		


#creates current room and determines actions for that room
def room_call(x):
	rnumber = roll(13)
	snumber = roll(10)
	enumber = roll(3)
	print "You enter a %s room." % room_adjectives[rnumber]
	print "%s" % next_sentence[snumber]
	print "current score: %d" % score
	chance = roll(2)
	if chance == 1:
		monster(1)
	else:	
		chance2 = roll(3)
		if chance2 == 1 or chance2 == 3:
			object(1)
		else:
			chance3 = roll(3)
			if chance3 == 2:
				death_message(1)
			else:
				room_advance(1)

				
#shows options for room exit
def room_advance(x):
	score_mod(roll(20))
	enumber = roll(11)
	print "There are exits to the %s and %s." % (exit_options[enumber], exit_options[enumber + 1])
	print "Which direction do you wish to go?."
	print "1. %s" % exit_options[enumber]
	print "2. %s" % exit_options[enumber + 1]
	direction_exit = raw_input(": ")
	room_call(1)
	
	
room_call(1)

