import json


def listTask():
    with open("data.json") as data_file:
        data = json.load(data_file)
        for task in data["tasks"]:
            print(task)



def saveToJson():
    task = input("Please input your tasks:")
    
    try:
        #loads data.json file with the tasks to prevent from creating a new file everytime
        with open("data.json") as f:
            data = json.load(f)
    except FileNotFoundError:
        data = {"tasks": []}

    data["tasks"].append(task)

    with open("data.json", "w") as f:
        json.dump(data, f)
    print("Saved to json file")
saveToJson()
listTask()
