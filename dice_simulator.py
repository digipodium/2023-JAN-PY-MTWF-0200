# wap to create a function that will 
# generate random 3 dice numbers and if all 3 match, then
# display "you win" else display "you lose / try again"
import random
def streak():
    dices = ['😀','😁','😂','😃','😄','😅']
    selection = random.choices(dices, k=3)
    if selection[0] == selection[1] == selection[2]:
        return selection, "You win"
    else:
        return selection, "You lose / try again"
    

ans,msg = streak()
print('Rolling the dices...')
print(" ".join(ans))
print(msg)