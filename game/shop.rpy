screen shopping_screen:
    frame:
        xalign 0.95 yalign 0.05
        
        has vbox
        textbutton "Energetyk 5 zł":
            action If(money >= 5, [SetVariable("money", money - 5), SetVariable("energy_drink_amount", energy_drink_amount + 1)])

        textbutton "Baton 3 zł":
            action If(money >= 3, [SetVariable("money", money - 3), SetVariable("bar_amount", bar_amount + 1)])
        
        textbutton "Piwo 6 zł":
            action If(money >= 6, [SetVariable("money", money - 6), SetVariable("beer_amount", beer_amount + 1)])



label shop_main:

    "Jesteś w sklepie"

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
