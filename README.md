# Visual-Novel
# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define j = Character("john")
define d = Character("dave")
define m = Character("mare")

# The game starts here.

label start:
    scene forest
    show dave_happy as d at right:


    "Welcome to the Forest Adventure, this is Dave."
    "I am here to celebrate my Birthday with my other two friends."
    "I, mare, and shawn are in this forest together for camping."

label forest1:
    scene forest1

    show john_happy as j at left:

    j "Welcome to our journey!"
    j "It is your time to make decisions and lead us towards the right path so that we can celebrate our friend's brithday between
    beautiful mountains."

    show john_happy as j at left
    with move
    show dave_happy as d at right
    with move
    show mare_happy as m

    d "The forest looks beautiful."
    j "Yes! I am so excited as it is my first time going for camping."
    m "It's Dave's 16th birthday! We should make it memorable for him."
    d "Thanks, but first we should search for a place where we can set our tent and bonfire ."

    menu:
        "Which way should we go?"

        "Let's check out the mountains on the left!":
            jump mountains
        "Take Right, because right is always the right way to go!":
            jump haunted_house

label mountains:
    scene f2
    show dave_happy as d at left
    show mare_happy as m at right
    with move

    d "I think we should place our tent near the mountains because it has lot to offer as we can also go for hiking."

    m "I agree, we will get to see widest array of stars at night."
    d "Let's go!"
    show mare_tired as m at right
    m "We are walking since 1 hour. I am very tired can we please take some rest?"

    scene lightning
    show john_scared as j at left
    show mare_scared as m at right
    with move

    j "Did you guys heard sounds of lightning and thunder?"
    m "Oh no! It started raining."
    j "Come on guys. Let's get going. The weather is getting worst."
    m "I'm scared! I think we should go back home our trip has almost ruined."
    j "That is not possible because it is raining heavily and we cannot see anything."

    scene rain

    menu:
        "Help dave, mare, and john to rescue from the forest"

        "Do you want to find a shed?":
            jump find_a_shed
        "Do you want to Continue straight and find a shed later?":
            jump river

label find_a_shed:
    show dave_scared as d at left
    show john_scared as j at right
    show mare_sad as m
    d "I am sorry guys this is all because of me. I insisted to go for camping and did not checked the weather."
    m "Don't blame yourself dave."

    "They shouted for help, but deep in the jungle their was no one to come to their rescue."
    "As night fell the children were afraid they would never be found and end up being eaten by a wild creature."
    "All three started running to escape the rain and get out of the forest."
    scene cave
    "Suddenly, they came across a gigantic cave."
    "What do you think? Should they go inside or not?"
    menu:
        "Yes, they should go inside to protect themselves from the power of the rain until next morning.":
            jump inside_the_cave
        "No, they should not go inside as their might be something scary inside.":
            jump outside_the_cave

label river:
    scene river
    "This is called a Blue River which flows between the forest. It is the most beautiful place for river rafting."
    show mare_happy as m at right
    show dave_normal as d at left
    m "This is the most beautiful place I have ever seen in my life."
    d "Did you noticed one thing?"
    m "What?"
    d "It stopped raining and the weather has turned sunny."
    show john_happy as j
    j "We found a perfect place for our camping."
    "They took out their camping equipments, 4-inch luxury sleeping pads and rain-proof tent making the camping portion
    of their trip much more enjoyable."
    scene camp
    show mare_happy as m at left
    m "Our tent is set. Now we are ready to celebrate our friend's birthday between this breathtaking scenery."
    show john_happy as j
    j "I have heard about this place it has a lot of camping activities. We can spend our time reading books, playing games, fishing,
    river rafting, or taking photos of the magnificent scenery."
    m "I think dave is not aware of these activities therefore, we should surprise him."
    j "Where is dave?"
    m "He has gone to take pictures of the scenery."
    j "That's great! I think we should go for fishing and cook something delicious for him."
    m "Good idea! Let's go."
    scene food
    show mare_happy as m at right
    m "This looks delicious. John, I din't knew you cook so well."
    show john_wink as j
    j "Thanks mare, I learned from my mom."
    m "Photography is dave's passion so I think he will be late. Till then we can also arrange rafting equipments."
    show john_happy as j
    j "We can rent them from a nearby store."
    "Mare and John were ready to surprise Dave."
    "After an hour of all preperations Dave comes in."
    show dave_happy as d at left
    m "SURPRISE...HAPPY BIRTHDAY FRIEND:)"
    j "HAPPY BIRTHDAY DAVE!"
    d "Thank you so much guys. The food looks yummm."
    m "We cooked for you and we have other surprise waiting for you."
    j "Let's eat first."
    d "The food is really good. I loved it!"
    scene rafting
    "After eating and taking rest they went for river rafting."
    show dave_happy as d
    d "Wowww! guys this is so wonderful and adventurous. I had no clue about these activities."
    show mare_happy as m at right
    show john_happy as j at left
    m "It's time to have some fun."
    j "Come on guys. Let's go for a water ride."
    d "This is the most daring experience of my life."
    "They all enjoyed these new activities and created best memories with each other."
    scene sky
    "Finally, their trip ends under the enchanting view of the bright stars shone all over in the sky."

    return


