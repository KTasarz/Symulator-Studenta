﻿label job_place_main:
    show screen stats_screen
    show screen inventory_button_screen
    scene bg job
    "Wchodzisz do biura pracy."
    jump job_place_choose

label job_place_choose:
    menu:
        "Co chcesz zrobić?"
        "Pracuj na pełną zmianę":
            $ add_hour(8)
            $ bonus = renpy.random.randint(25, 75)
            $ money += 200 + bonus
            $ stress += 30
            $ check_stats_surplus()
            "Zarobiłeś [200 + bonus] zł."
            if lose_flag:
                jump game_over_screen
            jump job_place_choose

        "Pracuj na pół zmiany":
            $ add_hour(4)
            $ bonus = renpy.random.randint(8, 30)
            $ money += 100 + bonus
            $ stress += 15
            $ check_stats_surplus()
            "Zarobiłeś [100 + bonus] zł."
            if lose_flag:
                jump game_over_screen
            jump job_place_choose

        "Wyjdź":
            jump choose