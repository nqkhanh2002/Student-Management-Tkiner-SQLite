from tkinter import *
from tkinter import  ttk, Tk, StringVar
import time;
from tkinter import messagebox
import sqlite3
from  PIL import *
import tkinter.ttk as ttk
from Admin_Dashboard import *
from tkcalendar import *
from tkinter.filedialog import askopenfilename

gg='#134e86'#secondary color
g="#0a2845#"#color
gw="white"

# def Database():
#     global conn, cursor
#     conn = sqlite3.connect('pythonn.db')
#     cursor = conn.cursor()
#     cursor.execute("CREATE TABLE IF NOT EXISTS `result` (st_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, st_name TEXT, c_name TEXT, c_code TEXT, f_name TEXT, quizes TEXT, midterm TEXT,finals TEXT,total TEXT)")

def Database_assignment():
    global conn, cursor
    conn = sqlite3.connect('pythonn.db')
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS `assignment` (post_no INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, post_pf_name TEXT, post_date TEXT, deadline TEXT, subject TEXT, title TEXT, content TEXT)")


def Database_pf():
    global conn, cursor
    conn = sqlite3.connect('pythonn.db')
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS `professor_admin` (pf_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, pf_name TEXT, pf_code TEXT, pf_pword TEXT, pf_subject_flag INTEGER, pf_student_flag INTEGER)")

def Database_st():
    global conn, cursor
    conn = sqlite3.connect('pythonn.db')
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS `student_admin` (st_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, st_name TEXT, st_code TEXT, st_pword TEXT, st_subject_flag INTEGER,st_professor_flag INTEGER)")


def Database_st_grade():
    global conn, cursor
    conn = sqlite3.connect('pythonn.db')
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS `all_students_grade` (st_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, st_name TEXT, st_grade_date TEXT, st_subject1 INTEGER, st_subject2 INTEGER, st_subject3 INTEGER, st_subject4 INTEGER, st_subject5 INTEGER, st_professor_code INTEGER, st_course_code INTEGER)")

def Database_upload_file():
    global conn, cursor
    conn = sqlite3.connect('pythonn.db')
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS `uploaded_file` (pf_id INTEGER, pf_name TEXT, uploaded_file_path TEXT)")


def ALogin ():
    username = AEusername.get()
    password = AEPassword.get()
    print("username:",username)
    print("password:",password)
    if(username == "admin") and (password == "admin"):
        goto_AdminHome()

def TLogin ():
    username = TEusername.get()
    password = TEPassword.get()
    print("username:",username)
    print("password:",password)
    Database_pf()
    
    finduser = ("SELECT * FROM 'professor_admin' WHERE pf_code == ? and pf_pword == ?")
    cursor.execute(finduser,[(username.lstrip()),(password.lstrip())])
    global results
    results = cursor.fetchall()
    global s
    s = str(results[0][1])
    print("professor's Name:",s)
    global course_flag
    course_flag = results[0][4]
    print('course_flag:',course_flag)
    
    finduser = ("SELECT * FROM 'course_admin' WHERE Course_No == ?")
    cursor.execute(finduser,[course_flag])
    global results_course
    results_course = cursor.fetchall()
    print('results_course:',results_course)
    
    finduser = ("SELECT * FROM 'student_admin' WHERE st_professor_flag == ?")
    st_flag = str(results[0][0])
    print("st_flag:",st_flag)
    cursor.execute(finduser,[st_flag])
    global students_list
    students_list = cursor.fetchall()
    print('students_list:',students_list)
    global students_name_list
    students_name_list = []
    for data in students_list:
        students_name_list.append(data[1])
    print("st_name_list",students_name_list)
    if results:
        goto_TeacherHome()

    else:
        TeacherLoginForm.destroy()
        messagebox.showinfo("Retry!", "Please enter correct username and password!")

def SLogin ():
    username = SEusername.get()
    password = SEPassword.get()
    print("username:",username)
    print("password:",password)
    Database_st()
    
    finduser = ("SELECT * FROM 'student_admin' WHERE st_code == ? and st_pword == ?")
    cursor.execute(finduser,[(username.lstrip()),(password.lstrip())])
    global results_st
    results_st = cursor.fetchall()
    global st
    st = str(results_st[0][1])
    print("students's Name:",st)
    global st_course_flag
    st_course_flag = results_st[0][4]
    print('st_course_flag:',st_course_flag)
    
    finduser = ("SELECT * FROM 'course_admin' WHERE Course_No == ?")
    cursor.execute(finduser,[st_course_flag])
    global results_st_course
    results_st_course = cursor.fetchall()
    print('results_st_course:',results_st_course)
    
    finduser = ("SELECT * FROM 'professor_admin' WHERE pf_student_flag == ?")
    pf_flag = str(results_st[0][5])
    print("pf_flag:",pf_flag)
    cursor.execute(finduser,[pf_flag])
    global st_professor_name
    st_professor_name = cursor.fetchall()
    print('st_professor_name:',st_professor_name[0][1])
    if results_st:
        goto_StudentHome()

    else:
        StLoginForm.destroy()
        messagebox.showinfo("Retry!", "Please enter correct username and password!")        
    
def quitA():
    AdminLoginForm.destroy()

def quitt ():
    TeacherLoginForm.destroy()
def AdminLogin ():
    global AdminLoginForm
    global AEusername
    global AEPassword
    AdminLoginForm = Tk()
    AdminLoginForm.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
    AdminLoginForm.resizable(0,0)
    AdminLoginForm.title('ĐĂNG NHẬP QUẢN TRỊ')
    AdminLoginForm.config(bg='white')
    
    frameH = Frame(AdminLoginForm, height = 50, width = 1277, bg  ='#3C6739').place(relx=0, y=30)
    frameC = Frame(AdminLoginForm, height = 80, width = 1277,bg='#F0F0F0').place(x=0 ,y=90)
    LAdminLogin = Label(AdminLoginForm, font=('Roboto', 30, 'bold'), text="ĐĂNG NHẬP QUẢN TRỊ").place(relx=0.35, y=100)
    frameF = Frame(AdminLoginForm, height=50, width=1277, bg='#3C6739').place(relx=0, y=180)
    ALusername = Label(AdminLoginForm, text="Tài Khoản", bg='white',  font = ('Roboto', 20)).place(x=380, y=356)
    AEusername = ttk.Entry(AdminLoginForm,font= ('Roboto', 20))
    ALPassword = Label(AdminLoginForm, text='Mật khẩu', bg='white', font=('Roboto', 20)).place(x=380, y=410)
    AEPassword = ttk.Entry(AdminLoginForm,font=('Roboto', 20),show = '*')
    ABLogin = Button(AdminLoginForm, text='ĐĂNG NHẬP', padx=170, pady=5, font=('Roboto', 12, 'bold'), bg='#3C6739', fg='white', command = ALogin).place(relx=0.32, y=470)
    AEusername.place(x=539, y=360)
    AEPassword.place(x=539, y=410)
    #------------ ------------------------------------TEACHER LOGIN START-------------------------------------------#