label inside_the_cave:
    scene inside_the_cave
    show dave_scared as d at right
    show mare_sad as m at left
    show john_scared as j

    d "It is so scary in here."
    m "Yes, and it is very dark too."
    j "It is dark and cold. We have to sleep and continue our journey tomorrow morning."
    m "I hope the weather gets better tomorrow."
    j "Guys, let's collect woods to build a bonfire it will provide us light and warmth."
    m "sounds good"
    scene bonfire
    show mare_normal as m at left
    show john_happy as j at right

    m "Now I feel much better."
    j "We should take rest now."
    "The three kids fall asleep hugging each other in the cave."
    "In the middle of the night they heard a strange noise."

    show mare_scared as m at left
    m "John, Dave wake up!"
    show john_scared as j at right
    j "What happened?"
    show dave_scared as d
    d "What's wrong mare why you are shouting?"
    show mare_scared as m at left
    m "Shush! Did you heard some noise?"
    show dave_scared as d
    d "Yes, what noise is that?"
    show john_afraid as j at right
    j "Mare, dave turn around! I see something coming towards us."

    scene lion
    show mare_scared as m
    "It's a lion. RUN RUN RUN."

    show dave_scared as d at right
    show john_afraid as j at left

    "They panicked!. All three ran to escape the danger."
    j "HELP! HELP! HELP!"
    "One of the lion jumped and stood infront of them and the other one attacked from behind."
    "The fierce lions dragged them to the depths of the cave."
    "They never returned. Who knew this would be the end of their journey and their life."

    return

label outside_the_cave:
    "John decides not to go inside the cave because he sensed danger."
    "Mare and dave argues with john."
    show mare_angry as m at right
    m "It's raining continuously why you choose to stay outside?."
    show john_sad as j at left
    j "It is a trap!"
    show dave_annoyed as d
    d "John, I think you have decided to spoil my birthday."
    j "Dave, don't take me wrong. Please!"
    m "Then tell us the reason behind not going in the cave."
    scene foot_prints
    show john_sad as j at left
    j "See, there are many prints of feet entering the cave, but I see no trace of any returning. It indicates that some kind of fierce animal might have set the trap so that
    he can trick his preys to enter the cave and devour them."
    show dave_normal as d
    d "I think john is right because we are in the middle of the forest so we should be cautious."
    show mare_sad as m at right
    m "Now where should we go??? I'm cold."
    j "We should keep walking until we find a safe place."
    "They got frustrated and kept on walking blaming each other for all the troubles."
    scene tree
    "After an hour of struggle they came across a gigantic tree which provided them fresh fruits and the shed."
    show mare_happy as m at right
    m "Guys! This tree looks wonderful. We can rest here till the weather gets better."
    show john_happy as j at left
    show dave_normal as d
    j "Look, I found so many fruits behind this tree branch."
    d "Thanks John for saving us from that trap."
    "They took rest under the tree for few hours, then they continued their journey."
    "They ended up finding a wonderful place called 'River Blue'."
    jump river


    return

