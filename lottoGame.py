import random

class Bill:
    def guessGenerator(self,guessType):
        return random.sample(range(1,91),guessType)

    def billsPrinter(*args):
        if not all(type(bill)==Bill for bill in args):
            raise(TypeError('Only object of class Bill!'))
        billsNumber=len(args)
        billNumberColumnWidth=max(len(str(billsNumber)),len('Bill number'))
        ruotaColumnWidth=len('Ruota')
        guessColumnWidth=len('Guesses')
        for bill in args:
            if ruotaColumnWidth<len(bill.city):
                ruotaColumnWidth=len(bill.city)
            
            if guessColumnWidth<len(str(bill.guessList))-2:
                guessColumnWidth=len(str(bill.guessList))-2
        
        billsTable=[]
        billsTable.append('+--{}--+--{}--+--{}--+'.format('-'*billNumberColumnWidth,'-'*ruotaColumnWidth,'-'*guessColumnWidth))
        billsTable.append('|  {}{}  |  {}{}  |  {}{}  |'.format('Bill number',' '*(billNumberColumnWidth-len('Bill number')),'Ruota',' '*(ruotaColumnWidth-len('Ruota')),'Guesses',' '*(guessColumnWidth-len('Guesses'))))
        billsTable.append('+--{}--+--{}--+--{}--+'.format('-'*billNumberColumnWidth,'-'*ruotaColumnWidth,'-'*guessColumnWidth))
        for i in range(len(args)):
            bill=args[i]
            guesses=', '.join(str(guess) for guess in bill.guessList)
            billsTable.append('|  {}{}  |  {}{}  |  {}{}  |'.format(i+1,' '*(billNumberColumnWidth-len(str(i))),bill.city,' '*(ruotaColumnWidth-len(bill.city)),guesses,' '*(guessColumnWidth-len(str(guesses)))))
        billsTable.append('+--{}--+--{}--+--{}--+'.format('-'*billNumberColumnWidth,'-'*ruotaColumnWidth,'-'*guessColumnWidth))
        print('\n'.join(billsTable))

    def winningBillsPrinter(*args):
        if not all(type(bill)==Bill for bill in args):
            raise(TypeError('Only object of class Bill!'))
        billsNumber=len(args)
        billNumberColumnWidth=max(len(str(billsNumber)),len('Bill number'))
        ruotaColumnWidth=len('Ruota')
        guessColumnWidth=len('Guesses')
        winningGuessColumnWidth=len('Winning guesses')
        for bill in args:
            if ruotaColumnWidth<len(bill.city):
                ruotaColumnWidth=len(bill.city)
            
            if guessColumnWidth<len(str(bill.guessList))-2:
                guessColumnWidth=len(str(bill.guessList))-2
            
            if winningGuessColumnWidth<len(str(bill.winsList))-2:
                winningGuessColumnWidth=len(str(bill.winsList))-2
        
        billsTable=[]
        billsTable.append('+--{}--+--{}--+--{}--+--{}--+'.format('-'*billNumberColumnWidth,'-'*ruotaColumnWidth,'-'*guessColumnWidth,'-'*winningGuessColumnWidth))
        billsTable.append('|  {}{}  |  {}{}  |  {}{}  |  {}{}  |'.format('Bill number',' '*(billNumberColumnWidth-len('Bill number')),'Ruota',' '*(ruotaColumnWidth-len('Ruota')),'Guesses',' '*(guessColumnWidth-len('Guesses')),'Winning guesses',' '*(winningGuessColumnWidth-len('Wining guesses'))))
        billsTable.append('+--{}--+--{}--+--{}--+--{}--+'.format('-'*billNumberColumnWidth,'-'*ruotaColumnWidth,'-'*guessColumnWidth,'-'*winningGuessColumnWidth))
        for i in range(len(args)):
            bill=args[i]
            guesses=', '.join(str(guess) for guess in bill.guessList)
            winningGuesses=', '.join(str(guess) for guess in bill.winsList)
            billsTable.append('|  {}{}  |  {}{}  |  {}{}  |  {}{}  |'.format(i+1,' '*(billNumberColumnWidth-len(str(i))),bill.city,' '*(ruotaColumnWidth-len(bill.city)),guesses,' '*(guessColumnWidth-len(str(guesses))),winningGuesses,' '*(winningGuessColumnWidth-len(str(winningGuesses)))))
        billsTable.append('+--{}--+--{}--+--{}--+--{}--+'.format('-'*billNumberColumnWidth,'-'*ruotaColumnWidth,'-'*guessColumnWidth,'-'*winningGuessColumnWidth))
        print('\n'.join(billsTable))

    def __init__(self,city,*args):
        if len(args)<1:
            raise(SyntaxError('At least one guess type is needed!'))
        elif not all(type(guess)==int for guess in args):
            raise(TypeError('Only int values for guessType!'))
        elif not all(guess in range(1,6) for guess in args):
            raise(SyntaxError('Review your guess types! One or more of them are not an existing guess type!'))
        elif sum(args)>10:
            raise(SyntaxError('At most 10 numbers for each bill!'))
        elif not city.lower() in ["bari", "cagliari", "firenze", "genova", "milano", "napoli", "palermo", "roma", "torino", "venezia","tutte"]:
            raise(SyntaxError('{} is not an existing "ruota"'.format(city)))
        else:
            guessList=[]
            for i in range(len(args)):
                guessList.append(self.guessGenerator(args[i]))
            self.guessList=guessList
            self.city=city
            self.winsList=[]
    
    def __str__(self):
        return 'Bill: Ruota di {} - {}'.format(self.city.capitalize(),self.guessList)