def TeacherLogin ():
    global TeacherLoginForm
    global TEusername
    global TEPassword
    TeacherLoginForm = Tk()
    TeacherLoginForm .geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
    TeacherLoginForm.resizable(0,0)
    TeacherLoginForm.title('ĐĂNG NHẬP GIẢNG VIÊN')
    TeacherLoginForm.config(bg='white')

    frameH = Frame(TeacherLoginForm, height = 50, width = 1277, bg  ='#3C6739').place(relx=0, y=30)
    frameC = Frame(TeacherLoginForm, height = 80, width = 1277,bg='#F0F0F0').place(x=0 ,y=90)
    LTeacherLogin = Label(TeacherLoginForm, font=('Roboto', 30, 'bold'), text="ĐĂNG NHẬP GIẢNG VIÊN").place(relx=0.35, y=100)
    frameF = Frame(TeacherLoginForm, height=50, width=1277, bg='#3C6739').place(relx=0, y=180)

    TLusername = Label(TeacherLoginForm, text="Tài Khoản", bg='white',  font = ('Roboto', 20)).place(x=380, y=356)
    TEusername = ttk.Entry(TeacherLoginForm,font= ('Roboto', 20))
    TLPassword = Label(TeacherLoginForm, text='Mật khẩu', bg='white', font=('Roboto', 20)).place(x=380, y=410)
    TEPassword = ttk.Entry(TeacherLoginForm,font=('Roboto', 20),show = '*')
    TBLogin = Button(TeacherLoginForm, text='ĐĂNG NHẬP', padx=170, pady=5, font=('Roboto', 12, 'bold'), bg='#3C6739', fg='white', command = TLogin).place(relx=0.32, y=470)
    TLMessage = Label(TeacherLoginForm, text='', fg='red', bg='white', font=('Roboto', 15)).place(relx=0.43,rely=0.72)
    TEusername.place(x=539, y=360)
    TEPassword.place(x=539, y=410)

def StudentLogin():
    global StLoginForm
    global SEusername
    global SEPassword
    StLoginForm = Tk()
    StLoginForm.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
    StLoginForm.resizable(0,0)
    StLoginForm.title('ĐĂNG NHẬP SINH VIÊN')
    StLoginForm.config(bg='white')

    frameH = Frame(StLoginForm, height = 50, width = 1277, bg  ='#3C6739').place(relx=0, y=30)
    frameC = Frame(StLoginForm, height = 80, width = 1277,bg='#F0F0F0').place(x=0 ,y=90)
    LStLogin = Label(StLoginForm, font=('Roboto', 30, 'bold'), text="ĐĂNG NHẬP SINH VIÊN").place(relx=0.35, y=100)
    frameF = Frame(StLoginForm, height=50, width=1277, bg='#3C6739').place(relx=0, y=180)

    SLusername = Label(StLoginForm, text="Tài khoản", bg='white',  font = ('Roboto', 20)).place(x=380, y=356)
    SEusername = ttk.Entry(StLoginForm,font= ('Roboto', 20))
    SLPassword = Label(StLoginForm, text='Mật khẩu', bg='white', font=('Roboto', 20)).place(x=380, y=410)
    SEPassword = ttk.Entry(StLoginForm,font=('Roboto', 20),show = '*')
    SBLogin = Button(StLoginForm, text='ĐĂNG NHẬP', padx=170, pady=5, font=('Roboto', 12, 'bold'), bg='#3C6739', fg='white', command = SLogin).place(relx=0.32, y=470)
    SLMessage = Label(StLoginForm, text='', fg='red', bg='white', font=('Roboto', 15)).place(relx=0.43,rely=0.72)
    SEusername.place(x=539, y=360)
    SEPassword.place(x=539, y=410)
    # ------------------------------------------------TEACHER LOGIN END-------------------------------------------#
    #------------------------------------------------TEACHER BUTTON END-------------------------------------------#

class TeacherHome(Tk):
    def __init__(self, *TeacherHomeWindow, **master):
        Tk.__init__(self, *TeacherHomeWindow, **master)

        self.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
        self.resizable(0, 0)
        self.title('Teacher Login')
        self.config(bg='white')

        self.AHframe = Frame(self, height=80, width=1280, bg='#3C6739').place(relx=0, y=0)

        self.LStudentLogin = Label(self, font=('Roboto', 30, 'bold'), text= "GIẢNG VIÊN " + str(s) + " - TRANG CHỦ", bg='white').place(relx=0.25,
                                                                                                               y=150)

        self.B_AttendanceReg = Button(self, text='Chuyên cần', width=15, height=8, bg='#3C6739', fg='white',
                                      font=('Roboto', 10), bd=6, command = goto_Attendance).place(x=120, rely=0.4)
        self.B_Course_manage = Button(self, text='Khóa học', width=15, height=8, bg='#3C6739', fg='white',
                                      font=('Roboto', 10), bd=6, command = view_course).place(x=320, rely=0.4)
        self.B_ReportCard = Button(self, text='Điểm số', width=15, height=8, bg='#3C6739', fg='white',
                                   font=('Roboto', 10), bd=6, command=student_grade_register).place(x=520, rely=0.4)
        self.B_EvaloutionForm = Button(self, text='Bài tập', width=15, height=8, bg='#3C6739', fg='white',
                                       font=('Roboto', 10), bd=6, command = assignment).place(x=720, rely=0.4)
        self.B_File_manage = Button(self, text='Thêm tệp', width=15, height=8, bg='#3C6739', fg='white',
                                      font=('Roboto', 10), bd=6,command = file_upload).place(x=920, rely=0.4)
        
        self.AFframe = Frame(self, height=35, width=1280, bg='#3C6739').place(relx=0, y=685)


def goto_TeacherHome():
    ojbTeacherHome = TeacherHome()

