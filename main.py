import random

def play():
    l=5
    w=5
    while(l>0 and w>0):
        user = input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissors\n")
        computer = random.choice(['r', 'p', 's'])
        print(computer)
        if user == computer:
           print('It\'s a tie you have',w,"lives left")
           # r > s, s > p, p > r
        if is_win(user, computer):
           l-=1
           print('You win and you have',w,'lives left. And the computer have',l,'lives left')
        if(is_win(user, computer)==False):
           w-=1
           print('Computer wins and you have',w,'lives left.And the computer have',l,'lives left')
        if(w==0):
            return ' GAME OVER YOU LOST!'
        if(l==0):
            return 'GAME OVER YOU WIN!'

def is_win(player, opponent):
    # return true if player wins
    # r > s, s > p, p > r
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') \
        or (player == 'p' and opponent == 'r'):
        return True
    elif(player!=opponent):
        return False

print(play())