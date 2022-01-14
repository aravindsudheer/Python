secret_word = "effort"
guess = ""
guess_count = 0
guess_cnt_lmt = 5
over_limit = False

while secret_word != guess and not(over_limit):
    if guess_count <= guess_cnt_lmt:
        guess = input ("Guess the secret word: ")
        guess_count += guess_count
    else:
        over_limit = True

if over_limit == True:
    print("Opps ran out of chances")
else:
    print("You WON!!")

        
    
    
    