class StudentHome(Tk):
    def __init__(self, *StudentHomeWindow, **master):
        Tk.__init__(self, *StudentHomeWindow, **master)

        self.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
        self.resizable(0, 0)
        self.title('ĐĂNG NHẬP SINH VIÊN')
        self.config(bg='white')

        self.AHframe = Frame(self, height=80, width=1280, bg='#3C6739').place(relx=0, y=0)

        self.LStudentLogin = Label(self, font=('Roboto', 30, 'bold'), text= "SINH VIÊN - " + str(st) + " - TRANG CHỦ", bg='white').place(relx=0.25,
                                                                                                               y=150)


        self.B_Course_manage = Button(self, text='Khoá học', width=15, height=8, bg='#3C6739', fg='white',
                                      font=('Roboto', 10), bd=6, command = view_course_st).place(x=220, rely=0.4)
        self.B_ReportCard = Button(self, text='Điểm số', width=15, height=8, bg='#3C6739', fg='white',
                                   font=('Roboto', 10), bd=6, command=view_st_grade).place(x=420, rely=0.4)
        self.B_EvaloutionForm = Button(self, text='Bài tập', width=15, height=8, bg='#3C6739', fg='white',
                                       font=('Roboto', 10), bd=6, command = view_assignment_st).place(x=620, rely=0.4)
        self.B_File_manage = Button(self, text='Truy xuất tệp', width=15, height=8, bg='#3C6739', fg='white',
                                      font=('Roboto', 10), bd=6,command = file_retrieve).place(x=820, rely=0.4)

        self.AFframe = Frame(self, height=35, width=1280, bg='#3C6739').place(relx=0, y=685)


def goto_StudentHome():
    ojbStudentHome = StudentHome()

def Exit_home():
    StudentHome.withdraw()

def Result():
    if (E_IDNO.get()== ""):
        messagebox.showinfo("Requirment!", "Vui lòng nhập mã ID")

    try:
        Database_st_grade()
        finduser = ("SELECT * FROM `all_students_grade` WHERE st_id == ?")
        cursor.execute(finduser,[str(E_IDNO.get())])
        fetch = cursor.fetchall()
        for data in fetch:
            tree.insert('', 'end', values=(data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7]))
        cursor.close()
        conn.close()
    except:
        IndexError
def view_st_grade():
    StGradeForm = Tk()
    StGradeForm.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
    StGradeForm.resizable(0, 0)
    StGradeForm.title('XEM ĐIỂM SỐ SINH VIÊN')
    StGradeForm.config(bg='white')

    AHframe = Frame(StGradeForm, height=80, width=1280, bg='#3C6739').place(relx=0, y=0)

    global tree
    global mytree
    global E_IDNO
    E_IDNO = StringVar()
    LStudentLogin = Label(StGradeForm, font=('Roboto', 30, 'bold'), text="Sinh Viên : " + str(st), bg='white').place(relx=0.38,rely=0.03)
    HeadingMessage = Label(StGradeForm, font= ('Roboto', 15, 'bold'),text='Nhập mã ID để xem kết quả của bạn ', bg='white').place(relx=0.36, rely=0.13)
    L_IDNO = Label(StGradeForm, text='Mã ID sinh viên khác', font = ('Roboto', 15, 'bold'), bg='white').place(relx=0.77, rely = 0.35)
    E_IDNO = ttk.Entry(StGradeForm, font= ('Roboto', 12))
    E_IDNO.place(relx=0.77, rely  = 0.45)
    B_CheckResult = Button(StGradeForm,text="Kiểm tra điểm sinh viên khác", bg='#3C6739', fg='white', font=('Roboto', 10), command= Result).place(relx=0.78, rely= 0.55)

    scrollbary = Scrollbar(StGradeForm, orient=VERTICAL)
    scrollbarx = Scrollbar(StGradeForm, orient=HORIZONTAL)
    tree = ttk.Treeview(StGradeForm, columns=(
        "st_id", "st_name","grade_date", "Subject_1", "Subject_2", "Subject_3", "Subject_4", "Subject_5"),
                        selectmode="extended", height=10, yscrollcommand=scrollbary.set,
                        xscrollcommand=scrollbarx.set)
    scrollbary.config(command=tree.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=tree.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)
    tree.heading('st_id', text="ID", anchor=W)
    tree.heading('st_name', text="Tên", anchor=W)
    tree.heading('grade_date', text="Ngày", anchor=W)
    tree.heading('Subject_1', text="MÔN HỌC 1", anchor=W)
    tree.heading('Subject_2', text="MÔN HỌC 2", anchor=W)
    tree.heading('Subject_3', text="MÔN HỌC 3", anchor=W)
    tree.heading('Subject_4', text="MÔN HỌC 4", anchor=W)
    tree.heading('Subject_5', text="MÔN HỌC 5", anchor=W)

    tree.column('#0', stretch=NO, minwidth=0, width=0)
    tree.column('#1', stretch=NO, minwidth=0, width=120)
    tree.column('#2', stretch=NO, minwidth=0, width=120)
    tree.column('#3', stretch=NO, minwidth=0, width=120)
    tree.column('#4', stretch=NO, minwidth=0, width=120)
    tree.column('#5', stretch=NO, minwidth=0, width=120)
    tree.column('#6', stretch=NO, minwidth=0, width=120)
    tree.column('#7', stretch=NO, minwidth=0, width=120)

    tree.place(x=50, rely=0.6)
    
    print('course:',results_st_course)
    scrollbary = Scrollbar(StGradeForm, orient=VERTICAL)
    scrollbarx = Scrollbar(StGradeForm, orient=HORIZONTAL)
    mytree = ttk.Treeview(StGradeForm, columns=(
        "grade_date", 'subject_1', 'subject_2', 'subject_3', 'subject_4','subject_5'),
                        selectmode="extended", height=10, yscrollcommand=scrollbary.set,
                        xscrollcommand=scrollbarx.set)
    scrollbary.config(command=mytree.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=mytree.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)

    mytree.heading('grade_date', text="Date", anchor=W)
    mytree.heading('subject_1', text = str(results_st_course[0][1]), anchor=W)
    mytree.heading('subject_2', text = str(results_st_course[0][2]), anchor=W)
    mytree.heading('subject_3', text = str(results_st_course[0][3]), anchor=W)
    mytree.heading('subject_4', text = str(results_st_course[0][4]), anchor=W)
    mytree.heading('subject_5', text = str(results_st_course[0][5]), anchor=W)

    mytree.column('#0', stretch=NO, minwidth=0, width=0)
    mytree.column('#1', stretch=NO, minwidth=0, width=120)
    mytree.column('#2', stretch=NO, minwidth=0, width=120)
    mytree.column('#3', stretch=NO, minwidth=0, width=120)
    mytree.column('#4', stretch=NO, minwidth=0, width=120)
    mytree.column('#5', stretch=NO, minwidth=0, width=120)
    mytree.place(x=50, rely=0.2)
    
    Database_st_grade()
    print('pf_name',st_professor_name)
    finduser = ("SELECT * FROM `all_students_grade` WHERE st_name == ?")
    cursor.execute(finduser,[str(st)])
    fetch = cursor.fetchall()
    for data in fetch:
        mytree.insert('', 'end', values=( data[2], data[3], data[4], data[5],data[6],data[7]))
    cursor.close()
    conn.close()
    AFframe = Frame(StGradeForm, height=35, width=1280, bg='#3C6739').place(relx=0, y=685)

