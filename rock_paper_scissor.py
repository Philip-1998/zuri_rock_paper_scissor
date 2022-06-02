from http.client import NotConnected
import random
import math

def play():
    player_input_status = False

    while not player_input_status:
        choice_list = ["r","p","s"]
        player_input = input("choose something p for paper, s for sciccor, r for rock: ")
        player_input = player_input.lower()

        if not player_input in choice_list:
            print("Not a valid choice")
            continue
        else:
            player_input_status = True

 
        

    cpu_input = random.choice(choice_list)
    if (player_input == cpu_input):
        print(f"Player chose ({player_input})   CPU chose ({cpu_input})")
        return 0
        

    elif player_win(player_input,cpu_input):
        print(f"Player chose ({player_input})   CPU chose ({cpu_input})")
        return 1

    else:
        print(f"Player chose ({player_input})   CPU chose ({cpu_input})")
        return -1
        

    


def player_win(player_input,cpu_input):
    if (player_input == "r" and cpu_input == "s") or (player_input == "s" and cpu_input == "p") or (player_input == "p" and cpu_input == "r"):
        return True
    else:
        return False


def play_n(n):
    necessary_wins = math.ceil(n/2)
    player_wins = 0
    cpu_wins = 0
    total_play = 0


    while total_play <= n:
        p=play()
        if p == 1:
            total_play +=1
            player_wins += 1
        elif p == -1:
            total_play += 1
            cpu_wins += 1
        else:
            total_play += 1
            player_wins += 0
            cpu_wins += 0
    if player_wins > cpu_wins:
        print(f"Hoooorayyyyy you have won player:{player_wins}  cpu:{cpu_wins}")
    
    elif player_wins == cpu_wins:
        print("Its a tie")

    else:
        print(f"Sorry You lost player:{player_wins}  cpu:{cpu_wins} ")
    
            

play_n(5)

    





