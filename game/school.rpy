label school_main:
    show screen stats_screen
    show screen inventory_button_screen
    scene bg hallway
    "Wchodzisz na uczelnie."

    jump school_choose

label school_choose:
    menu:
        "Stoisz na środku uczelnianego korytarza. Jaki jest twój plan?"

        "Idź na wykłady":
            $ add_hour(3)
            "Spędziłeś czas na słuchaniu wykładu."
            $ intelligence += 3
            $ check_stats_surplus()
            jump school_choose

        "Idź na warsztaty":
            $ add_hour(3)
            $ skills += 3
            $ check_stats_surplus()
            jump school_choose

        "Podejdź do egzaminu":
            if intelligence >= 20 and skills >= 15:
                "Zdałeś egzamin. Gratulacje!"
            else:
                "Nie jesteś jeszcze gotowy..."
            jump school_choose

        "Wyjść":
            jump choose