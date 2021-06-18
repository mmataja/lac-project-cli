import threading;

numberOfThreads = 3;
lista_brojeva = [];
threadLock = threading.RLock();


def listOfNonPrimeNumbers():
    global lista_brojeva;
    print("|");
    threadingMechanism();
    print("|");
    lista_brojeva = [];


def threadingMechanism():
    splitInterval = list(split(range(166000), numberOfThreads));

    thread1 = threading.Thread(target = checkIfPrime, args = (splitInterval[0],));
    thread2 = threading.Thread(target = checkIfPrime, args = (splitInterval[1],));
    thread3 = threading.Thread(target = checkIfPrime, args = (splitInterval[2],));

    thread1.start();
    thread2.start();
    thread3.start();

    thread1.join();
    thread2.join();
    thread3.join();

    print("|");
    print("|\t Lista neprostih brojeva:");
    print(lista_brojeva);
    print("|");
    print("|\t Zbroj svih neprostih brojeva iz navedenog intervala iznosi:", sum(lista_brojeva));
    print("|");


def checkIfPrime(interval):
    global lista_brojeva;
    for number in interval:
        if number > 1:
            for i in range(2, int(number / 2) + 1):
                if (number % i) == 0:
                    threadLock.acquire();
                    lista_brojeva.append(number);
                    threadLock.release();
                    break;


def split(a, n):
    k, m = divmod(len(a), n);
    return (a[i * k + min(i, m):(i + 1) * k + min(i + 1, m)] for i in range(n));
