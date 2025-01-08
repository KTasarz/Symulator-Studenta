# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define p = Character("Player", color="#0069ff") #Kolor Merito :)

init python:
    day = 1                 #dzien - ma śledzić aktualny dzień
    hour = 8                #godzina - przechodzenie do innych lokacji/interakcje powoduje postęp czasu
    hunger = 100            #głod - jeśli głód spadnie do zero - game over
    sleep = 100             #zmęczenie - jeśli zmęczenie spadnie do zera - game over
    satisfaction = 100      #zadowolenie - jeśli spadnie do zera nie można wykonywać niektórych czynności
    intelligence = 0        #inteligencja - wpływa na zaliczenia testu
    skills = 0              #umiejętoność praktyczne - wpływa na zaliczenia testu


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

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

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
    