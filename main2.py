from character import Character
import time
import sys

def yavas_yaz(metin, hiz=0.015):
    for harf in metin:
        sys.stdout.write(harf)
        sys.stdout.flush()
        time.sleep(hiz)
    print()

if __name__ == "__main__":

    yavas_yaz("Welcome to The Abandoned Asylum!\n"
          "Before we start lets create your character!")
    main_name = input("Please enter the name: ")
    main_character = Character(main_name)

    yavas_yaz("You have 3 lifes!")
    time.sleep(1)
    yavas_yaz("You should be careful cos during the journey you'll face a lot of challenges.")
    time.sleep(3)
    yavas_yaz("And you better don't loose your all lifes otherwise you can't win.\n"    
          "---------------------------------------------------------------------------------\n")
    time.sleep(3)
    yavas_yaz("GAME STARTS!")
    time.sleep(1)

    yavas_yaz("It’s a cold night. \n")
    yavas_yaz("You stand before the long-forgotten Harper Mental Asylum, far from the city. \n")
    time.sleep(3)
    yavas_yaz("The door creaks open. You turn on your flashlight — the beam flickers. \n")
    time.sleep(3)
    yavas_yaz("Rust covers the walls, old medical files scatter the floor, and water \n")
    time.sleep(3)
    yavas_yaz("drips somewhere in the distance. Then… a whisper echoes down the corridor: \n")
    time.sleep(3)
    yavas_yaz("“Don’t go… or stay forever…” Your heartbeat quickens. Your footsteps echo. \n")
    time.sleep(3)
    yavas_yaz("Suddenly, two doors appear before you: \n")
    time.sleep(3)
    yavas_yaz("The left door says “Emergency Ward” — you hear chains rattling from within. \n")
    time.sleep(3)
    yavas_yaz("The right door says “Archive Room” — a faint light leaks from under it. \n")
    time.sleep(3)
