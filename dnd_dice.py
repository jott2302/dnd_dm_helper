import random as r
import traceback


def throw_dice(dicemaxnum=20):
    return (r.randint(1, int(dicemaxnum)))


def run_game():
    print("Du kannst das Program jederzeit mit einer Würfeleingabe von 0 beenden!")
    gamestart = True

    while gamestart:
        try:
            user_dice = input("Wähle deinen zu werfenden Würfel:\n")
            if int(user_dice) == 0:
                print("Program beendet")
                break
            print(f"Du hast eine {throw_dice(int(user_dice))} gewürfelt\n\n")
        except ValueError:
            # traceback.print_exc()
            print("Würfel bitte nocheinmal, es ist etwas schief gelaufen.\n\n")
