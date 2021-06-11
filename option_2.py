import os;

def removeDir():
    print(os.getpid())
    dirPath = input("Adresa direktorija: ");

    while not dirPath:
        dirPath = input("Adresa direktorija: ");

    checkPath(dirPath);


    return print("Option 2 unos", dirPath);


def checkPath(path):
    if(os.path.exists(path)):
        print("POSTOJI PATH", path);