def view_assignment_st():
    StGradeForm = Tk()
    StGradeForm.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
    StGradeForm.resizable(0, 0)
    StGradeForm.title('XEM BÀI TẬP')
    StGradeForm.config(bg='white')

    AHframe = Frame(StGradeForm, height=80, width=1280, bg='#3C6739').place(relx=0, y=0)
    global tree
    LStudentLogin = Label(StGradeForm, font=('Roboto', 30, 'bold'), text="SINH VIÊN : " + str(st) + " - BÀI TẬP", bg='white').place(relx=0.3,y=100)
    HeadingMessage = Label(StGradeForm, font= ('Roboto', 15, 'bold'),text='XEM CÁC BÀI TẬP ĐƯỢC GIẢNG VIÊN GIAO', bg='white').place(relx=0.33, y=150)
    scrollbary = Scrollbar(StGradeForm, orient=VERTICAL)
    scrollbarx = Scrollbar(StGradeForm, orient=HORIZONTAL)
    tree = ttk.Treeview(StGradeForm, columns=(
        "post_no", "professor_name","post_date", "Subject", "Title", "Content"),
                        selectmode="extended", height=10, yscrollcommand=scrollbary.set,
                        xscrollcommand=scrollbarx.set)
    scrollbary.config(command=tree.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=tree.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)
    tree.heading('post_no', text="ID", anchor=W)
    tree.heading('professor_name', text="Tên giảng viên", anchor=W)
    tree.heading('post_date', text="Ngày đăng", anchor=W)
    tree.heading('Subject', text="Môn học", anchor=W)
    tree.heading('Title', text="Tiêu đề", anchor=W)
    tree.heading('Content', text="Nội dung", anchor=W)
    
    tree.column('#0', stretch=NO, minwidth=0, width=0)
    tree.column('#1', stretch=NO, minwidth=0, width=120)
    tree.column('#2', stretch=NO, minwidth=0, width=120)
    tree.column('#3', stretch=NO, minwidth=0, width=120)
    tree.column('#4', stretch=NO, minwidth=0, width=120)
    tree.column('#5', stretch=NO, minwidth=0, width=120)
    
    tree.place(x=160, rely=0.3)
    Database_assignment()
    print('pf_name',st_professor_name)
    finduser = ("SELECT * FROM `assignment` WHERE post_pf_name == ?")
    cursor.execute(finduser,[str(st_professor_name[0][1])])
    fetch = cursor.fetchall()
    for data in fetch:
        tree.insert('', 'end', values=(data[0], data[1], data[2], data[4], data[5], data[6]))
    cursor.close()
    conn.close()

    AFframe = Frame(StGradeForm, height=35, width=1280, bg='#3C6739').place(relx=0, y=685)

def student_grade_register():
    global  st_RegisterForm
    st_RegisterForm = Tk()
    st_RegisterForm.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
    st_RegisterForm.resizable(0,0)
    st_RegisterForm.title("Grade Dashboard")
    st_RegisterForm.config(bg='white')
    AHframe = Frame(st_RegisterForm, height=40, width=1280, bg='#3C6739').place(relx=0, y=0)
    AHHeading = Label(st_RegisterForm, text='GIẢNG VIÊN : ' + str(s) + ' .NHẬP ĐIỂM', font=('Roboto', 18), bg='#3C6739', fg='white').place(
            relx=0.5, rely=0)
    st_RegisterForm.Left = ttk.Frame(st_RegisterForm, width=300, height=1000, relief="raise")
    st_RegisterForm.Left.place(x=2, y=50)
    lbl = Label(st_RegisterForm, text="Thêm bản ghi mới", font=("Roboto", 10, 'bold'), bg='white')
    lbl.place(x=25, y=68)
    global ent_st_no
    global ent_st_name
    global ent_st_grade_date
    global ent_st_subject1
    global ent_st_subject2
    global ent_st_subject3
    global ent_st_subject4
    global ent_st_subject5
    
    lbl_reg_no = Label(st_RegisterForm, text="ID", font=("Roboto", 8, 'bold'), bg='white').place(x=16,
                                                                                                              y=100)
    lbl_st_name = Label(st_RegisterForm, text="Tên sinh viên", font=("Roboto", 8, 'bold'), bg='white').place(x=16,
                                                                                                               y=135)
    lbl_st_gender = Label(st_RegisterForm, text="Ngày bắt đầu", font=("Roboto", 8, 'bold'), bg='white').place(x=16,
                                                                                                               y=170)
    lbl_st_sub1 = Label(st_RegisterForm, text=str(results_course[0][1]), font=("Roboto", 8, 'bold'), bg='white').place(x=16, y=205)
    lbl_st_sub2 = Label(st_RegisterForm, text=str(results_course[0][2]), font=("Roboto", 8, 'bold'), bg='white').place(x=16,
                                                                                                               y=240)
    lbl_st_sub3 = Label(st_RegisterForm, text=str(results_course[0][3]), font=("Roboto", 8, 'bold'), bg='white').place(x=16, y=275)
    lbl_st_sub4 = Label(st_RegisterForm, text=str(results_course[0][4]), font=("Roboto", 8, 'bold'), bg='white').place(x=16, y=310)
    lbl_st_sub5 = Label(st_RegisterForm, text=str(results_course[0][5]), font=("Roboto", 8, 'bold'), bg='white').place(x=16, y=345)
        
    ent_st_no = ttk.Entry(st_RegisterForm, width=15)
    ent_st_no.place(x=115, y=100)
    ent_st_name = ttk.Combobox(st_RegisterForm, textvariable='', state='readonly',width = 13)
    ent_st_name['values'] = students_name_list
    ent_st_name.current(0)
    ent_st_name.place(x=115, y=135)
    ent_st_grade_date = ttk.Entry(st_RegisterForm, width=15)
    ent_st_grade_date.place(x=115, y=170)
    ent_st_subject1 = ttk.Entry(st_RegisterForm, width=15)
    ent_st_subject1.place(x=115, y=205)
    ent_st_subject2 = ttk.Entry(st_RegisterForm, width=15)
    ent_st_subject2.place(x=115, y=240)
    ent_st_subject3 = ttk.Entry(st_RegisterForm, width=15)
    ent_st_subject3.place(x=115, y=275)
    ent_st_subject4 = ttk.Entry(st_RegisterForm, width=15)
    ent_st_subject4.place(x=115, y=310)
    ent_st_subject5 = ttk.Entry(st_RegisterForm, width=15)
    ent_st_subject5.place(x=115, y=345)
    
    btn_show = ttk.Button(st_RegisterForm, text="Làm mới", command=Read_st_grade, width = 20).place(x = 40,y = 380)
    btn_add = ttk.Button(st_RegisterForm, text="Thêm bản ghi mới" ,command=add_book_st_grade,width = 20).place(x = 40,y = 410)
    btn_exit = ttk.Button(st_RegisterForm, text="Thoát", command = exit_register_st_grade,width = 20).place(x = 40,y = 440)
    st_RegisterForm.Right = ttk.Frame(st_RegisterForm, width=600, height=500, relief="raise")
    st_RegisterForm.Right.place(x=250, y=45)
    global tree

    scrollbary = Scrollbar(st_RegisterForm.Right, orient=VERTICAL)
    scrollbarx = Scrollbar(st_RegisterForm.Right, orient=HORIZONTAL)
    tree = ttk.Treeview(st_RegisterForm.Right, columns=(
            "st_id", "st_name", "st_grade_date", "st_sub1", "st_sub2","st_sub3","st_sub4","st_sub5","st_professor_code","st_course_code"),
                            selectmode="extended", height=500, yscrollcommand=scrollbary.set,
                            xscrollcommand=scrollbarx.set)
    scrollbary.config(command=tree.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=tree.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)
    tree.heading('st_id', text="ID", anchor=W)
    tree.heading('st_name', text="Tên sinh viên", anchor=W)
    tree.heading('st_grade_date', text="Ngày bắt đầu", anchor=W)
    tree.heading('st_sub1', text=str(results_course[0][1]), anchor=W)
    tree.heading('st_sub2', text=str(results_course[0][2]), anchor=W)
    tree.heading('st_sub3', text=str(results_course[0][3]), anchor=W)
    tree.heading('st_sub4', text=str(results_course[0][4]), anchor=W)
    tree.heading('st_sub5', text=str(results_course[0][5]), anchor=W)
    tree.heading('st_professor_code', text="Mã giảng viên", anchor=W)
    tree.heading('st_course_code', text="Mã khóa học", anchor=W)

    tree.column('#0', stretch=NO, minwidth=0, width=0)
    tree.column('#1', stretch=NO, minwidth=0, width=90)
    tree.column('#2', stretch=NO, minwidth=0, width=90)
    tree.column('#3', stretch=NO, minwidth=0, width=90)
    tree.column('#4', stretch=NO, minwidth=0, width=90)
    tree.column('#5', stretch=NO, minwidth=0, width=00)
    tree.column('#6', stretch=NO, minwidth=0, width=90)
    tree.column('#7', stretch=NO, minwidth=0, width=90)
    tree.column('#8', stretch=NO, minwidth=0, width=90)        
    tree.column('#9', stretch=NO, minwidth=0, width=90)        
    tree.pack()
   
    Read_st_grade()
    AFframe = Frame(st_RegisterForm, height=35, width=1280, bg='#3C6739').place(relx=0, y=685)
    st_RegisterForm.mainloop()

