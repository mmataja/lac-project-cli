import sys;
import option_1;
import option_2;
import option_3;
import option_4;
import option_5;
import option_6;

KRAJ = 'kraj';
IZLAZ = 'izlaz';

def menuOptions():
    print("*-------------------------------------------------------------------*")
    print("| GLAVNI IZBORNIK:");
    print("| \t 1 - Unos terminalnih naredbi");
    print("| \t 2 - Brisanje direktorija");
    print("| \t 3 - Unos broja signala koji se šalje trenutnom procesu");
    print("| \t 4 - Izračun i ispis neprostih brojeva iz intervala [0, 166000]");
    print("| \t 5 - Ispis liste neparnih i umanjenih brojeva");
    print("| \t 6 - Izračun kvadrata brojeva raspoređen na četiri dretve");
    print("| \t kraj ili izlaz - Završetak izvođenja programa");

def menuInputOption():
    print("|");
    option = input("| UNOS OPCIJE IZBORNIKA: ");
    print("*-------------------------------------------------------------------*")

    while (option != KRAJ or option != IZLAZ):
        if(option == KRAJ or option == IZLAZ):
            sys.exit();
        elif option == '1':
            option_1.cmdInput();
        elif option == '2':
            option_2.removeDir();
        elif option == '3':
            option_3.processSignal();
        elif option == '4':
            option_4.listOfNonPrimeNumbers();
        elif option == '5':
            option_5.oddNumbers();
        elif option == '6':
            option_6.squareNumbers();
        elif option == "":
            menuInputOption();
        else:
            print("| \t ERROR - Nepostojeća opcija izbornika.");

        print("|");
        menuOptions();
        print("|");
        option = input("| UNOS OPCIJE IZBORNIKA: ");
