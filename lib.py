import os
import random

def GenerateEnemyPosition():
    X = random.randint(-100, 100)
    Y = random.randint(50, 100)
    Z = random.randint(-100, 100)
    return X, Y, Z

def ReadFile(file):
    f=open(file, "r")
    data=f.read()
    f.close()
    return data

def WriteFile(file, data):
    f=open(file, "w")
    f.write(data)
    f.close()

def Create_save(Name):
    Saves = ReadFile("data/Saves.txt")
    Savenumber = int(Saves) + 1
    os.mkdir(f"data/Save_{str(Savenumber)}")
    WriteFile("data/Saves.txt", str(Savenumber))
    WriteFile(f"data/Save_{Savenumber}/Money.txt", "0")
    WriteFile(f"data/Save_{Savenumber}/LV.txt", "0")
    WriteFile(f"data/Save_{Savenumber}/HP.txt", "100")
    WriteFile(f"data/Save_{Savenumber}/Name.txt", Name)
    WriteFile(f"data/Save_{Savenumber}/X.txt", "0")
    WriteFile(f"data/Save_{Savenumber}/Y.txt", "0")
    WriteFile(f"data/Save_{Savenumber}/Z.txt", "0")
    WriteFile(f"data/Save_{Savenumber}/Volume.txt", "0.5")

def Save(Savenumber, Money, HP, LV, X, Y, Z, Volume):
    WriteFile(f"data/Save_{Savenumber}/Money.txt", Money)
    WriteFile(f"data/Save_{Savenumber}/LV.txt", LV)
    WriteFile(f"data/Save_{Savenumber}/HP.txt", HP)
    WriteFile(f"data/Save_{Savenumber}/X.txt", X)
    WriteFile(f"data/Save_{Savenumber}/Y.txt", Y)
    WriteFile(f"data/Save_{Savenumber}/Z.txt", Z)
    WriteFile(f"data/Save_{Savenumber}/Volume.txt", Volume)

def Load(Savenumber):
    X = ReadFile(f"data/Save_{Savenumber}/X.txt")
    Y = ReadFile(f"data/Save_{Savenumber}/Y.txt")
    Z = ReadFile(f"data/Save_{Savenumber}/Z.txt")
    LV = ReadFile(f"data/Save_{Savenumber}/LV.txt")
    HP = ReadFile(f"data/Save_{Savenumber}/HP.txt")
    Money = ReadFile(f"data/Save_{Savenumber}/Money.txt")
    Name = ReadFile(f"data/Save_{Savenumber}/Name.txt")
    Volume = ReadFile(f"data/Save_{Savenumber}/Volume.txt")
    return X, Y, Z, LV, HP, Money, Name, Volume
