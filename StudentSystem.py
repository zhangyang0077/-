import os
filename = 'student.txt'
def main():
    while True:
        menu()
        choice=int(input('请选择'))
        if choice in [0,1,2,3,4,5,6,7]:
            if choice ==0:
                answer=input('您确定要退出系统吗？y/n\n')
                if answer=='y' or answer=='Y':
                    print('谢谢使用！！！')
                    break #退出系统
                else:
                    continue
            elif choice ==1:
                insert()    #录入学生信息
            elif choice==2:
                search()    #查找学生信息
            elif choice==3:
                delete()    #删除学生信息
            elif choice ==4:
                modify()    #修改学生信息
            elif choice==5:
                sort()      #对学生成绩进行自定义排序
            elif choice==6:
                total()     #统计学生总数
            elif choice==7:
                show()      #显示所有学生信息

#管理系统主界面
def menu():
    print('===================学生信息管理系统==============')
    print('--------------------功能菜单--------------------')
    print('\t\t\t\t\t1.录入学生信息')
    print('\t\t\t\t\t2.查找学生信息')
    print('\t\t\t\t\t3.删除学生信息')
    print('\t\t\t\t\t4.修改学生信息')
    print('\t\t\t\t\t5.排序')
    print('\t\t\t\t\t6.统计学生总人数')
    print('\t\t\t\t\t7.显示所有学生信息')
    print('\t\t\t\t\t0.退出')
    print('=================================================')

def insert():
    student_List=[]
    while True:
        id = input('请输入学生ID（如1001）：')
        if not id:
            break
        name=input('请输入姓名：')
        if not name:
            break
        try:
            english = int(input('请输入英语成绩：'))
            python = int(input('请输入python成绩：'))
            java = int(input('请输入java成绩：'))
        except:
            print('输入无效，不是整数类型，请重新输入')
            continue
        #将录入的学生信息保存到字典中
        student ={'id': id, 'name': name, 'english': english, 'python': python, 'java': java}
        #将单个学生信息添加到列表中
        student_List.append(student)
        answer = input('是否继续添加？y/n\n')
        if answer == 'y':
            continue
        else:
            break
    save(student_List)
    print('学生信息保存完毕！！！')

def save(lst):
    try:
        stu_txt=open(filename, 'a', encoding='utf-8')
    except:
        stu_txt=open(filename, 'w',encoding='utf-8')
    for item in lst:
        stu_txt.write(str(item)+'\n')
    stu_txt.close()
def search():
    student_query=[]
    while True:
        id = ''
        name = ''
        if os.path.exists(filename):
            while True:
                mode=input('按ID查找请输入1，按姓名查找请输入2：')
                if mode=='1':
                    id = input('请输入学生ID：')
                    break
                elif mode=='2':
                    name= input('请输入学生姓名：')
                    break
                else:
                    print('输入有误，请重新输入！\n')
            with open(filename,'r',encoding='utf-8')as rfile:#读入文件信息到student中
                student = rfile.readlines()
                flag=False
                for item in student:
                    d=dict(eval(item))
                    if id!='':          #进行ID查找
                        if d['id']==id:
                            student_query.append(d)
                            show_student(student_query)  #显示查找学生信息
                            flag=True

                    if name!='':
                        if d['name']==name: #进行姓名查找
                            student_query.append(d)      #显示查找学生信息
                            show_student(student_query)
                            flag=True
                if not flag:
                    print('为查找到该学生！')
        else:
            print('未找到学生信息！')
            return
        answer=input('是否继续查询y/n：\n')
        student_query.clear()
        if answer=='y':
            continue
        else:
            break

def show_student(lst):    #显示lst中学生信息
    if len(lst)==0:
        print('没有查询到学生信息！')
        return
    for item in lst:
        #定义学生信息显示格式
        format_title='{:^6}\t{:^12}\t{:^8}\t{:^10}\t{:^10}\t{:^8}'
        print(format_title.format('Id','姓名','英语成绩','python成绩','java成绩','总成绩'))
        format_data='{:^6}\t{:^12}\t{:^8}\t{:^10}\t{:^10}\t{:^8}'
        print(format_data.format(item['id'],item['name'],item['english'],item['python'],item['java'],int(item['english']+item['python']+item['java'])))


