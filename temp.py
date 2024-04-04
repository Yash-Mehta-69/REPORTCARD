

from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk
import tkinter as tk
import mysql.connector as con
from tkinter import messagebox
from ttkwidgets.autocomplete import AutocompleteEntry
import ast


mydb = con.connect(host="localhost",user="root",password="yash1234",database="airport_school1")
cur = mydb.cursor()

class LoginPage:
    def __init__(self, window):
        self.window = window
        self.screen_width = self.window.winfo_screenwidth()
        self.screen_height = self.window.winfo_screenheight()
        # self.window.geometry(f'{self.screen_width}x{self.screen_height}')
        self.window.state('zoomed')
        self.window.resizable(0, 0)
        self.window.title('Login Page')

        # Create the login frame
        self.create_login_frame()

    def create_login_frame(self):

        # Load and resize background image
        self.bg_frame = Image.open('images\\background1.png')
        self.bg_frame = self.bg_frame.resize((self.screen_width, self.screen_height), Image.LANCZOS)
        self.bg_photo = ImageTk.PhotoImage(self.bg_frame)

        # Background panel
        self.bg_panel = Label(self.window, image=self.bg_photo)
        self.bg_panel.place(x=0, y=0, relwidth=1, relheight=1)


        # ====== Login Frame =========================
        login_frame_width = 1000
        login_frame_height = 650
        login_frame_x = (self.screen_width - login_frame_width) // 2
        login_frame_y = (self.screen_height - login_frame_height) // 2
        self.login_frame = Frame(self.window, width=login_frame_width, height=login_frame_height, bg="#FFFFF0")
        self.login_frame.place(x=login_frame_x, y=login_frame_y)
        self.lgn_frame = Frame(self.window, bg='#FFFFF0', width=login_frame_width, height=login_frame_height)
        self.lgn_frame.place(x=login_frame_x, y=login_frame_y)

        # ========================================================================
        # ========================================================
        # ========================================================================
        self.txt = "WELCOME"
        self.heading = Label(self.lgn_frame, text=self.txt, font=('yu gothic ui', 25, "bold"), bg="#FFFFF0",
                             fg='#4f4e4d',
                             bd=5,
                             relief=FLAT)
        self.heading.place(x=80, y=30, width=300, height=30)

        # ========================================================================
        # ============ Left Side Image ================================================
        # ========================================================================
        self.side_image = Image.open('images\\vector.png')
        photo = ImageTk.PhotoImage(self.side_image)
        self.side_image_label = Label(self.lgn_frame, image=photo, bg='#FFFFF0')
        self.side_image_label.image = photo
        self.side_image_label.place(x=5, y=100)

        # ========================================================================
        # ============ Sign In Image =============================================
        # ========================================================================
        self.sign_in_image = Image.open('images\\hyy.png')
        photo = ImageTk.PhotoImage(self.sign_in_image)
        self.sign_in_image_label = Label(self.lgn_frame, image=photo, bg='#FFFFF0')
        self.sign_in_image_label.image = photo
        self.sign_in_image_label.place(x=620, y=100)

        # ========================================================================
        # ============ Sign In label =============================================
        # ========================================================================
        self.sign_in_label = Label(self.lgn_frame, text="Sign In", bg="#FFFFF0", fg="#4f4e4d",
                                    font=("yu gothic ui", 17, "bold"))
        self.sign_in_label.place(x=650, y=210)

        # ========================================================================
        # ============================username====================================
        # ========================================================================
        self.username_label = Label(self.lgn_frame, text="Username", bg="#FFFFF0", fg="#4f4e4d",
                                    font=("yu gothic ui", 13, "bold"))
        self.username_label.place(x=550, y=270)

        self.username_entry = Entry(self.lgn_frame, highlightthickness=0, relief=FLAT, bg="#FFFFF0", fg="#6b6a69",
                                    font=("yu gothic ui ", 12, "bold"), insertbackground = '#6b6a69')
        self.username_entry.place(x=580, y=305, width=270)

        self.username_line = Canvas(self.lgn_frame, width=300, height=2.0, bg="#bdb9b1", highlightthickness=0)
        self.username_line.place(x=550, y=331)
        # ===== Username icon =========
        self.username_icon = Image.open('images\\username_icon.png')
        photo = ImageTk.PhotoImage(self.username_icon)
        self.username_icon_label = Label(self.lgn_frame, image=photo, bg='#FFFFF0')
        self.username_icon_label.image = photo
        self.username_icon_label.place(x=550, y=302)




        # ========================================================================
        # ============================password====================================
        # ========================================================================
        self.password_label = Label(self.lgn_frame, text="Password", bg="#FFFFF0", fg="#4f4e4d",
                                    font=("yu gothic ui", 13, "bold"))
        self.password_label.place(x=550, y=350)

        self.password_entry = Entry(self.lgn_frame, highlightthickness=0, relief=FLAT, bg="#FFFFF0", fg="#6b6a69",
                                    font=("yu gothic ui", 12, "bold"), show="*", insertbackground = '#6b6a69')
        self.password_entry.place(x=580, y=386, width=244)

        self.password_line = Canvas(self.lgn_frame, width=300, height=2.0, bg="#bdb9b1", highlightthickness=0)
        self.password_line.place(x=550, y=412)
        # ======== Password icon ================
        self.password_icon = Image.open('images\\password_icon.png')
        photo = ImageTk.PhotoImage(self.password_icon)
        self.password_icon_label = Label(self.lgn_frame, image=photo, bg='#FFFFF0')
        self.password_icon_label.image = photo
        self.password_icon_label.place(x=550, y=384)
        # ========= show/hide password ==================================================================
        self.show_image = ImageTk.PhotoImage \
            (file='images\\show.png')

        self.hide_image = ImageTk.PhotoImage \
            (file='images\\hide.png')

        self.show_button = Button(self.lgn_frame, image=self.show_image, command=self.show, relief=FLAT,
                                  activebackground="white"
                                  , borderwidth=0, background="white", cursor="hand2")
        self.show_button.place(x=860, y=390)






        # ========================================================================
        # ============================login button================================
        # ========================================================================


        def login_users():
            self.username = self.username_entry.get()
            self.password = self.password_entry.get()
            # print(self.username , self.password)


            cur.execute("select * from teachers where TUSERNAME=%s and TPASSWORD=%s and isApproved=1", (self.username, self.password))
            user = cur.fetchone()
            print(user)
            if user:
                messagebox.showinfo("Success", "Login successful!")
                if user[0] == 'admin' and user[1] == "Admin@321" and user[2] == None and user[3] == None and user[4] == 1:
                    admin_main(self.window)
                    # entry_page(self.window)
                else:
                    teacher_main(user,self.window)
            else:
                messagebox.showerror("ERROR", "Invalid Id Or Password or Wait for Admin's Approval")



        self.lgn_button = Image.open('images\\btn1.png')
        photo = ImageTk.PhotoImage(self.lgn_button)
        self.lgn_button_label = Label(self.lgn_frame, image=photo, bg='#FFFFF0')
        self.lgn_button_label.image = photo
        self.lgn_button_label.place(x=550, y=450)
        self.login = Button(self.lgn_button_label, text='LOGIN', font=("yu gothic ui", 13, "bold"), width=25, bd=0,
                            bg='#3047ff', cursor='hand2', command = login_users,activebackground='#3047ff', fg='white')
        self.login.place(x=20, y=10)

        # ========================================================================
        # =========== Sign Up ==================================================
        # ========================================================================


        self.sign_label = Label(self.lgn_frame, text='No account yet?', font=("yu gothic ui", 11, "bold"),
                                relief=FLAT, borderwidth=0, background="#FFFFF0", fg='#4f4e4d')
        self.sign_label.place(x=580, y=560)

        self.signup_img = ImageTk.PhotoImage(file='images\\register.png')
        self.signup_button_label = Button(self.lgn_frame, image=self.signup_img, bg='#98a65d', cursor="hand2",
                                          borderwidth=0, background="#FFFFF0", command = self.signup_page, activebackground="#FFFFF0")
        self.signup_button_label.place(x=720, y=555, width=111, height=35)

    def show(self):
        self.hide_button = Button(self.lgn_frame, image=self.hide_image, command=self.hide, relief=FLAT,
                                  activebackground="white"
                                  , borderwidth=0, background="white", cursor="hand2")
        self.hide_button.place(x=860, y=390)
        self.password_entry.config(show='')

    def hide(self):
        self.show_button = Button(self.lgn_frame, image=self.show_image, command=self.show, relief=FLAT,
                                  activebackground="white"
                                  , borderwidth=0, background="white", cursor="hand2")
        self.show_button.place(x=860, y=390)
        self.password_entry.config(show='*')
        




    def signup_page(self):
        self.login_frame.destroy()  # Destroy the login frame
        signup_frame_width = 1000
        signup_frame_height = 650
        signup_frame_x = (self.screen_width - signup_frame_width) // 2
        signup_frame_y = (self.screen_height - signup_frame_height) // 2
        self.signup_frame = Frame(self.window, width=signup_frame_width, height=signup_frame_height, bg="#FFFFF0")
        self.signup_frame.place(x=signup_frame_x, y=signup_frame_y)
        self.sgnp_frame = Frame(self.window, bg='#FFFFF0', width=signup_frame_width, height=signup_frame_height)
        self.sgnp_frame.place(x=signup_frame_x, y=signup_frame_y)


        # ========================================================================
        # ========================================================
        # ========================================================================
        self.txt = "REGISTER"
        self.heading = Label(self.sgnp_frame, text=self.txt, font=('yu gothic ui', 25, "bold"), bg="#FFFFF0",
                             fg='#4f4e4d',
                             bd=5,
                             relief=FLAT)
        self.heading.place(x=80, y=30, width=300, height=30)

        # ========================================================================
        # ============ Left Side Image ================================================
        # ========================================================================
        self.side_image = Image.open('images\\vector.png')
        photo = ImageTk.PhotoImage(self.side_image)
        self.side_image_label = Label(self.sgnp_frame, image=photo, bg='#FFFFF0')
        self.side_image_label.image = photo
        self.side_image_label.place(x=5, y=100)

        # ========================================================================
        # ============ Sign Up Image =============================================
        # ========================================================================
        self.sign_up_image = Image.open('images\\add-friend.png')
        photo = ImageTk.PhotoImage(self.sign_up_image)
        self.sign_up_image_label = Label(self.sgnp_frame, image=photo, bg='#FFFFF0')
        self.sign_up_image_label.image = photo
        self.sign_up_image_label.place(x=640, y=30)

        # ========================================================================
        # ============ Sign In label =============================================
        # ========================================================================
        self.sign_in_label = Label(self.sgnp_frame, text="Sign Up", bg="#FFFFF0", fg="#4f4e4d",
                                    font=("yu gothic ui", 17, "bold"))
        self.sign_in_label.place(x=650, y=140)

        # ========================================================================
        # ============================username====================================
        # ========================================================================
        self.username_label = Label(self.sgnp_frame, text="Username", bg="#FFFFF0", fg="#4f4e4d",
                                    font=("yu gothic ui", 13, "bold"))
        self.username_label.place(x=550, y=200)

        self.username_entry = Entry(self.sgnp_frame, highlightthickness=0, relief=FLAT, bg="#FFFFF0", fg="#6b6a69",
                                    font=("yu gothic ui ", 12, "bold"), insertbackground = '#6b6a69')
        self.username_entry.place(x=580, y=235, width=270)

        self.username_line = Canvas(self.sgnp_frame, width=300, height=2.0, bg="#bdb9b1", highlightthickness=0)
        self.username_line.place(x=550, y=261)
        # ===== Username icon =========
        self.username_icon = Image.open('images\\username_icon.png')
        photo = ImageTk.PhotoImage(self.username_icon)
        self.username_icon_label = Label(self.sgnp_frame, image=photo, bg='#FFFFF0')
        self.username_icon_label.image = photo
        self.username_icon_label.place(x=550, y=232)


        # ========================================================================
        # ============================password====================================
        # ========================================================================
        self.password_label = Label(self.sgnp_frame, text="Password", bg="#FFFFF0", fg="#4f4e4d",
                                    font=("yu gothic ui", 13, "bold"))
        self.password_label.place(x=550, y=280)

        self.password_entry = Entry(self.sgnp_frame, highlightthickness=0, relief=FLAT, bg="#FFFFF0", fg="#6b6a69",
                                    font=("yu gothic ui", 12, "bold"), show="*", insertbackground = '#6b6a69')
        self.password_entry.place(x=580, y=316, width=244)

        self.password_line = Canvas(self.sgnp_frame, width=300, height=2.0, bg="#bdb9b1", highlightthickness=0)
        self.password_line.place(x=550, y=342)
        # ======== Password icon ================
        self.password_icon = Image.open('images\\password_icon.png')
        photo = ImageTk.PhotoImage(self.password_icon)
        self.password_icon_label = Label(self.sgnp_frame, image=photo, bg='#FFFFF0')
        self.password_icon_label.image = photo
        self.password_icon_label.place(x=550, y=314)
        # ========= show/hide password ==================================================================
        self.show_image = ImageTk.PhotoImage \
            (file='images\\show.png')

        self.hide_image = ImageTk.PhotoImage \
            (file='images\\hide.png')

        self.show_button = Button(self.sgnp_frame, image=self.show_image, command=self.show_sgnup, relief=FLAT,
                                  activebackground="white"
                                  , borderwidth=0, background="white", cursor="hand2")
        self.show_button.place(x=860, y=320)






        self.class_label = Label(self.sgnp_frame, text="Class", bg="#FFFFF0", fg="#4f4e4d",
                                font=("yu gothic ui", 13, "bold"))
        self.class_label.place(x=600, y=365)

        self.class_combobox = ttk.Combobox(self.sgnp_frame, state="readonly", font=("yu gothic ui", 10, "bold"))
        self.class_combobox['values'] = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10','11 COMM','11 SCI','12 COMM','12 SCI')  # Add your class options here
        self.class_combobox.current(0)
        self.class_combobox.place(x=590, y=405, width=70)


        # Combobox for division selection
        self.division_label = Label(self.sgnp_frame, text="Division", bg="#FFFFF0", fg="#4f4e4d",
                                    font=("yu gothic ui", 13, "bold"))
        self.division_label.place(x=725, y=365)

        self.division_combobox = ttk.Combobox(self.sgnp_frame, state="readonly", font=("yu gothic ui", 10, "bold"))
        self.division_combobox['values'] = ('A', 'B', 'C', 'D')  # Add your division options here
        self.division_combobox.current(0)
        self.division_combobox.place(x=720, y=405, width=80)



        # =========== Sign Up ==================================================

        def signup_users():
            self.new_teacher_username = self.username_entry.get()
            self.new_teacher_password = self.password_entry.get()
            self.new_teacher_class = self.class_combobox.get()
            self.new_teacher_division = self.division_combobox.get()
            self.new_teacher_isApproved = 0

            cur.execute("select TUSERNAME from teachers")
            username_list = cur.fetchall()
            # print(username_list)
            flag_found = False
            for i in username_list:
                if i[0] == self.new_teacher_username:
                    flag_found = True

            if flag_found == True:
                messagebox.showerror("Error", "Username already exists!")
                                
            else:
                cur.execute("INSERT INTO teachers VALUES (%s, %s, %s, %s, %s)",(self.new_teacher_username, self.new_teacher_password, self.new_teacher_class, self.new_teacher_division, self.new_teacher_isApproved))

                self.username_entry.delete(0,END)
                self.password_entry.delete(0,END)
                self.class_combobox.current(0)
                self.division_combobox.current(0)

                messagebox.showinfo("Success", "Account created successfully!\nAsk admin to approve you.\n\nYour ID is: " + str(self.new_teacher_username) + " and Password is: " + self.new_teacher_password)
                mydb.commit()

                self.back_to_login()
            

        self.sgnp_button = Image.open('images\\btn1.png')
        photo = ImageTk.PhotoImage(self.sgnp_button)
        self.sgnp_button_label = Label(self.sgnp_frame, image=photo, bg='#FFFFF0')
        self.sgnp_button_label.image = photo
        self.sgnp_button_label.place(x=550, y=460)
        self.signnup = Button(self.sgnp_button_label, text='SIGNUP', font=("yu gothic ui", 13, "bold"), width=25, bd=0,
                            bg='#3047ff', cursor='hand2', command = signup_users, activebackground='#3047ff'
                            , activeforeground='white', fg='white')
        self.signnup.place(x=20, y=10)

        # Back button
        self.back_button = Button(self.sgnp_frame, text="Back to Login", bg="#FFFFF0", fg="#4f4e4d",
                                font=("yu gothic ui", 11, "bold"), relief=FLAT, activebackground="#FFFFF0", activeforeground='#4f4e4d',command=self.back_to_login)
        self.back_button.place(x=630, y=570)

        # Continue adding other components as before

    def back_to_login(self):
        # Destroy the signup frame
        self.signup_frame.destroy()
        # Recreate the login frame
        self.create_login_frame()

    def show_sgnup(self):
        self.hide_button = Button(self.sgnp_frame, image=self.hide_image, command=self.hide_sgnup, relief=FLAT,
                                  activebackground="white"
                                  , borderwidth=0, background="white", cursor="hand2")
        self.hide_button.place(x=860, y=320)
        self.password_entry.config(show='')

    def hide_sgnup(self):
        self.show_button = Button(self.sgnp_frame, image=self.show_image, command=self.show_sgnup, relief=FLAT,
                                  activebackground="white"
                                  , borderwidth=0, background="white", cursor="hand2")
        self.show_button.place(x=860, y=320)
        self.password_entry.config(show='*')


        


