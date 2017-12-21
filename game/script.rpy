# Characters
define d = Character("Diana", image="diana")
define s = Character("Saynni", image="saynni")
define v = Character("Vihaan", image="vihaan")
define a = Character("Andy", image="andy")
define k = Character("Keein", image="keein")
define ki = Character("Kioli", image="kioli")
define b = Character("Baethas", image="baethas")
define z = Character("Zhaleh", image="zhaleh")

# Portraits

# Variables
default cur_loc = "home"
default met_shitij = False
default met_andy = False
default met_keein = False


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
    
    play music "roots.mp3"

    "This is it. Our new home. Saynni is here with me, but she seems... Uncomfortable."
    
    show saynni nuetral at right

    s "The villagers did not seem happy to see me."

    s "Perhaps I should just stay inside!"
    
    menu:
        
        "They saw you for only a moment!":
            jump moment
            
        "I'm sure they will warm up to you in time.":
            jump warm
            
            
label moment:
    
    d "They saw you for only a moment!"
    
    s "A moment is enough for them to know I am a dragon."
    
    s "What I am is not exactly subtle."
    
    s "Even if the war is over..."
    
    jump nobattles
    
label warm:
    
    d "I'm sure they will warm up to you in time"
    
    s "I doubt that. The war only recently came to an end..."
    
label nobattles:
    
    s "They must still despise dragons."
    
    d "You know that we chose this destination due to its distance from my kingdom."
    
    d "There have been no battles here."
    
    s "I would much rather stay here until you know for sure."
    
    "Saynni seems much too anxious to head out from our new home."
    
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
    
    stop music fadeout 1.0
    
    "With our goodbyes said, I head out from the darkness of our new home and squint due to the brightness of the sun."
    
    scene black
    
    "Once I am able to see, I look out towards where the village lies ahead."
    
    "Our home is not too far from the village."
    
    "As I make my way towards it... I can't help but wonder if I will be able to convince those within that Saynni means no harm."
    
    "First, I will have to prove my own worth to them. Eventually, I hope that they can trust me enough to accept us both."
     
    "She may be a dragon, but she is one whose treasure is her heart of gold."
    
    "After asking around I learned of some points of interest. Where should I go?"
    
    jump nav_menu

label blacksmith:
    $ cur_loc = "blacksmith"
    scene bg blacksmith
    play music "rainyascent.mp3"
    if not met_shitij:
        call impressblacksmith from _call_impressblacksmith
    else:
        show shitij nuetral at right
        sh "Can't get enough of my handsome face? Come back tomorrow morning. Bright and early!"
    jump nav_menu

label impressblacksmith:
    show diana happy at left
    show shitij nuetral at right
    d "Hello. Is the blacksmith Vihaan here?"
    v "I'm sorry, I'm not taking any custom orders right now."
    d "No, I'm here for the apprenticeship. It was on the Craig's List bulletin back in Ardglass."
    v "You should have said so! Good old Craig. We've been friends for decades. Did you know he--"
    d "Is the position still open?"
    v "Indeed it is!"
    v "So you think you're good enough to be my apprentice? I'll warn you, many have tried to get this coveted position and failed."
    d "I'm a quick learner."
    v "But do you have the moxie? Let's see what you're capable of!"
    d "Wait, it's a learning position--"
    call forge_axe from _call_forge_axe
    v "What's your name?"
    d "Diana."
    v "Alright Diana. You have the privilege of being my apprentice. I expect you back here first thing tomorrow."
    "Understood!"
    $ met_shitij = True
    stop music fadeout 1.0
    return
    
label forge_axe:
    $ axepoints = 0
    $ safetyfirst = False
    $ dinner = False
    v "Let's see how you make an axe. Forge me an axe head."
    menu forge_axe1:
        "It looks like the forge is already lit, so I'm going to..."
        "Make dinner." if not dinner:
            $ dinner = True
            $ axepoints -= 1
            d "The oven's ready. Time to cook!"
            v "It's not for food!"
            jump forge_axe1
        "Melt metal into a block.":
            $ axepoints += 2
            v "Ha! I half expect you to start mining the metal yourself."
            v "There's some heated blocks in the forge you can use."
        "Heat metal.":
            $ axepoints += 1
            v "Good job! Some metal is already heated in the forge."
        "Safety first!" if not safetyfirst:
            $ axepoints += 1
            $ safetyfirst = True
            "I put on gloves, safety goggles, and an apron."
            v "That is quite important."
            jump forge_axe1
    if not safetyfirst:
        d "Hold up. I better put on gloves before I touch this stuff."
    menu:
        "I have a heated block of metal. Now I'll..."
        "Stab it a bunch.":
            $ axepoints += 1
            "I'm good at that. I've stabbed lots of things."
            "I pull out my knife but Vihaan stops me and hands me a dull, pointed tool."
        "Cool it off.":
            $ axepoints -= 1
            "Wait, isn't metal more malleable when it's heated?"
            "I'm pretty sure I need to shape this thing."
            "I'll try putting a hole in it for the handle."
    "I attack one side of the metal to wear a hole through it."
    menu forge_axe2:
        "Phew, that's done. What's next?"
        "Tape the head to a stick.":
            $ axepoints -= 2
            d "Hey, do you have any tape?"
            v "..."
            d "So I can put this on a stick."
            v "...{w} Have you ever seen an axe before?"
        "Dinner?" if dinner:
            $ dinner = False
            $ axepoints -= 1
            "I'm so hungry."
            "I wonder what Saynni wants to eat tonight?"
            v "Stop daydreaming!"
            "Crap!"
            jump forge_axe2
        "Hammer head.":
            $ axepoints += 1
            "I use a hammer to flatten the other side of the block."
            "This takes forever!"
    d "There! I'm done!"
    "The metal is lopsided and I don't think the hole for the handle is straight."
    v "Hmmm...."
    if axepoints == 5:
        v "Fantastic!"
    elif axepoints > 0:
        v "Acceptable."
    else:
        v "You tried."
    return



