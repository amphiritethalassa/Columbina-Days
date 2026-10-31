image columbina_idle = "columbina.png"
image columbina_hover = "columbina_hover.png"


label start:

    scene bg room

    call screen columbina_screen

    return


screen columbina_screen():

    imagebutton:
        idle "columbina_idle"
        hover "columbina_hover"
        focus_mask True
        xalign 0.5
        yalign 0.5
        action Call("columbina_dialogue")


label columbina_dialogue:

    $ dialogue = renpy.random.choice([
        "Oh? Did you need something?",
        "It's a lovely day, isn't it?",
        "You're back again. How sweet.",
        "Have you been thinking about me?",
        "Hehe. You're quite interesting.",
        "Is there something on your mind?",
        "You're rather persistent, aren't you?",
        "I wonder what you're thinking about."
    ])

    return
