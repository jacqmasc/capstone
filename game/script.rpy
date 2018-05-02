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

    "{i}This is it. Our new home. Saynni is here with me, but she seems... Uncomfortable.{/i}"
    
    show saynni nuetral at right

    s "The villagers did not seem happy to see me."

    s "Perhaps I should just stay inside!"
    
    menu:
        
        "They saw you for only a moment!":
            jump moment
            
        "I'm sure they will warm up to you in time.":
            jump warm
            
            
label moment:
    
    s "A moment is enough for them to know I am a dragon."
    
    s "What I am is not exactly subtle."
    
    s "Even if the war is over..."
    
    jump nobattles
    
label warm:
    
    s "I doubt that. The war only recently came to an end..."
    
label nobattles:
    
    s "They must still despise dragons."
    
    d "You know that we chose this destination due to its distance from my kingdom."
    
    d "There have been no battles here."
    
    s "I would much rather stay here until you know for sure."
    
    "{i}Saynni seems much too anxious to head out from our new home.{/i}"
    
    "{i}I know this may look like just a cave, but I know Saynni.{/i}"
    
    "{i}This will not look like 'just a cave' once we are able to settle in.{/i}"
    
    "{i}I just need to get Saynni comfortable enough to do that...{/i}"
    
    d "Would you feel better if I head out before you?"
    
    d "I know you want to but we can't just stay in this cave forever."
    
    s "Sure we can!" 
    
    d "You were just complaining a few minutes ago about the leyline connection."
    
    s "It's not my fault there's so little magic here I keep losing signal!"
    
    "{i}I let out a sigh, but it's probably for the best that my wife remains where she feels safe.{/i}"
    
    d "All right, all right! You can stay home for now."
    
    "{i}Saynni seems happy to hear that, but she also has that look on her face that tells me she has a question to ask before I head out.{/i}"
    
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
    
    "{i}It was symbolic. Throwing away the achievements from our past for our future together in peace.{/i}"
    
    s "The war is over. No point in still having them."
    
    s "Even so, there is no reason for us not to get a few animal skulls for decoration! We could even put flowers on them."
    
    jump goodbyes
    
label goodbyes:
    
    d "I'll get you those wildflowers."
    
    d "Though, I might have to get them on my way back."
    
    d "I want to explore the village a bit before I meet the blacksmith for the interview and I wouldn't want to ruin them."
    
    s "Sounds fine by me. You are the strongest human I know. They would be foolish not to accept you as their apprentice."
    
    d "Now, now... The blacksmith would not have put up an ad on Craig's list if they were not serious in finding an apprentice that suits their needs."
    
    s "Perhaps... Either way, my dearest. Good luck."
    
    d "Thank you, Saynni. For now, goodbye."
    
    hide saynni
    
    
    "{i}With our goodbyes said, I head out from the darkness of our new home and squint due to the brightness of the sun.{/i}"
    
    stop music fadeout 1.0
    
    scene black
    
    play music "homedeparture.mp3"
    
    "{i}Once I am able to see, I look out towards where the village lies ahead.{/i}"
    
    "{i}Our home is not too far from the village.{/i}"
    
    "{i}As I make my way towards it... I can't help but wonder if I will be able to convince those within that Saynni means no harm.{/i}"
    
    "{i}First, I will have to prove my own worth to them. Eventually, I hope that they can trust me enough to accept us both.{/i}"
     
    "{i}She may be a dragon, but she is one whose treasure is her heart of gold.{/i}"
    
    "{i}After asking around I learned of some points of interest. Where should I go?{/i}"
    
    stop music fadeout 1.0
    
    jump nav_menu

label blacksmith:
    $ cur_loc = "blacksmith"
    scene bg blacksmith
    play music "rainyascent.mp3"
    if not met_shitij:
        call impressblacksmith from _call_impressblacksmith
    else:
        show shitij nuetral at right
        v "Can't get enough of my handsome face? Come back tomorrow morning. Bright and early!"
    jump nav_menu
    stop music fadeout 1.0

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
    d "Understood!"
    $ met_shitij = True
    return
    
label forge_axe:
    $ axepoints = 0
    $ safetyfirst = False
    $ dinner = False
    v "Let's see how you make an axe. Forge me an axe head."
    menu forge_axe1:
        "{i}It looks like the forge is already lit, so I'm going to...{/i}"
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
            "{i}I put on gloves, safety goggles, and an apron.{/i}"
            v "That is quite important."
            jump forge_axe1
    if not safetyfirst:
        d "Hold up. I better put on gloves before I touch this stuff."
    menu:
        "{i}I have a heated block of metal. Now I'll...{/i}"
        "Stab it a bunch.":
            $ axepoints += 1
            "{i}I'm good at that. I've stabbed lots of things.{/i}"
            "{i}I pull out my knife but Vihaan stops me and hands me a dull, pointed tool.{/i}"
        "Cool it off.":
            $ axepoints -= 1
            "{i}Wait, isn't metal more malleable when it is heated?{/i}"
            "{i}I am pretty sure I need to shape this thing.{/i}"
            "{i}I will try putting a hole in it for the handle.{/i}"
    "{i}I attack one side of the metal to wear a hole through it.{/i}"
    menu forge_axe2:
        "{i}Okay, that is done. What is next?{/i}"
        "Tape the head to a stick.":
            $ axepoints -= 2
            d "Hey, do you have any tape?"
            v "..."
            d "So I can put this on a stick."
            v "...{w} Have you ever seen an axe before?"
        "Dinner?" if dinner:
            $ dinner = False
            $ axepoints -= 1
            "{i}I am so hungry...{/i}"
            "{i}I wonder what Saynni wants to eat tonight?{/i}"
            v "Stop daydreaming!"
            "Sorry!"
            jump forge_axe2
        "Hammer head.":
            $ axepoints += 1
            "{i}I use a hammer to flatten the other side of the block.{/i}"
            "{i}This takes forever!{/i}"
    d "There! I am done!"
    "{i}The metal is lopsided and I don't think the hole for the handle is straight.{/i}"
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
        "{i}This looks less like a church and more like the town meeting hall.{/i}"
        "{i}I'm pretty sure this is the town meeting hall.{/i}"
        a "Good day!"
        d "Are you the mayor?"
        a "What? No! I'm Andy. The mayor is Miss Jundiel. She hasn't been dismissed from the war yet."
        d "So you're ruling in her place?"
        a "Well... Most of the council had to fight in the war, and there hasn't been a vote for new members yet."
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
            a "I guide people along the path of --"
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
    jump nav_menu
    stop music fadeout 1.0