def Read_st_grade():
    tree.delete(*tree.get_children())
    Database_st_grade()
    finduser = ("SELECT * FROM `all_students_grade` WHERE st_professor_code == ?")
    cursor.execute(finduser,[str(results[0][0])])
    fetch = cursor.fetchall()
    for data in fetch:
        tree.insert('', 'end', values=(data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8],data[9]))
    cursor.close()
    conn.close()

def add_book_st_grade():
    if ent_st_no.get() == "" or ent_st_name.get() == "" or ent_st_grade_date.get() == "" or ent_st_subject1.get() == "" or ent_st_subject2.get() == "" or ent_st_subject3.get() == "" or ent_st_subject4.get() == "" or ent_st_subject5.get() == "":
        messagebox.showinfo("Requirment!", "Vui lòng điền đầy đủ thông tin!")
    else:
        Database_st_grade()
        cursor.execute("INSERT INTO 'all_students_grade' (st_id, st_name, st_grade_date, st_subject1, st_subject2, st_subject3, st_subject4, st_subject5, st_professor_code, st_course_code) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",  (str(ent_st_no.get()), str(ent_st_name.get()), str(ent_st_grade_date.get()), str(ent_st_subject1.get()), str(ent_st_subject2.get()),str(ent_st_subject3.get()),str(ent_st_subject4.get()),str(ent_st_subject5.get()),str(results[0][0]),course_flag))
        print("query runnning")
        conn.commit()    
        cursor.close()
        conn.close()

def exit_register_st_grade():
    st_RegisterForm.destroy()

