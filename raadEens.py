import random

poging = None
guess = None
ronde = 1
print ('NIEMAND WEET, NIEMAND WEET, DAT IK **** HEET')
print ('enter QUIT om te stoppen')

#answer = random.randint(1,1000)
#print (answer) #test
for i in range (20):
    answer = random.randint(1,1000)
    poging = 0
    print (f'START RONDE {ronde}')  
    print (answer) #test
    print ('^ dit is het antwoord als test. verwijder later')    
    while poging < 10:                                                  # while loop voor warm/heel-warm raden 10x
        try:                                                            # try/except is nu om te voorkomen dat je een valueerror krijgt bij het typen van een letter ipv een getal
            print ('raad het getal tussen de 1 en de 1000: ')
            guess = input ()
            if guess == 'quit' or guess == 'QUIT':
                print (f'je eindigde bij ronde {ronde}')
                print ('TOT ZIENS')
                exit()                                                  # dus niet system.exit haha
            guess = int(guess)
            if guess != answer and guess in range (answer - 20, answer + 20):              # het random getal minus of plus 20 = heel dichtbij
                print ('Je bent heel warm!')
            elif guess != answer and guess in range (answer - 50, answer + 50):            # het random getal minus of plus 50 = gewoon dichtbij
                print ('Je bent warm!')
            poging = poging + 1  
            print (f'dat was poging {poging} /10' )                               # elif en in deze volgrode want anders pakt hij altijd de 50 want 20 zit ook binnen een range van 50
        except ValueError:
            print ('Dat is geen geldig answer. Probeer het opnieuw')    # je poging /10 gaat ook niet omhoog op deze manier (dankzij continue)
            continue
        
        if guess == answer:
            print (f'IK DACHT INDERDAAD AAN HET GETAL {answer} ')
            ronde = ronde + 1
            if ronde <=3:
                print ('Nog een getal raden? J/N ')
            verderGaan = input ()
            if verderGaan in ['j','J','ja','Ja']:                       # als je input in de [ ] zit dan:
                break
            if verderGaan in['n', 'N', 'nee','Nee']:
                print (f'je eindigde bij ronde {ronde}')
                print ('TOT ZIENS')
                exit()
        elif poging == 10:
            print ('GAME OVER. DAT WAS POGING 10/10')
            print (f'JE EINDIGDE BIJ RONDE {ronde}')
            exit()
        
print (f'DIT WAS RONDE {ronde -1} JE HEBT MIJ VERSLAGEN. GEFELICITEERD.')  #-1 omdat het anders ronde 21 ipv 20 geeft. ik beb lui




    

