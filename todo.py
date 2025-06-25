FILE="todo.txt"
def File():
    try:
        with open(FILE,'r')as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError as e:
        return []
def Save_task(task):
    with open(FILE,'w') as file:
        for tasks in task:
            file.write(tasks+"\n")
def ViewTask(task):
    if not task:
        print("Tasks not found!.")
    else:
        print("___Your tasks___")
        for i,t in enumerate(task,1):
            print(f"{i}.{t}")
        print()
def AddTask(task):
    t=input("Enter your task:\n")
    if t:
        task.append(t)
        Save_task(task)
        print("Task added successfully.")
def RemoveTask(task):
    ViewTask(task)
    try:
        i=int(input("Enter the task number for removing:"))
        if(i>=1 & i<=len(task)):
            task=task.pop(i-1)
            Save_task(task)
            print("Task removed successfully.")
    except ValueError as e:
        print(f"ERROR:{e}")
ch=0
try:
    task=File()
    while ch!=4:
        print("Show Menu\n1.Add task\n2.Remove task\n3.View task\n4.Exit")
        ch=int(input("Enter your choice:"))
        if ch==1:
            AddTask(task)
        elif ch==2:
            RemoveTask(task)
        elif ch==3:
            ViewTask(task)
        else:
            print("Invaild option")
except Exception as e:
    print(f"ERROR:{e}")
else:
    print("__Thank you__")  