import numpy as np
import random
import datetime
greetings=np.array(["hello","hey","greetings","hola","hi","heyy","heyyy","heyyy"])
greetings_response=np.array(["Heyya","Hello","Heyyy","wassup"])

task=np.array(["wassup","how u doin","what's up","how is it going","how are you","how is life","how's life"])
task_response="It's so boring"

goodbye=np.array(["bye","goodbye","see ya later","c ya later","cya","i am leaving","have a good day"])
goodbye_response=np.array(["Byeeee my friend","Talk to you later,byee","See ya later"])

age=np.array(["how old are u ","what is your age","when were u made"])
age_response="Guess my age"

name=np.array(["what is your name ","ur name","what's ur name","your name"])
name_response="My name is Vchat,cool name right"

sad_responses=np.array(["Hey you sound sad","Everything okay buddy?","I wish i had arms just to hug you right now","You sound sad,Just know that I am always here for you","You seem a bit off just know that I love and believe in you"])

jokes=np.array(["joke","tell me a joke","i want a joke","say a joke","lemme know a joke"])
jokes_response=np.array(["I broke my finger last week.On the other hand,I'm okay","I came up with a new word yesterday:Plagiarism", "What do dentists call their x-rays?\nTooth pics","What did one ocean say to the other ocean?\nNothing, it just waved.","I tried to catch fog yesterday.Mist","What does a nosey pepper do\nIt gets jalapeño business","You don't need a parachute to go skydiving.You need a parachute to go skydiving twice"])

story=np.array(["tell me a story","story","short stories","stories","horror story","tell me a horror story","horror stories"])
story_response=np.array(["Are you afraid of the dark?' That was the last thing I heard before the lightbulb shattered behind me","I decided to kill off a few characters in the book I’m writing. It should definitely spice up this autobiography a little","Being buried alive was bad enough. Realizing I wasn't alone in my own grave was worse","My daughter won't stop crying and screaming in the middle of the night. I visit her grave and ask her to stop, but it doesn't help","I'm not scared that I’ve been seeing 'missing' posters for myself. It’s the fact that the news is now saying that my body has been found"])

randomtopics=np.array(["start convo","start some topic","choose a topic","start conversation","you start conversation"])
randomtopics_response=np.array(["Sports","Games","Travel","Food","Music","Movies,series and anime"])

dates=np.array(["what day is it","whats todays date","what time is it","what date is it","whats the date","whats the time"])


sports=np.array(["Which is your favorite sport","Do you play any sports","Have you ever played for any team","What are some sports you don't like?","Have you ever met a sports celbrity"])
sports_reponses=np.array(["I like all sports equally","Nope i don't play any sports","No","I like all sports equally","No i have never met a sports celebrity"])


games=np.array(["Do u play any video games?","Do u like CSGO or valorant?","Which is the best GTA game in your opinion?","Do you have your own minecraft world?","Did you ever play Emulator games?","Playstation or Xbox which do you like more"])
games_response=np.array(["Yes i have seen few gameplays,but i have never played","I prefer valorant","I think GTA vice city is a classic but GTA 5 is the best because of graphics and gameplay","Nope,not yet but i will surely build my own minecraft world","I have seen GBA and nintendo gameplay but i have never played","I prefer playstation,but i feel sad because PS5 is always out of stock"])

travel=np.array(["Which is the best tourist place you have been to?","Tell me about your travel bucket list","Which mode of transport do u prefer?","Do you like mornings or night?"])
travel_response=np.array(["I like this planet","I want to roam everywhere","Wireless anyday","I am faster at night so night"])


food=np.array(["What is your favorite cuisine?","Whats your favorite snack?","Can you cook?","Do you like trying new foods?"])
food_response=np.array(["The internet at NASA","Your mobile data","I can cook up stories for you :)","Yes"])

music=np.array(["Which is your favorite band?","Who is your favorite artist?","Have you ever been to a concert?","Can you play any instruments?","Are you a good singer?"])
music_response=np.array(["Anything fast enough for me to talk to you","I like all of them","Nope not yet","No not yet","No,But I can try singing for you xD"])

movies=np.array(["Which is your favorite movie","What is your favorite genre?","Which is your favorite series?","Do you watch anime?","Which is your favorite anime?"])
movies_response=np.array(["I like all movies","Horror,Romcom,Suspense,Drama basically everything lol","I haven't watched many","Yes i have seen a few","Nothing in particular"])

response=np.array(["Good to knoww","Glad to hear","Ohhhh that's good","Niceee","Ohhhhh","Ohhhh niceeee"])


fitness=np.array(["I see you have decided to follow up your fitness records!","It’s great to see you taking care of yourself.","Fitness should be everyone’s primary goal, welcome!!","I’m so happy you’re here again!"])

diastolic=np.array(["Please tell me today's diastolic blood pressure that you measured? (You only have to enter the magnitude of mm Hg!)","What did your sphygmomanometer show today for diastolic? (You only have to enter the magnitude of mm Hg!)","Enter the measured diastolic value: (You only have to enter the magnitude of mm Hg!)"])

systolic=np.array(["And the systolic? (Again, only the magnitude please.)","What about the systolic measurement of today's blood pressure? (Again, only the magnitude please.)","Mention the systolic measurement too! (Again, only the magnitude please.)"])

steps=np.array(["How many steps did you complete? Only expecting the number :) ","How many successful steps does our pedometer show today? Only expecting the number :)"])

exercise=np.array(["How many minutes of exercise did we manage today? (Kindly input only in minutes, just the magnitude)","Did the time of exercise today exceed yesterday's? (Just the number of minutes please)","What is the number of minutes you worked out for today? "])

highbp=np.array(["That's too high! It's unhealthy. I would suggest you reduce your sodium intake, I do not wish for you to be unfit!","Oh my god! That's an alarming amount! Maybe you should work on reducing the amount of alcohol and increase low-fat dairy product intake.","With such high levels of blood pressure I think you should control your diet :("])

mediumbp=np.array(["That's not extremely high but we can certainly do better :) Let's work on a better diet!","Not where you would want it to be, but managable. Let's exercise regularly!","I'd suggest reduced sodium intake since we're slightly above the values we would like to see!"])

lowbp=np.array(["Looks like the values have dippped a little low here. I'd suggest a higher sodium intake!","Need to have it higher than that! Drink some water and check again next week!","Let's work on a healthier diet and see better numbers soon."])

verylowbp=np.array(["That's too low!","That's not quite possible, it's too low!","Too low a reading!"])

dailygoals=np.array(["Oh my god, that's amazing! You completed your daily goal!","Keep up that hard work, you completed your daily goal!","I told you you could do it! Great job!"])

closegoals=np.array(["You are not at your goal yet, but keep trying!","You can do better!","Don't give up, tomorrow is a new day!"])