label church:
    $ cur_loc = "church"
    scene bg church
    play music "hiddengrotto.mp3"
    if met_andy:
        show diana happy at left
        show andy happy at right
        a "Hello!"
        a "Do you need something?"
    else:
        scene bg church
        show diana happy at left
        show andy happy at right
        "This looks less like a church and more like the town meeting hall."
        "I'm pretty sure this is the town meeting hall."
        a "Good day!"
        d "Are you the mayor?"
        a "What? No! I'm Andy. The mayor is Miss Jundiel. She hasn't been dismissed from the war yet."
        d "So you're ruling in her place?"
        a "Well... most of the council had to fight in the war, and there hasn't been a vote for new members yet."
        a "So you could say I'm one of the three 'rulers' right now."
        d "Cool thing Mister Ruler. I have some questions."
    menu ask_andy:
        "I was told this was a church.":
            a "It's a building with many functions."
            a "One of which is the worship of whatever deities you choose."
            a "Provided minimal setup is acceptable."
            jump ask_andy
        "What do you do?":
            a "I follow the teachings of Ihwaz and guide people along his path."
            d "Someone in my unit followed Ihwaz. They were very passive aggressive."
            a "I suppose that's one way of interpreting his teachings..."
            d "So you're a priest or something?"
            a "No, I'm just a passionate follower."
            d "What do you do all day?"
            a "I guide people along the path of--"
            d "So you're a priest."
            a "...{w} I believe the organized religion around him would take offense to that."
            a "Call me a counseler if you must."
            jump ask_andy
        "The mayor went off to war?":
            a "Most of the town got recruited. We're not sure who's alive and who's dead."
            a "But I got a letter from Miss Jundiel last week. She's in the capital. They've started dismissing troops, but hers is still on duty."
            d "Were you recruited?"
            a "No. I'm one of the lucky few."
            jump ask_andy
        "I got an apprenticeship with the blacksmith today." if met_shitij:
            a "You did? That's exciting!"
            a "He's been trying to find somebody for a while now."
            a "He's rather picky. I wonder what you did to impress him."
            d "Everyone's got their little secrets!"
            jump ask_andy
        "That's all.":
            d "That's all for now. Thank you!"
            a "I'm always happy to help."
    $ met_andy = True
    stop music fadeout 1.0
    jump nav_menu

label library:
    $ cur_loc = "library"
    scene bg library
    play music "homedeparture.mp3"
    show diana happy at left
    "Did someone repurpose their house?"
    "The sign outside said this was a library, but it looks more like a used book store..."
    "There are a few people quietly reading their books. Oh! My presence seems to have gotten someone's attention."
    show librarian nuetral at right
    ki "..."
    ki "... A face I do not recognize."
    ki "Welcome to the library, are you a traveller? It has been some time since anyone new has been here."
    d "I'm here to stay! I just moved in with my wife today, actually --"
    "My louder, more booming voice seems to startle a few people in the area. Specifically, a man at a table beside ours."
    hide librarian
    show keein nuetral at right
    k "Excuse me."
    k "This is a library, you should really keep your voice down."
    d "Right. My apologies, I was just excited to meet my new neighbors."
    k "You are the one with the dragon then, are you not?"
    "His announcement has a few heads lifting from their books to stare at me."
    "Before I can open my mouth to make a remark, the person from before interrupts."
    hide keein
    show librarian nuetral at right
    ki "... Keein. This is a library, do not make a scene."
    hide librarian nuetral
    show keein nuetral at right
    k "..."
    hide keein nuetral
    "He doesn't look happy about being interrupted, but he doesn't argue. He simply takes his book and heads towards the desk to check it out."
    show librarian nuetral at right
    ki "... That was Keein. He is our resident wizard. He is usually like that."
    ki "I am Kioli. I am the head librarian, so even he has to listen to me here."
    d "I see..."
    "I keep my voice quieter than earlier, and eventually the others in the library go back to their books."
    hide librarian
    
    $ met_keein = True
    stop music fadeout 1.0
    jump nav_menu

label home:
    $ cur_loc = "home"
    scene bg cave
    play music "roots.mp3"
    if met_shitij and met_andy:
        d "I picked up some wildflowers."
        return
    else:
        "Looks like Saynni is asleep..."
        "There's not much to do around here until she is awake. I'll head back to town."
        jump nav_menu


menu nav_menu:
    "Blacksmith." if cur_loc != "blacksmith":
        jump blacksmith
    "Church." if cur_loc != "church":
        jump church
    "Library." if cur_loc != "library":
        jump library
    "Home." if cur_loc != "home":
        jump home


