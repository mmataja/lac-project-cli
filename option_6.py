import threading;
import time;

bigNumber = 55550550550550550550;
maxRange = 177000;
minRange = 10;
numberOfThreads = 4;
semafor = threading.Semaphore(1);

def squareNumbers():
    while True:
        try:
            n = input("|\t Unesite broj u rasponu {} - {}: ".format(minRange, maxRange));
            int(n);
            if (int(n) < minRange or int(n) > maxRange):
                raise ValueError("|\t ERROR - Unos neispravan! Pokušajte ponovo.");
        except ValueError as error:
            if(n != ""):
                print("|\t ERROR - Unos neispravan! Pokušajte ponovo.");
            print("|");
            continue;
        else:
            break;

    print("|");

    splitInputInterval = list(split(range(int(n)), numberOfThreads));

    thread1 = threading.Thread(target = calculate, args = (splitInputInterval[0], 'Dretva 1'));
    thread2 = threading.Thread(target = calculate, args = (splitInputInterval[1], 'Dretva 2'));
    thread3 = threading.Thread(target = calculate, args = (splitInputInterval[2], 'Dretva 3'));
    thread4 = threading.Thread(target = calculate, args = (splitInputInterval[3], 'Dretva 4'));

    thread1.start();
    thread2.start();
    thread3.start();
    thread4.start();

    thread1.join();
    thread2.join();
    thread3.join();
    thread4.join();

    print("|");
    print("|\t Konačan rezultat oduzimanja je: ", bigNumber);
    bigNumber = 55550550550550550550;


def calculate(interval, threadName):
    global bigNumber;
    for number in interval:
        semafor.acquire();
        bigNumber = bigNumber - number**2;
        semafor.release();
    print("|\t {} je završila izvođenje u trajanju {}".format(threadName, time.thread_time()));


def split(a, n):
    k, m = divmod(len(a), n);
    return (a[i * k + min(i, m):(i + 1) * k + min(i + 1, m)] for i in range(n));
