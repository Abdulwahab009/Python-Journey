import random

print("welcome to the rock paper scissor Game")
User_Choice = input("Rock papper or scissor")
if User_Choice != "rock" and User_Choice != "papper" and User_Choice != "scissor":
    print("wrong word please enter again")

Computer_Choice = random.choice("rock","papper","scissor")

if User_Choice == "rock" and Computer_Choice == "papper":
    print("You Lose")
if User_Choice == "papper" and Computer_Choice == "scissor":
    print("You Lose")
if User_Choice == "scissor" and Computer_Choice == "rock":
    print("You Lose")
if User_Choice == "scissor" and Computer_Choice == "papper":
    print("You Win")
if User_Choice == "rock" and Computer_Choice == "scissor":
    print("You win")
if User_Choice == "papper" and Computer_Choice == "rock":
    print("You Win")
if User_Choice == Computer_Choice:
    print("its draw")


