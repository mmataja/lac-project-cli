import menu;
import time;
import threading;

timeout = 3;

def cmdInput():
    timerThread = threading.Timer(timeout, ifTimerExpire);
    timerThread.start();


    while True:
        try:
            arguments = input("|\t Unesite broj signala: ");
            timerThread.cancel();
        except ValueError as error:
            if(arguments != ""):
                print("|\t ERROR - Unos signala mora biti manji ili jednak 31.");
            print("|");
            continue;
        else:
            break;

    print("UPISANO JE", arguments);

def ifTimerExpire():
    print("|");
    print("|\t Vrijeme za unos isteklo.");
