import signal;
import os;

def receiveSignal(brojSignala, stog):
    print("|");
    print("|\t Zaprimljen je signal broj", brojSignala);
    print("|\t PPID je:", os.getppid());
    print("|\t PID je:", os.getpid());

    homeDir = os.path.expanduser("~");
    stogFile = open("{}/stog1.txt".format(homeDir), "w");
    stogFile.write("Signal broj {}\n".format(brojSignala) + str(stog));

    print("|");
    print("|\t Kreirana je stog1.txt datoteka unutar Vašeg kućnog direktorija u kojoj se nalazi trenutno stanje stoga --> {}{}".format(homeDir, "/stog1.txt"));
    print("|");

    return;

def processSignal():
    while True:
        try:
            signalNumber = input("|\t Unesite broj signala: ");
            int(signalNumber);
            if (int(signalNumber) > 31):
                raise ValueError("|\t ERROR - Unos signala mora biti manji ili jednak 31.");
        except ValueError as error:
            if(signalNumber != ""):
                print("|\t ERROR - Unos signala mora biti manji ili jednak 31.");
            print("|");
            continue;
        else:
            break;

    validSignals = signal.valid_signals();
    for key in validSignals:
        if (type(key) != int and key.value <= 31):
            if key.value in range(1, 9):
                signal.signal(key, signal.SIG_IGN);
            elif(key.value == 14 or key.value == 15):
                signal.signal(key, receiveSignal);


    signalNumber = int(signalNumber);
    signal.raise_signal(signalNumber);
