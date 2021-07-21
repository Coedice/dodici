import time

game_no_end = 12  # Traditionally 12

def after_game(turns_played):
    if (turns_played - 1) % 2:
        print("\nYou won! 😊")
    else:
        print("\nYou lost ☹️")


def player_turn():
    addToGameNo = int(input("You add: "))

    if 1 <= addToGameNo <= 3:
        return addToGameNo

    return 12


def corbobot_turn(game_no, game_no_end):
    game_nums_remaining = game_no_end - 1 - game_no  # The number of numbers until (game_no_end - 1)

    if (game_nums_remaining - 1) % 4 == 0:
        return 1
    elif (game_nums_remaining - 2) % 4 == 0:
        return 2
    elif (game_nums_remaining - 3) % 4 == 0:
        return 3
    else:
        return 1  # Return minimum to bide time for an opponent to make a mistake


game_num = 0  # The value of the shared total
turns_played = 0

while game_num < game_no_end:
    if turns_played % 2 == 0:  # Player's turn
        game_num += player_turn()
    else:  # CorboBot's turn
        time.sleep(0.5)
        add_to_game = corbobot_turn(game_num, game_no_end)
        game_num += add_to_game
        print("CorboBot adds: " + str(add_to_game))
        print("{}{} {}/{}".format("■"*game_num, "□"*(game_no_end - game_num), game_num, game_no_end))

    turns_played += 1

after_game(turns_played)
