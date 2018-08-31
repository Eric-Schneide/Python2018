import random
import time

#start up program to get this text.
name= input("Hello, thank you for speaking with the magic eight ball. Tell me now, what is your name?")

time.sleep(2)

print ("Thank you %s" %str(name.upper())+", I can see and answer all your questions. All you have to do is ask them.")

time.sleep(2)

print ("When you are done bothering the great magic eight ball with your questions, simply say stop.")
answers=["Yes, It is certain","My answer is no"," I see into my crystal ball.It says go away.",
         "Better not tell you now.","Without a doubt.","You may rely on it.", "I really dont care.",
         "There is no good way to say this","Let me ask you a question. Does this even matter",
         "Much like you this question doesn't matter.","The odds have never once been in your favor. I see no reason why that should start now,"
         "-_- I don't care enough to answer your question.","Hold on, one can not simply ask the great magic eight ball anything. Come on make it meaningful",
         "Really that is how you wish to spend your one question. What a waste.","I should have really gone back to college when I had the chance.",
         "I could bang a rat against the wall and get a better answer than the one I could give to your question."]

time.sleep(2)

#Empty variable 
question= ""

#Start of the questions
while question!= "stop":
    question= input("Now tell me %s" %str(name.upper()) + ", what questions do you have for the great magic eight ball?")

    time.sleep(2)
    
    #Exit
    if str(question)=="stop":
        print("Thank you for wasting the great magic eight ball's time. Now please get out.")
        break

    elif str(question)== "how old are you":
        print("My age has nothing to do with my wisdom now please ask a real question or get out of my program.")
        

    else:
        #Random generator to corespond to a list of answers
        print (random.choice(answers))

        #and back to the top of the loop
        time.sleep(2)
        
