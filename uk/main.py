import os, sys, subprocess, json, pyfiglet
from colorama import Style
from fernet import Fernet
from pynput import keyboard


def clear():
    os.system("cls")


def maintain():
    print("your sudo")
    while True:
        h = (
            "pwd",
            "ls",
            "touch",
            "rm",
            "rm-rf",
            "cat",
            "ukmd",
            "os",
            "exit",
            "cd",
            "vim",
            "miv",
            "lp",
            "cls",
        )
        pwd = os.getcwd()
        command = str(input(f"$"))
        cmd = command.split(" ")
        if cmd[0] == "pwd":
            print(pwd)
        elif cmd[0] == "ls":
            ls = os.listdir()
            for iver in ls:
                print(iver)
        elif cmd[0] == "touch":
            file = open(cmd[1], "w")
            os.remove(cmd[1])
        elif cmd[0] == "rm-rf":
            os.removedirs(cmd[1])
        elif cmd[0] == "cat":
            a = open(cmd[1], "r")
            b = a.read()
            c = b.split("\n")
            ount = 1
            ont = str(ount) + ":"
            for iver in c:
                print(ont + iver)
                ount = ount + 1
                ont = str(ount) + ":"
        elif cmd[0] == "os":
            o = os.name
            if o == "nt":
                print("windows")
            elif o == "posix":
                print("how are you using this")
        elif cmd[0] == "exit":
            title = """
            Things just really aren't that bad
            I got a nice mom and I got a cool dad
            I just stay in my room too long
            But I finally got a girlfriend and she's the bomb

            (Bye)
            (Hello)
            (Bye)
            """
            print(title)
            main()
        elif cmd[0] == "cd":
            os.chdir(cmd[1])
        elif cmd[0] == "vim":
            sfiles = open("config.json", "r")
            a = json.load(sfiles)
            vim = os.getcwd()
            vim += a["vim"]
            subprocess.run(vim)
        elif cmd[0] == "lp":
            sfiles = open("config.json", "r")
            a = json.load(sfiles)
            lp = os.getcwd()
            lp += a["lp"]
            subprocess.run(lp)
        elif cmd[0] == "miv":
            sfiles = open("config.json", "r")
            a = json.load(sfiles)
            miv = os.getcwd()
            miv += a["miv"]
            subprocess.run(miv)
        elif cmd[0] == "cls":
            os.system("cls")
        elif cmd[0] == "help":
            for he in h:
                print(he)
        elif cmd[0] == "ukmd":
            ver = "0.1"
            print(ver)
        elif cmd[0] == "mkdir":
            os.makedirs(cmd[1])
        elif cmd[0] == "rstclr":
            print(Style.RESET_ALL)
            continue
        elif cmd[0] == "":
            continue
        else:
            print("it is the wrong command")
            continue


def mt():
    ig = input("password[sudo]:")
    n = open("config.json", "r")
    j = json.load(n)
    b = j["pass"]
    c = str(b)
    c = c.encode()
    keys = "Y6jp1k09psK7NBg_HFJ8VOyuDIW3yoEtcUZy1BcuhzE="
    key = keys.encode()
    f = Fernet(key)
    it = f.decrypt(c)
    it = it.decode()
    if ig == it:
        print("ok your getting a promotion in")
        maintain()
    else:
        print("it didn't work")
        sys.exit()


def m():
    i = input("username:")
    ig = input("password:")
    n = open("config.json", "r")
    j = json.load(n)
    keys = "Y6jp1k09psK7NBg_HFJ8VOyuDIW3yoEtcUZy1BcuhzE="
    key = keys.encode()
    f = Fernet(key)
    a = j["name"]
    b = j["pass"]
    c = str(b)
    c = c.encode()
    it = f.decrypt(c)
    it = it.decode()
    if i == a and ig == it:
        print("ok your being logged in")
    else:
        print("it didn't work")
        sys.exit()


def msudo():
    ig = input("password[sudo]:")
    n = open("config.json", "r")
    j = json.load(n)
    b = j["pass"]
    c = str(b)
    c = c.encode()
    keys = "Y6jp1k09psK7NBg_HFJ8VOyuDIW3yoEtcUZy1BcuhzE="
    key = keys.encode()
    f = Fernet(key)
    it = f.decrypt(c)
    it = it.decode()
    if ig == it:
        print("ok your being promoted")
    else:
        print("it didn't work")
        sys.exit()


