from datetime import date
tasks=[]
today=date.today()
def show_menu():
    print("***TO DO LIST***")
    print(today)
    print("Would you like to")
    print("1.Add a task")
    print("2.View tasks")
    print("3.Delete tasks")
    print("4.Exit")
def add_task(tasks):
    task=input("Enter new task: ")
    tasks.append(task)
    print("Task has been successfully added!")
def view_tasks(tasks):
    if len(tasks)==0:
        print("Sorry no tasks yet")
    else:
        i=1
        while i<=len(tasks):
            print(str(i)+"."+tasks[i-1])
            i+=1
def delete_task(tasks):
    view_tasks(tasks)
    if len(tasks)==0:
        return
    num=int(input("Enter the number of the task you want to delete: "))
    if num>0 and num<=len(tasks):
        tasks.pop(num-1)
        print("Task has been deleted successfully")
    else:
        print("The number you have entered is not valid.")
        print("please try again!")
        num=int(input("Enter the number of the task you want to delete"))
        
while True:
    show_menu()
    c=input("Choose an option:")
    if c=="1":
        add_task(tasks)
    elif c=="2":
        view_tasks(tasks)
    elif c=="3":
        delete_task(tasks)
    elif c=="4":
        print("Enjoy your break:)")
    else:
        print("please choose a number from 1 to 4!")
    
    
            
    
  
    