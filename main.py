import scratchattach as scratch3
import random

with open("accounts.txt", "r") as file:
    accounts = [line.strip().split(" / ") for line in file]

print("Scratch Bot - By: sevenworks.eu.org")
projectid = input("Project ID: ")
comment = input("Comment: ")

while True:
    username, password = random.choice(accounts)
    session = scratch3.login(username, password)
    project = session.connect_project(projectid)
    project.post_comment(comment)
    print(f"Commented as {username}!")
