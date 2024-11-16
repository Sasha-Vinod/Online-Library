from tkinter.font import *
from tkinter import *
from tkinter.messagebox import *
from PIL import ImageTk,Image
from pickle import *
import mysql.connector as mysql
from datetime import *
def my_program():
    def register():
        mainscr.destroy()   
        global register_screen
        register_screen=Tk()
        font_1=Font(family='Arial', size=24, weight='bold')
        register_screen.attributes('-fullscreen', True)
        register_screen.title("Register Fast")
        can_1=Canvas(register_screen,width=1000,height=1000)
        can_1.pack(fill=BOTH, expand = True)
        def terms():
            term=Tk()
            term.attributes('-fullscreen', True)
            term.title("Terms And Conditions")
            f=open('..\\project\\files\\terms&conditions.dat','rb')
            c=0
            Label(term,text='\n\n\n').pack()
            font_1=Font(family='Arial', size=30, weight='bold',underline=1)
            font_2=Font(family='Helvetica', size=18, weight='normal')
            def cancel():
                term.destroy()
            while True:
                d=0
                
                try:
                    x=load(f)
                    if x.isupper():
                        Label(term,text=x,font=font_1).pack()
                        c+=1
                    else:
                        c+=1
                        Label(term,text=x,font=font_2).pack()
                except EOFError:
                    break
            b=Button(term,text="Exit",fg='Red',width=10,height=2,font=font_4,command=cancel).pack()
            f.close()
        def cancel():
            register_screen.destroy()
            mainscreen()
        def checkterms():
            if var.get()==1:
                register_storing()
            else:
                showerror('Online Library','Accept Terms and Condiitions')
        global username,userfirstname,userlastname,usercontactno,useremailid
        global passwd,firstname,lastname,contactno,emailid
        global userinput
        global userpassinput,userpasscon
        username = StringVar()
        paswd = StringVar()
        conpaswd=StringVar()
        firstname= StringVar()
        lastname= StringVar()
        contactno= StringVar()
        emailid=StringVar()
        
        font_1=Font(family='Arial', size=30, weight='bold')
        font_2=Font(family='Helvetica', size=18, weight='bold')
        font_3=Font(family='Helvetica', size=12, weight='bold')
        font_4=Font(family='Arial', size=16, weight='bold')
        font_5=Font(family='Arial', size=16, weight='normal',underline =1)

        register_screen.one=img_1=ImageTk.PhotoImage(Image.open('..\\project\\files\\bgreg_final.jpg'))
        can_1.create_image(0,0,anchor=NW,image=img_1)
        can_1.create_text(700,50,text='Please enter registeration details:',fill='Red',font=font_1)
        def toggle_pass():
            global userpassinput,cb
            if cb.var.get():
                userpassinput['show']=''
                userpasscon['show']=''
            else:
                userpassinput['show']='*'
                userpasscon['show']='*'
        userinput=Entry(register_screen,textvariable=username,font=font_2)
        userpassinput = Entry(register_screen,textvariable=paswd,font=font_2)
        userpasscon=Entry(register_screen,textvariable=conpaswd,font=font_2)
        userpassinput['show']='*'
        userpasscon['show']='*'
        userpassinput.default_show_val=userpassinput['show']
        userpasscon.default_show_val=userpasscon['show']
        global cb
        cb=Checkbutton(register_screen,text='Show Password',onvalue=True,offvalue=False,comman=toggle_pass)
        cb.var=BooleanVar(value=False)
        cb['variable']=cb.var
        userfirstname = Entry(register_screen,textvariable=firstname,font=font_2)
        userlastname = Entry(register_screen,textvariable=lastname,font=font_2)
        usercontactno = Entry(register_screen,textvariable=contactno,font=font_2)
        useremailid = Entry(register_screen,textvariable=emailid,font=font_2)
 
        can_1.create_text(160,130,text='Enter Username:',fill='Orange',font=font_2)
        can_1.create_window( 300, 110,anchor = "nw",window = userinput)
         
        can_1.create_text(160,180,text='Enter Password:',fill='Orange',font=font_2)
        can_1.create_window( 300, 160,anchor = "nw",window = userpassinput)
        can_1.create_text(800,230,text='Note: Password must contain atleast 2 small case letters,\n\
2 uppercase letters, 2 numbers and 2 symbols',fill='Yellow',font=font_3)
        can_1.create_text(800,180,text='Confirm Password:',fill='Orange',font=font_2)
        can_1.create_window( 950, 160,anchor = "nw",window = userpasscon)
        can_1.create_window( 200, 230,anchor = "nw",window = cb)
        
        can_1.create_text(160,310,text='Enter First Name:',fill='Orange',font=font_2)
        can_1.create_window( 300, 290,anchor = "nw",window = userfirstname)

        can_1.create_text(160,360,text='Enter Last Name:',fill='Orange',font=font_2)
        can_1.create_window( 300, 340,anchor = "nw",window = userlastname)

        can_1.create_text(160,410,text='Enter Contact Number:',fill='Orange',font=font_2)
        can_1.create_window( 300, 390,anchor = "nw",window = usercontactno)

        can_1.create_text(160,460,text='Enter Email ID:',fill='Orange',font=font_2)
        can_1.create_window( 300, 440,anchor = "nw",window = useremailid)
        
        var=IntVar()
        
        w=Button(register_screen,text="Terms and Conditions",bg='Cyan',fg='Red',width=20,font=font_5,command=terms)
        can_1.create_window( 900, 409,anchor = "nw",window = w)
        
        y=Checkbutton(register_screen,text='I Agree to Terms and Conditions',font=font_3,variable=var, onvalue=1, offvalue=0)
        can_1.create_window( 900, 450,anchor = "nw",window = y)
        
        b1=Button(register_screen,text="Register\
",width=10,height=2,bg='Cyan',fg='Red',font=font_4,command=checkterms)
        c=can_1.create_window( 120, 600,anchor = "nw",window = b1)
        
        b2=Button(register_screen,text="Cancel",bg='Cyan',fg='Red',width=10,height=2,font=font_4,command=cancel)
        can_1.create_window( 900, 600,anchor = "nw",window = b2)


    def register_storing():
        username = str(userinput.get())
        password = str(userpassinput.get())
        passcon=str(userpasscon.get())
        firstname=str(userfirstname.get())
        lastname=str(userlastname.get())
        contactno=str(usercontactno.get())
        mailid=str(useremailid.get())
        def check_pass(s):
            l=u=n=sy=0
            if len(s)>=8 and len(s)<=15:
                for x in s:
                    if x.isalpha():
                        if x.islower():
                            l+=1
                        elif x.isupper():
                            u+=1
                    elif x.isdigit():
                        n+=1
                    else:
                        sy+=1
                if l>=2 and u>=2 and n>=2 and sy>=2:
                    return (True,)
                else:
                    return (False,'Note: Password must contain atleast 2 small case letters,\n\
2 uppercase letters, 2 numbers and 2 symbols')
            else:
                return (False,'Password must contain minimum 8 characters and maximum 15 characters')
        def check_no(n):
            if n.isdigit():
                if len(n)==10:
                    return (True,)
                else:
                    return (False,'Contact No. must contain exactly 10 digits')
            else:
                return (False,'Contact No. must contain only numbers')
        def check_mail(m):
            if '@' in m and '.com' in m:
                return (True,)
            else:
                return (False,'Invalid mail ID')
        if(username == "" or password == ""or firstname=='' or lastname=='' or contactno=='' or mailid==''):                  
            showwarning("Online book store","All fields are mandatory\nPlease Ensure that all fields are filled")
        else:
            global cur,con
            q='select username from userdetails'
            cur.execute(q)
            r=cur.fetchall()
            l=[]
            for a in r:
                l.append(a[0])
            if username in l:
                showwarning("Online book store","This user name is already taken\nPlease use some other username.")
            else:
                a=check_pass(password)
                b=check_no(contactno)
                c=check_mail(mailid)
                if a[0]:
                    if password==passcon:
                        if b[0]:
                            if c[0]:
                                q='insert into userdetails values\
("'+username+'","'+password+'","'+firstname+'","'+lastname+'","'+contactno+'"    ,"'+mailid+'")'
                                cur.execute(q)
                                q='insert into userbooks  (UserName) values ("'+username+'")'
                                cur.execute(q)
                                con.commit()
                                showinfo("Online Book Store","Successfully registered you can login now !!!")
                                register_screen.destroy()
                                mainscreen()
                            else:
                                showerror("Online book store",c[1])
                        else:
                            showerror("Online book store",b[1])
                    else:
                        showerror("Online book store",'Passwords do not match')
                else:
                    showerror("Online book store",a[1])                
    def login():
        mainscr.destroy()
        global login_screen
        login_screen=Tk()
        login_screen.attributes('-fullscreen', True)
        login_screen.title("Login to continue ur reading")
        font_1=Font(family='Arial', size=30, weight='bold')
        font_2=Font(family='Helvetica', size=18, weight='bold')
        font_3=Font(family='Arial', size=16, weight='normal')
        can_1=Canvas(login_screen,width=1000,height=1000)
        can_1.pack(fill=BOTH, expand = True)
        login_screen.one=img_1=ImageTk.PhotoImage(Image.open('..\\project\\files\\bglog.jpg'))
        can_1.create_image(0,0,anchor=NW,image=img_1)
        
        can_1.create_text(500,100,text='Please enter the details to login',fill='Cyan',font=font_1)

        def toggle_pass():
            global userpassin,cb1
            if cb1.var.get():
                userpassin['show']=''
            else:
                userpassin['show']='*'
        global username
        global passwd
        global userinput
        global userpassin
        username = StringVar()
        paswd = StringVar()
        can_1.create_text(160,200,text='Username/Email ID *:',fill='Orange',font=font_2)
        userinput = Entry(login_screen,textvariable=username,font=font_2)
        can_1.create_window( 300, 180,anchor = "nw",window = userinput)
        can_1.create_text(160,250,text='Password *:',fill='Orange',font=font_2)
        userpassin = Entry(login_screen,textvariable=paswd,font=font_2)
        userpassin['show']='*'
        userpassin.default_show_val=userpassin['show']
        can_1.create_window( 300, 230,anchor = "nw",window = userpassin)     
        global cb1
        cb1=Checkbutton(login_screen,text='Show Password',onvalue=True,offvalue=False,comman=toggle_pass)
        cb1.var=BooleanVar(value=False)
        cb1['variable']=cb1.var
        can_1.create_window( 300, 280,anchor = "nw",window = cb1)
        def reg():
            login_screen.destroy()
            register()
        def cancel():
            login_screen.destroy()
            mainscreen()
        b1=Button(login_screen,text="Login",width=10,height=2,command=verification_storing,font=font_3)
        b2=Button(login_screen,text="Cancel",width=10,height=2,command=cancel,font=font_3)
        can_1.create_window( 100, 350,anchor = "nw",window = b1)
        can_1.create_window( 300, 350,anchor = "nw",window = b2)
                 
    

    def verification_storing():
        global un,cur
        un=userinput.get()
        pw=userpassin.get()
        if (un=="" or pw=="") or un.isspace() or pw.isspace():
            showerror("Online book store","username or password field should not be empty")
        else:
            def success():
                showinfo("online book store","login success")
                login_screen.destroy()
                user_homescreen()
            def fail():
                showwarning("Online book store","Username and password do not match\nPlease Try Again")
            userlist=[]
            emaillist=[]
            q='select Username,EmailId from userdetails'
            cur.execute(q)
            c=cur.fetchall()
            for a in c:
                userlist.append(a[0])
                emaillist.append(a[1])
            if un in userlist or un in emaillist:
                if '@' in un and '.com' in un:
                    q='select Password from userdetails where EmailID = "'+un+'"'
                    cur.execute(q)
                    c=cur.fetchall()
                    for a in c:
                        if a[0]==pw:
                            success()
                        else:
                            fail()
                else:
                        q='select Password from userdetails where UserName = "'+un+'"'
                        cur.execute(q)
                        c=cur.fetchall()
                        for a in c:
                            if a[0]==pw:
                                success()
                            else:
                                fail()
            else:
                    showerror("Online book store","No such username exists\nPlease try again or create an account")

    def user_books():
        global userhmscr
        userhmscr.destroy()
        user_bookscr=Tk()
        user_bookscr.attributes('-fullscreen', True)
        user_bookscr.title("Online Library")
        can_1=Canvas(user_bookscr,width=1000,height=1000)
        can_1.pack(fill=BOTH, expand = True)
        font_1=Font(family='Arial', size=30, weight='bold')
        font_2=Font(family='Helvetica', size=18, weight='bold')
        user_bookscr.one=img_1=ImageTk.PhotoImage(Image.open('..\\project\\files\\bgusrbkscr.jpg'))
        can_1.create_image(0,0,anchor=NW,image=img_1)
        #Insert Code Here



        
        def cancel():
            user_bookscr.destroy()
            user_homescreen()
        b1=Button(user_bookscr,text="Back to homescreen",height="1",width="20",bg="orange",font=font_2,command=cancel)
        b1_can = can_1.create_window( 1000, 50,anchor = "nw",window = b1)
    def shop_books():
        global shop
        userhmscr.destroy()
        shop=Tk()
        shop.attributes('-fullscreen', True)
        shop.title("Online Library")
        can_1=Canvas(shop,width=1000,height=1000)
        can_1.pack(fill=BOTH, expand = True)
        font_1=Font(family='Arial', size=30, weight='bold')
        font_2=Font(family='Helvetica', size=18, weight='bold')
        shop.one=img_1=ImageTk.PhotoImage(Image.open('..\\project\\files\\bgshop.jpg'))
        can_1.create_image(0,0,anchor=NW,image=img_1)
        #Insert Code Here





        
        def cancel():
            shop.destroy()
            user_homescreen()
        b1=Button(shop,text="Back to homescreen",height="1",width="20",bg="orange",font=font_2,command=cancel)
        b1_can = can_1.create_window( 1000, 50,anchor = "nw",window = b1)
    def user_homescreen():
        global userhmscr
        userhmscr=Tk()
        font_1=Font(family='Arial', size=30, weight='bold')
        userhmscr.attributes('-fullscreen', True)
        userhmscr.title("Online Library")
        can_1=Canvas(userhmscr,width=1000,height=1000)
        can_1.pack(fill=BOTH, expand = True)
        font_1=Font(family='Arial', size=30, weight='bold')
        font_2=Font(family='Helvetica', size=18, weight='bold')
        userhmscr.one=img_1=ImageTk.PhotoImage(Image.open('..\\project\\files\\bgpl.jpg'))
        can_1.create_image(0,0,anchor=NW,image=img_1)
        global un
        t='Welcome '+str(un) +'!!!'
        can_1.create_text(350,200,text=t,fill='Yellow',font=font_1)
        def tick():
            date = datetime.now().strftime('%d/%m/%y')
            time=datetime.now().strftime('%H:%M:%S')
            clock.config(text='Date:  '+date+'\n\nTime: '+time)
            clock.after(200, tick)
        clock = Label(userhmscr, font=("none", 30, "bold"), bg="blue", fg="red", bd=5, relief="ridge")
        can_1.create_window( 900, 300, anchor = "nw",window=clock)
        tick()
        def cancel():
            userhmscr.destroy()
            mainscreen()
        b1=Button(userhmscr,text="Your Books",height="3",font=font_2,width="20",fg='white',bg="red",command=user_books)
        b2=Button(userhmscr,text="Shop Books",height="3",width="20",fg='white',bg="red",font=font_2,command=shop_books)
        b3=Button(userhmscr,text="Log Out",height="1",width="10",bg="orange",font=font_2,command=cancel)
        b1_can = can_1.create_window( 100, 450,anchor = "nw",window = b1)
        b2_can = can_1.create_window( 500, 450, anchor = "nw",window = b2)
        b3_can = can_1.create_window( 900, 100, anchor = "nw",window = b3)        
        
        
    def mainscreen():
        global mainscr
        mainscr = Tk()      
        mainscr.attributes('-fullscreen', True)
        mainscr.title("Online Library")
        can_1=Canvas(mainscr,width=1000,height=1000)
        can_1.pack(fill =BOTH, expand = True)
        img=ImageTk.PhotoImage(Image.open('..\\project\\files\\bg.jpg'))
        font_1=Font(family='Arial', size=30, weight='bold')
        font_2=Font(family='Helvetica', size=18, weight='bold')
        can_1.create_image(0,0,anchor=NW,image=img)
        can_1.create_text(700,170,text='Welcome to Virtual Library',fill='Red',font=font_1)
        def cancel():
            mainscr.destroy()
        b1=Button(mainscr,text="Login",height="1",font=font_2,width="10",bg="yellow",command=login)
        b2=Button(mainscr,text="Register",height="1",width="10",bg="cyan",font=font_2,command=register)
        b3=Button(mainscr,text="Exit",height="1",width="10",bg="orange",font=font_2,command=cancel)
        b1_can = can_1.create_window( 500, 250,anchor = "nw",window = b1)
        b2_can = can_1.create_window( 700, 250, anchor = "nw",window = b2)
        b3_can = can_1.create_window( 600, 400, anchor = "nw",window = b3)
        mainscr.mainloop()
    mainscreen()
con=mysql.connect(host='localhost',user='root',password='mysqlp',database='project')
if con.is_connected():
    global cur
    cur=con.cursor()
    my_program()
else:
    print('Error in MySQL connection')
