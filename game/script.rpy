# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define p = Character("Player", color="#0069ff") #Kolor Merito :)

init python:
    day = 1                         #dzien - ma śledzić aktualny dzień
    hour = 8                        #godzina - przechodzenie do innych lokacji/interakcje powoduje postęp czasu
    hunger = 100                    #głod - jeśli głód spadnie do zero - game over
    hunger_drain_rate = 4           #szybkość spadku głodu
    sleep = 100                     #zmęczenie - jeśli zmęczenie spadnie do zera - game over
    sleep_drain_rate = 5            #szybkość spadku zmęczenia
    satisfaction = 100              #zadowolenie - jeśli spadnie do zera nie można wykonywać niektórych czynności
    satisfaction_drain_rate = 3     #szybkość spadku zadowolenia
    intelligence = 0                #inteligencja - wpływa na zaliczenia testu
    skills = 0                      #umiejętoność praktyczne - wpływa na zaliczenia testu
    lose_flag = False               #flaga pilnująca czy gracz żyje

    #Metoda do zmiany godziny, poprzez podanie ile czasu upłyneło, wpływa na statytyki
    def add_hour(number_of_hours_passed):
        global hour
        global hunger
        global sleep
        global satisfaction
        global day
        hour += number_of_hours_passed
        hunger -= (number_of_hours_passed * hunger_drain_rate)
        sleep -= (number_of_hours_passed * sleep_drain_rate)
        satisfaction -= (number_of_hours_passed * satisfaction_drain_rate)
        if hour >= 24:
            day += 1
            hour -= 24
        check_if_lose()
    
    #Metoda sprawdzająca czy statystyki są 0 lub mniejsze, jeśli tak to przenosi do game over screen
    def check_if_lose():
        global lose_flag
        if hunger <= 0 or sleep <= 0 or satisfaction <= 0:
            lose_flag = True

#Wyświetla statystyki na ekranie
screen stats_screen():
    frame:
        xalign 0.0 ypos 0
        vbox:
            text "Dzień [day]"
            text "Godzina [hour]"
            #TODO zmienić wyświetlane wartości na paski (zwyjątkiem intela i umiejętności)
            text "Głód [hunger]"
            text "Zmęczenie [sleep]"
            text "Zadowolenie [satisfaction]"
            text "Inteligencja [intelligence]"
            text "umiejętoność praktyczne [skills]"

#Znalazłem w dokumentacji Renpy
#TODO będzie trzeba zmienić położenie guzików i dodanie tła
screen main_menu():

    # This ensures that any other menu screen is replaced.
    tag menu

    # The background of the main menu.
    window:
        style "mm_root"

    # The main menu buttons.
    frame:
        style_prefix "mm"
        xalign .98
        yalign .98

        has vbox

        textbutton _("Start Game") action Start()
        textbutton _("Load Game") action ShowMenu("load")
        textbutton _("Preferences") action ShowMenu("preferences")
        textbutton _("Help") action Help()
        textbutton _("Quit") action Quit(confirm=False)

style mm_button:
    size_group "mm"

# The game starts here.

label start:
    show screen stats_screen()

    #TODO wywalić to jak dodamy własne tła/postacie
    scene bg room

    show eileen happy

    jump choose


    # This ends the game.

    return

label choose:
    #Tymczasowe menu pozwalające przechodzić na obiekty na mapie
    #TODO Zmienić to na mape z obiektami na kliknięcie
    menu:
        "Gdzie chcesz iść?"

        "Dom":
            jump house_main

        "Uczelnia":
            jump school_main

        "Reustaracja":
            jump restaurant_main

        "Sklep":
            jump shop_main

        "Park":
            jump park_main

        "Biuro Pracy":
            jump job_place_main

        "TESTZONE":
            jump test_zone                

label game_over_screen:
    "Przegrałeś"
    return

label test_zone:
    $ add_hour(2)
    if lose_flag:
        jump game_over_screen

    jump choose
    