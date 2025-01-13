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
            jump school_choose

        "Idź na warsztaty":
            jump school_choose

        "Wyjść":
            jump choose