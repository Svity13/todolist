import json

def saveToJson():
    tasks = input("Please input your tasks:")
    data = {"Task": tasks}
    with open("data.json", "w") as f:
        json.dump(data, f)
    print("Saved to json file")

saveToJson()
