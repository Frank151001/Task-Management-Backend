import requests

URL = "http://127.0.0.1:5000/tasks"

def create_task(summary, description):
    new_task = {
        "summary": summary,
        "description": description
    }
    response = requests.post(URL,json=new_task)
    if response.status_code == 201:
        print("Task successfully created!")
    else:
        print("something went wriong while trying to create task")

if __name__ == "__main__":
    print("-------------------------")
    create_task("test my service", "Validate that the system works")