def delete():
    while True:
        student_id = input('请输入要删除学生的ID：')
        if student_id !='':
            if os.path.exists(filename):
                with open(filename,'r',encoding='utf-8')as file:
                    student_old=file.readlines()
            else:
                student_old=[]
            flag=False
            if student_old:
                with open(filename,'w',encoding='utf-8')as wfile:
                    d={}
                    for item in student_old:
                        d=dict(eval(item))
                        if d['id']!=student_id:   #不是要删除信息，则写入文件
                            wfile.write(str(d)+'\n')
                        else:                     #是要删除信息，则不写入文件
                            flag=True
                    if flag:
                        print(f'id为{student_id}的学生信息已被删除')
                    else:
                        print(f'未找到id为{student_id}的学生信息！！！')
            else:
                print('无任何学生信息！！！')
                break
            show()
            c=input('是否继续删除？y/n')
            if c=='y'or c=='Y':
                continue
            else:
                break
def modify():
    student_id=input('请输入学生id：')
    if os.path.exists(filename):
        with open(filename,'r',encoding='utf-8')as file:
            student_old=file.readlines()
        with open(filename,'w',encoding='utf-8')as wfile:
            d={}
            flag = False  #判断是否找到要修改的学生
            for item in student_old:
                d=dict(eval(item))
                if d['id']==student_id:
                    flag=True
                    print('已找到该学生信息，可以开始修改！\n')
                    while True:
                        try:
                            d['name']=input('请输入学生姓名：')
                            d['english'] = int(input('请输入学生英语成绩：'))
                            d['python']=int(input('请输入学生python成绩：'))
                            d['java'] = int(input('请输入学生java成绩：'))
                        except:  #若输入错误，则要求重新输入
                            print('输入有误，请重新输入')
                            continue
                        break
                    wfile.write(str(d)+'\n')   #写入修改后信息
                    print('修改信息成功!')
                else:
                    wfile.write(str(d)+'\n')   #写入不修改学生信息
            if not flag :
                print('该学生信息不存在！')

    else:
        return
    answer=input('是否继续修改？y/n\n')
    if answer=='y'or answer=='Y':
        modify()
    else:
        return




def sort():
    stu_list=[]
    show()
    if os.path.exists(filename):
        with open(filename,'r',encoding='utf-8')as rfile:
            students=rfile.readlines()
            if students:
                for item in students:
                    stu_list.append(eval(item))
                while True:
                    choice=input('选择升序还是降序（0/1）：')
                    flag=False
                    if choice=='0':
                        flag=False
                        break
                    elif choice=='1':
                        flag=True
                        break
                    else:
                        print('输入错误，请重新输入！')
                        continue
                choice2=input('选择排序依据（1、英语成绩 2、python成绩 3、java成绩 4、总成绩）：')
                if choice2=='1':
                    stu_list.sort(key=lambda x: int(x['english']),reverse=flag)
                elif choice2=='2':
                    stu_list.sort(key=lambda x: int(x['python']),reverse=flag)
                elif choice2 == '3':
                    stu_list.sort(key=lambda x: int(x['java']), reverse=flag)
                elif choice2=='4':
                    stu_list.sort(key=lambda x: int(x['english']+x['python']+x['java']),reverse=flag)
                show_student(stu_list)  #显示排序结果
            else:
                print('无学生信息！')
    else:
        print('无学生信息！')
    answer=input('是否继续排序？（y/n）')
    if answer=='y':
        sort()


def total():
    if os.path.exists(filename):
        with open(filename,'r',encoding='utf-8')as rfile:
            students=rfile.readlines()
            if len(students)==0:
                print('无学生信息！')
            else:
                print(f'一共有{len(students)}个学生\n')
    else:
        print('无学生信息！\n')
        return

def show():
    students_inf=[]
    if os.path.exists(filename):
        with open(filename,'r',encoding='utf-8')as rfile:
            students=rfile.readlines()
            le=len(students)
            if le==0:
                print('无学生信息！')
                return
            else:
                for item in students:
                    students_inf.append(eval(item))
                show_student(students_inf)
    else:
        print('无学生信息！\n')


if __name__ == '__main__':
    main()