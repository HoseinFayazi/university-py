#from os import truncate
import webbrowser


action = input("select an action first>>[add,list,edit,delete,history,exit,help] :: ")
prog_run = True

students = list()

webadd = open("students-list.html","w")
webt = '''
    <style>
    .parent {
        width: 95%;
        height: 80px;
        padding: 0px;
        box-shadow: 0 0 5px 5px rgba(240, 240, 240, 0.842);
        margin: 20px auto;
    }
    
    .parent>div {
        width: 100%;
        text-align: center;
    }
    
    .parent span,
    .parent h4 {
        display: inline-block;
        margin: 0;
        height: 100%;
        padding: 5px;
        text-align: center;
        width: 20%;
    }
    
    .parent-head {
        background-color: black;
        color: white;
        height: 30px;
    }
    
    .parent-body {
        color: rgb(77, 70, 70);
        padding-top: 6px;
        height: 50px;
    }
    
    h2 {
        font-family: tahoma;
        text-align: center;
    }
    </style>
    
    <h2>history of student's(create by:<a href="http://hoseinfayazi.ir">hosein fayazi</a>)</h2>

'''
webadd.write(webt)
webadd.close()

def student_add_to_file(file,student):
    f = open(file,"a")
    web = open("students-list.html","a")
    code = student['code']
    name = student['name']
    lastname = student['lastname']
    age = student['age']
    webstr = '''    
    
    <div class="parent">
        <div class="parent-head">
            <h4>code</h4>
            <h4>name</h4>
            <h4>lastname</h4>
            <h4>age</h4>
        </div>
        <div class="parent-body">
            <span>'''+code+'''</span>
            <span>'''+name+'''</span>
            <span>'''+lastname+'''</span>
            <span>'''+age+'''</span>
        </div>
    </div>
     '''
    

    web.write(webstr)
    web.close()


    txt = "\n"
    for key in student.keys():
        txt += key + " : " + student[key] + "\n" 
    f.write(txt)
    f.write("-"*20+"\n")
    f.close()

def stu_code_exist(code):
    for stu in students:
        if stu.get("code",0) == code:
            return True
            break


while prog_run:
    def title(val):
        print(" "*40,"\n")
        print("*"*30)
        print(" "*10,val)
        print("*"*30)
        print(" "*40)

    if (action == "help"):
        title("help")
        print("add"," => ","command add is for create a new studend...")
        print("list"," => ","command list is for showing studens list...")
        print("edit"," => ","command edit is for edit a studend...")
        print("history"," => ","history of students that you create until now")
        print("delete"," => ","command delete is for delete a studend...")
        print("exit"," => ","for ending program")

    elif (action == "add"):
        title("add")
        name = input("please enter studen's name : ")
        lastname = input("please enter student's lastname : ")
        age = input("please enter student's age : ")
        code = input("please enter student's code : ")
        while stu_code_exist(code):
            if stu_code_exist(code):
                code = input("the code exists...try another code please ::")
        student = {
            "name":name,
            "lastname":lastname,
            "age":age,
            "code":code
        }
        students.append(student)
        student_add_to_file("students-list.txt",student)

    elif (action == "list"):
        title("list")
        for s in students:
            for key,val in list(s.items()):
                print(key," : ",val)
            print("-"*30)

    elif (action == "delete"):
        title("delete")
        code = input("please enter the student's code you want to delete : ")
        count = 0
        for s in students:
            if code == s['code']:
                print("are you sure you wnat to delete ",s['name']," ",s['lastname'],"??!!!!!!")
                ayousure = input("[y,n] :: ")
                if ayousure == "y":
                    del students[count]
                break
            count = count + 1

    elif (action == "edit"):
        title("edit")
        code = input("please enter the student's code you want to edit : ")
        count = 0
        for s in students:
            if code == s['code']:
                print("which field you want to edit>>[name,lastname,age]")
                field = input("the field >>> ")
                if field in s:
                    s[field] = input("please enter new value you want :")
                    print("ok...we change the value to",s[field])
                else :
                    print("please enter a valid field name...")
                break
            count = count + 1

    elif (action == "history"):
        title("history")
        f = open("students-list.txt")
        ftxt =f.read()
        webbrowser.open('students-list.html', new=2)
        print(ftxt)

    elif (action == "exit") :
        print("done....")
        prog_run = False
        break

    else :
        print("please enter a vlid command...")

    print("\n")
    action = input("select an action first>>[add,list,edit,delete,exit,help] :: ")
