define p = Character("[name]", color="#0069ff") #Kolor Merito :)
define h = Character("Bezdomnny", color= "#4f3e20")
define m = Character("???", color= "#CECECE")

init python:
    name = "Player"                     #nazwa - imie gracza
    day = 1                             #dzien - ma śledzić aktualny dzień
    hour = 8                            #godzina - przechodzenie do innych lokacji/interakcje powoduje postęp czasu
    hunger = 100                        #głod - jeśli głód spadnie do zero - game over
    hunger_drain_rate = 4               #szybkość spadku głodu
    sleep = 100                         #zmęczenie - jeśli zmęczenie spadnie do zera - game over
    sleep_drain_rate = 5                #szybkość spadku zmęczenia
    satisfaction = 100                  #zadowolenie - jeśli spadnie do zera nie można wykonywać niektórych czynności
    satisfaction_drain_rate = 3         #szybkość spadku zadowolenia
    stress = 0                          #stres - jeśli urośnie do 100 to gracz przegrywa
    stress_gain_rate = 1                #szybkość rosniecia stresu
    intelligence = 0                    #inteligencja - wpływa na zaliczenia testu
    skills = 0                          #umiejętoność praktyczne - wpływa na zaliczenia testu
    money = 10                          #ilość pięniedzy w posiadaniu bohatera
    energy_drink_amount = 0             #ilość napoju energetycznego
    bar_amount = 0                      #ilość batoników
    beer_amount = 0                     #ilość piwa
    lose_flag = False                   #flaga pilnująca czy gracz żyje
    lose_tuition_flag = False           #flaga która określa że gracz przegrał przez brak zapłaconych czesnych
    family_house_flag = False           #flaga która określa czy gracz mieszka w domu rodzinnym
    dormitory_flag = False              #flaga która określa czy grasz mieszka w akademiku
    eaten_dinner_with_family = False    #flaga która określa czy grasz zjadł obiad z rodziną
    meet_mystery_trader_at_Park = False #flaga która określa czy grasz spotkał tajemniczego handlarza w parku

    #Metoda do zmiany godziny, poprzez podanie ile czasu upłyneło, wpływa na statytyki
    def add_hour(number_of_hours_passed):
        global hour
        global hunger
        global sleep
        global satisfaction
        global stress
        global day
        hour += number_of_hours_passed
        hunger -= (number_of_hours_passed * hunger_drain_rate)
        sleep -= (number_of_hours_passed * sleep_drain_rate)
        satisfaction -= (number_of_hours_passed * satisfaction_drain_rate)
        stress += (number_of_hours_passed * stress_gain_rate)
        if hour >= 24:
            day += 1
            hour -= 24
            flags_reset()
        check_if_lose()
        if day % 30 == 0:
            renpy.call("tuition")


    def flags_reset():
        global eaten_dinner_with_family
        eaten_dinner_with_family = False
        global meet_mystery_trader_at_Park
        meet_mystery_trader_at_Park = False
    
    #Metoda sprawdzająca czy statystyki są 0 lub mniejsze, jeśli tak to przenosi do game over screen
    def check_if_lose():
        global lose_flag
        if hunger <= 0 or sleep <= 0 or satisfaction <= 0:
            lose_flag = True
        else:
            lose_flag = False

    #Metoda sprawdzająca czy statystyki wyszły powyżej maksimum
    def check_stats_surplus():
        global hunger
        global sleep
        global satisfaction
        global stress
        global money
        if hunger > 100:
            hunger = 100
        if sleep > 100:
            sleep = 100
        if satisfaction > 100:
            satisfaction = 100
        if stress < 0:
            stress = 0
        if money < 0:
            money = 0

#Wyświetla pare statystyk na ekranie
screen stats_screen:
    frame:
        xalign 0.0 ypos 60
        vbox:

            text "Dzień: [day]"
            text "Godzina: [hour]"
            text "Pieniądze: [money] zł"

#Wyświetla statystyki na ekranie
screen stats_expanded_screen:
    frame:
        xalign 0.0 ypos 60
        xsize 500
        vbox:

            text "Dzień: [day]"
            text "Godzina: [hour]"
            text "Pieniądze: [money] zł"
            #TODO zmienić wyświetlane wartości na paski (zwyjątkiem intela i umiejętności)
            text "Głód:"
            bar:
                value StaticValue(hunger, 100)               
            text "Energia:"
            bar:
                value StaticValue(sleep, 100)
            text "Zadowolenie:"
            bar:
                value StaticValue(satisfaction, 100)
            text "Stres:"
            bar:
                value StaticValue(stress, 100)
            text "Inteligencja: [intelligence]"
            text "Umiejętność praktyczne: [skills]"

