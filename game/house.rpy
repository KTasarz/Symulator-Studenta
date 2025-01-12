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
            $ event_random = renpy.random.randint(1, 20)
            if event_random <= 4:
                #EVENT - Za długa drzemka...
                "Twoja drzemka była dłuższa niż się spodziewałeś..."
                $ sleep = sleep + (10 + sleep_drain_rate * event_random)
            elif event_random == 5:
                #EVENT - remont sąsiada
                $ sleep = sleep - (10 + sleep_drain_rate * 2)
                play sound "audio/renovation.mp3"
                "Oczywiście kiedy chciałeś się zdrzemnąć to sąsiad ma remont...{p}Jedyne co osiągnąłeś z tej drzemki to ból głowy..."
                $ satisfaction = satisfaction - 2
            else:
                #Brak eventów
                "To byla dobra drzemka"
            $ check_stats_surplus()
            if lose_flag:
                jump game_over_screen
            jump family_house_choose
        
        "Zjeść obiad" if (hour >= 14 and hour <= 17) and eaten_dinner_with_family == False:
            $ add_hour(1)
            $ hunger = hunger + (30 + hunger_drain_rate)
            $ sleep = sleep + 2
            $ stress = stress - 5
            $ check_stats_surplus()
            if lose_flag:
                jump game_over_screen
            "Zjadłeś dobry obiad razem z rodziną"
            $ eaten_dinner_with_family = True
            jump family_house_choose

        "Pouczyć się":
            $ add_hour(2)
            if lose_flag:
                jump game_over_screen
            $ event_random = renpy.random.randint(1, 8)
            if event_random == 1:
                #EVENT - Brak skupienia
                "Probowałeś się pouczyć{w} ale zamiast tego zacząłeś przeglądać memy na telefonie..."
                $ satisfaction = satisfaction + (5 + satisfaction_drain_rate * 2)
                "Przynajmniej miło spędziłeś czas"
            else:
                #Brak eventów
                $ intelligence = intelligence + renpy.random.randint(1, 5)
                $ skills = skills + renpy.random.randint(0, 2)
                "Nauczyłeś się kilku nowych rzeczy"

        "Wyjść z domu":
            jump choose

#wybory w akademiku
label dormitory_choose:
    scene bg dormitory
    menu:
        "Jesteś w swoim pokoju"
        "Co chesz zrobić?"
        "Pójść spać" if hour >= 22 or hour <= 6:
            $ event_random = renpy.random.randint(1, 8)
            $ add_hour(8)
            if event_random == 1:
                #EVENT - impreza
                play sound "audio/muffed party music.mp3" volume 0.3
                "Już miałeś iść spać, kiedy nagle usłyszałeś dźwiek głośnej muzyki w pokoju obok{p}Najwidoczniej twoi znajomi ze studiów postanowili zrobić impreze..."
                menu:
                    "Możesz spróbować zasnąć, bądź zabawić się razem z nimi"
                    "Spróbuj zasnąć":
                        "Niestety współlokatorzy imprezowali do samego rana{p}Przez co ledwo odpoczołeś w nocy..."
                        $ sleep = sleep + (10 + sleep_drain_rate * 8)
                    "Dołącz do imprezy":
                        p "Dobra, pora by do tej imprezy dołączył król disco!"
                        "Szybko się przebrałeś i dołączyłeś do imprezy{p}Pokazałeś im swoje ruchy taneczne!"
                        $ stress = stress - (10 + stress_gain_rate * 8)
                        $ satisfaction = satisfaction + (40 + satisfaction_drain_rate * 8)
                        "Impreza trwała do samego rana...{p}Czujesz się po niej niesamowicie zmęczony...{p}Ale uważasz że było warto"
                stop sound
            else:
                $ sleep = sleep + (80 + sleep_drain_rate * 8)
                $ stress = stress - 10
                "Wyspałeś się"
            $ check_stats_surplus()
            $ check_if_lose()
            if lose_flag:
                jump game_over_screen
            jump dormitory_choose
        
        "Pójść się zdrzemnąć" if hour > 6 and hour < 22:
            $ add_hour(2)
            $ sleep = sleep + (10 + sleep_drain_rate * 2)
            $ event_random = renpy.random.randint(1, 20)
            if event_random <= 4:
                #EVENT - Za długa drzemka...
                "Twoja drzemka była dłuższa niż się spodziewałeś..."
                $ sleep = sleep + (10 + sleep_drain_rate * event_random)
            else:
                #Brak eventów
                "To byla dobra drzemka"
            $ check_stats_surplus()
            if lose_flag:
                jump game_over_screen
            "To byla dobra drzemka"
            jump dormitory_choose

        "Pouczyć się":
            $ add_hour(2)
            if lose_flag:
                jump game_over_screen
            $ event_random = renpy.random.randint(1, 6)
            if event_random == 1:
                #EVENT - Brak skupienia
                "Probowałeś się pouczyć{w} ale zamiast tego zacząłeś przeglądać memy na telefonie..."
                $ satisfaction = satisfaction + (5 + satisfaction_drain_rate * 2)
                "Przynajmniej miło spędziłeś czas"
            else:
                #Brak eventów
                $ intelligence = intelligence + renpy.random.randint(1, 5)
                $ skills = skills + renpy.random.randint(0, 2)
                "Nauczyłeś się kilku nowych rzeczy"

        "Wyjść z domu":
            jump choose
