player = { 
    "name": "p1", 
    "score": 0
    }

def intro():
	print "Nice to see you! Please enter your name!"
	player["name"] = raw_input("please enter your name: ")

	print "Welcome! " + player["name"] + "!"

	print "This test is to know more about your personality."
	print "Dr. Phill who is a prominent psychologist asked Opera Whimpery for better understanding about herself."
	print "This test is quite accurate and takes only 2 minutes!"
	print ""

	raw_input ("press enter >>")

	print ""
	print "The purpose of this test is to know yourself in your current status. "
	print "Also, many companies use this test to evaluate their applicants to learn more about their personalities."
	print "Please answer the below questions to learn more about you!"
	print ""

	raw_input ("press enter >>")

	print ""
	question1()

def question1(): 
	print "1. When is the best time of a day?\n"
	print "a) Mornig\nb) Afternoon or early evening\nc) late at night\n"
	pcmd = raw_input ("Please type your answer [a, b, c]")
	if (pcmd == "a"):
		player["score"] = int(player["score"]) + 2
		question2()
	elif (pcmd == "b"):
		player["score"] = int(player["score"]) + 4 
		question2()
	elif (pcmd == "c"):
		player["score"] = int(player["score"]) + 6
		question2()
	else:
		print "Please enter proper answer\n"
		question1()


def question2():
	print "2. When you walk, you usually...\n"
	print "a) walk fast with a big stride.\nb) walk fast with a small stride."
	print "c) look forward, and walk slowly.\nd) look down, and walk slowly.\ne) walk very slowly.\n"
	pcmd = raw_input ("Please type your answer [a, b, c, d, e]")

	if (pcmd == "a"):
		player["score"] = int(player["score"]) + 6
		question3()
	elif (pcmd == "b"):
		player["score"] = int(player["score"]) + 4 
		question3()
	elif (pcmd == "c"):
		player["score"] = int(player["score"]) + 7
		question3()
	elif (pcmd == "d"):
		player["score"] = int(player["score"]) + 2
		question3()
	elif (pcmd == "e"):
		player["score"] = int(player["score"]) + 1
		question3()
	else:
		print "please enter proper answer!\n"
		question2()

def question3():
	print "3. When you have a conversation with people, you...\n"
	print "a) fold your arms."
	print "b) hold your hands together."
	print "c) place your hands behind your back."
	print "d) touch the person you are talking to."
	print "e) touch your ear, jaw or hair.\n"
	pcmd = raw_input ("Please type your answer [a, b, c, d, e]\n")

	if (pcmd == "a"):
		player["score"] = int(player["score"]) + 4
		question4()
	elif (pcmd == "b"):
		player["score"] = int(player["score"]) + 2
		question4()
	elif (pcmd == "c"):
		player["score"] = int(player["score"]) + 5
		question4()
	elif (pcmd == "d"):
		player["score"] = int(player["score"]) + 7
		question4()
	elif (pcmd == "e"):
		player["score"] = int(player["score"]) + 6
		question4()
	else:
		print "please enter proper answer!\n"
		question3()


def question4():
	print "4. When you sit to take a rest, you...\n"
	print "a) put legs side by side."
	print "b) hold your legs crossed."
	print "c) put your leg straight."
	print "d) put one leg under the other leg.\n"
	pcmd = raw_input ("Please type your answer [a, b, c, d]\n")

	if (pcmd == "a"):
		player["score"] = int(player["score"]) + 4
		question5()
	elif (pcmd == "b"):
		player["score"] = int(player["score"]) + 6
		question5()
	elif (pcmd == "c"):
		player["score"] = int(player["score"]) + 2
		question5()
	elif (pcmd == "d"):
		player["score"] = int(player["score"]) + 1
		question5()
	else:
		print "please enter proper answer!\n"
		question4()


def question5():
	print "5. When something funny happens, you..."
	print ""
	print "a) laugh loudly without hiding your feeling.\nb) laugh but not very loudly. "
	print "c) laugh quietly \nd) only smile like you are shy\n."
	pcmd = raw_input ("Please type your answer [a, b, c, d]")

	if (pcmd == "a"):
		player["score"] = int(player["score"]) + 6
		question6()
	elif (pcmd == "b"):
		player["score"] = int(player["score"]) + 4
		question6()
	elif (pcmd == "c"):
		player["score"] = int(player["score"]) + 3
		question6()
	elif (pcmd == "d"):
		player["score"] = int(player["score"]) + 2
		question6()
	else:
		print "please enter proper answer!\n"
		question5()

def question6():
	print "6. When you go to a place with lots of people such as a party, you..."
	print ""
	print "a) burst into the place in order to draw attention."
	print "b) enter calmly into the place and find a friend or acquaintance. "
	print "c) enter queitly.\n"
	
	pcmd = raw_input ("Please type your answer [a, b, c, d]")

	if (pcmd == "a"):
		player["score"] = int(player["score"]) + 6
		question7()
	elif (pcmd == "b"):
		player["score"] = int(player["score"]) + 4
		question7()
	elif (pcmd == "c"):
		player["score"] = int(player["score"]) + 2
		question7()
	else:
		print "please enter proper answer!"
		question6()