def goto_Attendance():
    AttendanceReg = Toplevel()
    AttendanceReg.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
    AttendanceReg.resizable(0, 0)
    AttendanceReg.title('ĐĂNG KÝ CHUYÊN CẦN')
    AttendanceReg.config(bg='white')
    
    AHframe = Frame(AttendanceReg, height=40, width=1280, bg='#3C6739').place(relx=0, y=0)
    AHHeading = Label(AttendanceReg, text='GIẢNG VIÊN: ' + str(s) + '  . SINH VIÊN CHUYÊN CẦN', font=('Roboto', 18), bg='#3C6739', fg='white').place(
            relx=0.4, rely=0)
    
    LeftMayFrame = Frame(AttendanceReg, width=1002, height=650, bd=2, relief="raise", bg='white')
    LeftMayFrame.pack(side=LEFT)
    RightMayFrame = Frame(AttendanceReg, width=350, height=650, bd=2, relief="raise", bg='white')
    RightMayFrame.pack(side=RIGHT)
    
    LeftMayFrame1 = Frame(LeftMayFrame, width=1000, height=100, bd=2, relief="raise", bg='white')
    LeftMayFrame1.place(y=0.70)
    LeftMayFrame2 = Frame(LeftMayFrame, width=1000, height=546, bd=2, relief="raise", bg='white')
    LeftMayFrame2.place(y=101)
    
    RightMayFrame1 = Frame(RightMayFrame, width=350, height=350,bd=2, relief="raise", bg='white')
    RightMayFrame1.place(y=0.100)
    RightMayFrame2 = Frame(RightMayFrame, width=350, height=350, bd=2, relief="raise", bg='white')
    RightMayFrame2.place(y=300)
    
    DateofOrder = StringVar()
    DateofOrder.set(time.strftime("%d/%m/%y"))
    
    cont = Canvas(RightMayFrame1, width = 200, height = 300, bg='white')
    cont.place(relx=0.1, y=0)
    
    name = ''
    stname_L = Label(RightMayFrame2).place(relx=0.5 , rely=0.5)
    image0 = PhotoImage(file = "stdeomo.png")
    image =  cont.create_image(100, 150, image = image0)
    lblNo = Label(LeftMayFrame1, font=('Roboto', 10, 'bold'), text="No", bg='white').place(x=50, rely=0.3)
    lblStudentNo = Label(LeftMayFrame1, font=('Roboto', 10, 'bold'), text="ID", bg='white').place(x=120, rely=0.3)
    lblStudentName = Label(LeftMayFrame1, font=('Roboto', 10, 'bold'), text="Tên sinh viên", bg='white').place(x=240,
                                                                                                                 rely=0.3)
    lblCourseCode = Label(LeftMayFrame1, font=('Roboto', 10, 'bold'), text="Mã khóa học", bg='white').place(x=400, rely=0.3)
    
    box = ttk.Combobox(LeftMayFrame1, textvariable='', state='readonly')
    box['values'] = ('', 'Present', 'Absent', 'Leave', 'Late', 'Sick')
    box.current(0)
    box.place(x=550, rely=0.3)
    
    btnFill = ttk.Button(LeftMayFrame1, text='Fill').place(x=720, rely=0.27)
    
    btnReset = ttk.Button(LeftMayFrame1, text='Reset').place(x=815, rely=0.27)
    lblDateofOrder = Label(LeftMayFrame1, font=('Roboto', 10, 'bold'), textvariable=DateofOrder, padx=2, pady=2, bd=2,fg='black', bg='white', relief='sunken').place(x=900, rely=0.3)    
    
    i = 0
    for data in students_list:
        i = i + 1
        st_no = Label(LeftMayFrame2, text=str(i), font =('Roboto', 10, 'bold'), bg='white').place(x=53, y=10 + 38*(i-1))
        st_id = Label(LeftMayFrame2, text=str(data[0]), font =('Roboto', 10, 'bold'), bg='white').place(x=142, y=10 + 38*(i-1))
        st_name = Label(LeftMayFrame2, text=str(data[1]), font=('Roboto', 10, 'bold'), bg='white').place(x=260, y=10 + 38*(i-1))
        st_course = Label(LeftMayFrame2, text=str(data[4]), font=('Roboto', 10, 'bold'), bg='white').place(x=422, y=10 + 38*(i-1))
        box = ttk.Combobox(LeftMayFrame2,state='readonly')
        box['values'] = ('', 'Present', 'Absent', 'Leave', 'Late', 'Sick')
        box.current(0)
        box.place(x=550, y=10 + 38*(i-1))
        #img_name = "st"+str(data[0])+".png"
        #image_real= PhotoImage(file = str(img_name))
        def pic():    
            print('img_name:',img_name)    
            image = cont.create_image(70, 150, image = image_real)
        StDetails1 = ttk.Button(LeftMayFrame2, text='Xem chi tiết', width=27)
        StDetails1.place(x=720, y=10 + 38*(i-1))
    AttendanceReg.mainloop()


def view_course():
    global  cr_RegisterForm
    cr_RegisterForm = Tk()
    cr_RegisterForm.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
    cr_RegisterForm.resizable(0,0)
    cr_RegisterForm.title("KHÓA HỌC GIẢNG VIÊN")
    cr_RegisterForm.config(bg='white')
    AHframe = Frame(cr_RegisterForm, height=40, width=1280, bg='#3C6739').place(relx=0, y=0)
    AHHeading = Label(cr_RegisterForm, text="GIẢNG VIÊN :  " + str(s) + "  -  KHÓA HỌC", font=('Roboto', 18), bg='#3C6739', fg='white').place(
            relx=0.4, rely=0)
    cr_1 = Button(cr_RegisterForm, text=str(results_course[0][1]), width=15, height=8, bg='#3C6739', fg='white',
                                      font=('Roboto', 10), bd=6).place(x=120, rely=0.4)
    cr_2 = Button(cr_RegisterForm, text=str(results_course[0][2]), width=15, height=8, bg='#3C6739', fg='white',
                                      font=('Roboto', 10), bd=6).place(x=320, rely=0.4)
    cr_3 = Button(cr_RegisterForm, text=str(results_course[0][3]), width=15, height=8, bg='#3C6739', fg='white',
                                   font=('Roboto', 10), bd=6).place(x=520, rely=0.4)
    cr_4 = Button(cr_RegisterForm, text=str(results_course[0][4]), width=15, height=8, bg='#3C6739', fg='white',
                                       font=('Roboto', 10), bd=6).place(x=720, rely=0.4)
    cr_5 = Button(cr_RegisterForm, text=str(results_course[0][5]), width=15, height=8, bg='#3C6739', fg='white',
                                      font=('Roboto', 10), bd=6).place(x=920, rely=0.4)
    AFframe = Frame(cr_RegisterForm, height=50, width=1280, bg='#3C6739').place(relx=0, y=685)
    
def view_course_st():
    global  cr_RegisterForm
    cr_RegisterForm = Tk()
    cr_RegisterForm.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
    cr_RegisterForm.resizable(0,0)
    cr_RegisterForm.title("Student's Course")
    cr_RegisterForm.config(bg='white')
    AHframe = Frame(cr_RegisterForm, height=40, width=1280, bg='#3C6739').place(relx=0, y=0)
    AHHeading = Label(cr_RegisterForm, text="Student:  " + str(st) + "  .  Course", font=('Roboto', 18), bg='#3C6739', fg='white').place(
            relx=0.35, rely=0)
    cr_1 = Button(cr_RegisterForm, text=str(results_st_course[0][1]), width=15, height=8, bg='#3C6739', fg='white',
                                      font=('Roboto', 10), bd=6).place(x=120, rely=0.4)
    cr_2 = Button(cr_RegisterForm, text=str(results_st_course[0][2]), width=15, height=8, bg='#3C6739', fg='white',
                                      font=('Roboto', 10), bd=6).place(x=320, rely=0.4)
    cr_3 = Button(cr_RegisterForm, text=str(results_st_course[0][3]), width=15, height=8, bg='#3C6739', fg='white',
                                   font=('Roboto', 10), bd=6).place(x=520, rely=0.4)
    cr_4 = Button(cr_RegisterForm, text=str(results_st_course[0][4]), width=15, height=8, bg='#3C6739', fg='white',
                                       font=('Roboto', 10), bd=6).place(x=720, rely=0.4)
    cr_5 = Button(cr_RegisterForm, text=str(results_st_course[0][5]), width=15, height=8, bg='#3C6739', fg='white',
                                      font=('Roboto', 10), bd=6).place(x=920, rely=0.4)
    AFframe = Frame(cr_RegisterForm, height=50, width=1280, bg='#3C6739').place(relx=0, y=685)
              

