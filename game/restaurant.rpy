screen restaurant_screen():
    $ check_stats_surplus()
    frame:
        xalign 1.0 yalign 0.0

        has vbox
        
        text "Kliknij tu aby kupić co chcesz"
        text "----------------------------------"
        textbutton "Pizza 30 zł (Głód 40)":
            action If(money >= 30 and hunger < 100, [SetVariable("money", money - 30), SetVariable("hunger", hunger + 40)])
            activate_sound "audio/Eating-sound.mp3"
        textbutton "Kebab 25 zł (Głód 30)":
            action If(money >= 25 and hunger < 100, [SetVariable("money", money - 25), SetVariable("hunger", hunger + 30)])
            activate_sound "audio/Eating-sound.mp3"
        textbutton "Cola 7 zł (Głód 10)":
            action If(money >= 7 and hunger < 100, [SetVariable("money", money - 7), SetVariable("hunger", hunger + 10)])
            activate_sound "audio/Drinking.mp3"
        text "----------------------------------"    

label restaurant_main:
    show screen stats_screen
    show screen inventory_button_screen
    scene bg restaurant
    "Wchodzisz do reustaracji."
    jump restaurant_choose

label restaurant_choose:
    menu:
        "Siadasz do stolika."

        "Zamów coś":
            show screen restaurant_screen
            "Kliknij aby wyjść"
            hide screen restaurant_screen
            jump restaurant_choose
        "Wyjdź":
            jump choose