def admin_main(window):
    for widget in window.winfo_children():
            widget.destroy()

    screenheight = window.winfo_screenheight()
    screenwidth = window.winfo_screenwidth() 
    MENU_FRAME=Frame(window,relief=RIDGE,bg="lightblue",height=screenheight/8,width=screenwidth,borderwidth=5)
    MENU_FRAME.place(x=0,y=0)

    MAIN_FRAME=Frame(window,relief=RIDGE,bg="white",height=screenheight//1.5,width=screenwidth//1.25,borderwidth=4) 
    MAIN_FRAME.place(x=150,y=150)

    def add_teacher():
        print("add_teacher")

    def edit_teacher():
        for widget in MAIN_FRAME.winfo_children():
            widget.destroy()

        # Increase label font size
        label_font = ('Arial', 15)

        # Calculate the center x-coordinate of MAIN_FRAME
        main_frame_width = MAIN_FRAME.winfo_reqwidth()
        main_frame_center_x = main_frame_width // 2

        # Calculate the width of the labels and entries
        label_width = 140
        entry_width = 30

        # Space between label and entry
        space_between = 40

        # Calculate the space on the left and right of labels and entries
        side_space = (main_frame_width - (label_width + entry_width + space_between)) // 3



        # Labels
        username_label = Label(MAIN_FRAME, text="Username:", bg="white", font=label_font, padx=5, pady=10, anchor="e")
        username_label.place(x=side_space, y=20)

        password_label = Label(MAIN_FRAME, text="Password:", bg="white", font=label_font, padx=5, pady=10, anchor="e")
        password_label.place(x=side_space, y=70)

        class_label = Label(MAIN_FRAME, text="Class:", bg="white", font=label_font, padx=5, pady=10, anchor="e")
        class_label.place(x=side_space, y=120)

        division_label = Label(MAIN_FRAME, text="Division:", bg="white", font=label_font, padx=5, pady=10, anchor="e")
        division_label.place(x=side_space, y=170)

        approve_label = Label(MAIN_FRAME, text="Approve:", bg="white", font=label_font, padx=5, pady=10, anchor="e")
        approve_label.place(x=side_space, y=220)

        # Increase entry font size
        entry_font = ('Arial', 15)

        # Get the list of usernames from the database   
        cur.execute("select TUSERNAME from teachers")
        data = cur.fetchall()
        username_list = []
        for i in data:
            if i[0] == 'admin':
                continue
            else:
                username_list.append(i[0])


        


        # Entry fields
        username_entry = AutocompleteEntry(MAIN_FRAME, width=entry_width, completevalues=username_list, font=entry_font)
        username_entry.place(x=side_space + label_width + space_between, y=30)

        password_entry = Entry(MAIN_FRAME, width=entry_width, bg="#FFFFF0", font=entry_font)
        password_entry.place(x=side_space + label_width + space_between, y=80)

        class_entry = ttk.Combobox(MAIN_FRAME, state="readonly", values=['1', '2', '3', '4', '5', '6', '7', '8', '9', '10','11 COMM','11 SCI','12 COMM','12 SCI'], width=entry_width, font=entry_font)
        class_entry.place(x=side_space + label_width + space_between, y=130)

        division_entry = ttk.Combobox(MAIN_FRAME, state="readonly", values=['A', 'B', 'C', 'D'], width=entry_width, font=entry_font)
        division_entry.place(x=side_space + label_width + space_between, y=180)

        approve_var = IntVar()
        approve_check = Checkbutton(MAIN_FRAME, bg="white", variable=approve_var)
        approve_check.place(x=side_space + label_width + space_between, y=230)


        def fill_details(event=None):
            # Get the entered username
            entered_username = username_entry.get()

            # Fetch details from the database based on the entered username
            cur.execute("SELECT TUSERNAME, TPASSWORD, CLASS, DIVISION, isApproved FROM teachers WHERE TUSERNAME = %s", (entered_username,))
            data = cur.fetchone()  # Assuming there's only one matching record

            # Check if data is found
            if data:
                # Fill the entry fields with the retrieved data
                # username_entry.insert(data[0])
                password_entry.delete(0, END)
                password_entry.insert(0, data[1])
                class_entry.set(data[2])
                division_entry.set(data[3])
                if data[4] == 1:
                    approve_check.select()
                else:
                    approve_check.deselect(0)

        # Bind the fill_details function to the Enter key event of the autocomplete entry
        username_entry.bind('<Return>', fill_details)

        def save_details():
            entered_username = username_entry.get()
            if not entered_username:
                messagebox.showerror("Error!", "Username cannot be empty!")
            else:
                tecaher_password = password_entry.get()
                teacher_class = class_entry.get()
                techaer_division = division_entry.get()
                teacher_approve = approve_var.get()

                # print("Username:", username)
                # print("Password:", password)
                # print("Class:", teacher_class)
                # print("Division:", division)
                # print("Approve:", approve)

                cur.execute("update teachers set TPASSWORD = %s, CLASS = %s, DIVISION = %s, isApproved = %s where TUSERNAME = %s",(tecaher_password,teacher_class,techaer_division,teacher_approve,entered_username))

                mydb.commit()

                username_entry.delete(0,END)
                password_entry.delete(0,END)
                class_entry.set('')
                division_entry.set('')
                approve_check.deselect()

                messagebox.showinfo("Succes","{}'s Details Updated Successfully!".format(entered_username))

        # Save button
        save_button = Button(MAIN_FRAME, text="Save", command=save_details, bg="#3047ff", fg="white", width=10, font=('Arial', 20))
        save_button.place(x=main_frame_center_x - 50, y=270)








    def reports():
        print("reports")


    def approvals():

        class ApproveTable(Frame):
            def __init__(self, master, headings, data):
                super().__init__(master)
                self.master = master
                self.headings = headings
                self.data = data
                self.create_table()

            def create_table(self):



                if not self.data:
                    # If no data, display a message
                    empty_label = Label(self, text="No pending approvals", padx=10, pady=5)
                    empty_label.grid(row=0, column=0, columnspan=len(self.headings)+2, padx=5, pady=5)
                    return
                

                
                # Create heading labels
                for j, heading in enumerate(self.headings):
                    label = Label(self, text=heading, padx=10, pady=5, borderwidth=3, relief="solid", width=15)
                    label.grid(row=0, column=j, padx=5, pady=5)


                # Create data labels and buttons
                for i, row_data in enumerate(self.data):
                    for j, column_data in enumerate(row_data):
                        label = Label(self, text=column_data, padx=10, pady=5, borderwidth=1, relief="solid", width=15)
                        label.grid(row=i+1, column=j, padx=5, pady=5)

                    yes_button = Button(self, text="Yes", command=lambda i=i: self.approve(i, True), width=8)
                    yes_button.grid(row=i+1, column=len(row_data), padx=5, pady=5)

                    no_button = Button(self, text="No", command=lambda i=i: self.approve(i, False), width=8)
                    no_button.grid(row=i+1, column=len(row_data)+1, padx=5, pady=5)

            def approve(self, index, approval):
                if approval:
                    # print(f"Approved: {self.data[index]}")
                    cur.execute("UPDATE teachers SET isApproved = 1 WHERE TUSERNAME = '{}'".format(self.data[index][0]))
                    mydb.commit()
                else:
                    # print(f"Not approved: {self.data[index]}")
                    cur.execute("delete from teachers WHERE TUSERNAME = '{}'".format(self.data[index][0]))
                    mydb.commit()
                # Delete the row
                del self.data[index]
                self.refresh_table()

            def refresh_table(self):
                # Clear current widgets
                for widget in self.winfo_children():
                    widget.destroy()
                # Recreate the table with updated data
                self.create_table()


        sample_headings  = ["TUSERNAME","TPASSWORD","CLASS","DIVISION","APPROVE","REJECT"]

        cur.execute("SELECT TUSERNAME,TPASSWORD,CLASS,DIVISION FROM teachers WHERE isApproved = 0")
        non_approved_teachers = cur.fetchall()
        # print(non_approved_teachers)

        approve_table = ApproveTable(MAIN_FRAME, sample_headings, non_approved_teachers)
        approve_table.place(x=MAIN_FRAME.winfo_width()//6, y=10)

    image_teacher= Image.open(r"images\teacher.png")
    image_teacher= image_teacher.resize((55,55))
    img_teacher= ImageTk.PhotoImage(image_teacher)
    teacher_BTN=Button(MENU_FRAME,image = img_teacher,bg='lightblue',compound=TOP,text="ADD TEACHER",command=add_teacher,padx=2,pady=2,activebackground='lightblue',relief=FLAT)
    teacher_BTN.place(x=100,y=5)

    image_edit= Image.open(r"images\user.png")
    image_edit= image_edit.resize((55,55))
    img_edit= ImageTk.PhotoImage(image_edit)
    edit_BTN=Button(MENU_FRAME,image = img_edit,bg='lightblue',compound=TOP,text="EDIT TEACHER",command=edit_teacher,padx=2,pady=2,activebackground='lightblue',relief=FLAT)
    edit_BTN.place(x=250,y=5) 

    image_fees_report= Image.open(r"images\report.png")
    image_fees_report= image_fees_report.resize((55,55))
    img_fees_report= ImageTk.PhotoImage(image_fees_report)
    FEES_REPORT_BTN=Button(MENU_FRAME,image = img_fees_report,bg='lightblue',compound=TOP,text="REPORTS",command=reports,padx=2,pady=2,activebackground='lightblue',relief=FLAT)
    FEES_REPORT_BTN.place(x=400,y=5) 

    image_fees_approve= Image.open(r"images\approve.png")
    image_fees_approve= image_fees_approve.resize((55,55))
    img_fees_approve= ImageTk.PhotoImage(image_fees_approve)
    FEES_approve_BTN=Button(MENU_FRAME,image = img_fees_approve,bg='lightblue',compound=TOP,text="Pending Approvals",command=approvals,padx=2,pady=2,activebackground='lightblue',relief=FLAT)
    FEES_approve_BTN.place(x=550,y=5) 


    window.mainloop()



def teacher_main(user,window):
    for widget in window.winfo_children():
            widget.destroy()
    # print(user)



    def add_term1_marks():
        for widget in window.winfo_children():
            widget.destroy()

        
        standard = user[2] + "-" +user[3]
        STANDARD_CLASS = standard.split("-")[0]
        # print(STANDARD_CLASS)




        cur.execute("SELECT standard, subjects FROM standard_wise_subjects")

        # Fetch all rows from the result
        rows = cur.fetchall()

        # Create an empty dictionary to store subject lists
        subjects_dict = {}

        # Process fetched data and populate the dictionary
        for row in rows:
            standard_1 = row[0]
            subjects_list_1 = ast.literal_eval(row[1])  # Convert string representation of list to actual list
            subjects_dict[standard_1] = subjects_list_1

        # print(subjects_dict)

        if STANDARD_CLASS in subjects_dict:
            subject_list = subjects_dict[STANDARD_CLASS]

        print(subject_list)
        # Assuming you have a list of subjects for a particular standard
        # subject_list = ['english', 'hindi' , 'maths', 'evs', 'gujarati', 'computer', 'gk']

        # Generate column definitions for each subject
        column_definitions = []
        for subject in subject_list:
            for term in ['pt_1', 'nb_1', 'sea_1', 'half_yearly', 'pt_2', 'nb_2', 'sea_2', 'annual_yearly']:
                column_name = f"{subject}_{term}"
                column_definition = f"{column_name} VARCHAR(50)"
                column_definitions.append(column_definition)

        # Additional columns
        additional_columns = [
            "gr_no INT PRIMARY KEY",
            "attendence_1 VARCHAR(50)",
            "out_of_1 VARCHAR(50)",
            "work_education_1 VARCHAR(50)",
            "art_education_1 VARCHAR(50)",
            "health_physical_education_1 VARCHAR(50)",
            "discipline_1 VARCHAR(50)",
            "height_in_cm_1 VARCHAR(50)",
            "weight_in_kg_1 VARCHAR(50)",
            "remarks_1 VARCHAR(50)",
            "attendence_2 VARCHAR(50)",
            "out_of_2 VARCHAR(50)",
            "work_education_2 VARCHAR(50)",
            "art_education_2 VARCHAR(50)",
            "health_physical_education_2 VARCHAR(50)",
            "discipline_2 VARCHAR(50)",
            "height_in_cm_2 VARCHAR(50)",
            "weight_in_kg_2 VARCHAR(50)",
            "remarks_2 VARCHAR(50)"
        ]

        # Combine all column definitions
        all_columns = ",\n".join(column_definitions + additional_columns)

        # Generate the final CREATE TABLE query
        create_table_query = f'''CREATE TABLE if not exists `{STANDARD_CLASS}` (
        {all_columns}
        )'''

        # print(create_table_query)
        cur.execute(create_table_query)
        mydb.commit()


        def fetch_data_from_mysql(query):
            cur.execute(query)
            result = cur.fetchall()
            return result
        

        def process_data(current_gr_no):
            global current_index
            # print(current_index)
            
            if next_button['text'] == "Next":
                # Update attendance before updating marks
                attendance_value = attendance_entry.get()
                out_of_entry_value = out_of_entry.get()
                height_entry_value = height_entry.get()
                weight_entry_value = weight_entry.get()
                work_edu_value = work_edu_entry.get()
                art_edu_value = art_edu_entry.get()
                hp_edu_value = hp_edu_entry.get()
                discipline_value = discipline_entry.get()
                remarks_value = remarks_entry.get()
                update_attendance(attendance_value,out_of_entry_value,height_entry_value,weight_entry_value,work_edu_value,art_edu_value,hp_edu_value,discipline_value,remarks_value,current_gr_no)
                update_marks_if_gr_no_matches(current_gr_no)
                

            # Update visibility of the "Next" button
            if current_index == len(student_data) -1:
                try:
                    next_button.pack_forget()
                    # Show a dialog box when reaching the last record
                    result = messagebox.askquestion("Data Updated", "Data is updated. Do you want to close the window?")
                    if result == 'yes':
                        window.destroy()  # Close the window if user clicks "Yes"
                    else:
                        current_index = 0  # Restart from the first record if user clicks "No"
                        tree.delete(*tree.get_children())
                        tree.insert('', 'end', values=student_data[current_index])
                        next_button.pack(side=tk.RIGHT)
                        previous_button.pack_forget()  # Hide the "Previous" button initially
                        fetch_and_populate_data(student_data[current_index][5])
                        
                except TclError:
                    pass
            
            else:
                try:
                    next_button.pack(side=tk.RIGHT)
                    current_index = (current_index + 1) % len(student_data)
                    tree.delete(*tree.get_children())
                    tree.insert('', 'end', values=student_data[current_index])
                    # Fetch and populate data for the next record
                    fetch_and_populate_data(student_data[current_index][5])
                except TclError:
                    pass

            # Update visibility of the "Previous" button
            if current_index == 0:
                try:
                    previous_button.pack_forget()  # Hide the "Previous" button if it's the first record
                except TclError:
                    pass
            else:
                try:
                    previous_button.pack(side=tk.LEFT)  # Show the "Previous" button for all other records
                except TclError:
                    pass 


        def fetch_and_populate_data(current_gr_no):

            # Initialize the query string
            data_query = f"""
                SELECT 
                attendence_1,
                out_of_1,
                work_education_1,
                art_education_1,
                health_physical_education_1,
                discipline_1,
                height_in_cm_1,
                weight_in_kg_1,
                remarks_1,
            """

            # Iterate over the subjects list
            for subject in subject_list:
                # Concatenate columns for each subject
                data_query += f"""
                    {subject}_pt_1, {subject}_nb_1, {subject}_sea_1, {subject}_half_yearly,"""

            # Remove the trailing comma and add the final part of the query
            data_query = data_query[:-1]  # Remove the trailing comma
            data_query += f"""
                FROM `{STANDARD_CLASS}`
                WHERE gr_no = "{current_gr_no}"
            """
            #print(data_query)
            cur.execute(data_query)
            data_row = cur.fetchone()
            #print(data_row)

            if data_row:
                attendance_value = data_row[0] if data_row[0] is not None else "0"  # Set a default value if attendance_value is None
                attendance_entry.delete(0, 'end')  # Clear existing value
                attendance_entry.insert(0, attendance_value)  # Set fetched attendance value
                
                out_of_value = data_row[1] if data_row[1] is not None else "0"  # Set a default value if out_of_value is None
                out_of_entry.delete(0, 'end')  # Clear existing value
                out_of_entry.insert(0, out_of_value)  # Set fetched out_of value

                work_education_value = data_row[2] if data_row[2] is not None else options[0]  # Set a default value if work_education_value is None
                work_edu_entry.delete(0, 'end')  # Clear existing value
                work_edu_entry.set(work_education_value)  # Set fetched work_education value

                art_education_value = data_row[3] if data_row[3] is not None else options[0]  # Set a default value if art_education_value is None
                art_edu_entry.delete(0, 'end')  # Clear existing value
                art_edu_entry.set( art_education_value)  # Set fetched art_education value

                health_physical_education_value = data_row[4] if data_row[4] is not None else options[0]  # Set a default value if health_physical_education_value is None
                hp_edu_entry.delete(0, 'end')  # Clear existing value
                hp_edu_entry.set( health_physical_education_value)  # Set fetched health_physical_education value

                discipline_value = data_row[5] if data_row[5] is not None else options[0]  # Set a default value if discipline_value is None
                discipline_entry.delete(0, 'end')  # Clear existing value
                discipline_entry.set( discipline_value)  # Set fetched discipline value

                height_in_cm_value = data_row[6] if data_row[6] is not None else "0"  # Set a default value if height_in_cm_value is None
                height_entry.delete(0, 'end')  # Clear existing value
                height_entry.insert(0, height_in_cm_value)  # Set fetched height_in_cm value

                weight_in_kg_value = data_row[7] if data_row[7] is not None else "0"  # Set a default value if weight_in_kg_value is None
                weight_entry.delete(0, 'end')  # Clear existing value
                weight_entry.insert(0, weight_in_kg_value)  # Set fetched weight_in_kg value

                remarks_value = data_row[8] if data_row[8] is not None else options1[0]  # Set a default value if remarks_value is None
                remarks_entry.delete(0, 'end')  # Clear existing value
                remarks_entry.set( remarks_value)  # Set fetched remarks value


                # Update the entry fields with fetched marks data
                for i, marks_value in enumerate(data_row[9:]):
                    # Use '0' as default value if marks_value is None
                    marks_value = marks_value if marks_value is not None else '0'
                    entries[i].delete(0, 'end')  # Clear existing value
                    entries[i].insert('end', marks_value)  # Set fetched marks value


            else:
                # If no data found, populate the entry fields with zeros
                attendance_entry.delete(0, 'end')  # Clear existing value
                attendance_entry.insert(0, '0')  # Set default value to 0
                for entry in entries:
                    entry.delete(0, 'end')  # Clear existing value
                    entry.insert('end', '0')  # Set default value to 0

        def display_previous_record():
            global current_index
            current_index = (current_index - 1) % len(student_data)
            tree.delete(*tree.get_children())
            tree.insert('', 'end', values=student_data[current_index])
            fetch_and_populate_data(student_data[current_index][5])

            # Update visibility of the "Previous" button
            if current_index == 0:
                try:
                    previous_button.pack_forget()  # Hide the "Previous" button if it's the first record
                except TclError:
                    pass
            else:
                try:
                    previous_button.pack(side=tk.LEFT)  # Show the "Previous" button for all other records
                except TclError:
                    pass 


        def update_attendance(attendance_value,out_of_entry_value,height_entry_value,weight_entry_value,work_edu_value,art_edu_value,hp_edu_value,discipline_value,remarks_value,current_gr_no):    
            # Defining the query to update attendance in the table for the current student
            update_query = f'''
            UPDATE `{STANDARD_CLASS}` 
            SET
            attendence_1 = '{attendance_value}',
            out_of_1 = '{out_of_entry_value}',
            work_education_1 = '{work_edu_value}',
            art_education_1 = '{art_edu_value}',      
            health_physical_education_1 = '{hp_edu_value}',
            discipline_1 = '{discipline_value}',
            height_in_cm_1 = '{height_entry_value}',          
            weight_in_kg_1 = '{weight_entry_value}',
            remarks_1 = '{remarks_value}'
            WHERE gr_no = "{current_gr_no}"
            '''

            
            # Executing the update query
            cur.execute(update_query)
            mydb.commit()


        def update_marks_if_gr_no_matches(gr_no):
            
            # Defining the query to check if GR_NO already exists in the target table
            check_query = f'''
            SELECT gr_no 
            FROM `{STANDARD_CLASS}` 
            WHERE gr_no = "{gr_no}"
            '''
            # Executing the check query
            cur.execute(check_query)
            # Fetching the result of the check query
            existing_gr_no = cur.fetchone()
            
            # If GR_NO exists in the target table, update the marks
            if existing_gr_no:
                # Fetch the marks data from the entry fields
                marks_data = []
                #print(marks_data)
                for entry in entries:
                    marks_data.append(entry.get())
                    

                # Initialize the update query
                update_query = f'''
                UPDATE `{STANDARD_CLASS}` 
                SET 
                '''

                # Loop through the subject list to dynamically construct the SET clause of the update query
                for index, subject in enumerate(subject_list):
                    # Construct column names dynamically based on subject
                    pt1_column = f'{subject}_pt_1'
                    nb_1_column = f'{subject}_nb_1'
                    sea_1_column = f'{subject}_sea_1'
                    half_yearly_column = f'{subject}_half_yearly'

                    # Append the dynamically constructed column names and placeholders to the update query
                    update_query += f'''
                    {pt1_column} = '{marks_data[subject_list.index(subject) * 4]}',
                    {nb_1_column} = '{marks_data[subject_list.index(subject) * 4 + 1]}',
                    {sea_1_column} = '{marks_data[subject_list.index(subject) * 4 + 2]}',
                    {half_yearly_column} = '{marks_data[subject_list.index(subject) * 4 + 3]}'
                    '''
                    # Check if it's the last subject, if not, add a comma
                    if index < len(subject_list) - 1:
                        update_query += ','

                # Add the WHERE clause
                update_query += f'''
                WHERE gr_no = {gr_no}
                '''

                # Print or execute the update_query
                # print(update_query)
                cur.execute(update_query)
                mydb.commit()

        
        global current_index  # Define current_index as a global variable
        current_index = 0

        screenheight = window.winfo_screenheight()
        screenwidth = window.winfo_screenwidth() 

        MAIN_FRAME = tk.Frame(window, relief=tk.RIDGE, bg="white", height=screenheight//1.2, width=screenwidth//1.2, borderwidth=4) 
        MAIN_FRAME.place(x=(screenwidth-screenwidth//1.2)//2, y=(screenheight-screenheight//1.2)//2)


        student_data_query = f'''
        SELECT 
            CONCAT(gr_details.NAME, ' ', gr_details.SURNAME) AS full_name,
            gr_details.FATHER, 
            gr_details.MOTHER, 
            gr_details.BIRTH_DATE, 
            academic_detail.roll_no,
            gr_details.GR_NO, 
            CONCAT(academic_detail.curr_std, '-', academic_detail.division) AS class_info 
        FROM 
            gr_details
        JOIN 
            academic_detail 
        ON 
            gr_details.GR_NO = academic_detail.gr_no 
        WHERE 
            CONCAT(academic_detail.curr_std, '-', academic_detail.division) = "{standard}"
        '''
        
        
        # print(student_data_query)
        student_data = fetch_data_from_mysql(student_data_query)

        student_frame = tk.Frame(MAIN_FRAME)
        student_frame.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.1)

        tree_style = ttk.Style()
        tree_style.theme_use("clam")
        tree_style.configure("Treeview", background="white", fieldbackground="white", font=('Arial', 12))

        tree = ttk.Treeview(student_frame, columns=("Name", "FathersName", "MothersName", "DOB", "RollNo", "GrNo", "Class"), show='headings', height=2)
        tree.heading("Name", text="Name")
        tree.heading("FathersName", text="Father's Name")
        tree.heading("MothersName", text="Mother's Name")
        tree.heading("DOB", text="DOB")
        tree.heading("RollNo", text="Roll No")
        tree.heading("GrNo", text="GR No")
        tree.heading("Class", text="Class")

        tree.column("Name", width=170, anchor='center')
        tree.column("FathersName", width=170, anchor='center')
        tree.column("MothersName", width=170, anchor='center')
        tree.column("DOB", width=100, anchor='center')
        tree.column("RollNo", width=100, anchor='center')
        tree.column("GrNo", width=100, anchor='center')
        tree.column("Class", width=100, anchor='center')

        if student_data:
            tree.insert('', 'end', values=student_data[current_index])

        tree.pack(side=tk.LEFT, fill=tk.BOTH, padx=10, pady=10)

        subject_frame = tk.Frame(MAIN_FRAME)
        subject_frame.place(relx=0.02, rely=0.15, relwidth=0.96, relheight=0.4)

        tk.Label(subject_frame, text="Scholastic Areas", width=20, font=('Arial', 14)).grid(row=0, column=0)
        tk.Label(subject_frame, text="TERM - 1 ", width=20, font=('Arial', 14)).grid(row=0, column=2,columnspan=2)
        tk.Label(subject_frame, text="Subjects", width=20, font=('Arial', 14)).grid(row=1, column=0)

        terms = ["PT 1", "N.B", "SEA", "HALF YEARLY"]
        for j, term in enumerate(terms):
            tk.Label(subject_frame, text=term, width=15, font=('Arial', 12)).grid(row=1, column=j + 1)



        entries = []
        # Calculate maximum width needed for labels
        max_label_width = max([len(subject) for subject in subject_list]) +2

        for i, subject in enumerate(subject_list):
            tk.Label(subject_frame, text=subject.capitalize(), font=('Arial', 12)).grid(row=i + 2, column=0, sticky='w', padx=max_label_width*10, pady=2)
            for j in range(len(terms)):
                entry = tk.Entry(subject_frame, width=15, font=('Arial', 12))
                entry.insert('end', '0')  # Set default value to 0
                entry.grid(row=i + 2, column=j + 1, padx = 7, pady = 2)
                entries.append(entry)

        for student in student_data:
            # Extracting GR_NO from the student data
            gr_no = student[5]  # Assuming GR_NO is at index 5
            # Defining the query to check if GR_NO already exists in the target table
            check_query = f'''
            SELECT gr_no 
            FROM `{STANDARD_CLASS}` 
            WHERE gr_no = "{gr_no}"
            '''
            # Executing the check query
            cur.execute(check_query)
            # Fetching the result of the check query
            existing_gr_no = cur.fetchone()
            # If GR_NO doesn't exist in the target table, insert it
            if not existing_gr_no:
                # Defining the query to insert GR_NO into another table
                insert_query = f'''
                INSERT INTO `{STANDARD_CLASS}` (gr_no) 
                VALUES ({gr_no})
                '''
                # Executing the insert query
                cur.execute(insert_query)
        mydb.commit()


        additional_entries_frame = tk.Frame(MAIN_FRAME)
        additional_entries_frame.place(relx=0.02, rely=0.6, relwidth=0.96, relheight=0.2)

        # First column
        attendance_label = tk.Label(additional_entries_frame, text="Attendance")
        attendance_label.grid(row=0, column=0, sticky='e', padx=10, pady=5)
        attendance_entry = tk.Entry(additional_entries_frame, width=10)
        attendance_entry.insert('end', '0')
        attendance_entry.grid(row=0, column=1, sticky='w', padx=10, pady=5)

        height_label = tk.Label(additional_entries_frame, text="Height")
        height_label.grid(row=1, column=0, sticky='e', padx=10, pady=5)
        height_entry = tk.Entry(additional_entries_frame, width=10)
        height_entry.insert('end', '0')
        height_entry.grid(row=1, column=1, sticky='w', padx=10, pady=5)


        # Second column
        out_of_label = tk.Label(additional_entries_frame, text="Out of")
        out_of_label.grid(row=0, column=2, sticky='e', padx=10, pady=5)
        out_of_entry = tk.Entry(additional_entries_frame, width=10)
        out_of_entry.insert('end', '0')
        out_of_entry.grid(row=0, column=3, sticky='w', padx=10, pady=5)

        weight_label = tk.Label(additional_entries_frame, text="Weight")
        weight_label.grid(row=1, column=2, sticky='e', padx=10, pady=5)
        weight_entry = tk.Entry(additional_entries_frame, width=10)
        weight_entry.insert('end', '0')
        weight_entry.grid(row=1, column=3, sticky='w', padx=10, pady=5)

        # Third column
        options = ['A', 'B', 'C', 'D', 'E', 'F']
        work_edu_label = tk.Label(additional_entries_frame, text="Work Education")
        work_edu_label.grid(row=0, column=4, sticky='e', padx=10, pady=5)
        work_edu_entry = ttk.Combobox(additional_entries_frame, values=options)
        work_edu_entry.grid(row=0, column=5, sticky='w', padx=10, pady=5)
        work_edu_entry.set(options[0])

        art_edu_label = tk.Label(additional_entries_frame, text="Art Education")
        art_edu_label.grid(row=1, column=4, sticky='e', padx=10, pady=5)
        art_edu_entry = ttk.Combobox(additional_entries_frame, values=options)
        art_edu_entry.grid(row=1, column=5, sticky='w', padx=10, pady=5)
        art_edu_entry.set(options[0])

        hp_edu_label = tk.Label(additional_entries_frame, text="Health and Physical Education")
        hp_edu_label.grid(row=2, column=4, sticky='e', padx=10, pady=5)
        hp_edu_entry = ttk.Combobox(additional_entries_frame, values=options)
        hp_edu_entry.grid(row=2, column=5, sticky='w', padx=10, pady=5)
        hp_edu_entry.set(options[0])

        discipline_label = tk.Label(additional_entries_frame, text="Discipline")
        discipline_label.grid(row=3, column=4, sticky='e', padx=10, pady=5)
        discipline_entry = ttk.Combobox(additional_entries_frame, values=options)
        discipline_entry.grid(row=3, column=5, sticky='w', padx=10, pady=5)
        discipline_entry.set(options[0])

        options1 = ["good", "bad"]
        remarks_label = tk.Label(additional_entries_frame, text="Remarks")
        remarks_label.grid(row=0, column=6, sticky='e', padx=10, pady=5)
        remarks_entry = ttk.Combobox(additional_entries_frame, values=options1)
        remarks_entry.grid(row=0, column=7, sticky='w', padx=10, pady=5)
        remarks_entry.set(options1[0])










        buttons_frame = tk.Frame(MAIN_FRAME)
        buttons_frame.place(relx=0.02, rely=0.86, relwidth=0.96, relheight=0.1)

        previous_button = tk.Button(buttons_frame, text="Previous", font=('Arial', 12), command=display_previous_record)
        previous_button.pack(side=tk.LEFT, padx=10, pady=5)


        next_button = tk.Button(buttons_frame, text="Next", font=('Arial', 12), command=lambda: process_data(student_data[current_index][5]))
        next_button.pack(side=tk.RIGHT, padx=10, pady=5)

        # Fetch and populate data for the first student
        if student_data:
            fetch_and_populate_data(student_data[current_index][5])
            # Update visibility of the "Previous" button
            if current_index == 0:
                try:
                    previous_button.pack_forget()  # Hide the "Previous" button if it's the first record
                except TclError:
                    pass
            else:
                try:
                    previous_button.pack(side=tk.LEFT)  # Show the "Previous" button for all other records
                except TclError:
                    pass 

        else:
            messagebox.showerror("Error","Data is not found!")
            LoginPage(window)


















    #-------------------------------------------------------------------------------







    def add_term2_marks():


        for widget in window.winfo_children():
            widget.destroy()

        
        standard = user[2] + "-" +user[3]
        STANDARD_CLASS = standard.split("-")[0]
        # print(STANDARD_CLASS)





        cur.execute("SELECT standard, subjects FROM standard_wise_subjects")

        # Fetch all rows from the result
        rows = cur.fetchall()

        # Create an empty dictionary to store subject lists
        subjects_dict = {}

        # Process fetched data and populate the dictionary
        for row in rows:
            standard_1 = row[0]
            subjects_list_1 = ast.literal_eval(row[1])  # Convert string representation of list to actual list
            subjects_dict[standard_1] = subjects_list_1

        # print(subjects_dict)

        if STANDARD_CLASS in subjects_dict:
            subject_list = subjects_dict[STANDARD_CLASS]

        print(subject_list)
        # Assuming you have a list of subjects for a particular standard
        # subject_list = ['english', 'hindi' , 'maths', 'evs', 'gujarati', 'computer', 'gk']



        #----------------------------------------------------------------------------


        # def term1_marks_added(STANDARD_CLASS):
        #     try:
        #         # Query to fetch term 1 marks data for a specific student

        #         check_term_1_query = '''
                
        #         SELECT attendence_1, out_of_1, work_education_1,
        #         art_education_1,health_physical_education_1, 
        #         discipline_1, height_in_cm_1, weight_in_kg_1, 
        #         remarks_1,
        #         '''
                
        #         for index, subject in enumerate(subject_list):
        #             # Construct column names dynamically based on subject
        #             pt1_column = f'{subject}_pt_1,'
        #             nb_1_column = f'{subject}_nb_1,'
        #             sea_1_column = f'{subject}_sea_1,'
        #             half_yearly_column = f'{subject}_half_yearly'

        #             check_term_1_query = check_term_1_query + f"{pt1_column} {nb_1_column} {sea_1_column} {half_yearly_column}"
        #             # Check if it's the last subject, if not, add a comma
        #             if index < len(subject_list) - 1:
        #                 check_term_1_query += ','

        #         check_term_1_query = check_term_1_query + f" FROM `{STANDARD_CLASS}`"

        #         print(check_term_1_query)
        #         cur.execute(check_term_1_query)
        #         term1_marks_data = cur.fetchall()

        #         for individual_data in term1_marks_data: 
        #             # Check if any of the required columns contain NULL values
        #             if any(value is None for value in individual_data):
        #                 print(individual_data)
        #                 any_student_is_not_added = False  # Term 1 marks not added
        #             else :
        #                 any_student_is_not_added = True  # Term 1 marks added

        #         return any_student_is_not_added

        #     except con.Error as err:
        #         print(f"Error: {err}")
        #         return False  # Return False in case of any error



        # if not term1_marks_added(STANDARD_CLASS):
        #     print("Term 1 marks are not added yet.")
        #     messagebox.showerror("Error","Term 1 marks are not added yet!")
        # else:
        #     print("Term 1 marks are added.")


        #----------------------------------------------------------------------------


        # Generate column definitions for each subject
        column_definitions = []
        for subject in subject_list:
            for term in ['pt_2', 'nb_1', 'sea_1', 'half_yearly', 'pt_2', 'nb_2', 'sea_2', 'annual_yearly']:
                column_name = f"{subject}_{term}"
                column_definition = f"{column_name} VARCHAR(50)"
                column_definitions.append(column_definition)

        # Additional columns
        additional_columns = [
            "gr_no INT PRIMARY KEY",
            "attendence_1 VARCHAR(50)",
            "out_of_1 VARCHAR(50)",
            "work_education_1 VARCHAR(50)",
            "art_education_1 VARCHAR(50)",
            "health_physical_education_1 VARCHAR(50)",
            "discipline_1 VARCHAR(50)",
            "height_in_cm_1 VARCHAR(50)",
            "weight_in_kg_1 VARCHAR(50)",
            "remarks_1 VARCHAR(50)",
            "attendence_2 VARCHAR(50)",
            "out_of_2 VARCHAR(50)",
            "work_education_2 VARCHAR(50)",
            "art_education_2 VARCHAR(50)",
            "health_physical_education_2 VARCHAR(50)",
            "discipline_2 VARCHAR(50)",
            "height_in_cm_2 VARCHAR(50)",
            "weight_in_kg_2 VARCHAR(50)",
            "remarks_2 VARCHAR(50)"
        ]

        # Combine all column definitions
        all_columns = ",\n".join(column_definitions + additional_columns)

        # Generate the final CREATE TABLE query
        create_table_query = f'''CREATE TABLE if not exists `{STANDARD_CLASS}` (
        {all_columns}
        )'''

        # print(create_table_query)
        cur.execute(create_table_query)
        mydb.commit()


        def fetch_data_from_mysql(query):
            cur.execute(query)
            result = cur.fetchall()
            return result
        

        def process_data(current_gr_no):
            global current_index
            # print(current_index)
            
            if next_button['text'] == "Next":
                # Update attendance before updating marks
                attendance_value = attendance_entry.get()
                out_of_entry_value = out_of_entry.get()
                height_entry_value = height_entry.get()
                weight_entry_value = weight_entry.get()
                work_edu_value = work_edu_entry.get()
                art_edu_value = art_edu_entry.get()
                hp_edu_value = hp_edu_entry.get()
                discipline_value = discipline_entry.get()
                remarks_value = remarks_entry.get()
                update_attendance(attendance_value,out_of_entry_value,height_entry_value,weight_entry_value,work_edu_value,art_edu_value,hp_edu_value,discipline_value,remarks_value,current_gr_no)
                update_marks_if_gr_no_matches(current_gr_no)
                

            # Update visibility of the "Next" button
            if current_index == len(student_data) -1:
                try:
                    next_button.pack_forget()
                    # Show a dialog box when reaching the last record
                    result = messagebox.askquestion("Data Updated", "Data is updated. Do you want to close the window?")
                    if result == 'yes':
                        window.destroy()  # Close the window if user clicks "Yes"
                    else:
                        current_index = 0  # Restart from the first record if user clicks "No"
                        tree.delete(*tree.get_children())
                        tree.insert('', 'end', values=student_data[current_index])
                        next_button.pack(side=tk.RIGHT)
                        previous_button.pack_forget()  # Hide the "Previous" button initially
                        fetch_and_populate_data(student_data[current_index][5])
                        
                except TclError:
                    pass
            
            else:
                try:
                    next_button.pack(side=tk.RIGHT)
                    current_index = (current_index + 1) % len(student_data)
                    tree.delete(*tree.get_children())
                    tree.insert('', 'end', values=student_data[current_index])
                    # Fetch and populate data for the next record
                    fetch_and_populate_data(student_data[current_index][5])
                except TclError:
                    pass

            # Update visibility of the "Previous" button
            if current_index == 0:
                try:
                    previous_button.pack_forget()  # Hide the "Previous" button if it's the first record
                except TclError:
                    pass
            else:
                try:
                    previous_button.pack(side=tk.LEFT)  # Show the "Previous" button for all other records
                except TclError:
                    pass 


        def fetch_and_populate_data(current_gr_no):

            # Initialize the query string
            data_query = f"""
                SELECT 
                attendence_2,
                out_of_2,
                work_education_2,
                art_education_2,
                health_physical_education_2,
                discipline_2,
                height_in_cm_2,
                weight_in_kg_2,
                remarks_2,
            """

            # Iterate over the subjects list
            for subject in subject_list:
                # Concatenate columns for each subject
                data_query += f"""
                    {subject}_pt_2, {subject}_nb_2, {subject}_sea_2, {subject}_annual_yearly,"""

            # Remove the trailing comma and add the final part of the query
            data_query = data_query[:-1]  # Remove the trailing comma
            data_query += f"""
                FROM `{STANDARD_CLASS}`
                WHERE gr_no = "{current_gr_no}"
            """
            #print(data_query)
            cur.execute(data_query)
            data_row = cur.fetchone()
            #print(data_row)

            if data_row:
                attendance_value = data_row[0] if data_row[0] is not None else "0"  # Set a default value if attendance_value is None
                attendance_entry.delete(0, 'end')  # Clear existing value
                attendance_entry.insert(0, attendance_value)  # Set fetched attendance value
                
                out_of_value = data_row[1] if data_row[1] is not None else "0"  # Set a default value if out_of_value is None
                out_of_entry.delete(0, 'end')  # Clear existing value
                out_of_entry.insert(0, out_of_value)  # Set fetched out_of value

                work_education_value = data_row[2] if data_row[2] is not None else options[0]  # Set a default value if work_education_value is None
                work_edu_entry.delete(0, 'end')  # Clear existing value
                work_edu_entry.set(work_education_value)  # Set fetched work_education value

                art_education_value = data_row[3] if data_row[3] is not None else options[0]  # Set a default value if art_education_value is None
                art_edu_entry.delete(0, 'end')  # Clear existing value
                art_edu_entry.set( art_education_value)  # Set fetched art_education value

                health_physical_education_value = data_row[4] if data_row[4] is not None else options[0]  # Set a default value if health_physical_education_value is None
                hp_edu_entry.delete(0, 'end')  # Clear existing value
                hp_edu_entry.set( health_physical_education_value)  # Set fetched health_physical_education value

                discipline_value = data_row[5] if data_row[5] is not None else options[0]  # Set a default value if discipline_value is None
                discipline_entry.delete(0, 'end')  # Clear existing value
                discipline_entry.set( discipline_value)  # Set fetched discipline value

                height_in_cm_value = data_row[6] if data_row[6] is not None else "0"  # Set a default value if height_in_cm_value is None
                height_entry.delete(0, 'end')  # Clear existing value
                height_entry.insert(0, height_in_cm_value)  # Set fetched height_in_cm value

                weight_in_kg_value = data_row[7] if data_row[7] is not None else "0"  # Set a default value if weight_in_kg_value is None
                weight_entry.delete(0, 'end')  # Clear existing value
                weight_entry.insert(0, weight_in_kg_value)  # Set fetched weight_in_kg value

                remarks_value = data_row[8] if data_row[8] is not None else options1[0]  # Set a default value if remarks_value is None
                remarks_entry.delete(0, 'end')  # Clear existing value
                remarks_entry.set( remarks_value)  # Set fetched remarks value


                # Update the entry fields with fetched marks data
                for i, marks_value in enumerate(data_row[9:]):
                    # Use '0' as default value if marks_value is None
                    marks_value = marks_value if marks_value is not None else '0'
                    entries[i].delete(0, 'end')  # Clear existing value
                    entries[i].insert('end', marks_value)  # Set fetched marks value


            else:
                # If no data found, populate the entry fields with zeros
                attendance_entry.delete(0, 'end')  # Clear existing value
                attendance_entry.insert(0, '0')  # Set default value to 0
                for entry in entries:
                    entry.delete(0, 'end')  # Clear existing value
                    entry.insert('end', '0')  # Set default value to 0

        def display_previous_record():
            global current_index
            current_index = (current_index - 1) % len(student_data)
            tree.delete(*tree.get_children())
            tree.insert('', 'end', values=student_data[current_index])
            fetch_and_populate_data(student_data[current_index][5])

            # Update visibility of the "Previous" button
            if current_index == 0:
                try:
                    previous_button.pack_forget()  # Hide the "Previous" button if it's the first record
                except TclError:
                    pass
            else:
                try:
                    previous_button.pack(side=tk.LEFT)  # Show the "Previous" button for all other records
                except TclError:
                    pass 


        def update_attendance(attendance_value,out_of_entry_value,height_entry_value,weight_entry_value,work_edu_value,art_edu_value,hp_edu_value,discipline_value,remarks_value,current_gr_no):
            # Defining the query to update attendance in the table for the current student
            update_query = f'''
            UPDATE `{STANDARD_CLASS}` 
            SET
            attendence_2 = '{attendance_value}',
            out_of_2 = '{out_of_entry_value}',
            work_education_2 = '{work_edu_value}',
            art_education_2 = '{art_edu_value}',      
            health_physical_education_2 = '{hp_edu_value}',
            discipline_2 = '{discipline_value}',
            height_in_cm_2 = '{height_entry_value}',          
            weight_in_kg_2 = '{weight_entry_value}',
            remarks_2 = '{remarks_value}'
            WHERE gr_no = "{current_gr_no}"
            '''

            
            # Executing the update query
            cur.execute(update_query)
            mydb.commit()


        def update_marks_if_gr_no_matches(gr_no):
            
            # Defining the query to check if GR_NO already exists in the target table
            check_query = f'''
            SELECT gr_no 
            FROM `{STANDARD_CLASS}` 
            WHERE gr_no = "{gr_no}"
            '''
            # Executing the check query
            cur.execute(check_query)
            # Fetching the result of the check query
            existing_gr_no = cur.fetchone()
            
            # If GR_NO exists in the target table, update the marks
            if existing_gr_no:
                # Fetch the marks data from the entry fields
                marks_data = []
                #print(marks_data)
                for entry in entries:
                    marks_data.append(entry.get())
                    

                # Initialize the update query
                update_query = f'''
                UPDATE `{STANDARD_CLASS}` 
                SET 
                '''

                # Loop through the subject list to dynamically construct the SET clause of the update query
                for index, subject in enumerate(subject_list):
                    # Construct column names dynamically based on subject
                    pt2_column = f'{subject}_pt_2'
                    nb_2_column = f'{subject}_nb_2'
                    sea_2_column = f'{subject}_sea_2'
                    annual_yearly_column = f'{subject}_annual_yearly'

                    # Append the dynamically constructed column names and placeholders to the update query
                    update_query += f'''
                    {pt2_column} = '{marks_data[subject_list.index(subject) * 4]}',
                    {nb_2_column} = '{marks_data[subject_list.index(subject) * 4 + 1]}',
                    {sea_2_column} = '{marks_data[subject_list.index(subject) * 4 + 2]}',
                    {annual_yearly_column} = '{marks_data[subject_list.index(subject) * 4 + 3]}'
                    '''
                    # Check if it's the last subject, if not, add a comma
                    if index < len(subject_list) - 1:
                        update_query += ','

                # Add the WHERE clause
                update_query += f'''
                WHERE gr_no = {gr_no}
                '''

                # Print or execute the update_query
                # print(update_query)
                cur.execute(update_query)
                mydb.commit()

        
        global current_index  # Define current_index as a global variable
        current_index = 0

        screenheight = window.winfo_screenheight()
        screenwidth = window.winfo_screenwidth() 

        MAIN_FRAME = tk.Frame(window, relief=tk.RIDGE, bg="white", height=screenheight//1.2, width=screenwidth//1.2, borderwidth=4) 
        MAIN_FRAME.place(x=(screenwidth-screenwidth//1.2)//2, y=(screenheight-screenheight//1.2)//2)


        student_data_query = f'''
        SELECT 
            CONCAT(gr_details.NAME, ' ', gr_details.SURNAME) AS full_name,
            gr_details.FATHER, 
            gr_details.MOTHER, 
            gr_details.BIRTH_DATE, 
            academic_detail.roll_no,
            gr_details.GR_NO, 
            CONCAT(academic_detail.curr_std, '-', academic_detail.division) AS class_info 
        FROM 
            gr_details
        JOIN 
            academic_detail 
        ON 
            gr_details.GR_NO = academic_detail.gr_no 
        WHERE 
            CONCAT(academic_detail.curr_std, '-', academic_detail.division) = "{standard}"
        '''
        
        
        # print(student_data_query)
        student_data = fetch_data_from_mysql(student_data_query)

        student_frame = tk.Frame(MAIN_FRAME)
        student_frame.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.1)

        tree_style = ttk.Style()
        tree_style.theme_use("clam")
        tree_style.configure("Treeview", background="white", fieldbackground="white", font=('Arial', 12))

        tree = ttk.Treeview(student_frame, columns=("Name", "FathersName", "MothersName", "DOB", "RollNo", "GrNo", "Class"), show='headings', height=2)
        tree.heading("Name", text="Name")
        tree.heading("FathersName", text="Father's Name")
        tree.heading("MothersName", text="Mother's Name")
        tree.heading("DOB", text="DOB")
        tree.heading("RollNo", text="Roll No")
        tree.heading("GrNo", text="GR No")
        tree.heading("Class", text="Class")

        tree.column("Name", width=170, anchor='center')
        tree.column("FathersName", width=170, anchor='center')
        tree.column("MothersName", width=170, anchor='center')
        tree.column("DOB", width=100, anchor='center')
        tree.column("RollNo", width=100, anchor='center')
        tree.column("GrNo", width=100, anchor='center')
        tree.column("Class", width=100, anchor='center')

        if student_data:
            tree.insert('', 'end', values=student_data[current_index])

        tree.pack(side=tk.LEFT, fill=tk.BOTH, padx=10, pady=10)

        subject_frame = tk.Frame(MAIN_FRAME)
        subject_frame.place(relx=0.02, rely=0.15, relwidth=0.96, relheight=0.4)

        tk.Label(subject_frame, text="Scholastic Areas", width=20, font=('Arial', 14)).grid(row=0, column=0)
        tk.Label(subject_frame, text="TERM - 2 ", width=20, font=('Arial', 14)).grid(row=0, column=2,columnspan=2)
        tk.Label(subject_frame, text="Subjects", width=20, font=('Arial', 14)).grid(row=1, column=0)

        terms = ["PT 2", "N.B", "SEA", "HALF YEARLY"]
        for j, term in enumerate(terms):
            tk.Label(subject_frame, text=term, width=15, font=('Arial', 12)).grid(row=1, column=j + 1)



        entries = []
        # Calculate maximum width needed for labels
        max_label_width = max([len(subject) for subject in subject_list]) + 2

        for i, subject in enumerate(subject_list):
            tk.Label(subject_frame, text=subject.capitalize(), font=('Arial', 12)).grid(row=i + 2, column=0, sticky='w', padx=max_label_width*10, pady=2)
            for j in range(len(terms)):
                entry = tk.Entry(subject_frame, width=15, font=('Arial', 12))
                entry.insert('end', '0')  # Set default value to 0
                entry.grid(row=i + 2, column=j + 1, padx=7, pady=2)
                entries.append(entry)

        for student in student_data:
            # Extracting GR_NO from the student data
            gr_no = student[5]  # Assuming GR_NO is at index 5
            # Defining the query to check if GR_NO already exists in the target table
            check_query = f'''
            SELECT gr_no 
            FROM `{STANDARD_CLASS}` 
            WHERE gr_no = "{gr_no}"
            '''
            # Executing the check query
            cur.execute(check_query)
            # Fetching the result of the check query
            existing_gr_no = cur.fetchone()
            # If GR_NO doesn't exist in the target table, insert it
            if not existing_gr_no:
                # Defining the query to insert GR_NO into another table
                insert_query = f'''
                INSERT INTO `{STANDARD_CLASS}` (gr_no) 
                VALUES ({gr_no})
                '''
                # Executing the insert query
                cur.execute(insert_query)
        mydb.commit()


        additional_entries_frame = tk.Frame(MAIN_FRAME)
        additional_entries_frame.place(relx=0.02, rely=0.6, relwidth=0.96, relheight=0.2)

        # First column
        attendance_label = tk.Label(additional_entries_frame, text="Attendance")
        attendance_label.grid(row=0, column=0, sticky='e', padx=10, pady=5)
        attendance_entry = tk.Entry(additional_entries_frame, width=10)
        attendance_entry.insert('end', '0')
        attendance_entry.grid(row=0, column=1, sticky='w', padx=10, pady=5)

        height_label = tk.Label(additional_entries_frame, text="Height")
        height_label.grid(row=1, column=0, sticky='e', padx=10, pady=5)
        height_entry = tk.Entry(additional_entries_frame, width=10)
        height_entry.insert('end', '0')
        height_entry.grid(row=1, column=1, sticky='w', padx=10, pady=5)


        # Second column
        out_of_label = tk.Label(additional_entries_frame, text="Out of")
        out_of_label.grid(row=0, column=2, sticky='e', padx=10, pady=5)
        out_of_entry = tk.Entry(additional_entries_frame, width=10)
        out_of_entry.insert('end', '0')
        out_of_entry.grid(row=0, column=3, sticky='w', padx=10, pady=5)

        weight_label = tk.Label(additional_entries_frame, text="Weight")
        weight_label.grid(row=1, column=2, sticky='e', padx=10, pady=5)
        weight_entry = tk.Entry(additional_entries_frame, width=10)
        weight_entry.insert('end', '0')
        weight_entry.grid(row=1, column=3, sticky='w', padx=10, pady=5)

        # Third column
        options = ['A', 'B', 'C', 'D', 'E', 'F']
        work_edu_label = tk.Label(additional_entries_frame, text="Work Education")
        work_edu_label.grid(row=0, column=4, sticky='e', padx=10, pady=5)
        work_edu_entry = ttk.Combobox(additional_entries_frame, values=options)
        work_edu_entry.grid(row=0, column=5, sticky='w', padx=10, pady=5)
        work_edu_entry.set(options[0])

        art_edu_label = tk.Label(additional_entries_frame, text="Art Education")
        art_edu_label.grid(row=1, column=4, sticky='e', padx=10, pady=5)
        art_edu_entry = ttk.Combobox(additional_entries_frame, values=options)
        art_edu_entry.grid(row=1, column=5, sticky='w', padx=10, pady=5)
        art_edu_entry.set(options[0])

        hp_edu_label = tk.Label(additional_entries_frame, text="Health and Physical Education")
        hp_edu_label.grid(row=2, column=4, sticky='e', padx=10, pady=5)
        hp_edu_entry = ttk.Combobox(additional_entries_frame, values=options)
        hp_edu_entry.grid(row=2, column=5, sticky='w', padx=10, pady=5)
        hp_edu_entry.set(options[0])

        discipline_label = tk.Label(additional_entries_frame, text="Discipline")
        discipline_label.grid(row=3, column=4, sticky='e', padx=10, pady=5)
        discipline_entry = ttk.Combobox(additional_entries_frame, values=options)
        discipline_entry.grid(row=3, column=5, sticky='w', padx=10, pady=5)
        discipline_entry.set(options[0])

        options1 = ["good", "bad"]
        remarks_label = tk.Label(additional_entries_frame, text="Remarks")
        remarks_label.grid(row=0, column=6, sticky='e', padx=10, pady=5)
        remarks_entry = ttk.Combobox(additional_entries_frame, values=options1)
        remarks_entry.grid(row=0, column=7, sticky='w', padx=10, pady=5)
        remarks_entry.set(options1[0])










        buttons_frame = tk.Frame(MAIN_FRAME)
        buttons_frame.place(relx=0.02, rely=0.86, relwidth=0.96, relheight=0.1)

        previous_button = tk.Button(buttons_frame, text="Previous", font=('Arial', 12), command=display_previous_record)
        previous_button.pack(side=tk.LEFT, padx=10, pady=5)


        next_button = tk.Button(buttons_frame, text="Next", font=('Arial', 12), command=lambda: process_data(student_data[current_index][5]))
        next_button.pack(side=tk.RIGHT, padx=10, pady=5)

        # Fetch and populate data for the first student
        if student_data:
            fetch_and_populate_data(student_data[current_index][5])
            # Update visibility of the "Previous" button
            if current_index == 0:
                try:
                    previous_button.pack_forget()  # Hide the "Previous" button if it's the first record
                except TclError:
                    pass
            else:
                try:
                    previous_button.pack(side=tk.LEFT)  # Show the "Previous" button for all other records
                except TclError:
                    pass 

        else:
            messagebox.showerror("Error","Data is not found!")
            LoginPage(window)

    def generate_results():
        print("Generate Results")

    button1 = tk.Button(window, text="Add Term 1 Marks", command=add_term1_marks)
    button1.place(x=50, y=50, width=200, height=50)

    button2 = tk.Button(window, text="Add Term 2 Marks", command=add_term2_marks)
    button2.place(x=50, y=120, width=200, height=50)

    button3 = tk.Button(window, text="Generate Results", command=generate_results)
    button3.place(x=50, y=190, width=200, height=50)

def page():
    window = Tk()
    LoginPage(window)
    window.mainloop()


if __name__ == '__main__':
    page()