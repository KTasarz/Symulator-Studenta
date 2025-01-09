<<<<<<< Updated upstream
﻿screen shopping_screen:
    frame:
        xalign 0.95 yalign 0.05
        
        has vbox
        textbutton "Energetyk 5 zł":
            action If(money >= 5, [SetVariable("money", money - 5), SetVariable("energy_drink_amount", energy_drink_amount + 1)])

        textbutton "Baton 3 zł":
            action If(money >= 3, [SetVariable("money", money - 3), SetVariable("bar_amount", bar_amount + 1)])
        
        textbutton "Piwo 6 zł":
            action If(money >= 6, [SetVariable("money", money - 6), SetVariable("beer_amount", beer_amount + 1)])


=======
﻿screen shoping_screen():
    frame:
        xalign 1.0 yalign 0.0

        has vbox

        text "Kliknij tu aby kupić co chcesz"
        text "----------------------------------"
        textbutton "Energetyk 5 zł":
            action If(money >= 5, [SetVariable("money", money - 5), SetVariable("energy_drink_amount", energy_drink_amount + 1)])
            activate_sound "audio/Cha Ching.mp3"
        textbutton "Baton 3 zł":
            action If(money >= 3, [SetVariable("money", money - 3), SetVariable("bar_amount", bar_amount + 1)])
            activate_sound "audio/Cha Ching.mp3"
        textbutton "Piwo 6 zł":
            action If(money >= 6, [SetVariable("money", money - 6), SetVariable("beer_amount", beer_amount + 1)])
            activate_sound "audio/Cha Ching.mp3"
        text "----------------------------------"
>>>>>>> Stashed changes

label shop_main:

    scene bg shop
    "Jesteś w sklepie"
    
    jump shop_choose

<<<<<<< Updated upstream
    jump shop_choose

label shop_choose:
    menu:
        "Co chcesz zrobić?"
            
        "Zrobić zakupy":
            show screen shopping_screen
            "Kliknij aby wyjść"
            hide screen shopping_screen
        "Wyjść":
            jump choose    
=======
label shop_choose:
    menu:
        "Co chesz teraz zrobić w sklepie?"

        "Zrobić zakupy":
            show screen shoping_screen
            "Kliknij aby wyjść"
            hide screen shoping_screen
            jump shop_choose
        "Wyjść":
            jump choose
>>>>>>> Stashed changes
