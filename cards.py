#cards.py
#Author: Kiran Bhadury

#JOKER A = 0, JOKER B = -1
#BOTTOM OF DECK AT INDEX 0, TOP AT INDEX 53

#Convert value and suit into a single number
cards = [20, 39, 36, 49, 25, 45, 28, 52, 0, 17, 9, 7, 13,\
16, 23, 47, 37, 18, 41, 1, 22, 11, 42, 30, 44, 14,\
46, 26, 12, 50, 38, 15, 2, 24, 33, 31, -1, 32, 3,\
21, 19, 6, 29, 43, 10, 5, 48, 51, 40, 4, 27, 34,\
35, 8]

cards = cards[::-1] #I had the deck in the wrong order!

inp = raw_input('Enter to continue, x to stop')
while(inp != 'x'):
	
	#Move jokers
	
	ja = cards.index(0) #find joker A
	if(ja == 0): #wrap around to top
		cards.insert(53,0)
		del cards[0]
	else: #swap joker A with card below it
		cards.insert(ja+1,cards[ja-1])
		del cards[ja-1]
	
	jb = cards.index(-1) #find joker B
	if(jb == 0): #move below second-to-top card
		cards.insert(52,-1)
		del cards[0]
	elif(jb == 1): #move just beneath top card
		cards.insert(53,-1)
		del cards[1]
	else:
		cards.insert(jb-2,-1)
		del cards[jb+1]
	
	#Perform triple cut
	
	#Find both jokers
	jtop = cards.index(0)
	jbot = cards.index(-1)
	#Figure out which one is on top (larger index)
	if(jtop < jbot):
		(jtop,jbot) = (jbot,jtop)
	#Identify sections
	top = cards[jtop+1:]
	bottom = cards[0:jbot]
	middle = cards[jbot:jtop+1]
	#Perform swap
	cards = top + middle + bottom
	
	#Perform count cut
	
	#Get bottom card's value
	bot_card = cards[0]
	if(bot_card <= 0):
		bot_card = 53 #Jokers' value
	#Identify sections
	count_cut = cards[54-bot_card:]
	bot_cut = cards[0:1]
	middle = cards[1:54-bot_card]
	#Perform swap
	cards = bot_cut + count_cut + middle
	
	#Get value
	
	top_card = cards[53]
	final_val = cards[53-top_card]
	if(final_val <= 0):
		print('Joker!  Restarting...')
	else:
		print('Final value:',final_val)

	inp = raw_input('Enter to continue, x to stop')