class Extraction:
    ruoteList=["bari", "cagliari", "firenze", "genova", "milano", "napoli", "palermo", "roma", "torino", "venezia"]
    def __init__(self):
        extraction={}
        for ruota in Extraction.ruoteList:
            extraction[ruota]=random.sample(range(1,91),5) 
        self.extractions=extraction
    
    def __str__(self):
        extraction=self.extractions
        ruotaColumnWidth=len('Ruota')
        numbersColumnWidth=len('Extracted numbers')
        for ruota in Extraction.ruoteList:
            if ruotaColumnWidth<len(ruota):
                ruotaColumnWidth=len(ruota)
            
            if numbersColumnWidth<len(str(list(extraction[ruota])))-2:
                numbersColumnWidth=len(str(list(extraction[ruota])))-2
        
        extractionsTable=[]
        extractionsTable.append('+--{}--+--{}--+'.format('-'*ruotaColumnWidth,'-'*numbersColumnWidth))
        extractionsTable.append('|  {}{}  |  {}{}  |'.format('Ruota',' '*(ruotaColumnWidth-len('Ruota')),'Extracted numbers',' '*(numbersColumnWidth-len('Extracted numbers'))))
        extractionsTable.append('+--{}--+--{}--+'.format('-'*ruotaColumnWidth,'-'*numbersColumnWidth))
        for ruota in extraction:
            extractedNumbers=', '.join(str(number) for number in extraction[ruota])
            extractionsTable.append('|  {}{}  |  {}{}  |'.format(ruota.capitalize(),' '*(ruotaColumnWidth-len(ruota)),extractedNumbers,' '*(numbersColumnWidth-len(extractedNumbers))))
        extractionsTable.append('+--{}--+--{}--+'.format('-'*ruotaColumnWidth,'-'*numbersColumnWidth))
        return '\n'.join(extractionsTable)

def winCheck(bill,extraction):
    if type(bill)!=Bill:
        raise(TypeError('Only bill objects for bill argument!'))
    elif type(extraction)!=Extraction:
        raise(TypeError('Only extraction objects for extraction argument!'))
    
    guessList=bill.guessList
    ruota=bill.city.lower()
    if ruota=='tutte':
        extractions=extraction.extractions
        for ruota in extractions:
            for guess in guessList:
                if set(guess).issubset(set(extractions[ruota])):
                    if not guess in bill.winsList:
                        bill.winsList.append(guess)
    else:
        for guess in guessList:
                if set(guess).issubset(set(extractions[ruota])):
                    if not guess in bill.winsList:
                        bill.winsList.append(guess)
    
    if len(bill.winsList)>0:
        return True
    else:
        return False