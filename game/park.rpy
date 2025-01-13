#głowny label parku
label park_main:
    show screen stats_screen
    show screen inventory_button_screen
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
            $ event_random = renpy.random.randint(1, 10)
            if event_random == 1:
                #EVENT - Zaspanie na ławce
                ".{w}.{w}.{w}.{w}."
                $ add_hour(3)
                $ sleep = sleep + 3 + sleep_drain_rate * 3
                "Jakimś cudem zasnąłeś na ławce{w} i teraz cie bolą plecy od spania na ławce..."
            elif event_random == 2:
                #EVENT - Zaspanie na ławce i stracenie paru monet
                ".{w}.{w}.{w}.{w}."
                python:
                    add_hour(2)
                    sleep = sleep + 2 + sleep_drain_rate * 2
                    money = money - renpy.random.randint(1, 25)
                "Jakimś cudem zasnąłeś na ławce{w} i twój portfel wydaje się lżejszy..."
            elif event_random == 3:
                #EVENT - Znalezienie monet na ławce
                "Znalazłeś pare monet na ławce!"
                $ money = money + renpy.random.randint(1, 5)
                "Odpocząłeś chwilę na ławce"
            elif event_random == 4:
                #EVENT - dziki!
                play sound "audio/Boar chrum.mp3"
                "Jak tylko usiadłeś na ławce zacząłeś slyszeć chrumczenie z krzaków!"
                "To dziki!{p}Chyba lepiej stąd znikać!"
                play sound "audio/Boar chrum.mp3"
                "W sumie to nigdy nie widziałeś, żeby dziki zrobiły jakąś krzywde ludziom.{p}Może jednak warto zostać i spróbować się z nimi zaprzyjaźnić?"
                $ event_random = renpy.random.randint(1, 2)
                menu:
                    "Lepiej nie ryzykować":
                        $ sleep = sleep - sleep_drain_rate
                        $ stress = stress + (5 + stress_gain_rate)
                        jump choose
                    "Spróbuj je pogłaskać":
                        p "W sumie co złego się może stać?"
                        play sound "audio/Boar chrum.mp3"
                        p "No chodź bliżej, nic ci nie zrobie"
                        if event_random == 1:
                            "Dziki dały się pogłaskać"
                            play sound "audio/Boar chrum.mp3"
                            p "No kto jest dobrym dzikiem?{p}tak ty jesteś~"
                            play sound "audio/Boar chrum.mp3"
                            "Nawet nie wiesz jak szybko minął czas kiedy głaskałeś dziki.{p}Po intesywnej terapii głaskania, dziki odeszły zostawiając cie samego w parku"
                            $ satisfaction = satisfaction + 15
                            $ stress = stress - 10
                            $ score_boar += 1
                        else:
                            play sound "audio/Boar chrum.mp3"
                            "Dziki nie dały się pogłaskać."
                            "Ostatnie co pamiętasz to szarżujący w twoją stronę dzik."
                            $ add_hour(renpy.random.randint(2, 4))
                            $ stress = stress + 10
                            "Wstajesz z ziemi lekko obity, ale na szczęście nic poważnego ci się nie stało."
            else:
                #Bez Eventów
                "Odpocząłeś chwilę na ławce."
            $ check_stats_surplus()
            if lose_flag:
                jump game_over_screen
            jump park_choose

        "Pobiegać":
            $ add_hour(1)
            $ event_random = renpy.random.randint(1, 10)
            if event_random == 1:
                #EVENT - przewrócenie się podczas biegu
                "Podczas biegania przewróciłeś się.{p}Na szczeście nic poważnego się nie stało.{p}Ale ból nie pozwolił ci kontynuować biegania..."
                $ sleep = sleep - 2;
            elif event_random == 2:
                #EVENT - Bezdomny zaczepia cie/Dziwny sprzedawca proponuje ci swoje towary
                if (hour >= 20 or hour <= 4) and meet_mystery_trader_at_Park == False:
                    #Wersja nocna
                    "Już miałeś zaczynać swój bieg, kiedy nagle zaczepiła cię tajemnicza osoba w czarnym płaszczu."
                    m "Hej...{w} chcesz może...{w} kupić...{w} faworka?"
                    "Spojrzałeś na niego jak na wariata."
                    m "Jak nie chcesz...{w} faworka...{w} mogę ci udostępić...{w} inne 'Wyjątkowe' Towary..."
                    $ meet_mystery_trader_at_Park = True
                    menu:
                        "Co chcesz kupić?"
                        
                        "Faworka(5 zł)"if money >= 5:
                            $ money = money - 5
                            p "Wezmę tego faworka."
                            "Sprzedawca bez słowa podał ci...{w} zwykłego faworka?"
                            "Bierzesz faworka w dłoń i na niego spoglądasz.{p}Sądziłeś że faworek to jakiś słowo kod, i chce ci on sprzedać coś nielegalnego."
                            "Kiedy podnosisz głowe by pożegnać się ze sprzedawcą, go już nie ma, zupełnie jakby się rozpłynął."
                            "Postanawiasz zjeść tego faworka.{p}Smakuje jak...{w} zwykły faworek?!"
                            $ hunger = hunger + 5
                        "Książka \"Jak używać 100%% mózgu\"(100zł)" if money >= 100:
                            $ money = money - 100
                            p "Wezmę tą książkę!"
                            "Sprzedawca bez słowa podał ci książkę."
                            "Spoglądasz na tą cegłe i zastanawiasz czy nie popełniłeś błędu."
                            "Kiedy podnosisz głowe by pożegnać się ze sprzedawcą, go już nie ma, zupełnie jakby się rozpłynął."
                            "Postanawiasz przeczytać tą cegłe.{p}Okazuje się bardzo dobrze napisana!{p}Bardzo szybką ją przeczytałeś i czujesz się mądrzejszy!"
                            $ intelligence = intelligence + 50
                        "Książka \"Użycie swojej w wiedzy w praktyce! Wydanie dla osób z niskim IQ!\"(100zł)" if money >= 100:
                            $ money = money - 100
                            p "Wezmę tą książkę!"
                            "Sprzedawca bez słowa podał ci książkę."
                            "Spoglądasz na tą cegłe i zastanawiasz czy nie popełniłeś błędu."
                            "Kiedy podnosisz głowe by pożegnać się z sprzedawcą, go już nie ma, zupełnie jakby się rozpłynął."
                            "Postanawiasz przeczytać tą cegłe.{p}Okazuje się, że wiekszość stron to obrazki z przykładami!{p}Bardzo szybką ją przeczytałeś i czujesz jak masz więcej umiętejntności!"
                            $ skills = skills + 50
                        "Złota tabletka (500zł)" if money >= 500:
                            $ money = money - 500
                            p "Wezmę tą tabletkę!"
                            m "Najlepiej weź tą tabletkę od razu...{w} bo inaczej będzie bezużyteczna."
                            "Korzystając z rady tejemniczego jegomości, bierzesz tabletkę."
                            "Po chwili twój zwrok zaczął wariować i czujesz dziwne uczucie w brzuchu.{p}Ten stan nie trwał długo i teraz czujesz się..."
                            $ event_random = renpy.random.randint(1, 5)
                            if event_random == 1:
                                "Jak nowy człowiek!"
                                $ hunger = 100
                                $ sleep = 100
                                $ satisfaction = 100
                                $ stress = 0
                            elif event_random == 2:
                                "Mądrzejszy!"
                                $ intelligence = intelligence + 50
                                $ skills = skills + 50
                            elif event_random == 3:
                                "Jakbyś mógł jeść mniej!"
                                $ hunger_drain_rate = hunger_drain_rate - 1
                            elif event_random == 4:
                                "Jakbyś się mniej męczył!"
                                $ sleep_drain_rate = sleep_drain_rate - 1
                            elif event_random == 5:
                                "Jabyś był szcześliwszy!"
                                $ satisfaction_drain_rate = satisfaction_drain_rate - 1
                            $ score_pill += 1
                        "Nic":
                            p "Nie dzięki, nic nie potrzebuje."
                            m "Twoja strata."
                            "Tajemniczy jegomość odwrócił się od ciebie i zaczął iść w swoją strone.{p}A ty wróciłeś do pierwotnego planu."
                            "Jednak myśl że po parku chodzi tajemniczy typ nie dawała ci spokoju..."
                            $ sleep = sleep - 2;
                            $ satisfaction = satisfaction + 10 + satisfaction_drain_rate
                            "Pobiegałeś sobie wokół parku{w}, Czując czyjś wzrok..."
                else:
                    #Wersja dzienna
                    "Podczas twojego biegu zaczepił cię bezdomny."
                    h "Panie kierowniku, poratuj Pan mnie złotóweczką!"
                    menu:
                        "Wiesz, że jeżeli nie dasz mu tej złotówki to cie nie zostawi..."
                        
                        "Daj mu złotówke" if money > 0:
                            p "Proszę to dla ciebie."
                            $ money = money - 1;
                            "Dajesz mu złotówke."
                            h "Dzięki Ci kierowniku!"
                            "Tak szybko jak się pojawił bezdommy, tak zniknął.{w} Kontynuowałeś swoje bieganie bez większych problemów."
                            $ sleep = sleep - 2;
                            $ satisfaction = satisfaction + 10 + satisfaction_drain_rate
                        
                        "Spróbuj go spławić":
                            p "Przepraszam, nie mam przy sobie portfela."
                            $ event_random = renpy.random.randint(1, 4)
                            if event_random == 1:
                                #Bezdommy ci wierzy
                                h "No trudno... W takim razie miłego biegania kierowniku!"
                                "Bezdommy z smutną miną odwrócił się od ciebie i poszedł w swoją strone."
                                $ sleep = sleep - 2;
                                $ satisfaction = satisfaction + 10 + satisfaction_drain_rate
                            else:
                                #Bezdomny nie uwierzył tobie
                                h "No panie kierowniku... Nie bądź taki, proszę jedynie o złotóweczkę."
                                "Próbowałeś go jeszcze pare razy go spławić, ale dał sobie spokój dopiero po godzinie...{p}Przez ten cały czas w ogóle nie pobiegałeś..."
                                $ stress = stress + 5               
            else:
                #Bez Eventów
                $ sleep = sleep - 2;
                $ satisfaction = satisfaction + 10 + satisfaction_drain_rate
                "Pobiegałeś wokół parku."
                if hour >= 20 or hour <= 4:
                    $ stress = stress - 10 - stress_gain_rate
                    "Dodatkowo pobieganie w nocy i samotności uspokoiło twoje nerwy."
            $ check_stats_surplus()
            if lose_flag:
                jump game_over_screen 
            jump park_choose

        "Pójść gdzieś indziej":
            jump choose