#Wyświetla menu z użyciem przedmiotów
screen inventory_screen:
    frame:
        xalign 0.0 yalign 0.655
        xsize 500
        has vbox

        text "Twoje aktualne przedmioty:"
        textbutton "Użyj: Energetyk([energy_drink_amount])":
            action If(energy_drink_amount >= 1 and sleep <= 88, [SetVariable("sleep", sleep + 12), SetVariable("energy_drink_amount", energy_drink_amount - 1)])
            activate_sound "audio/Drinking.mp3"
        textbutton "Użyj: Batonik([bar_amount])":
            action If(bar_amount >= 1 and hunger <= 96, [SetVariable("hunger", hunger + 4), SetVariable("bar_amount", bar_amount - 1)])
            activate_sound "audio/Eating-sound.mp3"
        textbutton "Użyj: Piwo([beer_amount])":
            action If(beer_amount >= 1 and satisfaction <= 94, [SetVariable("satisfaction", satisfaction + 6), SetVariable("beer_amount", beer_amount - 1)])
            activate_sound "audio/Drinking.mp3"

#Guzik do rozszerzania ekwipunku
screen inventory_button_screen:
    frame:
        xalign 0.0 yalign 0.0
        has vbox

        textbutton "Ekwipunek":
            action [ToggleScreen("stats_screen"),ToggleScreen("stats_expanded_screen"),ToggleScreen("inventory_screen")]

# The game starts here.

label start:
    #Prolog
    #Możemy dodać bardziej kwieciste dialogi
    scene bg void
    "Leżysz sobie w swoim łóżku,{w} myśląc sobie o nowym scenariuszu życia, który otwiera się przed tobą..."
    "Od jutra jesteś studentem, a co za tym idzie, nowe obowiązki i cele..."
    menu:
        "Wybierając studia postanowiłeś że..."
        "Będziesz dalej mieszkać z rodzicami":
            $ family_house_flag = True
            "W końcu uczelnia nie jest daleko od twojego domu, to możesz dalej mieszkać na garnuszku rodziców..."
        "Zamieszkasz w akademiku":
            $ dormitory_flag = True
            "Postanowiłeś się w końcu usamodzielnić od rodziców i poznać smak samodzielnego życia..."
    "Pora w końcu zasnąć, żeby jutro świat poznał nowego studenta,{w} nowego ciebie,{w} nowego..."
    $ name = renpy.input("(Podaj swoje imie)")
    $ name = name.strip()

    p "Jestem gotów na jutro!"
    "Zamknąłeś oczy i pochłoneły cię objęcia snu..."

    if family_house_flag:
        scene bg house
    elif dormitory_flag:
        scene bg dormitory
    "Rano, wstałeś z łóżka, umyłeś zęby i zjadłeś śniadanie{p}Teraz jesteś gotowy by rozpocząć nowy dzień jako student!"
    show screen stats_screen
    show screen inventory_button_screen
    jump choose


label choose:
    hide screen stats_screen
    hide screen inventory_button_screen
    hide screen stats_expanded_screen
    hide screen inventory_screen
    #Tymczasowe menu pozwalające przechodzić na obiekty na mapie
    #TODO Zmienić to na mape z obiektami na kliknięcie
    scene bg city
    menu:
        "Gdzie chcesz iść?"
        "Dom":
            show screen stats_screen
            show screen inventory_button_screen
            jump house_main

        "Uczelnia":
            show screen stats_screen
            show screen inventory_button_screen
            jump school_main

        "Restauracja":
            show screen stats_screen
            show screen inventory_button_screen
            jump restaurant_main

        "Sklep":
            show screen stats_screen
            show screen inventory_button_screen
            jump shop_main

        "Park":
            show screen stats_screen
            show screen inventory_button_screen
            jump park_main

        "Biuro Pracy":
            show screen stats_screen
            show screen inventory_button_screen
            jump job_place_main

        "TESTZONE":
            jump test_zone                

label game_over_screen:
    "Przegrałeś"
    return

label tuition:
    "Nadszedł czas na zapłate czesnych - 930zł!"
    if money >= 930:
        "Zapłaciłeś czesne, możesz kontynuować nauke"
    else:
        "Niestety nie stać cię na zapłatę czesnych, przez co zostajesz wydalony z uczelni..."
        jump game_over_screen

label test_zone:
    python:
        money = money + 1000
        energy_drink_amount = energy_drink_amount + 10
        bar_amount = bar_amount + 10
        beer_amount = beer_amount + 10
        day = 29
    
    jump choose
    