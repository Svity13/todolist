import json
option = input("What would you like to do\n1. Add a task \n2. View tasks \n3. Mark a task done \n")
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
    task = input("Please input your tasks:")
    
    try:
        #loads data.json file with the tasks to prevent from creating a new file everytime
        with open("data.json") as f:
            data = json.load(f)
    except FileNotFoundError:
        data = {"tasks": []}

    data["tasks"].append({"text": task, "done": False})

    with open("data.json", "w") as f:
        json.dump(data, f)
    print("Saved to json file")
