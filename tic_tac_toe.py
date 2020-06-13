import os
import random
block_is_filled=[0]*10
block_entry=[" "]*10
global player_chance
winning_combo=[[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]
player_chance=1

def print_table():
    os.system("cls")
    print("\n\n\t")
    print("\t"+block_entry[7]+"|"+block_entry[8]+"|"+block_entry[9])
    print("\t"+"-|-|-")
    print("\t"+block_entry[4]+"|"+block_entry[5]+"|"+block_entry[6])
    print("\t"+"-|-|-")
    print("\t"+block_entry[1]+"|"+block_entry[2]+"|"+block_entry[3])
    print("\n")
# LOGIC FOR COMPUTER TO SELECT A BOX AS INPUT AND RETURN IT TO MAIN FUNCTION
def computer_logic():
    for i in range(len(winning_combo)):
        if((block_entry[winning_combo[i][0]]=="o" and block_entry[winning_combo[i][1]]=="o") and block_is_filled[winning_combo[i][2]]==0):
            return(winning_combo[i][2])
        if((block_entry[winning_combo[i][0]]=="o" and block_entry[winning_combo[i][2]]=="o") and block_is_filled[winning_combo[i][1]]==0):
            return(winning_combo[i][1])
        if((block_entry[winning_combo[i][1]]=="o" and block_entry[winning_combo[i][2]]=="o") and block_is_filled[winning_combo[i][0]]==0):
            return(winning_combo[i][0])
    for i in range(len(winning_combo)):
        if(((block_entry[winning_combo[i][0]]=="o" and block_entry[winning_combo[i][1]]=="o") or (block_entry[winning_combo[i][0]]=="x" and block_entry[winning_combo[i][1]]=="x")) and block_is_filled[winning_combo[i][2]]==0):
            return(winning_combo[i][2])
        if(((block_entry[winning_combo[i][0]]=="o" and block_entry[winning_combo[i][2]]=="o") or (block_entry[winning_combo[i][0]]=="x" and block_entry[winning_combo[i][2]]=="x")) and block_is_filled[winning_combo[i][1]]==0):
            return(winning_combo[i][1])
        if(((block_entry[winning_combo[i][1]]=="o" and block_entry[winning_combo[i][2]]=="o") or (block_entry[winning_combo[i][1]]=="x" and block_entry[winning_combo[i][2]]=="x")) and block_is_filled[winning_combo[i][0]]==0):
            return(winning_combo[i][0])
    if((block_entry[1]=="o" or  block_entry[2]=="o" or block_entry[3]=="o" or block_entry[4]=="o" or block_entry[6]=="o" or block_entry[7]=="o" \
    or block_entry[8]=="o" or block_entry[9]=="o") and block_is_filled[5]==0):
        return(5)
    else:
        return(random.randint(1,9))
def print_results():
    for i in range(len(winning_combo)):
        if(block_entry[winning_combo[i][0]]==block_entry[winning_combo[i][1]]==block_entry[winning_combo[i][2]]=="o"\
        or block_entry[winning_combo[i][0]]==block_entry[winning_combo[i][1]]==block_entry[winning_combo[i][2]]=="x"):
            print_table()
            if(block_entry[winning_combo[i][0]]==block_entry[winning_combo[i][1]]==block_entry[winning_combo[i][2]]=="x"):
                print("You have won the game")
            if(block_entry[winning_combo[i][0]]==block_entry[winning_combo[i][1]]==block_entry[winning_combo[i][2]]=="o"):
                print("Computer has won the game")
            a=input("Game completed")
            exit()
while(1):
    print_table()
    print_results()
    if(0 not in block_is_filled[1:]):
        print("Game is a draw")
        print_results()
        break
# PLAYER PLAYING HIS CHANCE
    while(player_chance==1):
        if(0 not in block_is_filled[1:]):
            break
        player_choice=int(input("Layout of game board is same as numKey layout on the keyboard \n\
Player: x, PC: o \nEnter the box to fill in: "))
        if(block_is_filled[player_choice]==1):
            print("Block is already filled")
        else:
            block_entry[player_choice]="x"
            block_is_filled[player_choice]=1
            player_chance=0
            break
    print_results()
    if(0 not in block_is_filled[1:]):
        print_table()
        print("Game is a draw")
        print_results()
        break
#COMPUTER PLAYING ITS CHANCE
    while(player_chance==0):
        if(0 not in block_is_filled[1:]):
            break
        computer_choice=computer_logic()
        if(block_is_filled[computer_choice]==1):
            print()
        else:
            block_entry[computer_choice]="o"
            block_is_filled[computer_choice]=1
            player_chance=1
            break
