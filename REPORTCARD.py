

from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk
import mysql.connector as con
from tkinter import messagebox

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
        self.login_frame = Frame(self.window, width=login_frame_width, height=login_frame_height, bg="#B6D0E2")
        self.login_frame.place(x=login_frame_x, y=login_frame_y)
        self.lgn_frame = Frame(self.window, bg='#040405', width=login_frame_width, height=login_frame_height)
        self.lgn_frame.place(x=login_frame_x, y=login_frame_y)

        # ========================================================================
        # ========================================================
        # ========================================================================
        self.txt = "WELCOME"
        self.heading = Label(self.lgn_frame, text=self.txt, font=('yu gothic ui', 25, "bold"), bg="#040405",
                             fg='white',
                             bd=5,
                             relief=FLAT)
        self.heading.place(x=80, y=30, width=300, height=30)

        # ========================================================================
        # ============ Left Side Image ================================================
        # ========================================================================
        self.side_image = Image.open('images\\vector.png')
        photo = ImageTk.PhotoImage(self.side_image)
        self.side_image_label = Label(self.lgn_frame, image=photo, bg='#040405')
        self.side_image_label.image = photo
        self.side_image_label.place(x=5, y=100)

        # ========================================================================
        # ============ Sign In Image =============================================
        # ========================================================================
        self.sign_in_image = Image.open('images\\hyy.png')
        photo = ImageTk.PhotoImage(self.sign_in_image)
        self.sign_in_image_label = Label(self.lgn_frame, image=photo, bg='#040405')
        self.sign_in_image_label.image = photo
        self.sign_in_image_label.place(x=620, y=100)

        # ========================================================================
        # ============ Sign In label =============================================
        # ========================================================================
        self.sign_in_label = Label(self.lgn_frame, text="Sign In", bg="#040405", fg="white",
                                    font=("yu gothic ui", 17, "bold"))
        self.sign_in_label.place(x=650, y=210)

        # ========================================================================
        # ============================username====================================
        # ========================================================================
        self.username_label = Label(self.lgn_frame, text="Username", bg="#040405", fg="#4f4e4d",
                                    font=("yu gothic ui", 13, "bold"))
        self.username_label.place(x=550, y=270)

        self.username_entry = Entry(self.lgn_frame, highlightthickness=0, relief=FLAT, bg="#040405", fg="#6b6a69",
                                    font=("yu gothic ui ", 12, "bold"), insertbackground = '#6b6a69')
        self.username_entry.place(x=580, y=305, width=270)

        self.username_line = Canvas(self.lgn_frame, width=300, height=2.0, bg="#bdb9b1", highlightthickness=0)
        self.username_line.place(x=550, y=331)
        # ===== Username icon =========
        self.username_icon = Image.open('images\\username_icon.png')
        photo = ImageTk.PhotoImage(self.username_icon)
        self.username_icon_label = Label(self.lgn_frame, image=photo, bg='#040405')
        self.username_icon_label.image = photo
        self.username_icon_label.place(x=550, y=302)

        # ========================================================================
        # ============================login button================================
        # ========================================================================


        def login_users():
            self.username = self.username_entry.get()
            self.password = self.password_entry.get()
            print(self.username , self.password)



        self.lgn_button = Image.open('images\\btn1.png')
        photo = ImageTk.PhotoImage(self.lgn_button)
        self.lgn_button_label = Label(self.lgn_frame, image=photo, bg='#040405')
        self.lgn_button_label.image = photo
        self.lgn_button_label.place(x=550, y=450)
        self.login = Button(self.lgn_button_label, text='LOGIN', font=("yu gothic ui", 13, "bold"), width=25, bd=0,
                            bg='#3047ff', cursor='hand2', command = login_users,activebackground='#3047ff', fg='white')
        self.login.place(x=20, y=10)

        # ========================================================================
        # =========== Sign Up ==================================================
        # ========================================================================


        self.sign_label = Label(self.lgn_frame, text='No account yet?', font=("yu gothic ui", 11, "bold"),
                                relief=FLAT, borderwidth=0, background="#040405", fg='white')
        self.sign_label.place(x=580, y=560)

        self.signup_img = ImageTk.PhotoImage(file='images\\register.png')
        self.signup_button_label = Button(self.lgn_frame, image=self.signup_img, bg='#98a65d', cursor="hand2",
                                          borderwidth=0, background="#040405", command = self.signup_page, activebackground="#040405")
        self.signup_button_label.place(x=720, y=555, width=111, height=35)

        # ========================================================================
        # ============================password====================================
        # ========================================================================
        self.password_label = Label(self.lgn_frame, text="Password", bg="#040405", fg="#4f4e4d",
                                    font=("yu gothic ui", 13, "bold"))
        self.password_label.place(x=550, y=350)

        self.password_entry = Entry(self.lgn_frame, highlightthickness=0, relief=FLAT, bg="#040405", fg="#6b6a69",
                                    font=("yu gothic ui", 12, "bold"), show="*", insertbackground = '#6b6a69')
        self.password_entry.place(x=580, y=386, width=244)

        self.password_line = Canvas(self.lgn_frame, width=300, height=2.0, bg="#bdb9b1", highlightthickness=0)
        self.password_line.place(x=550, y=412)
        # ======== Password icon ================
        self.password_icon = Image.open('images\\password_icon.png')
        photo = ImageTk.PhotoImage(self.password_icon)
        self.password_icon_label = Label(self.lgn_frame, image=photo, bg='#040405')
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
        self.signup_frame = Frame(self.window, width=signup_frame_width, height=signup_frame_height, bg="#B6D0E2")
        self.signup_frame.place(x=signup_frame_x, y=signup_frame_y)
        self.sgnp_frame = Frame(self.window, bg='#040405', width=signup_frame_width, height=signup_frame_height)
        self.sgnp_frame.place(x=signup_frame_x, y=signup_frame_y)


        # ========================================================================
        # ========================================================
        # ========================================================================
        self.txt = "REGISTER"
        self.heading = Label(self.sgnp_frame, text=self.txt, font=('yu gothic ui', 25, "bold"), bg="#040405",
                             fg='white',
                             bd=5,
                             relief=FLAT)
        self.heading.place(x=80, y=30, width=300, height=30)

        # ========================================================================
        # ============ Left Side Image ================================================
        # ========================================================================
        self.side_image = Image.open('images\\vector.png')
        photo = ImageTk.PhotoImage(self.side_image)
        self.side_image_label = Label(self.sgnp_frame, image=photo, bg='#040405')
        self.side_image_label.image = photo
        self.side_image_label.place(x=5, y=100)

        # ========================================================================
        # ============ Sign Up Image =============================================
        # ========================================================================
        self.sign_up_image = Image.open('images\\add-friend.png')
        photo = ImageTk.PhotoImage(self.sign_up_image)
        self.sign_up_image_label = Label(self.sgnp_frame, image=photo, bg='#040405')
        self.sign_up_image_label.image = photo
        self.sign_up_image_label.place(x=640, y=30)

        # ========================================================================
        # ============ Sign In label =============================================
        # ========================================================================
        self.sign_in_label = Label(self.sgnp_frame, text="Sign Up", bg="#040405", fg="white",
                                    font=("yu gothic ui", 17, "bold"))
        self.sign_in_label.place(x=650, y=140)

        # ========================================================================
        # ============================username====================================
        # ========================================================================
        self.username_label = Label(self.sgnp_frame, text="Username", bg="#040405", fg="#4f4e4d",
                                    font=("yu gothic ui", 13, "bold"))
        self.username_label.place(x=550, y=200)

        self.username_entry = Entry(self.sgnp_frame, highlightthickness=0, relief=FLAT, bg="#040405", fg="#6b6a69",
                                    font=("yu gothic ui ", 12, "bold"), insertbackground = '#6b6a69')
        self.username_entry.place(x=580, y=235, width=270)

        self.username_line = Canvas(self.sgnp_frame, width=300, height=2.0, bg="#bdb9b1", highlightthickness=0)
        self.username_line.place(x=550, y=261)
        # ===== Username icon =========
        self.username_icon = Image.open('images\\username_icon.png')
        photo = ImageTk.PhotoImage(self.username_icon)
        self.username_icon_label = Label(self.sgnp_frame, image=photo, bg='#040405')
        self.username_icon_label.image = photo
        self.username_icon_label.place(x=550, y=232)


        # ========================================================================
        # ============================password====================================
        # ========================================================================
        self.password_label = Label(self.sgnp_frame, text="Password", bg="#040405", fg="#4f4e4d",
                                    font=("yu gothic ui", 13, "bold"))
        self.password_label.place(x=550, y=280)

        self.password_entry = Entry(self.sgnp_frame, highlightthickness=0, relief=FLAT, bg="#040405", fg="#6b6a69",
                                    font=("yu gothic ui", 12, "bold"), show="*", insertbackground = '#6b6a69')
        self.password_entry.place(x=580, y=316, width=244)

        self.password_line = Canvas(self.sgnp_frame, width=300, height=2.0, bg="#bdb9b1", highlightthickness=0)
        self.password_line.place(x=550, y=342)
        # ======== Password icon ================
        self.password_icon = Image.open('images\\password_icon.png')
        photo = ImageTk.PhotoImage(self.password_icon)
        self.password_icon_label = Label(self.sgnp_frame, image=photo, bg='#040405')
        self.password_icon_label.image = photo
        self.password_icon_label.place(x=550, y=314)
        # ========= show/hide password ==================================================================
        self.show_image = ImageTk.PhotoImage \
            (file='images\\show.png')

        self.hide_image = ImageTk.PhotoImage \
            (file='images\\hide.png')

        self.show_button = Button(self.sgnp_frame, image=self.show_image, command=self.show, relief=FLAT,
                                  activebackground="white"
                                  , borderwidth=0, background="white", cursor="hand2")
        self.show_button.place(x=860, y=320)






        self.class_label = Label(self.sgnp_frame, text="Class", bg="#040405", fg="#4f4e4d",
                                font=("yu gothic ui", 13, "bold"))
        self.class_label.place(x=600, y=365)

        self.class_combobox = ttk.Combobox(self.sgnp_frame, state="readonly", font=("yu gothic ui", 10, "bold"))
        self.class_combobox['values'] = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10')  # Add your class options here
        self.class_combobox.current(0)
        self.class_combobox.place(x=590, y=405, width=70)


        # Combobox for division selection
        self.division_label = Label(self.sgnp_frame, text="Division", bg="#040405", fg="#4f4e4d",
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

            cur.execute("INSERT INTO teachers VALUES (%s, %s, %s, %s, %s)",(self.new_teacher_username, self.new_teacher_password, self.new_teacher_class, self.new_teacher_division, self.new_teacher_isApproved))


            messagebox.showinfo("Success", "Account created successfully!\nGo to Login Page.\nYour ID is: " + str(self.new_teacher_username) + " and Password is: " + self.new_teacher_password)
            mydb.commit()

            entry_page(self.window)

        self.sgnp_button = Image.open('images\\btn1.png')
        photo = ImageTk.PhotoImage(self.sgnp_button)
        self.sgnp_button_label = Label(self.sgnp_frame, image=photo, bg='#040405')
        self.sgnp_button_label.image = photo
        self.sgnp_button_label.place(x=550, y=460)
        self.signnup = Button(self.sgnp_button_label, text='SIGNUP', font=("yu gothic ui", 13, "bold"), width=25, bd=0,
                            bg='#3047ff', cursor='hand2', command = signup_users, activebackground='#3047ff'
                            , activeforeground='white', fg='white')
        self.signnup.place(x=20, y=10)

        # Back button
        self.back_button = Button(self.sgnp_frame, text="Back to Login", bg="#040405", fg="white",
                                font=("yu gothic ui", 11, "bold"), relief=FLAT, activebackground="#040405", activeforeground='white',command=self.back_to_login)
        self.back_button.place(x=630, y=570)

        # Continue adding other components as before

    def back_to_login(self):
        # Destroy the signup frame
        self.signup_frame.destroy()
        # Recreate the login frame
        self.create_login_frame()

    def show(self):
        self.hide_button = Button(self.sgnp_frame, image=self.hide_image, command=self.hide, relief=FLAT,
                                  activebackground="white"
                                  , borderwidth=0, background="white", cursor="hand2")
        self.hide_button.place(x=860, y=320)
        self.password_entry.config(show='')

    def hide(self):
        self.show_button = Button(self.sgnp_frame, image=self.show_image, command=self.show, relief=FLAT,
                                  activebackground="white"
                                  , borderwidth=0, background="white", cursor="hand2")
        self.show_button.place(x=860, y=320)
        self.password_entry.config(show='*')



class entry_page:
    def __init__(self, window):
        # Destroy all widgets within the window
        for widget in window.winfo_children():
            widget.destroy()


def page():
    window = Tk()
    LoginPage(window)
    window.mainloop()


if __name__ == '__main__':
    page()