def assignment():
    AssignmentForm = Tk()
    AssignmentForm.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
    AssignmentForm.resizable(0, 0)
    AssignmentForm.title('Assignment Page')
    AssignmentForm.config(bg='white')

    AHframe = Frame(AssignmentForm, height=80, width=1280, bg='#3C6739').place(relx=0, y=0)

    LAssignment = Label(AssignmentForm, font=('Roboto', 30, 'bold'), text="GIẢNG VIÊN . " + str(s) + "  - UPLOAD BÀI TẬP", bg='white').place(relx=0.26,
                                                                                                        y=100)
    HeadingMessage = Label(AssignmentForm, font=('Roboto', 15, 'bold'),text='VUI LÒNG ĐIỀN THÔNG TIN BÀI TẬP CẦN TẠO!',bg='white').place(relx=0.34, y=150)
    
    global EAssignment_No
    global ETitle
    global EContent
    global Subject
    global deadline
    global post_date
    global EA_No
    global ETitle_val
    global Subject_val
    global EContent_val
    EA_No = StringVar()
    ETitle_val = StringVar()
    EContent_val = StringVar()
    Subject = StringVar()
    deadline =StringVar()
    post_date = StringVar()
    def pick_date():
        def select_date():
            print("Deadline:",cal.selection_get())
            deadline = cal.selection_get()
            LDeadline = Label(AssignmentForm,font=('Roboto', 10, 'bold'),text = deadline,width = 10,bg='white')
            LDeadline.place(relx=0.5, rely=0.3)
            print(deadline)
            return str(deadline)
        top = Toplevel()
        cal = Calendar(top, font="Roboto 14", selectmode='day', locale='en_US',
               cursor="hand1")
        cal.pack(fill="both", expand=True)
        ttk.Button(top, text="ok", command=select_date).pack()  

    Body = Frame(AssignmentForm, bg='#F0F0F0', height = 475, width= 1000).place(relx=0.12, rely=0.28)
    LDate = Label(AssignmentForm, text='Ngày đăng', font= ('Roboto', 10, 'bold')).place(relx=0.14, rely=0.3)
    DateofOrder = StringVar()
    DateofOrder.set(time.strftime("%y-%m-%d"))
    print("post_date:",time.strftime("%y-%m-%d"))
    post_date = time.strftime("%y-%m-%d")
    lblDateofOrder = Label(AssignmentForm, width = 10, font=('Roboto', 10, 'bold'), text=post_date, padx=2, pady=2, bd=2,fg='black', bg='white', relief='sunken').place(relx=0.25, rely=0.3)    
    B_Deadline=ttk.Button(AssignmentForm, text='Deadline', command=pick_date).place(relx = 0.4,rely = 0.3)
    #deadline.set(deadline)
    

    LAssignment_No = Label(AssignmentForm, text='Số thứ tự bài tập', font= ('Roboto', 10, 'bold')).place(relx=0.14 , rely=0.36)
    EAssignment_No = ttk.Entry(AssignmentForm,width = 10, textvariable = EA_No,font= ('Roboto', 14))
    EAssignment_No.place(relx=0.14, rely=0.39)

    LSubject = Label(AssignmentForm, text='Môn học', font= ('Roboto', 10, 'bold')).place(relx=0.52, rely=0.36)
    Subject = ttk.Combobox(AssignmentForm, state='readonly',font= ('Roboto', 14))
    Subject['values'] =  ('', results_course[0][1], results_course[0][2], results_course[0][3], results_course[0][4], results_course[0][5])
    Subject.current(0)
    Subject.place(relx=0.52, rely=0.39)
    
    #self.ESubject_name = ttk.Entry(textvariable = Program, width = 40, font = ('Roboto', 14)).place(relx=0.52, rely=0.39)

    LTitle = Label(AssignmentForm, text='Tiêu đề bài tập', font = ('Roboto', 10, 'bold')).place(relx=0.14, rely=0.45)
    ETitle = ttk.Entry(AssignmentForm,width=30,textvariable = ETitle_val, font=('Roboto', 14))
    ETitle.place(relx=0.14, rely=0.48)

    LContent = Label(AssignmentForm, text = 'Nội dung bài tập', font = ('Roboto', 10, 'bold')).place(relx=0.14, rely=0.54)
    EContent = ttk.Entry(AssignmentForm,textvariable = EContent_val, width = 60, font = ('Roboto', 14))
    EContent.place(relx=0.14, rely=0.57)

    BSubmit = ttk.Button(AssignmentForm,text='Đăng bài tập', command = add_assignment,width=20).place(relx=0.5, rely=0.69)
    BReset = ttk.Button(AssignmentForm, text='Làm mới', command = reset_assignment,width=20).place(relx=0.4, rely=0.69)
    BHome = ttk.Button(AssignmentForm,text='Back',command = back ,width=20).place(relx=0.3, rely=0.69)

def add_assignment():
    if EAssignment_No.get() == "" or ETitle.get() == "" or EContent.get() == "" or Subject.get() == "" or post_date == "":
        messagebox.showinfo("Requirment!", "Vui lòng điền đầy đủ thông tin!")
    else:
        Database_assignment()
        cursor.execute("INSERT INTO 'assignment' (post_no, post_pf_name, post_date, deadline, subject, title, content) VALUES(?, ?, ?, ?, ?, ?, ?)",  (str(EAssignment_No.get()), str(s),str(post_date), str(deadline), str(Subject.get()), str(ETitle.get()), str(EContent.get())))
        conn.commit()
        messagebox.showinfo("Thành công!", "Thêm bài tập thành công!.")
def reset_assignment():
    print('reset')
    
 

