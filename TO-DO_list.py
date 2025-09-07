total_task=[]
print("Welcome to TO-DO Task Manager")
contine_not='yes'
while(contine_not.lower()=='yes'):
    print("Enter the Number to Perform the Following")
    print("1.Add task \n2.View Task \n3.Mark Task as Complete \n4.Delete Task \n5.Exit")
    option=int(input())
    if option==1:
        count=int(input("How Many Task Do you Want to Add :"))
        for i in range (count):
            task=input(f"Enter the {i+1} Task :")
            total_task.append(task)
        print("Task's are Added Successfully !")
    elif option==2:
        if not total_task:
            print("No Task Where Added ")
        else:
            for i,value in enumerate(total_task):
                print(f"{i}.{value}")
                
    elif option==3:
        task_no=int(input("Enter Task Number to Mark as Completed"))
        size=len(total_task)
        if not total_task:
            print("No Tasks were Added !")
        else:
            if(task_no>size or task_no<1):
                print("Task Number Was Not Execeeds !")
            else:
                if '- Completed' not in total_task[task_no-1]:
                    mark='- Completed'
                    total_task[task_no-1]+=mark
                else:
                    print("Task is Already Completed!")
                print("Task Marked as Completed Successfully!")
    elif option==4:
        task_no=int(input("Enter Task No to Delete :"))
        size=len(total_task)
        if not total_task:
            print("Task were Not Added !!")
        else:
            if(task_no>size or task_no<1):
                print("Task Number Was Not Execeeds !")
            else:
                del total_task[task_no-1]
                print("Task was Deleted Successfully!")
    elif option==5:
        print("Tansks for Visiting ")
        exit(1)
    else:
        print("Please Enter Mentioned Numbers to Perform :")
    contine_not=input("Do you Want to Continue (Yes or No) :")
print("Thanks for Visiting !!!")


        
