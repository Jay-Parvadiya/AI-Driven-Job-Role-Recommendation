import pandas as pd
import streamlit as st
import os
from click import password_option
from streamlit import session_state, query_params
from streamlit_option_menu import option_menu
import random
import smtplib
from email.message import EmailMessage
from main import main
from main import userstatus
from main import navigate


if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.username = None

if "OTP" not in st.session_state: # done
    st.session_state.OTP = ""

if "select_user" not in st.session_state: # done
    st.session_state.select_user=""

if "user" not in st.session_state: #done
    st.session_state.user=""

if "emp" not in st.session_state: #done
    st.session_state.emp=False

if "rec" not in st.session_state: # done
    st.session_state.rec=False

# if 'page' not in st.session_state:
#     st.session_state.page = "login"

# Check query params

# if "auth" in st.query_params and query_params["auth"] == "true":
#     st.session_state.logged_in = True

# if "auth" in st.query_params:
#     st.session_state.logged_in = True

page=st.query_params.get("page", "login")

def login():
    with st.sidebar:
        sidebar_select = option_menu("Main", ["Log-in", "Sign-Up"], default_index=0,
                                     menu_icon="house", icons=["lock", "unlock"], orientation="vertical")

    # if st.session_state.logged_in:
    #     # st.query_params["auth"] = "true"
    #     # navigate("profile")
    #     # main()
    #     # userstatus(session_state)
    if sidebar_select == "Log-in":
        login_form()
    elif sidebar_select == "Sign-Up":
        signup_form()

# Login Form
def login_form():

    with st.form("LoginForm"):
        st.title("Log In")
        select_user=st.selectbox("Select User Type", ["Employee", "Recruiter"])
        username = st.text_input("Enter Your Username")
        password = st.text_input("Enter Your Password", type="password")
        submit = st.form_submit_button("Submit")

        if submit:
            if check_user_data(select_user,username, password):
                st.session_state.logged_in = True
                st.session_state.username = username
                # st.query_params["auth"] = "true"
                st.session_state.user=select_user
                # st.session_state.page = "profile"
                userstatus(session_state)
                main()
                st.success("Login Successfully ✅")
                # query_params.update(logged_in="ture" , username=username, user=select_user)
            else:
                st.error("Invalid Username or Password ❌")


# Signup Form
def signup_form():
    with st.expander("select_field"):
        if st.button("Employee"):
            st.session_state.emp = True
            st.session_state.rec = False  # Ensure only one selection
        if st.button("Recruiter"):
            st.session_state.rec = True
            st.session_state.emp = False  # Ensure only one selection

            # Show form based on selection
    if st.session_state.emp:
        st.session_state.select_user="Employee"
        check_for_employee()
    elif st.session_state.rec:
        st.session_state.select_user="Recruiter"
        check_for_recruiter()

def check_for_employee():
    with st.form("SignupForm"):
        st.title("Sign Up")
        new_username = st.text_input("Enter New Username")
        new_password = st.text_input("Enter Password", type="password")
        user_name=st.text_input("Enter Your Name")
        user_email=st.text_input("Enter Your Email Id")
        send_submit = st.form_submit_button("Send OTP")

    if send_submit:

        try:
            if new_username=="":
                st.error("Enter New Username")
            elif new_password=="":
                st.error("Enter New Password")
            if user_name=="":
                st.error("Enter User Name")
            elif user_email=="":
                st.error("Enter Email")
            elif check_user_available(new_username,st.session_state.select_user):
                st.error("Username already taken ❌")
            else:
                st.session_state.OTP= mail_varify(user_email,user_name,st.session_state.select_user)

        except smtplib.SMTPRecipientsRefused:
            st.error("Enter Valid Email ID")

    if len(session_state.OTP)==6:
        with st.form("check_form"):
            user_otp = st.text_input("Enter OTP:")
            submit8=st.form_submit_button("submit")

        if submit8:
            if check_user_available(new_username,st.session_state.select_user):
                st.success("User Successfully Registered 🎉")
            else:
                if user_otp==st.session_state.OTP:
                    enter_new_data(st.session_state.select_user,new_username,new_password)
                    add_employee_folder(new_username)
                    st.success("User Successfully Registered 🎉")


                elif user_otp=="":
                    st.error("Enter OTP First")
                else:
                    print(st.session_state.OTP)
                    st.error("Invalid OTP")