def file_upload():
    File_Upload_Form = Tk()
    File_Upload_Form.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
    File_Upload_Form.resizable(0, 0)
    File_Upload_Form.title('Trang upload file')
    File_Upload_Form.config(bg='white')

    AHframe = Frame(File_Upload_Form, height=80, width=1280, bg='#3C6739').place(relx=0, y=0)

    LTitle = Label(File_Upload_Form, font=('Roboto', 30, 'bold'), text="Professor . " + str(s) + "  : Upload FIle", bg='white').place(relx=0.26,
                                                                                                        y=100)
    HeadingMessage = Label(File_Upload_Form, font=('Roboto', 15, 'bold'),text='Vui lòng chọn và upload file',bg='white').place(relx=0.45, y=150)
    FBody = Frame(File_Upload_Form, bg='#F0F0F0', height = 475, width= 1000).place(relx=0.12, rely=0.28)
    global T_file_path
    #T_file_path = StringVar()
    #name = StringVar()
    def OpenFile():
        name = askopenfilename(initialdir="/",
                           filetypes =(("Text File", "*.txt"),("All Files","*.*")),
                               title = "Choose a file.")
        T_file_path.insert(END,name)
        print('selected_file_path:',name)
        #return name

    B_FileSelect = Button(File_Upload_Form, text='Chọn file', width=9, height=2, bg='#3C6739', fg='white',
                                      font=('arial black', 10), bd=6, command = OpenFile).place(x=580, rely=0.35)             
    L_file_path = Label(File_Upload_Form, text='Tên file đã chọn', font = ('arial', 10, 'bold')).place(x=570, rely=0.5)
    T_file_path = Text(File_Upload_Form, height=2, width=60)
    T_file_path.place(x = 370, rely = 0.55)
    
    def view_file():
        root = Tk()
        name = str(T_file_path.get('1.0',END))
        name = name.strip()
        with open(name, "r") as f:
            Label(root, text=f.read()).pack()    
        root.mainloop()
    
    def save_file():
        name = str(T_file_path.get('1.0',END))
        name = name.strip()
        Database_upload_file()
        cursor.execute("INSERT INTO 'uploaded_file' (pf_id, pf_name, uploaded_file_path) VALUES(?, ?, ?)",  (results[0][0], str(s),name))
        conn.commit()
        messagebox.showinfo("Thành công!", "Up load đường dẫn file thành công!.")
        
    
    B_file_content = Button(File_Upload_Form, text='Xem nội dung file', width = 15,height = 2,bg='#3C6739', fg='white',
                            font = ('arial black', 10),bd=6,command = view_file).place(x=570, rely=0.65)
    B_save_file = Button(File_Upload_Form, text='Lưu đường dẫn file', width = 15,height = 2,bg='#3C6739', fg='white',
                            font = ('arial black', 10),bd=6,command = save_file).place(x=570, rely=0.75)    
    

def file_retrieve():
    File_Upload_Form = Tk()
    File_Upload_Form.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
    File_Upload_Form.resizable(0, 0)
    File_Upload_Form.title('File_Upload Page')
    File_Upload_Form.config(bg='white')

    AHframe = Frame(File_Upload_Form, height=80, width=1280, bg='#3C6739').place(relx=0, y=0)

    LTitle = Label(File_Upload_Form, font=('Roboto', 30, 'bold'), text="St . " + str(st) + "  : File_Retrieve", bg='white').place(relx=0.26,
                                                                                                        y=100)
    HeadingMessage = Label(File_Upload_Form, font=('arial', 15, 'bold'),text='Please Retrieve All Uploaded Files',bg='white').place(relx=0.34, y=150)
    FBody = Frame(File_Upload_Form, bg='#F0F0F0', height = 475, width= 1000).place(relx=0.12, rely=0.28)
    
    global tree
    
    scrollbary = Scrollbar(File_Upload_Form, orient=VERTICAL)
    scrollbarx = Scrollbar(File_Upload_Form, orient=HORIZONTAL)
    tree = ttk.Treeview(File_Upload_Form, columns=(
        "pf_id", "professor_name","uploaded_file_path"),
                        selectmode="extended", height=10, yscrollcommand=scrollbary.set,
                        xscrollcommand=scrollbarx.set)
    scrollbary.config(command=tree.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=tree.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)
    tree.heading('pf_id', text="Professor_ID", anchor=W)
    tree.heading('professor_name', text="Professor Name", anchor=W)
    tree.heading('uploaded_file_path', text="Uploaded File Path", anchor=W)
    
    tree.column('#0', stretch=NO, minwidth=0, width=0)
    tree.column('#1', stretch=NO, minwidth=0, width=300)
    tree.column('#2', stretch=NO, minwidth=0, width=300)
    
    tree.place(x=250, rely=0.4)
    Database_upload_file()
    finduser = ("SELECT * FROM `uploaded_file` WHERE 1 == 1")
    cursor.execute(finduser)
    fetch = cursor.fetchall()
    for data in fetch:
        tree.insert('', 'end', values=(data[0], data[1], data[2]))
    cursor.close()
    conn.close()

win = Tk()
window_height = 620
window_width = 1200

screen_width = win.winfo_screenwidth()
screen_height = win.winfo_screenheight()

x_cordinate = int((screen_width/2) - (window_width/2))
y_cordinate = int((screen_height/3) - (window_height/3))

win.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
# win.geometry("1200x620+0+0")
win.config(bg='white')
win.title("QUẢN LÝ SINH VIÊN - TRANG CHỦ")
win.resizable(0,0)

_Header = PhotoImage(file='Header.png')
_HeaderLabel = Label(win, image = _Header, height=300, width=300).place(x=100, y=2000)
_Footer = PhotoImage(file ="FOOTER.gif")
# _HeadLabel = Label(win, text='abc', width=100, height=100, bg='#3C6739').place(x=-5500, y=1000)
_background = PhotoImage(file='Background.gif')
_image = PhotoImage(file='HomeBackground.gif')

_IconAdminButton = PhotoImage(file="AdminIcon.gif")
_IconTeacherButton = PhotoImage(file="TeacherIcon.gif")
_IconStudentButton = PhotoImage(file='StudentIcon.gif')

_Label1 = Label(win, image=_background).place(x=0, y=0)
_Label2 = Label(win, image=_image). place(relx=0.5, rely=0.5, anchor = 'center', height = 450, width = 920)

_AdminButton = Button(win, image=_IconAdminButton, text='Admin', width=200, height=235, bg='#3C6739', command = AdminLogin).place(x=300, rely=0.5, anchor = 'center')
_AdminLabel = Label(win, text='QUẢN TRỊ VIÊN', font=('Roboto', 20, 'bold')).place(x=205, y=480)

_TeacherButton = Button(win, image=_IconTeacherButton, text='Teacher', width=200, height=235, bg='#3C6739', command = TeacherLogin).place(x=620, rely=0.5, anchor = 'center')
_TeacherLabel = Label(win, text='GIẢNG VIÊN', font=('Roboto', 20, 'bold')).place(x=545, y=480)


_StudentButton = Button(win, image=_IconStudentButton, text='Student', width=200, height=235, bg='#3C6739', command= StudentLogin).place(x=910, rely=0.5, anchor = 'center')
_StudentButton = Label(win, text='SINH VIÊN', font=('Roboto', 20, 'bold')).place(x=850, y=480)

_HeaderLabel = Label(win, image=_Header, text='Teacher', width=1200, height=80,bg='#fff').place(x=0, rely=0)
_FooterLabel = Label(win, image = _Footer,height=40, width=1277, bg='#3C6739').place(x = 0.5, y = 677)

win.mainloop()


