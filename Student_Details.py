#Program for Student Detail Management
stud={}
print("Welcome to Student Details Management !!")
cont='yes'
while(cont.lower()=='yes'):
    print("Enter What You Want to Do")
    print("1.Add \n2.View \n3.Update \n4.Delete \n5.Exit")
    try:
        option=int(input())   
        if(option==1):
            try:
                name=input("Enter the Name of the Student :")
                roll=input("Enter the Roll Number of the Student :")
                age=int(input("Enter the Age of the Student :"))  
                size=len(stud)
                size+=1
                stud[f"Student {size}"]={"Name":name,"Roll No":roll,"Age":age}
                print("Student Details was Added Succesfully!")
            except ValueError as e:
                print("Error Occured :",e,"\nPlease Enter the Valid Data!!")
        elif(option==2):
            if not stud:
                print("No Students Datas!!!")
            else:
                try:
                    view=int(input("Do you Want to View All Students Details or Particular Student Details \n(1.All Students \n2.Particular Student)"))
                    if(view==1):
                        for n,detail in stud.items():
                            print(n," Details")
                            for data,value in detail.items():
                                print(f"{data}:{value}")
                    elif(view==2):
                        try:
                            stu=int(input("Enter the Particular Student No"))
                            which=f"Student {stu}"                        
                            if which in stud:
                                for data,value in stud[which].items():                                           
                                    print(which,' Details')
                                    print(f"{data} : {value}")
                            else:
                                print("Student Number was not Found!!")
                        except ValueError as e:
                            print("Error Occured :",e,"\nPlease Enter the Number")
                    else:
                        print("Please Enter 1 or 2")
                except ValueError as e:
                    print("Error Occured :",e,"\nPlease Enter the Valid Number")
        elif(option==3):
            try:
                stu=int(input("Enter the Student Number to Update"))        
                which=f"Student {stu}"
                if which in stud:
                    try:
                        update=input("Enter What You Want to Update (Name of the Student , Age of the Studnet , Roll Number of the Student)\nYou Can also Enter the Number to Update\n1.Name\n2.Age\n3.Roll No")
                        if update.lower()=='name':
                            try:
                                name=input("Enter the Name You Want to Change ")                
                                stud[which]['Name']=name
                                print(f"Name of the Student {stu} was Updated Successfully!!")
                            except ValueError as e:
                                print("Error Occured :",e,"\nPlease Enter the Valid Name ")
                        elif update.lower()=='age' or update==2:
                            try:
                                age=int(input("Enter the Age You Want to Change"))
                                stud[which]['Age']=age 
                                print(f"Age of the Student {stu} was Updated Successfully!!")
                            except ValueError as e:
                                print("Error Occured :",e,"\nPlease Enter the Valid Age")    
                        elif update.lower().replace(" ","")=='rollno' or update==3:
                            try:
                                roll=int(input("Enter the Roll Number do You want to Change"))
                                stud[which]['Roll No']=roll
                                print(f"Roll Number of the Student {stu} was Updated Successfully!!")
                            except ValueError as e:
                                print("Error Occured :",e,"\nPlease Enter the Valid Roll Number")
                        else:
                            print("Student Number was Not Found !!")
                    except ValueError as e:
                        print("Error Occured :",e,"\nPlease Enter the Valid Option to Update!")
            except ValueError as e:
                print("Error Occured :",e,"\nPlease Enter the Students Valid Number")                            
        elif option==4:
            try:
                stu=int(input("Enter the Student Number to Delete :"))        
                which=f"Student {stu}"  
                if which in stud:
                    del stud[which]
                    print("Deleted Successfully!")
                else:
                    print("Student Number Was not Found!!")
            except ValueError as e:
                print("Error Occured :",e,"\nPlease Enter the Valid Student Number!")
        elif option==5:
            print("Thanks for Visiting !!!")
            break                 
        else:
            print("Please Enter the Valid Number!!")
        cont=input("Do You want to Continue (Yes or No) :")
    except ValueError as e:
        print("Error Occured :",e,"\nPlease Enter the Valid Data!")