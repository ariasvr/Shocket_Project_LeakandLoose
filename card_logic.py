
def returnListDataCards(p):
    listDataCards = []
    if 7 in p:
        listDataCards.append(7)
    if 8 in p:
        listDataCards.append(8)
    if 9 in p:
        listDataCards.append(9)

    return listDataCards

def returnListProtectCards(p):
    listProtectCards = []
    if 1 in p:
        listProtectCards.append(1)
    if 3 in p:
        listProtectCards.append(3)
    if 4 in p:
        listProtectCards.append(4)

    return listProtectCards
    
def reviveDataCards(p):
    if not 7 in p:
        p.append(7)
    if not 8 in p:
        p.append(8)
    if not 9 in p:
        p.append(9)
    return p

def whiteHatCard(p):
    try:
        listDataCards = returnListDataCards(p)
        if len(listDataCards) != 0:
            print("No need to use the white hat card")

        else: 
            print("Don't worry you're still alive")
            p.pop(p.index)

    except:
        print("WhiteHatCard function encounters ERR")

    return p

def blackHatCard(p):
    listProtectCard = returnListProtectCards(p)
    if len(listProtectCard) == 0: #No white-hat card or PROTECT cards in hand
        print("Player out!")
        p = [] #End game
        return p

    else: #There is at least one PROTECT cards in hand
        print("You're still alive")
        p.pop(p.index(listProtectCard[0]))
    
    return p

def multipleAuthCard(p):
    p.append(3)
    return p

def antiVirusCard(p):
    p.append(4)
    return p

def loveLetterCard(p):
    listDataCards = returnListDataCards(p)
    listProtectCards = returnListProtectCards(p)

    if len(listProtectCards) != 0: #there is at least a PROTECT card in player's hand
        p.pop(p.index(listProtectCards(0)))
    
    else: #there is none PROTECT card
        p.pop(p.index(listDataCards[0]))
        listDataCards.pop(0)
        p.pop(p.index(listDataCards[0]))

    return p

def strangeURLCard(p):
    if 7 in p:
        p.pop(p.index(7))

    elif 8 in p:
        p.pop(p.index(8))

    elif 9 in p:
        p.pop(p.index(9))

    return p

def calculateGame(p, cardPlayed):
    if cardPlayed == 1: #use white-hat card
        p = whiteHatCard(p)
    
    elif cardPlayed == 2: #drew a black-hat card
        p = blackHatCard(p)
        
    elif cardPlayed == 3: #drew a multiple-auth card
        p = multipleAuthCard(p)
        
    elif cardPlayed == 4: #drew an antivirus card
        p = antiVirusCard(p)
        
    elif cardPlayed == 5: #drew a love-letter card
        p = loveLetterCard(p)
        
    elif cardPlayed == 6: #drew a strange-url card
        p = strangeURLCard(p)
        
    return p