def question7():
	print "7. When you are totally immersed and disturbed, you..."
	print ""
	print "a) take it as a break time. "
	print "b) are very irritated "
	print "c) feel lost.\n"
	
	pcmd = raw_input ("Please type your answer [a, b, c, d]")

	if (pcmd == "a"):
		player["score"] = int(player["score"]) + 6
		question8()
	elif (pcmd == "b"):
		player["score"] = int(player["score"]) + 2
		question8()
	elif (pcmd == "c"):
		player["score"] = int(player["score"]) + 4
		question8()
	else:
		print "please enter proper answer!"
		question7()

def question8():
	print "8. What is your favorite color?"
	print ""
	print "a) Red or orrange"
	print "b) Black "
	print "c) Yellow or light blue"
	print "d) Green"
	print "e) Dark blue or purple"
	print "f) White"
	print "g) Brown or gray\n"

	pcmd = raw_input ("Please type your answer [a, b, c, d, e, f, g]")

	if (pcmd == "a"):
		player["score"] = int(player["score"]) + 6
		question9()
	elif (pcmd == "b"):
		player["score"] = int(player["score"]) + 7
		question9()
	elif (pcmd == "c"):
		player["score"] = int(player["score"]) + 5
		question9()
	elif (pcmd == "d"):
		player["score"] = int(player["score"]) + 4
		question9()
	elif (pcmd == "e"):
		player["score"] = int(player["score"]) + 3
		question9()
	elif (pcmd == "f"):
		player["score"] = int(player["score"]) + 2
		question9()
	elif (pcmd == "g"):
		player["score"] = int(player["score"]) + 1
		question9()
	else:
		print "please enter proper answer!\n"
		question8()

def question9():
	print "9. Right before you fall asleep, you..."
	print ""
	print "a) sleep on your front."
	print "b) sleep on your back. "
	print "c) sleep in the fetal position"
	print "d) sleep on your side and put a head on your arm."
	print "e) put the blanket above your head\n"

	pcmd = raw_input ("Please type your answer [a, b, c, d, e]")

	if (pcmd == "a"):
		player["score"] = int(player["score"]) + 7
		question10()
	elif (pcmd == "b"):
		player["score"] = int(player["score"]) + 6
		question10()
	elif (pcmd == "c"):
		player["score"] = int(player["score"]) + 4
		question10()
	elif (pcmd == "d"):
		player["score"] = int(player["score"]) + 2
		question10()
	elif (pcmd == "e"):
		player["score"] = int(player["score"]) + 1
		question10()
	else:
		print "please enter proper answer!\n"
		question9()

def question10():
	print "10. I often dream of this."
	print ""
	print "a) A dream of falling \nb) A dream of fighting or making effort "
	print "c) A dream of searching for a thing or a person"
	print "d) A dream of flying\ne) I don't usually dream"
	print "f) I always dream of good feeling\n"

	pcmd = raw_input ("Please type your answer [a, b, c, d, e]")

	if (pcmd == "a"):
		player["score"] = int(player["score"]) + 4
		quizOver()
	elif (pcmd == "b"):
		player["score"] = int(player["score"]) + 2
		quizOver()
	elif (pcmd == "c"):
		player["score"] = int(player["score"]) + 3
		quizOver()
	elif (pcmd == "d"):
		player["score"] = int(player["score"]) + 5
		quizOver()
	elif (pcmd == "e"):
		player["score"] = int(player["score"]) + 6
		quizOver()
	elif (pcmd == "f"):
		player["score"] = int(player["score"]) + 1
		quizOver()
	else:
		print "please enter proper answer!\n"
		question10()



def quizOver():
	print "-----------------------------------------------"
	print "And your score is " + str(player["score"])

	if int(player["score"] > 60):
		character1()
	elif int(60 >= player["score"] > 50):
		character2()
	elif int(50 >= player["score"] > 40):
		character3()
	elif int(40 >= player["score"] > 30):
		character4()
	elif int(30 >= player["score"] > 20):
		character5()
	elif int(player["score"] < 20):
		character6()

def character1():
	print "You are a vanity, self-centered, and extremely dominant person. "
	print "There may be those who envy you and try to look like you, but they will not trust you because they don't want to become close to you."

def character2():
	print "People around you think you are easily excited, fickle and impulsive. "
	print "But with the qualities of a leader, you can make bold decisions in no time. "
	print "You are adventurous, bold and seem to be a strong type of chance. "
	print "The people around you are attracted to the intensity you make."

def character3():
	print "People around you think you are fresh, youthful, realistic, fun and attractive." 
	print "You can draw people's attention from anywhere, but it doesn't mean you are arrogant."
	print "You can be thought of as a kind, friendly and understanding person."

def character4():
	print "People around you think you are prudent, wise, careful and realistic. And also smart, talented and capable but a humble person. " 
	print "You prudently approach to people when you make friends."
	print "Those who know you know realize that it is difficult to lose your trust. But they also know that once somebody loses it, it is almost impossible to recover."

def character5():
	print "Your friends see you as a persistent, a very cautious, slow but steady forwarder."
	print "If your friends see you being impusive, they will be shocked."
	print "Because they know you are the one who reject everything after thoroughly checking in every aspects."

def character6():
	print "Your friends see you as a shy, timid, indecisive and always caring. "
	print "Everytime you make a decisition, you think it as really hard. "
	print "And you are not very good at making a relationship with others. "
	print "People think of you as Don Quixote, a person who creats problems that do not exist. People close to you know this is not true, but the rest will not, and they also think you are a boring person."

intro()
