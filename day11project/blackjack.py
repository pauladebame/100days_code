import random
def list_sum(List):
    total = 0
    for x in List:
        total += x
    return(total)
#this funtion is used to compare between the total of the computer and the total of the player
def compare():
    if computer_sum > 21 or computer_sum < user_sum:
        print("you win")
    elif computer_sum > user_sum or user_sum > 21:
        print("you loose")
    else:
        print ("its a draw")
    return

#the stand function
def Stand(computer_sum):

    while computer_sum < 17:
        pickc = random.choice(cards)
        for j in range(1):
            computer.append(pickc)
        if pickc == 11:
            i = len(computer)
            computer_sum = list_sum(user)
            if computer_sum > 21:
                computer_sum -= 10
                computer[i-1] = 1
        else:
            x = list_sum(computer)
        computer_sum = x
    return computer_sum
   
#the hit function
def hit(user):
    hit_flag = True
    while hit_flag:
        pick = random.choice(cards)
        user.append(pick)
        if pick == 11: #check if number is ace
            i = len(user)
            user_sum = list_sum(user)
            if user_sum > 21:
                user_sum -= 10
                user[i-1] = 1
                print(f'player: {user}, Total: {user_sum}')

        #the picked card is not ace        
        else:
            #add number to player_sum
            user_sum = list_sum(user)
            print(f'player:{user} Total: {user_sum}' )
        if user_sum > 21:
            print(f'dealer: {computer}, Total: {computer_sum} you loose')
            hit_flag = False
            return False
        else:
            hit_stand = input(f'Enter H for hit and S for stand: ').lower()
            if hit_stand == 'h':
                hit_flag = True
            else: 
                return user_sum

stand_hit = True
#create a list of numbers or the cards
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10,]
# now create an empty list for the computer and the user 
computer = []
user = []
#randomely pick two numbers from the card list to give to computer and user
for i in range(2):
    computer.append(random.choice(cards))
    user.append(random.choice(cards))
computer1 = ['#', computer[1]]
user_sum = list_sum(user)
computer_sum = list_sum(computer)
#check if two ace is picked
#if so convert, one of the card to 1 instead of 11
if user_sum == 22:
    i = len(user) 
    user_sum -= 10
    user[i-1] = 1
elif computer_sum == 22:
    i = len(computer)
    computer_sum -=10
    computer[i-1]
print(f'Computer: {computer1} \n Player: {user} Total: {user_sum}')

#check for black jack
if user_sum == 21 and computer_sum == 21 or computer_sum == 21:
    print(f"{computer} \ncomputer wins")
    stand_hit = False
elif user_sum == 21 and computer_sum < 21:
    print("you win!")
    stand_hit = False

#this is the heart of the game, where you pick between stand or hit
while stand_hit == True : 
    hit_stand = input(f'Enter H for hit and S for stand: ').lower()
    if hit_stand == 's':
        computer_sum = Stand(computer_sum)
        print(f'dealer: {computer} total: {computer_sum}')
        compare()
        stand_hit = False
    elif hit_stand == "h":
        test = hit(user) # store the return value of the hit() funtion into a variable 
        #so it can be reuseable
        if test == False:
            stand_hit = False
        else:
            user_sum= test
            if computer_sum > user_sum:
                print(f'dealer: {computer}, Total: {computer_sum} you loose')
                stand_hit = False
            else:
                computer_sum = Stand(computer_sum)
                print(f'dealer: {computer} total: {computer_sum}')
                compare()
        stand_hit = False
    else:
        print("please enter H or S:")