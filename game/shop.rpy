screen shoping_screen():
    frame:
        xalign 0.5 yalign 0.4

        has vbox

        text "Kliknij tu aby kupić co chcesz"
        text "----------------------------------"
        textbutton "Energetyk 5 zł":
            action If(money >= 5, [SetVariable("money", money - 5), SetVariable("energy_drink_amount", energy_drink_amount + 1)])
            activate_sound "audio/Cha Ching.mp3"
        textbutton "Baton 3 zł":
            action If(money >= 3, [SetVariable("money", money - 3), SetVariable("bar_amount", bar_amount + 1)])
            activate_sound "audio/Cha Ching.mp3"
        textbutton "Piwo 4 zł":
            action If(money >= 4, [SetVariable("money", money - 4), SetVariable("beer_amount", beer_amount + 1)])
            activate_sound "audio/Cha Ching.mp3"
        textbutton "Piwo Mocny Full 10 zł":
            action If(money >= 10, [SetVariable("money", money - 10), SetVariable("big_beer_amount", big_beer_amount + 1)])
            activate_sound "audio/Cha Ching.mp3"
        text "----------------------------------"

label shop_main:
    show screen stats_screen
    show screen inventory_button_screen
    scene bg shop
    "Wchodzisz do sklepu."
    
    jump shop_choose

label shop_choose:
    menu:
        "Co checsz teraz zrobić w sklepie?"

        "Zrobić zakupy":
            show screen shoping_screen
            "Kliknij aby wyjść"
            hide screen shoping_screen
            jump shop_choose
        "Wyjść":
            jump choose