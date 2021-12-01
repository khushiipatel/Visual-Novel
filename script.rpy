label start:
    scene infinity
    "Welcome to Endless Possibilities!"
    menu:
        "please choose which game you would like to play"

        "Nation Ruler":
            jump NationRuler
        "Khushi":
            jump Khushi
        "Zainab":
            jump Zainab




#----------------------------------------------------------------
#﻿Conrad
define c = Character(_("King Con"), color="#c8ffc8")
define k = Character(_("Knight"), color="#c8c8ff")

label NationRuler:
    scene town

    show knight as k at left:
        yalign 0.6


    k "Welcome to The Nation of Conradia, this is your nation King Con."

    k "I am one of your many knights, and I am here to assist you."

    k "You will be charged with leading this nation to prosperity. If you make
    any mistakes, this whole nation and everyone in it could perish.
    No pressure though!"

    jump palace



label palace:

    scene palace

    show king con normal as c

    "Welcome to your palace!"
    "You have a lot of decisions to make.
    It seems like one of your knights is headed towards your right now."

    show king con normal as c at left
    show knight as k at right

    k "King Con! I have some rather urgent news."
    c "What is it?"
    k "Remember last week when you ordered us to raid a village,
    but to only steal their wine so you could throw a big party?"
    c "I vaguely remember that. Why do you ask?"
    k "Well the village wasn't so happy about that. Their leader, who goes by
    the name of Sir Constantine Hicklebottom, has requested to have a civil meeting with you."

    menu:

        "How do you chose to proceed?"

        "Agree to meet with Constantine Hicklebottom":
            jump meeting

        "Raid their village again, and steal more wine for another party":
            jump war

label war:
    hide palace
    hide king con normal
    hide knight

    "All 500 of your troops have been sent to the nearby village to steal wine."
    "After 3 days you are given an update."

    scene palace
    show king con normal at left
    show knight at right

    k "King Con, I have some good news and some bad news, sir."

    c "What's the good news?"

    k "The good news is we stole all of their wine."

    c "And the bad news?"

    k "The troops drank all of the wine and while they were intoxicated, they got
    attacked by a pack of wolves, and now we have no troops."

    show king con sad at left

    k "There are no more able-bodied people in the nation to train. How should we
    proceed?"

    menu:

        "Leave Conradia defenseless.":
            jump defenseless

        "Train child soldiers to defend Conradia.":
            jump childSoldier




label defenseless:
    "good choice"
label childSoldier:
    "good choice"



label meeting:
    "good choice"
















#--------------------------------------------------------------
#Khushi

label Khushi:
    "this is khushi's game please change label name to your game name"
















#--------------------------------------------------------------
#Zainab

label Zainab:
    "this is Zainab's game please change label name to your game name"
