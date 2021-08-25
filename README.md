## Ombot

!!! USE V2, V1 IS AN OLDER VERSION !!!

(sorry if the formatting for this readme seems super cheesy, I had to do it that way for the rubric)

Hi, my name is Tyson. I’m a student in an AP Computer Science class, tasked with making an interactive discord bot in Python. Introducing...

Ombot!

Ombot is a (slightly) interactive bot to add to servers. Using the ‘/’ prefix, Ombot can:

/commands: Give all of the available commands (it’s just this list, but in discord, wow)

/react: Reacts to the message, more of a test than anything else

/hello: Really simple, just says hi to you

/face: Prints out a little ascii face

/tarot: Gives you a tarot reading

/maze: Makes a playable (still not randomized >_<) maze

/tic: Creates a tic-tac-toe board to play against the player. (ombot might cheat just a bit ;) )

And a super-secret super-annoying dad joke function!
If Ombot sees anyone send a message with an “I’m”, it’ll react and make a dad joke off the occasion! “I’m really starting to hate this bot” “Hi really starting to hate this bot, I’m dad!”
You get the idea.
Using waaay too many loops, it iterates through the message, and records every word from the first I’m to the next punctuation marker. After that, it removes the marker, and puts it into the response template, sending it in the respective server.

Along with that, it’s got some secret responses, hidden in the code for only I to see. Try doing something like /beep, /boop, or /hey ombot.

It was good to get back in and relearn some python. I had a bit of experience when I was super young, but nothing more than "wow I printed a list," so I'm glad to see how far my coding's come.

(also yeah, the code could use some cleaning up, I made half of it in my calc class, and the other half at 1am, cut me some slack)
