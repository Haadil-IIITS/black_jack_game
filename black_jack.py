import art2
import random

print(art2.logo)
cards=['A',2,3,4,5,6,7,8,9,10,10,10]
sum_user=0
dealer=list()
user=list()
def check(word):
    for i in range(len(word)):
        if word[i]=="A":
            word[i]=11
            if sum(word)>21:
                word[i]=1
    return word

def add_dealer(sum_dealer,dealer):
    while(sum_dealer<17):
        print(f" Dealer cards are {dealer} so dealer pick another cards")
        dealer.append(random.choice(cards))
        dealer=check(dealer)
        sum_dealer=sum(dealer)
    return sum_dealer,dealer

for i in range (0,2):
    dealer.append(random.choice(cards))
    user.append(random.choice(cards))
    dealer=check(dealer)
user=check(user)
sum_user=sum(user)
sum_dealer=dealer[0]

print(f" The dealer cards are {dealer[0]} , sum of dealer card is : {sum_dealer}")
print(f" The user cards are {user}, sum of user cards is : {sum_user}")
again='y'

while again=='y':
    again=(str(input(" \n stand=='n' or hit=='y' "))).lower()
    if sum_user>21:
        print("the dealer win ")
        break
    if sum_dealer>21:
        print("You won ")
        break


    if again=='n':
        if sum_dealer<17:
            sum_dealer,dealer=add_dealer(sum_dealer,dealer)

        print(f" the dealer cards are  {dealer}. The sum of dealer card is {sum_dealer}")
        print(f" The user cards are {user}, sum of user cards is : {sum_user}")

        if sum_user>21:
            print("\n the dealer win ")
            break

        if sum_dealer>21:
            print("\n You won ")
            break


        if sum_dealer>sum_user:
            print("\n dealer win")
            break
        elif sum_dealer==sum_user:
            print("Draw")
        else:
            print("\n You Won")
            break
    else:
        
        user.append(random.choice(cards))
        user=check(user)
        sum_user=sum(user)
        print(f" The user cards are {user}, sum of user cards is : {sum_user}")

    if sum_user>21:
        print("the dealer win ")
        break
    if sum_dealer>21:
        print(" \nYou won ")
        break