def check_for_recruiter():
    with st.form("SignupForm2"):
        st.title("Sign Up")
        new_username = st.text_input("Enter New Username")
        new_password = st.text_input("Enter Password", type="password")
        user_name=st.text_input("Enter Your Name")
        user_email=st.text_input("Enter Your Email Id")
        send_submit = st.form_submit_button("Send OTP")

    if send_submit:
        try:
            if new_username=="":
                st.error("Enter New Username")
            elif new_password=="":
                st.error("Enter New Password")
            elif user_name=="":
                st.error("Enter User Name")
            elif user_email=="":
                st.error("Enter Email")
            elif check_user_available(new_username,st.session_state.select_user):
                st.error("Username already taken ❌")
            else:
                st.session_state.OTP= mail_varify(user_email,user_name,st.session_state.select_user)

        except smtplib.SMTPRecipientsRefused:
            st.error("Enter Valid Email ID")

    if len(session_state.OTP)==6:
        with st.form("check_form"):
            user_otp = st.text_input("Enter OTP:")
            submit8=st.form_submit_button("submit")

        if submit8:
            if check_user_available(new_username,st.session_state.select_user):
                st.success("User Successfully Registered 🎉")
            else:
                if user_otp==st.session_state.OTP:
                    enter_new_data(st.session_state.select_user,new_username, new_password)
                    add_recruiter_folder(new_username)
                    st.success("User Successfully Registered 🎉")

                elif user_otp=="":
                    st.error("Enter OTP First")
                else:
                    print(st.session_state.OTP)
                    st.error("Invalid OTP")

# Store new user credentials
def check_user_data(selected_user,username, password):
    try:
        if selected_user=="Employee":
            df = pd.read_excel("Dataset/Data/Employee_data.xlsx")
            return any((df["User Name"] == username) & (df["Password"].astype(str) == password))
        elif selected_user=="Recruiter":
            df = pd.read_excel("Dataset/Data/Recruiter_data.xlsx")
            return any((df["User Name"] == username) & (df["Password"].astype(str) == password))
    except FileNotFoundError:
        return False
    except Exception as e:
        st.error(f"Error reading user data: {e}")
        return False
# Check if username is already taken
def check_user_available(username,select_user):
    try:
        if select_user == "Employee":
            df = pd.read_excel("Dataset/DATA/Employee_data.xlsx")
            return username in df['User Name'].values
        elif select_user == "Recruiter":
            df = pd.read_excel("Dataset/DATA/Recruiter_data.xlsx")
            return username in df['User Name'].values
    except FileNotFoundError:
        return False

def enter_new_data(user_select,username, password):
    file_path=""
    if user_select=="Employee":
        file_path = "Dataset/DATA/Employee_data.xlsx"
    elif user_select=="Recruiter":
        file_path = "Dataset/DATA/Recruiter_data.xlsx"
    try:
        existing_data = pd.read_excel(file_path)
    except FileNotFoundError:
        existing_data = pd.DataFrame(columns=["No", "User Name", "Password"])

    new_data = pd.DataFrame([{'No': len(existing_data) + 1, 'User Name': username, 'Password': str(password)}])
    updated_data = pd.concat([existing_data, new_data], ignore_index=True)
    updated_data.to_excel(file_path, index=False)

def mail_varify(user_mail,user_name,select_user):
    otp = ""

    for i in range(6):
        otp += str(random.randint(0, 9))

    # print(otp)

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()

    from_mail = "pateldax2601@gmail.com"
    server.login(from_mail, "tvou ifug xacj nyha")
    to_mail = user_mail

    msg = EmailMessage()
    msg["Subject"] = "OTP Verification"
    msg["From"] = from_mail
    msg["To"] = to_mail
    msg.set_content(f"{select_user} {user_name} , Your OTP is :" + otp)
    server.send_message(msg)
    return otp


# work with datasets

def add_employee_folder(new_username):

    path = f"Dataset/Employee/{new_username}"
    os.makedirs(path, exist_ok=True)
    print("Folders created successfully!")

def add_recruiter_folder(new_username):
    path = f"Dataset/Employee/{new_username}"
    os.makedirs(path, exist_ok=True)
    print("Folders created successfully!")


# # Redirect based on login state
# if st.session_state.logged_in:
#     userstatus(session_state)
#     main()
# else:
if page == "login":
    login()

    # if st.session_state.page == "login":


