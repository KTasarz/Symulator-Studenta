#Główny label domu, przenosi do wyborów zależnie od domu w którym mieszka gracz
label house_main:

    if (family_house_flag):
        jump family_house_choose
    elif (dormitory_flag):
        jump dormitory_choose

#Wybory w domu rodzinnym
label family_house_choose:
    scene bg house
    menu:
        "Jesteś w swoim domu rodzinnym"
        "Co chesz zrobić?"

        "Pójść spać" if hour >= 22 or hour <= 6:
            $ add_hour(8)
            $ sleep = sleep + (80 + sleep_drain_rate * 8)
            $ stress = stress - 10
            $ check_stats_surplus()
            if lose_flag:
                jump game_over_screen
            "Wyspałeś się"
            jump family_house_choose
        
        "Pójść się zdrzemnąć" if hour > 6 and hour < 22:
            $ add_hour(2)
            $ sleep = sleep + (10 + sleep_drain_rate * 2)
            $ check_stats_surplus()
            if lose_flag:
                jump game_over_screen
            "To byla dobra drzemka"
            jump family_house_choose
        
        "Zjeść obiad" if hour >= 14 and hour <= 17:
            $ add_hour(1)
            $ hunger = hunger + (30 + hunger_drain_rate)
            $ sleep = sleep + 2
            $ stress = stress - 5
            $ check_stats_surplus()
            if lose_flag:
                jump game_over_screen
            "Zjadłeś dobry obiad razem z rodziną"
            jump family_house_choose

        "Wyjść z domu":
            jump choose

#wybory w akademiku
label dormitory_choose:
    "Jesteś w swoim pokoju"
    jump choose
