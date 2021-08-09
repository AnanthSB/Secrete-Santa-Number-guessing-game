"""
______Secrete santa game______

Concept of the game is, 
         you are going to add numbers secretly of you
         and your friend inlucding santa number.
        At the end Santa will guess the the number you'll have
Assume that you have a secrete box and the numbers you are going to store
in the secrete box you are not going tell anyone    """


import random
santa_number = random.randrange(2,30,2)

print(""""Hi!\n\tWelcome to: 'SECRETE SANTA GAME'\n""")
enter = input("Enter small 's' to start or 'e' to exit\nHere___")
if enter == 'e':
    print("Thank you for playing the game\nHave a Good Day")
    if enter == "e":
        exit()
    
print("\nConcept of the game is, \n\t you are going to add numbers secretly of you\n\t and your friend inlucding santa number.\n\tAt the end Santa will guess the the number you\'ll have")

print("Assume that you have a secrete box and the numbers you are going to store\nin the secrete box you are not going tell anyone ")

txt = "\nDone?__Enter_'s'_once_done,\nelse_enter_any_key_to_exit_the_game_\nHere__"

inp1 = input(txt)
if inp1 == 's':

    print("\nChose any random even number from 1 to 100 and keep it in your secrete box")
    inp2 = input(txt)
    if inp2 =='s':
        
        print("\nTake same exact even number for one of your friend also ")
        print("Add both numbers\n")
        print("NOw you have sum of two people")
        inp3 = input(txt)
        
        if inp3 == "s":
            print(f"\nNow add {santa_number} into the sum as santa\'s number\n")
            print("Now you have sum of three people.")
            inp4 = input(txt)
  
            
            if inp4 == "s":
                print("\nGive half of whole sum to God.\n\tExample:You have(2+2+2 = 6) then 6/2 = 3(half) \n")
                inp5 =input(txt)
                
                if inp5 == "s":
                    print("Give number back to your friend, which you have taken from him/her.")
                    inp6 = input(txt)
                    
                    if inp6 == "s":
                        print("\nalright.\n")
                        print("Santa guessed  the number left/you are having now.")
                        santa_guess = input(""""Enter__'show me'__to_know_whether_santa_guessed_rigth_number_you_have_or_not\norElse_enter_anykey_to_exit\nEnter__here__ """)
                        
                        if santa_guess == "show me":
                            print("\nSanta says you are left with ",int(santa_number/2))
                            print("\n\nThanks for playing the Secrete Santa game.\n\n\t Have a nice day :)")
                        else:
                            print(exit())
                    else:
                        print(exit())
                else:
                    print(exit())
            else:
                print(exit())
        else:
            print(exit())        
    else:
        print(exit())
else:
    print(exit())