label haunted_house:
    scene do_not_enter
    show dave_happy as d at right
    d "Guys, it says do not enter. What should we do?"
    show mare_happy as m at left
    m "I think we should proceed to this route it maybe placed here to trick us. We are here for fun and we should make
    our trip adventourous."
    show john_happy as j
    j "I disagree, we should change our route. The board is placed for a reason so we should follow the rules."
    show mare_angry as m at left
    m "Come on john! Don't be a spoilsport. We are here to experience something new and this is your first time camping in the woods.
    You should enjoy and do not overthink."
    show dave_normal as d at right
    d "I agree with what mare said. Please john, don't ruin my birthday."
    show john_happy as j
    j "Alright, Let's go."
    scene gate
    show john_confused as j at right
    j "What is this place?"
    show dave_normal as d at left
    d "It suddenly got so dark in here."
    show mare_normal as m
    m "Look, there is a large gate. It seems like it is an old mansion."

    show dave_normal as d at left
    show mare_normal as m
    show john_scared as j at right
    d "Let's go inside this mansion I want to explore what's in there and we can also take rest for sometime."
    m "You are right dave. I will open this gate."
    j "Be careful mare."

    scene open_gate
    "Mare opened the gate, and it squeaked like it was million years old."
    scene haunted_house
    show mare_happy as m at right
    m "Wow, the house looks amazing and beautiful. Thankfully, we have so many lights in here."
    show dave_happy as d at left
    d "I know right. Where is john?"
    show mare_happy as m at right
    m "He might be somewhere around here seating in one corner. I am going upstairs there are so many rooms, I will choose one for
    myself."
    show john_afraid as j
    j "Mare, dave! don't go inside any rooms. I request."
    show mare_angry as m at right
    m "Now what happened john. You are very annoying."
    show john_afraid as j
    j "....Don't go in there!"
    show dave_normal as d at left
    d "....Why not?"
    show john_afraid as j
    j "You won't come out."
    show mare_angry as m at right
    m "What do you mean?"
    show john_afraid as j
    j "Something strange has caught your ears and if you follow it through it will be done with you."
    show mare_angry as m at right
    m "What nonsense."
    d "I don't understand"
    "John steps a bit forward our from the dark, revealing a cut on his shoulder."
    j "I have been marked."
    "Dave tends to John's shoulder with a handkerchief."
    d "Sit down. Sit down, please. How did this happen?"
    j "I entered that room. I heard these sounds, beckoning me--"
    m "Someone, calling you?"
    j "Yes, like a trance. I opened the door and entered. That's when I felt someone or something grab hold of me and
    forced me down to the floor. But I fought it off...all the while I couldn't see a face, I could not see what grabbed
    hold of me. I was fighting off this invisible being. I felt it, the figure of a man's being but could not see him."
    "Dave stands straight and turns his attention to the door."
    m "I think you might have mistaken because this mansion is too old so there might be some kind of wild cat or insects who
    may have scratched or bitten you."

label john_dave:
    scene haunted_house
    show dave_scared as d at left
    show john_afraid as j at right
    d "I and mare are going inside the room to navigate who is there."
    j "Don't go in there! I'm warning you. Wait till morning, when it's bright. You can investigate it then. It isn't safe.
    Please, believe me."
    d "I believe you, I believe you. I want to care for your shoulder."
    scene open_door
    "The door slowly opens behind them. Boyner turns around."
    show dave_annoyed as d
    d "Who's there?! Answer me! Who's there?!"
    d "Where is mare???"
    "The door slams shut."
    "Dave storms ahead toward the door."
    show john_afraid as j at left
    show dave_annoyed as d
    j "Don't go!"
    "Dave tries to open the door but it is locked shut."
    d "Open up! Open up right now, damn you!"
    d "Mare where are you? Please stop playing games."
    "The door slowly opens gently."
    j "Please, please don't go in there. I'm warning you. Please!"
    d "I cannot leave mare alone. I am going inside."
    "John follows dave because he cannot leave either of his friends alone."
    d "Who's in there? Show yourself!."
    show scary_man as s at right
    show john_afraid as j at left
    show dave_annoyed as d
    j "Who's there? Please show your face."

    scene grabbed_their_legs
    "Someone grabbed their legs from behind and dragged them through the forest while looking for more kids to prey out."
    scene dead
    "It is said that a man from this town was on the run from the police and lurked around in the darkness and kidnapped teenage kids.
    John, Dave and Mare were dead and their soul was possessed by that man."


    return
