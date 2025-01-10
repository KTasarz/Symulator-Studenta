# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# The game starts here.

label job_place_main:

    scene bg job
    "Jesteś w biurze pracy"

    # This ends the game.

    jump job_place_choose

label job_place_choose:
    menu:
        "Co chcesz zrobić?"
        "Pracuj na pełną zmianę":
            $ add_hour(8)
            $ bonus = renpy.random.randint(20, 50)
            $ money += 100 + bonus
            $ stress += 30
            $ check_stats_surplus()
            "Zarobiłeś [100 + bonus] zł."
            if lose_flag:
                jump game_over_screen
            jump job_place_choose

        "Pracuj na pół zmiany":
            $ add_hour(4)
            $ bonus = renpy.random.randint(5, 20)
            $ money += 50 + bonus
            $ stress += 30
            $ check_stats_surplus()
            "Zarobiłeś [50 + bonus] zł."
            if lose_flag:
                jump game_over_screen
            jump job_place_choose

        "Wyjdź":
            jump choose