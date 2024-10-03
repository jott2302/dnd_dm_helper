import random as r


def throw_multiple_dice():
    while True:
        try:
            dicemaxnum = int(input("Welchen Würfel willst du werfen?: "))
            dice_count = int(input("Wie oft willst du den Würfel werfen?: "))
            all_dice = []
            for _ in range(dice_count):
                dice_result = (r.randint(1, int(dicemaxnum)))
                all_dice.append(dice_result)
            print(f"Du hast {all_dice} gewürfelt.")
            print("\n")
            break
        except ValueError:
            print("\nDie Eingaben für die Würfel müssen Zahlen sein.\n")


def throw_dice(dicemaxnum=20):
        return(r.randint(1, int(dicemaxnum)))



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