label library:
    $ cur_loc = "library"
    scene bg library
    play music "inthebranches.mp3"
    show diana happy at left
    "{i}Did someone repurpose their house?{/i}"
    "{i}The sign outside said this was a library, but it looks more like a used book store...{/i}"
    "{i}There are a few people quietly reading their books. Oh! My presence seems to have gotten someone's attention.{/i}"
    show librarian nuetral at right
    ki "..."
    ki "... A face I do not recognize."
    ki "Welcome to the library, are you a traveller? It has been some time since anyone new has been here."
    d "I'm here to stay! I just moved in with my wife today, actually --"
    "{i}My louder, more booming voice seems to startle a few people in the area. Specifically, a man at a table beside ours.{/i}"
    hide librarian
    show keein nuetral at right
    k "Excuse me."
    k "This is a library, you should really keep your voice down."
    d "Right. My apologies, I was just excited to meet my new neighbors."
    k "You are the one with the dragon then, are you not?"
    "{i}His announcement has a few heads lifting from their books to stare at me.{/i}"
    "{i}Before I can open my mouth to make a remark, the person from before interrupts.{/i}"
    hide keein
    show librarian nuetral at right
    ki "... Keein. This is a library. Do not make a scene."
    hide librarian nuetral
    show keein nuetral at right
    k "..."
    hide keein nuetral
    "{i}He doesn't look happy about being interrupted, but he doesn't argue. He simply takes his book and heads towards the desk to check it out.{/i}"
    show librarian nuetral at right
    ki "... That was Keein. He is our resident wizard. He is usually like that."
    ki "I am Kioli. I am the head librarian, so even he has to listen to me here."
    d "I see... Thank you for the explanation."
    "{i}I keep my voice quieter than earlier, and eventually the others in the library go back to their books.{/i}"
    "{i}While Kioli seems friendly enough after a few words with them, I still feel a little awkward after that moment with Keein.{/i}"
    "{i}I decide to leave for now.{/i}"
    hide librarian
    
    $ met_keein = True
    jump nav_menu
    stop music fadeout 1.0

label home:
    $ cur_loc = "home"
    if met_shitij and met_andy and met_keein:
        hide diana happy
        scene black
        play music "homedeparture.mp3"
        
        "{i}I've been out awhile...{/i}"
        "{i}I should head home.{/i}"
        "{i}... Though, wasn't there something else I was supposed to do?{/i}"
        
        menu:

            "Remember to pick wildflowers.":
                jump remember

            "Forget to pick wildflowers.":
                jump forget
            
        label remember:
        "{i}That's right! Saynni wanted wildflowers to decorate the cave with.{/i}"
        "{i}On my way back home I pick up some wildflowers for her.{/i}"
        stop music fadeout 1.0
        scene bg cave
        play music "roots.mp3"
        show diana happy at left
        d "Saynni, I'm home!"
        show saynni nuetral at right
        s "Welcome home!"
        s "Oh! You remembered to pick up the wildflowers for me!"
        s "Now, I can decorate the cave with them tomorrow. Thank you, my love!"
        d "You're welcome! You're also looking at the village blacksmith's new apprentice!"
        s "Hah! I knew you would be. I even caught your favorite meal to celebrate."
        d "You're the best! Let's eat."
        stop music fadeout 1.0
        return
        
        label forget:
        "{i}Nothing is coming to mind...{/i}"
        "{i}I must have forgotten.{/i}"
        "{i}I just head home.{/i}"
        stop music fadeout 1.0
        scene bg cave
        play music "roots.mp3"
        show diana happy at left
        d "Saynni, I'm home!"
        show saynni nuetral at right
        s "Welcome home!"
        s "Diana! Did you forget the wildflowers for me?"
        "{i}Shoot! I forgot that Saynni wanted wildflowers to decorate the cave with.{/i}"
        d "I forgot..."
        s "I was going to decorate with them tomorrow..."
        s "Oh, well. That's alright."
        s "I can get them myself tomorrow."
        "{i}Though she may say that it's alright, I can tell that she is disappointed that I forgot...{/i}"
        d "At least I got the apprenticeship with that blacksmith?" 
        s "I knew you would... I even caught your favorite meal to celebrate."
        "{i}Now I definitely feel guilty that I forgot the wildflowers...{/i}"
        "{i}I will have to make it up to her in the future.{/i}"
        "You're the best! Let's eat."
        stop music fadeout 1.0
        return
    else:
        scene bg cave
        play music "roots.mp3"
        "{i}Looks like Saynni's asleep...{/i}"
        "{i}There's not much to do around here until she is awake. I'll head back to town.{/i}"
        
        jump nav_menu
        stop music fadeout 1.0


menu nav_menu:
    "Blacksmith." if cur_loc != "blacksmith":
        jump blacksmith
    "Church." if cur_loc != "church":
        jump church
    "Library." if cur_loc != "library":
        jump library
    "Home." if cur_loc != "home":
        jump home


