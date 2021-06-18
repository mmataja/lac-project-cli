import os;
import sys;

def removeDir():
    dirPath = input("|\t Adresa direktorija: ");

    while not dirPath:
        dirPath = input("|\t Adresa direktorija: ");

    if(checkPath(dirPath)):
        try:
            os.rmdir(dirPath);
            fullPath = os.path.abspath(dirPath);
            removeDirPathFromPath = fullPath.split("/")[:-1];
            parentOfRemovedDir = "/".join(removeDirPathFromPath);
            pgid = os.getpgrp();

            print("|");
            print("|**** Direktorij uspješno pobrisan! ****");
            print("|\t Adresa nadređenog direktorija: ", parentOfRemovedDir);
            print("|\t Identifikator grupe vlasnika direktorija:", pgid);
            print("|\t Sadržaj nadređenog direktorija nakon brisanja:");
            print(os.listdir(parentOfRemovedDir));
            return;
        except OSError as error:
            print("|\t ERROR - Došlo je do greške.", error);
            print("|");
            removeDir();
    else:
        removeDir();



def checkPath(path):
    if not(os.path.exists(path)):
        print("|\t ERROR - Unijeli ste neispravnu adresu.");
        print("|");
        return False;

    return True;
