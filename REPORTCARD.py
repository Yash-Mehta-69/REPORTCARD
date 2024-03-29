

from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk
import tkinter as tk
import mysql.connector as con
from tkinter import messagebox
from ttkwidgets.autocomplete import AutocompleteEntry


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
                    entry_page(self.window)
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
        self.class_combobox['values'] = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10')  # Add your class options here
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



class entry_page:
    def __init__(self, window):
        # Destroy all widgets within the window
        for widget in window.winfo_children():
            widget.destroy()



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

        class_entry = ttk.Combobox(MAIN_FRAME, state="readonly", values=['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'], width=entry_width, font=entry_font)
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


def page():
    window = Tk()
    LoginPage(window)
    window.mainloop()


if __name__ == '__main__':
    page()