def main():
    print(pyfiglet.figlet_format("salaam unix"))
    while True:
        pwd = os.getcwd()
        h = (
            "pwd",
            "ls",
            "touch",
            "rm",
            "rm-rf",
            "cat",
            "ukmd",
            "os",
            "exit",
            "cd",
            "vim",
            "cls",
        )
        command = str(input(f"$"))
        cmd = command.split(" ")
        if cmd[0] == "pwd":
            print(pwd)
        elif cmd[0] == "ls":
            ls = os.listdir()
            for iver in ls:
                print(iver)
        elif cmd[0] == "touch":
            file = open(cmd[1], "w")
        elif cmd[0] == "rm":
            os.remove(cmd[1])
        elif cmd[0] == "rm-rf":
            os.removedirs(cmd[1])
        elif cmd[0] == "cat":
            a = open(cmd[1], "r")
            b = a.read()
            c = b.split("\n")
            ount = 1
            ont = str(ount) + ":"
            for iver in c:
                print(ont + iver)
                ount = ount + 1
                ont = str(ount) + ":"
        elif cmd[0] == "os":
            o = os.name
            if o == "nt":
                print("windows")
            elif o == "posix":
                print("how are you using this")
        elif cmd[0] == "exit":
            sys.exit()
        elif cmd[0] == "cd":
            os.chdir(cmd[1])
        elif cmd[0] == "vim":
            sfiles = open("config.json", "r")
            a = json.load(sfiles)
            vim = os.getcwd()
            vim += a["vim"]
            subprocess.run(vim)
        elif cmd[0] == "lp":
            sfiles = open("config.json", "r")
            a = json.load(sfiles)
            lp = os.getcwd()
            lp += a["lp"]
            subprocess.run(lp)
        elif cmd[0] == "miv":
            sfiles = open("config.json", "r")
            a = json.load(sfiles)
            miv = os.getcwd()
            miv += a["miv"]
            subprocess.run(miv)
        elif cmd[0] == "cls":
            os.system("cls")
        elif cmd[0] == "help":
            for he in h:
                print(he)
        elif cmd[0] == "ukmd":
            ver = "0.1"
            print(ver)
        elif cmd[0] == "mkdir":
            os.makedirs(cmd[1])
        elif cmd[0] == "su":
            mt()
        elif cmd[0] == "rstclr":
            print(Style.RESET_ALL)
            continue
        elif cmd[0] == "sudo":
            msudo()
            print("your sudo hooray")
            h = (
                "pwd",
                "ls",
                "touch",
                "rm",
                "rm-rf",
                "cat",
                "ukmd",
                "os",
                "exit",
                "cd",
                "vim",
                "cls",
            )
            command = str(input(f"$$"))
            cmd = command.split(" ")
            if cmd[0] == "pwd":
                print(pwd)
            elif cmd[0] == "ls":
                ls = os.listdir()
                for iver in ls:
                    print(iver)
            elif cmd[0] == "touch":
                file = open(cmd[1], "w")
            elif cmd[0] == "rm":
                os.remove(cmd[1])
            elif cmd[0] == "rm-rf":
                os.removedirs(cmd[1])
            elif cmd[0] == "cat":
                a = open(cmd[1], "r")
                b = a.read()
                c = b.split("\n")
                ount = 1
                ont = str(ount) + ":"
                for iver in c:
                    print(ont + iver)
                    ount = ount + 1
                    ont = str(ount) + ":"
            elif cmd[0] == "os":
                o = os.name
                if o == "nt":
                    print("windows")
                elif o == "posix":
                    print("how are you using this")
            elif cmd[0] == "exit":
                sys.exit()
            elif cmd[0] == "cd":
                os.chdir(cmd[1])
            elif cmd[0] == "vim":
                sfiles = open("config.json", "r")
                a = json.load(sfiles)
                vim = os.getcwd()
                vim += a["vim"]
                subprocess.run(vim)
            elif cmd[0] == "lp":
                sfiles = open("config.json", "r")
                a = json.load(sfiles)
                lp = os.getcwd()
                lp += a["lp"]
                subprocess.run(lp)
            elif cmd[0] == "miv":
                sfiles = open("config.json", "r")
                a = json.load(sfiles)
                miv = os.getcwd()
                miv += a["miv"]
                subprocess.run(miv)
            elif cmd[0] == "cls":
                os.system("cls")
            elif cmd[0] == "help":
                for he in h:
                    print(he)
            elif cmd[0] == "ukmd":
                ver = "0.1"
                print(ver)
            elif cmd[0] == "mkdir":
                os.makedirs(cmd[1])
            elif cmd[0] == "su":
                mt()
            elif cmd[0] == "rstclr":
                print(Style.RESET_ALL)
                continue
            elif cmd[0] == "":
                continue
            else:
                print("it is the wrong command")
                continue
        elif cmd[0] == "":
            continue
        else:
            print("it is the wrong command")
            continue


if __name__ == "__main__":
    m()
    main()
