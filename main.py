# Här skriver du ditt textäventyr
import random
import time
randomnumber = random.randint (1,38)
randomcard1 = random.randint (1,11)
randomcard2 = random.randint (1,11)
randomcard3 = random.randint (1,11)
randomcard4 = random.randint (1,11)
randomcard5 = random.randint (1,11)
randomcardd1 = random.randint (1,11)
randomcardd2 = random.randint (1,11)
randomcardd3 = random.randint (1,11)
randomcardd4 = random.randint (1,11)
randomcardd5 = random.randint (1,11)
player1 = input("Player1-Name").lower()
print(player1+"-vaknar upp från sin säng klär på sig och går ut och ser sin kolega")
time.sleep(2.5)
print ("vill du säga hej till din kolega...") 
Hey = input ("ja eller nej")
if Hey == ("ja"):
    print("hej-"+player1+"-vad trevligt att se dig idag")
    time.sleep(2.5)
    print("trevligt att se dig idag")
else:
    print(player1+"-ignorerade din kolega")
    time.sleep(2.5)
    print("det kommer hon att komma ihåg")
time.sleep(2.5)
print("du fortsätter och att gå tills du ser en korsning vill du gå vänster eller höger")
Vänsterellerhöger = input("vänster eller höger")
if Vänsterellerhöger == ("vänster"):
    print(player1+("-tog en vänster i korsningen och komm fram till ett kasion"))
    time.sleep(2.5)
    print("går du in eller inte")
    oppåpå = input ("ja eller nej")
    if oppåpå == ("ja"):
        print("du gick in bra ide")
        time.sleep(2.5)
        print("vill du gå till rulet eller black jack")
        blackjackellerrulet = input ("rulet eller black jack-").lower()
        if blackjackellerrulet == ("blackjack"):
            spelaellerrulet = input  ("spela eller gå hem").lower()
            if spelaellerrulet == ("spela"):
                print(randomcard1+randomcard2)
                print(int("deler-")+randomcardd1+randomcardd2)
                hitorstand1 = input("hit or stand").lower()
                if hitorstand1 ==("hit"):
                    print(randomcard1+randomcard2+randomcard3)
                    print(randomcardd1+randomcardd2+randomcardd3)
                    hitorstand2 = input ("hit or stand").lower()
                    if hitorstand2 ==("hit"):
                        print(randomcard1+randomcard2+randomcard3+randomcard4)
                        print(randomcardd1+randomcardd2+randomcardd3+randomcardd4)
                        hitorstand3 = input ("hit or stand").lower()
                        if hitorstand3 == ("hit"):
                            print(randomcard1+randomcard2+randomcard3+randomcard4+randomcard5)
                            print(randomcardd1+randomcardd2+randomcardd3+randomcardd4+randomcardd5)
                            if (randomcard1+randomcard2+randomcard3+randomcard4+randomcard5)>(randomcardd1+randomcardd2+randomcardd3+randomcardd4+randomcardd5):
                                print ("du van 1 milijon")
                            else:
                                print ("bättre lycka nästa gång")
                        else: 
                            print(randomcard1+randomcard2+randomcard3+randomcard4)
                            print(randomcardd1+randomcardd2+randomcardd3+randomcardd4)
                            if(randomcard1+randomcard2+randomcard3+randomcard4)>(randomcardd1+randomcardd2+randomcardd3+randomcardd4):
                                print("du van 1 miljon")
                            else: 
                                print("bättre lycka nästa gång")
                    else:
                        print(randomcard1+randomcard2+randomcard3)
                        print(randomcardd1+randomcardd2+randomcardd3)
                        if (randomcard1+randomcard2+randomcard3)>(randomcardd1+randomcardd2+randomcardd3):
                            print("du van 1 miljon")
                        else:
                            print("bättre lyck nästa gång")
                else:
                    print(randomcard1+randomcard2)
                    print(randomcardd1+randomcardd2)
                    if (randomcard1+randomcard2)>(randomcardd1+randomcardd2):
                        print ("du van 1 miljon")
                    else:
                        print ("bättre lycka nästa gång")
            else:
                print("du gick hem. Fegis")            
        if blackjackellerrulet == ("rulet"):
            print("vill du spela??? Ja eller Nej")
            popppp = input ("ja eller nej-").lower()
            if popppp == ("ja"):
                spin = input ("svart eller röd eller grön").lower()
                if spin == ("svart"):
                    if randomnumber == (1,13):
                        print("du van 1 miljon")
                    else: 
                        print("du förlorade")
                elif spin == ("röd"):
                    if randomnumber == (38,16):
                        print ("du van 1 miljon")
                    else:
                        print("du förlorade")
                elif spin == ("grön"):
                    if randomnumber == (14,15):
                        print("du van 1 miljon")
                    else:
                        print("du förlorade")
    else:
        print("VARFÖR DUM IDE DU DOG")
if Vänsterellerhöger == ("höger"):
    print("Du tog vägen och kom fram till dit jobb men du måste testa den andra vägen.")
    if Hey == ("nej"):
        print("kommer du ihåg din kolega hon kom och dödade dig.")
    else: 
        print("du sa hej till din kolega du får en miljon")