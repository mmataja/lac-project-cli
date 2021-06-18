import threading;

minNumber = 2450000;
oddNumbersList = [];
reducedOddNumbersList = [];
semafor = threading.Semaphore(1);

def oddNumbers():
    while True:
        try:
            n = input("|\t Unesite broj veći od {}: ".format(minNumber));
            int(n);
            if (int(n) <= minNumber):
                raise ValueError("|\t ERROR - Unos neispravan! Pokušajte ponovo.");
        except ValueError as error:
            if(n != ""):
                print("|\t ERROR - Unos neispravan! Pokušajte ponovo.");
            print("|");
            continue;
        else:
            break;

    global oddNumbersList;
    thread1 = threading.Thread(target = getListOfOddNumbers, args = (int(n),));
    thread2 = threading.Thread(target = getReducedListOfOddNumbers, args = (oddNumbersList,));

    thread1.start();
    thread2.start();

    thread1.join();
    thread2.join();

    createFile = open("./umanjenje.txt", "w");
    createFile.write(str(reducedOddNumbersList));

    print("|");
    print("|\t Dretva zadužna za izradu tekst datoteke -> ", thread2.name);
    print("|\t Datoteke umanjenje.txt uspješno kreirana.");


def getListOfOddNumbers(number):
    global oddNumbersList;

    for num in range(0, number):
        if(num % 2) != 0:
            semafor.acquire();
            oddNumbersList.append(num);
            semafor.release();

def getReducedListOfOddNumbers(numbersList):
    for num in numbersList:
        reduceNum = num - (num * 0.25);
        reducedOddNumbersList.append(reduceNum);
