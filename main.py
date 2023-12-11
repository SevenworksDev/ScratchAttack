import scratchattach as scratch3
from pick import pick
import random, os, time

banner = """
   ██                    ███
   █████               ██████
   ████████    ██████████████              ████████                                                    ████
   ██████████████████████████              ███   ██                                  ████              ████
    ███████████████████████████            ███       ████████ ████████ █████████  ███████   ████████   ████████
    █████████████████████████████          ████████  ██       ███             ██    ███     ██         ███  ███
    ██████████████████████████████              ███  ██       ███      █████████    ███     ██         ███  ███
  █████████████████████████████████        ██   ███  ██    ██ ███      ███   ███    ███     ██     ██  ███  ███
 ███████████████████████████████████       ████████  ████████ ███      █████████    █████   █████████  ███  ███
 ███████████████████████████████████
███████████████████████████████████████
█████████████████████████████████████████         █████      ███     ████                       ████
█████████████████████████████████████████        ███████   ████████ ███████ █████████  ████████ ████  █████
 ████████████████████████████████████████       ██     ███   ███     ███          ███  ██       ████████
  ██████████████████████████████████████       ███     ███   ███     ███    █████████  ██       ██████
   ████████████████████████████████████        ████████████  ███     ███    ██    ███  ██       ████████
     █████████████████████████████████        ████     ████  ██████  ██████ █████████  ████████ ████  █████
       ████████████████████████████
           ████████████████████
Version v0.0.1 - Made by: sevenworks.eu.org
"""

print(banner)
time.sleep(2)
if os.name == 'nt':
    os.system('cls')
else:
    os.system('clear')

try:
    with open("accounts.txt", "r") as file:
        accounts = [line.strip().split(" / ") for line in file]
except:
    input("accounts.txt does not exist.")

tools = ["Project Comment Spammer", "Profile Comment Spammer", "Studio Comment Spammer", "Profile Followbot", "Studio Followbot", "Project Love Bot", "Project Favorite Bot", "Project Share Bot"]
tool, _ = pick(tools, "Choose a tool: ")
comment = input("Comment: ")

if tool == str("Project Comment Spammer"):
    projectid = input("Project ID: ")
    while True:
        username, password = random.choice(accounts)
        session = scratch3.login(username, password)
        project = session.connect_project(projectid)
        project.post_comment(comment)
        print(f"Commented as {username}!")
elif tool == str("Profile Comment Spammer"):
    un = input("Username: ")
    while True:
        username, password = random.choice(accounts)
        session = scratch3.login(username, password)
        user = session.connect_user(un)
        user.post_comment(comment)
        print(f"Commented as {username}!")
elif tool == str("Studio Comment Spammer"):
    studioid = input("Studio ID: ")
    while True:
        username, password = random.choice(accounts)
        session = scratch3.login(username, password)
        studio = session.connect_studio(studioid)
        studio.post_comment(content=comment)
        print(f"Commented as {username}!")
elif tool == str("Profile Followbot"):
    un = input("Username: ")
    while True:
        username, password = random.choice(accounts)
        session = scratch3.login(username, password)
        user = session.connect_user(un)
        user.follow()
        print(f"Followed as {username}!")
elif tool == str("Studio Followbot"):
    studioid = input("Studio ID: ")
    while True:
        username, password = random.choice(accounts)
        session = scratch3.login(username, password)
        studio = session.connect_studio(studioid)
        studio.follow()
        print(f"Followed as {username}!")
elif tool == str("Project Love Bot"):
    projectid = input("Project ID: ")
    while True:
        username, password = random.choice(accounts)
        session = scratch3.login(username, password)
        project = session.connect_project(projectid)
        project.love()
        print(f"Loved as {username}!")
elif tool == str("Project Favorite Bot"):
    projectid = input("Project ID: ")
    while True:
        username, password = random.choice(accounts)
        session = scratch3.login(username, password)
        project = session.connect_project(projectid)
        project.favorite()
        print(f"Favorited as {username}!")
elif tool == str("Project Share Bot"):
    projectid = input("Project ID: ")
    while True:
        username, password = random.choice(accounts)
        session = scratch3.login(username, password)
        project = session.connect_project(projectid)
        project.share()
        print(f"Shared as {username}!")
else:
    print("XD LMAO")

input()
