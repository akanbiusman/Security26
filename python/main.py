help_inp = input("Press 'help' to get a list of car operations: ")
print("Below are some commands")
print("-"*len("Below are some commands"))
print("start - to start the car")
print("stop - to stop the car")
print("quit - to exit")

while help_inp.lower() == 'help':
    cmd_now = input(">").lower().strip()
    
    if cmd_now == "start":
        print("Car started...Ready to go!")
    elif cmd_now == "stop":
        print("Car stopped")
    elif cmd_now == "quit":
        break
    else:
        print("I don't understand that...")




# secret_number = 9
# guess_count = 0
# guess_limit = 3

# while guess_count < guess_limit:
#     guess = int(input("Guess: "))
#     guess_count += 1
    
#     if guess == secret_number:
#         print("You won!")
#         break

# else:
#     print("Sorry, You failed!")



# print("Weight Converter")
# print("-"*len("Weight Converter"))

# user_weight = int(input("Weight: "))

# user_unit = str(input("(L)bs or (K)g: "))

# if user_unit.lower() == "l":
#     print(f"{user_weight * 0.45}pounds")
# elif user_unit.lower() == "k":
#     print(f"{user_weight/0.45}kilos")
# else:
#     print("you didn't pick the right choice of unit!")