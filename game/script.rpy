# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
define d = Character(_('Diana'), color="#258256")
define s = Character(_('Saynni'), color="#00b8cc")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg cave

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show diana happy at left

    "This is it. Our new home. Saynni is here with me, but she seems... Uncomfortable."
    
    show saynni nuetral at right

    s "The villagers did not seem happy to see me."

    s "Perhaps I should just stay inside!"
    
    d "They saw you for only a moment! I am sure they will warm up to you in time."
    
    s "I doubt that. The war only recently came to an end..."
    
    s "They must still despise dragons."
    
    d "You know that we chose this destination due to its distance from my kingdom."
    
    d "There have been no battles here."
    
    s "I would much rather stay here until you know for sure."
    
    "Saynii seems much too anxious to head out from our new home."
    
    "I know this may look like just a cave, but I know Saynni."
    
    "This will not look like 'just a cave' once we are able to settle in."
    
    "I just need to get Saynni comfortable enough to do that..."
    
    d "Would you feel better if I head out before you?"
    
    d "I know you want to but we can't just stay in this cave forever."
    
    s "Sure we can!" 
    
    d "You were just complaining a few minutes ago about the leyline connection."
    
    s "It's not my fault there's so little magic here I keep losing signal!"
    
    "I let out a sigh, but it's probably for the best that my wife remains where she feels safe."
    
    d "All right, all right! You can stay home for now."
    
    "Saynni seems happy to hear that, but she also has that look on her face that tells me she has a question to ask before I head out."
    
    s "I have been thinking about how to decorate our home. Flowers or skulls?"
    
    menu:

        "Flowers.":
            jump flowers

        "Skulls.":
            jump skulls
            
label flowers:
    
    s "I saw a patch of wildflowers on the way here!"
    
    s "Do you think you could get some on your way out for me?"
    
    d "Of course, my love."
    
    jump goodbyes
    
label skulls:
    
    s "Damn. I should have kept my trophies from the war."
    
    d "In any case, I saw a patch of wildflowers on the way here. How about I get you some of those for now?"
    
    s "I was going to say that if you had chosen flowers!"
    
    d "I couldn't resist."
    
    d "Anyway, we threw out our trophies before we got married..."
    
    "It was symbolic. Throwing away the achievements from our past for our future together in peace."
    
    s "The war is over. No point in still having them."
    
    s "Even so, there is no reason for us not to get a few animal skulls for decoration! We could even put flowers on them."
    
    jump goodbyes
    
label goodbyes:
    
    d "I will get you those wildflowers."
    
    d "Though, I might have to get them on my way back."
    
    d "I want to explore the village a bit before I meet the blacksmith for the interview and I wouldn't want to ruin them."
    
    s "Sounds fine by me. You are the strongest human I know. They would be foolish not to accept you as their apprentice."
    
    d "Now, now... The blacksmith would not have put up an ad on Craig's list if they were not serious in finding an apprentice that suits their needs."
    
    s "Perhaps... Either way, my dearest. Good luck."
    
    d "Thank you, Saynni. For now, goodbye."
    
    hide saynni
    
    "With our goodbyes said, I head out from the darkness of our new home and squint due to the brightness of the sun."
    
    "Once I am able to see, I look out towards where the village lies ahead."
    
    "Saynni and I's home is not too far from the village."
    
    "As I make my way towards it... I can't help but wonder if I will be able to convince those within that Saynni means no harm."
    
    "First, I will have to prove my own worth to them. Eventually, I hope that they can trust me enough to accept us both."
     
    "She may be a dragon, but she is one whose treasure is her heart of gold."

    # This ends the game.

    return
