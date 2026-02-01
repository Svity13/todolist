import json


def markDone():
    listTask()
    task_num = int(input("Which task you wanna mark done"))

    with open("data.json") as f:
            data = json.load(f)

    data["tasks"][task_num - 1]["done"] = True

    with open("data.json", "w") as f:
                   json.dump(data, f)
    print("Task was completed. Good Job!")


def listTask():
    with open("data.json") as f:
        data = json.load(f)
        for i, task in enumerate(data["tasks"], 1):
                   if task["done"] == True:
                        status = "✓" 
                   else:
                        status = " "
                   print(f"{i}. [{status}] {task['text']}")



def saveToJson():

    while True:
        task = input("Please input your task:\nInput 'stop' if you wanna choose another option: ")
        if task == "stop":
            break
        else:
            try:
                #loads data.json file with the tasks to prevent from creating a new file everytime
                with open("data.json") as f:
                    data = json.load(f)
            except FileNotFoundError:
                data = {"tasks": []}
            data["tasks"].append({"text": task, "done": False})

            with open("data.json", "w") as f:
                json.dump(data, f)
            print("Task added!")

def deleteTask():
    while True:
        listTask()
        task = int(input("Please input the tasks you want to remove:\nInput -1 if you wanna choose another option: "))
        if task == -1:
            break
        else:
            with open("data.json") as f:
                data = json.load(f)
                
            removeTask = data["tasks"].pop(task - 1)


            with open("data.json", "w") as f:
                json.dump(data,f)

            print(f"Removed task {removeTask['text']}")

def mainMenu():
    while True:
        option = int(input("What would you like to do\n1. Add a task \n2. View tasks \n3. Mark a task done \n4. Delete a task\n5.Input 0 if you wanna quit the app\n"))
        if option == 0:
            break
        elif option == 1:
            saveToJson()
        elif option == 2:
            listTask()
        elif option == 3:
            markDone()
        elif option == 4:
            deleteTask()

mainMenu()
