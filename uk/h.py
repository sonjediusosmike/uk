import os
import sys
import subprocess
import json
import pyfiglet
from colorama import Style
from cryptography.fernet import Fernet


COMMANDS = [
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
    "help",
    "mkdir",
    "rstclr",
    "su",
    "sudo",
]


def maintain():
    print("your sudo")
    while True:
        pwd = os.getcwd()
        command = input(f"{pwd}$ ").strip()
        cmd = command.split()

        if not cmd:
            continue

        cmd_action = cmd[0]
        cmd_args = cmd[1:] if len(cmd) > 1 else []

        if cmd_action in COMMANDS:
            globals()[f"cmd_{cmd_action}"](cmd_args, pwd)
        else:
            print("it is the wrong command")


def cmd_pwd(args, pwd):
    print(pwd)


def cmd_ls(args, pwd):
    for item in os.listdir():
        print(item)


def cmd_touch(args, pwd):
    with open(args[0], "w"):
        pass


def cmd_rm(args, pwd):
    os.remove(args[0])


def cmd_rm_rf(args, pwd):
    os.removedirs(args[0])


def cmd_cat(args, pwd):
    with open(args[0], "r") as file:
        for count, line in enumerate(file, 1):
            print(f"{count}: {line}", end="")


def cmd_ukmd(args, pwd):
    print("0.1")


def cmd_os(args, pwd):
    print("windows" if os.name == "nt" else "how are you using this")


def cmd_exit(args, pwd):
    sys.exit()


def cmd_cd(args, pwd):
    os.chdir(args[0])


def cmd_vim(args, pwd):
    run_subprocess_command("vim")


def cmd_miv(args, pwd):
    run_subprocess_command("miv")


def cmd_lp(args, pwd):
    run_subprocess_command("lp")


def cmd_cls(args, pwd):
    os.system("cls")


def cmd_help(args, pwd):
    for cmd in COMMANDS:
        print(cmd)


def cmd_mkdir(args, pwd):
    os.makedirs(args[0])


def cmd_rstclr(args, pwd):
    print(Style.RESET_ALL)


def cmd_su(args, pwd):
    if validate_password("password[sudo]:"):
        print("ok you're getting a promotion in")
        maintain()
    else:
        print("it didn't work")
        sys.exit()


def cmd_sudo(args, pwd):
    if validate_password("password:"):
        print("ok you're being promoted")
        maintain()
    else:
        print("it didn't work")
        sys.exit()


def run_subprocess_command(command_key):
    try:
        with open("config.json", "r") as sfile:
            config = json.load(sfile)
        command = os.path.join(os.getcwd(), config[command_key].lstrip("\\"))
        print(f"Running command: {command}")  # Debug statement
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        print(result.stdout)
        print(result.stderr)  # Capture and print any errors
    except KeyError:
        print(f"No configuration found for command: {command_key}")
    except Exception as e:
        print(f"Failed to run command: {e}")


def validate_password(prompt):
    password = input(prompt)
    with open("config.json", "r") as f:
        config = json.load(f)
    encrypted_pass = config["pass"].encode()
    key = "Y6jp1k09psK7NBg_HFJ8VOyuDIW3yoEtcUZy1BcuhzE=".encode()
    decrypted_pass = Fernet(key).decrypt(encrypted_pass).decode()
    return password == decrypted_pass


def m():
    username = input("username:").strip()
    password = input("password:").strip()
    if validate_password_from_file(username, password):
        print("ok you're being logged in")
    else:
        print("it didn't work")
        sys.exit()


def validate_password_from_file(username, password):
    with open("config.json", "r") as f:
        config = json.load(f)
    key = "Y6jp1k09psK7NBg_HFJ8VOyuDIW3yoEtcUZy1BcuhzE=".encode()
    decrypted_pass = Fernet(key).decrypt(config["pass"].encode()).decode()
    return username == config["name"] and password == decrypted_pass


def main():
    print(pyfiglet.figlet_format("salaam unix"))
    while True:
        maintain()


if __name__ == "__main__":
    m()
    main()
