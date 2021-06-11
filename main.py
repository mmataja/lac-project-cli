import os;
import datetime;
import sys;
import platform;
import menu;

def main():
    weekDays = ("Ponedjeljak","Utorak","Srijeda","Četvrtak","Petak","Subota","Nedjelja");

    dateNow = datetime.date.today().strftime("%d+%m+%Y");
    timeNow = datetime.datetime.now().strftime("%H*%M*%S");
    dayInWeek = weekDays[datetime.datetime.today().weekday()];

    print();
    print("Dobrodošli {}!".format(os.getlogin()));
    print("Sada je {} {} {}".format(timeNow, dayInWeek, dateNow));
    print("Python verzija", platform.python_version());
    print("Operacijski sustav:", os.uname()[0]);
    print();

    menu.menuOptions();
    print();
    menu.menuInputOption();


if __name__ == "__main__":
    main();
    print("\n");
