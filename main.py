import os, sys, subprocess, json, errors


def maintain():
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
        else:
            errors.typee()


def mt():
    ig = input("password[sudo]:")
    f = open("config.json", "r")
    j = json.load(f)
    b = j["pass"]
    if ig == b:
        print("ok your getting a promotion in")
        maintain()
    else:
        print("it didn't work")
        sys.exit()


def m():
    i = input("username:")
    ig = input("password:")
    f = open("config.json", "r")
    j = json.load(f)
    a = j["name"]
    b = j["pass"]
    if i == a and ig == b:
        print("ok your being logged in")
    else:
        print("it didn't work")
        sys.exit()


def msudo():
    ig = input("password:")
    f = open("config.json", "r")
    j = json.load(f)
    b = j["pass"]
    if ig == b:
        print("ok your being promoted")
    else:
        print("it didn't work")
        sys.exit()


def main():
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
        elif cmd[0] == "sudo":
            msudo()

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
            else:
                errors.typee()
        else:
            errors.typee()


if __name__ == "__main__":
    m()
    main()
