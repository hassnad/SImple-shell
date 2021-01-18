import os

def main():
    while True:
        command = input("$ ")
        inputList = command.split()
        if inputList[0] == "exit":
            exit()
        else:
            execute_command(inputList)

def execute_command(inputList):
    command = inputList[0]
    argList = []
    if len(inputList) > 1:
        for x in inputList[1:]:
            argList.append(x) 
    #print(command, argList)

    if command == "echo":
        echo(argList)
    elif command == "pwd":
        pass
    elif command == "ls":
        pass
    elif command == "cd":
        pass        
    elif command == "man":
        pass
    elif command == "cat":
        pass
    elif command == "head":
        pass
    elif command == "tail":
        pass
    elif command == "touch":
        pass
    elif command == "rm":
        pass
    elif command == "cp":
        pass
    elif command == "mv":
        pass
    elif command == "help":
        pass
    elif command == "exit":
        pass
    else:
        print("Command not found, try \"help\"")

def echo(string):
    print(" ".join(string))

def man(command):
    if command == "echo":
        pass
    elif command == "pwd":
        pass
    elif command == "ls":
        pass
    elif command == "cd":
        pass        
    elif command == "man":
        pass
    elif command == "cat":
        pass
    elif command == "head":
        pass
    elif command == "tail":
        pass
    elif command == "touch":
        pass
    elif command == "rm":
        pass
    elif command == "cp":
        pass
    elif command == "mv":
        pass


main()