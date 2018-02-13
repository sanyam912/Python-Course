guesses=[]
count=0
ans='python'
word=[]

while (count<10):
    guess=input('guess a letter : ')
    if (''.join(guesses)==ans):
        print('you win')
        break
    elif len(guess)>1 and ans==guess:
        print(ans)
        print('you win')
        break
    else:
        guesses.append(guess)
        for char in ans:
            if char in guesses:
                word.append(char)
                print(char)
        
            else:
                print('_')
        count+=1
        
else:
    print('you lose')
