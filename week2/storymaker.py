print ("Welcome!")
print ("Answer the questions below to play!")
print ("-----------------------------------")

adjective1 = raw_input ("Enter your favorite adjective: ")
name1 = raw_input ("Enter your name: ")
name2 = raw_input ("Enter your friend's name: ")
adjective2 = raw_input ("Enter an adjective you don't really like: ")
maxim1 = raw_input ("Enter a Maxim you like: ")

story = "Once upon a time, there was a " + adjective1 + " cat named " + name1 +
". The cat did not like a dog called " + name2 + " who lived with " + name1 + 
" because the dog was too " + adjective2 + ". So, the cat called " + name1 + " told "
+ name2 + " to " + maxim1 + ". " + name2 + " was so impressed and " + name1 + " and "
+ name2 + " lived happily ever after. "

print (story)
