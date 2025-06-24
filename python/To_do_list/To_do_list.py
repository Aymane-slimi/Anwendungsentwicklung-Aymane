not_done={}
done={}
progress={}






def Introduction():
    print(" Hello to your to do list ".center(100,"#"))
    print("1-Show lists \n 2-Add a task \n 3-Update task \n 4-Delete task \n 5-Exit")
    select1=int(input("type what you want (note:just the number): "))
    if select1 in [1,2,3,4,5]:
        if select1 == 1:
            show()
        elif select1==2:
            add()
        elif select1==3:
            update()
        elif select1==4:
            delete()
        elif select1==5:
            print("Exiting to-do list...")
    else:
        print("Invalid value")
        return
def show():
    global not_done,done,progress
    print(f"Not done tasks:{not_done}")
    print(f"Tasks in progress:{progress}")
    print(f"Done tasks:{done}")
def add():
    global not_done,done,progress
    print("1-Not done \n 2-Progress \n 3-Done")
    status=input("What Statue of your task(note:just the number)")
    if status in ["1","2","3"]:
        Task=input("Enter the task :")
        progress0=input("Enter your progress without %: ")
        if status =="1":
            not_done[Task]=progress0+"%"
        if status =="2":
            progress[Task]=progress0+"%"
        if status =="3":
            done[Task]=progress0+"%"
    else:
        print("Invalid value")
        return
def update():
    global not_done,done,progress
    y_n=input("You want to transfer the task? (yes/no)")
    if y_n =="yes":
        show()
        task=input("Enter name of task:")
        dic=input("where you want to transfer it(choose only number): 1-Not done     2- In progress       3- Done")
        if dic in ["1","2","3"]:
            new_progress=input("What is your new value in progress (note: type it without %)")
            if dic =="1":
                if task in progress:
                    not_done[task] = progress.pop(task)
                elif task in done:
                    not_done[task] = done.pop(task)
                not_done[task]=new_progress+"%"
            if dic =="2":
                if task in not_done:
                    progress[task] = not_done.pop(task)
                elif task in done:
                    progress[task] = done.pop(task)
                progress[task]=new_progress+"%"
            if dic =="3":
                if task in progress:
                    done[task] = progress.pop(task) 
                elif task in not_done:
                    done[task] = not_done.pop(task) 
                done[task]=new_progress+"%"
    if y_n =="no":
        task=input("Enter name of task:")
        new_progress=input("What is your new value in progress (note: type it without %)")
        if task in not_done:
            not_done[task]=new_progress+"%"
        elif task in progress:
            progress[task]=new_progress+"%"
        elif task in done:
            done[task]=new_progress+"%"
        else:
            print("Your task is not in the options")
            return
def delete():
    global not_done,done,progress
    name=input("Enter the name of task you want to delete")
    if name in done:
        del done[name]
    elif name in progress:
        del progress[name]
    elif name in not_done:
        del not_done[name]
    else:
        print("Invalid value")
        return
while True:
    Introduction()
    input("Press any charachter to continue")


