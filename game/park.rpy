#głowny label parku
label park_main:
    scene bg park
    jump park_choose

#wybory w parku
label park_choose:
    menu:
        "Co chesz zrobić w parku?"

        "Odpocząć na ławce":
            $ add_hour(1)
            $ sleep = sleep + sleep_drain_rate
            $ stress = stress - (10 - stress_gain_rate)
            $ check_stats_surplus()
            "Odpocząłeś chwilę na ławce"
            if lose_flag:
                jump game_over_screen
            jump park_choose

        "Pójść pobiegać":
            $ add_hour(1)
            $ sleep = sleep - 2;
            $ satisfaction = satisfaction + 10 + satisfaction_drain_rate
            $ check_stats_surplus()
            "Pobiegałeś sobie wokół parku"
            if hour >= 20 or hour <= 4:
                $ stress = stress - 10 - stress_gain_rate
                $ check_stats_surplus()
                "Dodatkowo pobieganie w nocy i samotności uspokoiło twoje nerwy"
            if lose_flag:
                jump game_over_screen 
            jump park_choose

        "Pójść gdzieś indziej":
            jump choose
