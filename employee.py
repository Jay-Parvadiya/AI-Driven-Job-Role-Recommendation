import random

import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import os
from datetime import date
import time
from streamlit_pdf_viewer import pdf_viewer
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from scipy.sparse import hstack

gender_group = ["Male", "Female", "Transgender"]
education_group =[
    "High School / 10th Pass",
    "Higher Secondary / 12th Pass",
    "Diploma",
    "Bachelor of Arts (BA)",
    "Bachelor of Science (BSc)",
    "Bachelor of Commerce (BCom)",
    "Bachelor of Technology (BTech)",
    "Bachelor of Engineering (BE)",
    "Bachelor of Computer Applications (BCA)",
    "Bachelor of Business Administration (BBA)",
    "Bachelor of Education (BEd)",
    "Bachelor of Law (LLB)",
    "Bachelor of Pharmacy (BPharm)",
    "Bachelor of Architecture (BArch)",
    "Bachelor of Design (BDes)",
    "Master of Arts (MA)",
    "Master of Science (MSc)",
    "Master of Commerce (MCom)",
    "Master of Technology (MTech)",
    "Master of Engineering (ME)",
    "Master of Computer Applications (MCA)",
    "Master of Business Administration (MBA)",
    "Master of Education (MEd)",
    "Master of Law (LLM)",
    "Master of Pharmacy (MPharm)",
    "Master of Design (MDes)",
    "Doctor of Philosophy (PhD)",
    "Chartered Accountant (CA)",
    "Company Secretary (CS)",
    "Certified Financial Analyst (CFA)",
    "ITI / Vocational Training",
    "Others"
]
technology_group =[
    "Software Development",
    "Web Development",
    "Mobile App Development",
    "Frontend Development",
    "Backend Development",
    "Full Stack Development",
    "Data Science",
    "Machine Learning",
    "Artificial Intelligence",
    "Cloud Computing",
    "DevOps",
    "Cybersecurity",
    "Blockchain",
    "Game Development",
    "Embedded Systems",
    "Internet of Things (IoT)",
    "UI/UX Design",
    "Graphic Design",
    "Product Management",
    "Project Management",
    "Business Analysis",
    "Quality Assurance / Testing",
    "Technical Support",
    "IT Infrastructure",
    "Database Management",
    "System Administration",
    "Network Engineering",
    "Digital Marketing",
    "Content Writing",
    "SEO/SEM",
    "Sales and Marketing",
    "Human Resources",
    "Finance and Accounting",
    "Operations Management",
    "Customer Support",
    "Legal and Compliance",
    "Consulting",
    "Education and Training",
    "Research and Development (R&D)",
    "Healthcare / Medical",
    "Logistics and Supply Chain",
    "Retail and E-commerce",
    "Banking and Finance",
    "Insurance",
    "Telecommunications",
    "Construction and Real Estate",
    "Manufacturing",
    "Energy and Utilities",
    "Media and Entertainment",
    "Public Relations",
    "Travel and Tourism",
    "Others"
]
place_group =[
    "Mumbai",
    "Delhi",
    "Bengaluru",
    "Hyderabad",
    "Chennai",
    "Kolkata",
    "Pune",
    "Ahmedabad",
    "Surat",
    "Jaipur",
    "Lucknow",
    "Kanpur",
    "Nagpur",
    "Indore",
    "Bhopal",
    "Patna",
    "Ludhiana",
    "Agra",
    "Nashik",
    "Vadodara",
    "Faridabad",
    "Meerut",
    "Rajkot",
    "Varanasi",
    "Amritsar",
    "Visakhapatnam",
    "Coimbatore",
    "Thiruvananthapuram",
    "Kochi",
    "Mysuru",
    "Noida",
    "Gurugram",
    "Chandigarh",
    "Jodhpur",
    "Ranchi",
    "Guwahati",
    "Raipur",
    "Dehradun",
    "Vijayawada",
    "Madurai",
    "Aurangabad",
    "Jabalpur",
    "Gwalior",
    "Udaipur",
    "Thrissur",
    "Bhavnagar",
    "Hubli-Dharwad",
    "Salem",
    "Tiruchirappalli",
    "Bilaspur",
    "Warangal",
    "Jammu",
    "Panaji",
    "Shimla",
    "Shillong",
    "Aizawl",
    "Itanagar",
    "Imphal",
    "Gangtok",
    "Puducherry",
    "Siliguri",
    "Dhanbad",
    "Bhilai",
    "Kolhapur",
    "Aligarh",
    "Bareilly",
    "Moradabad",
    "Tirupati",
    "Allahabad (Prayagraj)"
]
skill_group= [
    # Programming Languages
    "Python", "Java", "JavaScript", "C", "C++", "C#", "Go", "Ruby", "Kotlin", "Swift", "PHP", "TypeScript", "R",
    "MATLAB",

    # Web Development
    "HTML", "CSS", "React.js", "Angular", "Vue.js", "Node.js", "Django", "Flask", "Next.js", "Express.js",
    "Tailwind CSS", "Bootstrap",

    # Data Science & Machine Learning
    "Pandas", "NumPy", "Scikit-learn", "TensorFlow", "PyTorch", "Matplotlib", "Seaborn", "Keras", "OpenCV", "XGBoost",
    "NLP", "Deep Learning",
    "Data Analysis", "Data Visualization", "Statistics", "Power BI", "Tableau", "Machine Learning",
    "Artificial Intelligence", "Big Data",

    # Cloud & DevOps
    "AWS", "Azure", "Google Cloud Platform (GCP)", "Docker", "Kubernetes", "CI/CD", "Git", "GitHub", "Jenkins",
    "Terraform", "Linux",

    # Software Tools & Platforms
    "Figma", "Adobe XD", "Photoshop", "Illustrator", "Notion", "Slack", "Jira", "VS Code", "Eclipse", "IntelliJ",
    "Postman",

    # Database & Backend
    "SQL", "MySQL", "PostgreSQL", "MongoDB", "Oracle", "Firebase", "Redis", "REST API", "GraphQL", "SQLite",

    # Mobile Development
    "Flutter", "React Native", "SwiftUI", "Android Studio", "iOS Development", "Java (Android)",

    # Design & UI/UX
    "UI/UX Design", "Wireframing", "Prototyping", "Design Thinking", "User Research", "Interaction Design",

    # Business & Management
    "Project Management", "Agile Methodology", "Scrum", "Business Analysis", "Requirement Gathering",
    "Stakeholder Management",

    # Marketing
    "SEO", "SEM", "Google Analytics", "Email Marketing", "Social Media Marketing", "Content Writing", "Copywriting",
    "Brand Management",

    # Soft Skills
    "Communication", "Problem Solving", "Teamwork", "Leadership", "Creativity", "Critical Thinking", "Adaptability",
    "Time Management",

    # Others
    "Blockchain", "Cybersecurity", "AR/VR", "Game Development", "Testing / QA", "Selenium", "Penetration Testing",
    "Ethical Hacking",
    "Salesforce", "SAP", "Zoho", "Tally", "Microsoft Excel", "ChatGPT / AI Tools", "Prompt Engineering",
    "Language Proficiency (English, Hindi, etc.)",
    "Remote Collaboration", "Technical Writing", "Customer Service"
]
mode_group = ["On-Side", "Remote", "Internship"]
industries = [
    "Information Technology (IT)",
    "Software & Web Development",
    "Artificial Intelligence / Machine Learning",
    "Data Science & Analytics",
    "Cybersecurity",
    "Telecommunications",
    "E-commerce",
    "Financial Services / FinTech",
    "Banking & Insurance",
    "Healthcare / HealthTech",
    "Pharmaceuticals / Biotech",
    "Education / EdTech",
    "Manufacturing",
    "Automotive",
    "Aerospace / Aviation",
    "Construction & Real Estate",
    "Logistics / Supply Chain / Transportation",
    "Retail / Wholesale",
    "Consumer Goods / FMCG",
    "Media & Entertainment",
    "Marketing / Advertising / Digital Media",
    "Human Resources / Staffing",
    "Legal / Law Firms",
    "Government / Public Sector",
    "Non-Profit / NGOs",
    "Agriculture / Agritech",
    "Energy / Utilities / Oil & Gas",
    "Environmental Services / CleanTech",
    "Hospitality / Tourism / Travel",
    "Food & Beverage / FoodTech",
    "Sports & Recreation",
    "Fashion & Apparel",
    "Mining & Metals",
    "Chemicals",
    "Printing / Publishing",
    "Electronics / Hardware",
    "Robotics / Automation",
    "Marine / Shipping",
    "Textiles",
    "Event Management",
    "Animation / VFX / Gaming",
    "Architecture / Interior Design",
    "Consulting / Business Services",
    "Investment / Venture Capital / Private Equity",
    "Blockchain / Cryptocurrency",
    "Customer Service / BPO",
    "Freelance / Gig Economy",
    "Spiritual / Wellness / Yoga",
    "Pet Care / Veterinary",
    "Other"
]

my_dic={
    "username":"",
    "name":"",
    "number":"",
    "email":"",
    "gender":"",
    "bdate":"",
    "location":"",
    "education":"",
    "10th":"",
    "12th":"",
    "CGPA":"",
    "technology":"",
    "skills":"",
    "experience":"",
    "current_position":"",
    "linkedin_link":"",
    "github_link":""
}
project_dic={}

ran_int = ""
for i in range(6):
    ran_int += str(random.randint(0, 9))

# candidate_id = f"{st.session_state.username}" + ran_int
candidate_id=""

# main employee page
def main_employee():
    st.session_state.select_user="Employee"
    with st.sidebar:
        sidebar=option_menu("Employee",["Home","Profile","Project","Resume","Job","Role Recommendation","Visualization","Contact","About Project","Logout"],default_index=0,menu_icon="pie-chart",icons=["house","person","star","clipboard","lightbulb","star","bar-chart-fill","phone","bell","lock"], orientation="vertical")

    home(sidebar)
    profile(sidebar)
    About_Project(sidebar)
    resume(sidebar)
    job(sidebar)
    recommendation(sidebar)
    contact(sidebar)
    logout(sidebar)
    project(sidebar)

# home navigation
def home(sidebar):
    if sidebar=="Home":
        global candidate_id
        candidate_id=f"{st.session_state.username}"+ran_int
        st.header("RecruitWise")
        st.toast(" Welcome To RecruitWise",icon="🎊")
        st.success(f'{st.session_state.username} , Login Successfully ✅')
        st.subheader("AI-Driven Intelligent Skill-Based Role Recommendation Model for Optimized Recruitment")
        st.image("image1.jpg")

        with st.expander("See More Info 🔽"):
            st.write('''The AI-Driven Resume and Job Matching System for Optimal Talent Acquisition is designed to 
                                        enhance the recruitment process by intelligently connecting candidates with the most relevant job 
                                        opportunities. Utilizing advanced machine learning algorithms and natural language processing, the 
                                        system analyzes job requirements and candidate profiles to identify the best-fit opportunities. By 
                                        leveraging data-driven insights and predictive analytics, it ensures a seamless and efficient hiring 
                                        experience for both employers and job seekers. This system optimizes talent acquisition by fostering 
                                        meaningful connections, reducing hiring complexities, and improving overall workforce alignment.''')

# profile navigation
def profile(sidebar):
    if sidebar == "Profile":
        st.caption("Employee")
        file_path = f"Dataset/{st.session_state.user}/{st.session_state.username}/profile_{st.session_state.username}.csv"
        if os.path.exists(file_path):
            profile_pic_path=f"Dataset/{st.session_state.user}/{st.session_state.username}/Profile_picture_{st.session_state.username}.jpg"
            profile_data_entry()
            col1 , col2 =st.columns(2,gap="small",vertical_alignment="center")
            with col1:
                st.image(profile_pic_path,width=200)
            with col2:
                st.title(my_dic['name'].upper())
                st.write(f"username :   **{my_dic['username']}**")
                st.write(f"type :   **{st.session_state.user}**")
            st.divider()
            profile_details()
            st.divider()
            profile_edit=st.button("Edit")

        else:
            print("File does not exist.")
            st.info("You Have To Add Data First !!")
            if st.button("Add Profile"):
                Add_New_Profile_Data()

def profile_details():
    st.caption("Personal :")
    st.write(f"Gender  :  **{my_dic['gender']}**")
    st.write(f"Birth Date  :  **{my_dic['bdate']}**")
    st.write("Location :")
    st.write("Age :")

    st.divider()

    st.caption("Education :")
    st.write(f"Higher Education  :  **{my_dic['education']}**")
    st.write(f"CGPA  :  **{my_dic['CGPA']}**")
    st.write(f"10th  :  **{my_dic['10th']} %**")
    st.write(f"12th  :  **{my_dic['12th']} %**")

    st.divider()

    st.caption("Professional :")
    st.write(f"Technology  :  **{my_dic['technology']}**")
    st.write(f"Skills  :  **{my_dic['skills']}**")
    st.write(f"Experience  :  **{my_dic['experience']}**")
    st.write(f"Current Status  :  **{my_dic['current_position']}**")

    st.divider()

    st.caption("Contact :")
    st.write(f"Phone Number  :  **{my_dic['number']}**")
    st.write(f"Email ID  :  **{my_dic['email']}**")
    st.write(f"LinkedIN Link  :  **{my_dic['linkedin_link']}**")
    st.write(f"GitHub Link  :  **{my_dic['github_link']}**")

def project(sidebar):
    if sidebar=="Project":
        if os.path.exists(f"Dataset/{st.session_state.user}/{st.session_state.username}/Project_{st.session_state.username}.csv"):
            df=pd.read_csv(f"Dataset/{st.session_state.user}/{st.session_state.username}/Project_{st.session_state.username}.csv")
            rows ,cols =df.shape
            options = ["View All Projects","Add Project","Delete Project"]
            view_all_projects , add_project , delete_project = st.tabs(options)

            with view_all_projects:
                if rows==0:
                    st.info("There Is No Projects Yet !")
                for i in range(0, rows):
                    st.markdown(
                        f"""
                        <style>
                        .box {{
                            background-color: #121212; 
                            padding: 15px; 
                            border-radius: 8px; 
                            margin: 10px 0px;
                            border : 0.02px solid gray;
                            box-shadow: 2px 2px 5px rgba(0,0,0,0.1);
                        }}
                        </style>

                        <div class="box">
                            <h4>{df.at[i, 'Project Name']}</h4>
                            <p>{df.at[i, 'Project Description']}</p>
                            <p>{df.at[i, 'Project Status']}</p>
                            <p>{df.at[i, 'Project Technology']}</p>
                        </div>
                        """,
                        unsafe_allow_html=True
                    )
            # add
            with add_project:
                st.subheader("Add New Projects")
                file_path = f"Dataset/{st.session_state.user}/{st.session_state.username}/Project_{st.session_state.username}.csv"
                project_df = pd.read_csv(file_path)
                rows, cols = project_df.shape
                with st.form(key="add projects"):
                    project_name = st.text_input("Project Name", max_chars=20)
                    project_description = st.text_input("Project Description")
                    project_status = st.selectbox("Project Status",
                                                  ["Finished", "Progress", "Pending", "Hold", "Issue"])
                    project_technology = st.multiselect("Technology", technology_group)
                    project_link = st.text_input("Project Link")
                    project_submit = st.form_submit_button("Submit Project")

                    if project_submit:
                        if not project_name:
                            st.error("Enter Project Name!!")
                        elif not project_description:
                            st.error("Enter Project Description")
                        elif not project_status:
                            st.error("Enter Project Status")
                        elif not project_technology:
                            st.error("Enter Used Technology Used In Project")
                        else:
                            new_data = pd.DataFrame(
                                [{'Project ID': rows + 1, 'Project Name': project_name,
                                  'Project Description': project_description,
                                  'Project Status': project_status, 'Project Technology': project_technology,
                                  'Project Link': project_link}])
                            # Append and save
                            df = pd.concat([project_df, new_data], ignore_index=True)
                            df.to_csv(file_path, index=False)
                            st.success("Successfully Uploaded Data.")

            # delete
            with delete_project:
                file_path = f"Dataset/{st.session_state.user}/{st.session_state.username}/Project_{st.session_state.username}.csv"
                project_df = pd.read_csv(file_path)
                rows, cols = project_df.shape
                list_of_projects = []
                for i in range(0, rows):
                    list_of_projects.append(project_df.at[i, "Project Name"])

                if list_of_projects == []:
                    st.info("No Projects Found !!")
                else:
                    with st.form(key="delete"):
                        st.subheader("Delete Projects")
                        project_name = st.selectbox("Select Project Name Which You Want To Delete", list_of_projects)
                        project_submit = st.form_submit_button("Delete")

                        if project_submit:
                            if not project_name:
                                st.error("Enter Project Name!!")
                            else:

                                # Append and save
                                df = project_df[project_df['Project Name'] != project_name]
                                df.to_csv(file_path, index=False)
                                st.success("Data Deleted")

        else:
            st.info("You Have To Add Projects First !!")
            if st.button("Add Project"):
                add_new_project_data()

# resume navigation
def resume(sidebar):
    if sidebar=="Resume":
        file_path=f"Dataset/{st.session_state.user}/{st.session_state.username}/Resume_{st.session_state.username}.pdf"
        if os.path.exists(file_path):
            process_bar()
            st.title(f"Resume")
            pdf_viewer(file_path)
        else:
            st.info("You Don`t Have Upload Resume Yet!!")

def contact(sidebar):
    if sidebar=="Contact":
        st.title("Contact Us")
        st.divider()
        st.markdown(
            """ We’d love to hear from you! Whether you have questions about our AI-driven revenue forecasting system, need support, or just want to share feedback, feel free to reach out.  
### Email Us  
For inquiries, collaborations, or support, email us at:  
*✉ bhesdadiyadaksh2601@gmail.com*  

### Call Us  
Prefer speaking with someone? Give us a call:  
*📱 +91 - 8799355080*  

### Stay Connected  
Follow us on social media for the latest updates and insights:  
- *[LinkedIn](#)*  
- *[Twitter](#)*  
- *[Instagram](#)*  

We look forward to connecting with you! 😊    
            """)

def job(sidebar):
    if sidebar=="Job":
        options = ["Recommended Jobs", "All Jobs","Applied Jobs"]

        recommended_jobs , all_jobs , applied_jobs = st.tabs(options)
        with recommended_jobs:
            st.subheader("Recommended Jobs")
            st.markdown(
                f"""
                        <style>
                        .box {{
                            background-color: #121212; 
                            padding: 15px; 
                            border-radius: 8px; 
                            margin: 10px 0px;
                            border : 0.05px solid gray;
                            box-shadow: 2px 2px 5px rgba(0,0,0,0.1);
                        }}
                        </style>

                        <div class="box">
                            <h4>Box 1:{st.session_state.username}</h4>
                            <p>This is the first styled box.</p>
                        </div>
                        """,
                unsafe_allow_html=True
            )
            st.write("R jobs")
        with all_jobs:
            st.subheader("All Jobs")
            st.markdown(
                f"""
                        <style>
                        .box {{
                            background-color: #121212; 
                            padding: 15px; 
                            border-radius: 8px; 
                            margin: 10px 0px;
                            border : 0.05px solid gray;
                            box-shadow: 2px 2px 5px rgba(0,0,0,0.1);
                        }}
                        </style>

                        <div class="box">
                            <h4>Box 1:{st.session_state.username}</h4>
                            <p>This is the first styled box.</p>
                        </div>
                        """,
                unsafe_allow_html=True
            )
            st.write("All Jobs")
        with applied_jobs:
            st.subheader("Applied Jobs")
            st.markdown(
                f"""
                        <style>
                        .box {{
                            background-color: #121212; 
                            padding: 15px; 
                            border-radius: 8px; 
                            margin: 10px 0px;
                            border : 0.05px solid gray;
                            box-shadow: 2px 2px 5px rgba(0,0,0,0.1);
                        }}
                        </style>

                        <div class="box">
                            <h4>Box 1:{st.session_state.username}</h4>
                            <p>This is the first styled box.</p>
                        </div>
                        """,
                unsafe_allow_html=True
            )
            st.write("Applied Jobs")

# about project navigation
def About_Project(side_bar_select):
    if side_bar_select=="About Project":

        st.title("Project Title")
        st.divider()
        st.write("AI-Driven Intelligent Skill-Based Role Recommendation Model for Optimized Recruitment")

        st.subheader("Abstract:")
        st.write('''The AI-Driven Resume and Job Matching System for Optimal Talent Acquisition is designed to 
                    enhance the recruitment process by intelligently connecting candidates with the most relevant job 
                    opportunities. Utilizing advanced machine learning algorithms and natural language processing, the 
                    system analyzes job requirements and candidate profiles to identify the best-fit opportunities. By 
                    leveraging data-driven insights and predictive analytics, it ensures a seamless and efficient hiring 
                    experience for both employers and job seekers. This system optimizes talent acquisition by fostering 
                    meaningful connections, reducing hiring complexities, and improving overall workforce alignment.''')

        st.subheader("Problems in the Existing System")
        st.write('''1. Time-Consuming Manual Screening – HR professionals spend excessive time reviewing resumes.''')
        st.write('''2. Mismatch in Job Selection – Candidates often apply for roles that do not match their skills.''')
        st.write('''3. Lack of Data-Driven Insights – Traditional hiring processes do not leverage predictive analytics.''')
        st.write('''4. Inefficient Talent Acquisition – Employers struggle to find the best-fit candidates efficientl''')
        st.write('''5. Bias in Recruitment – Human-led screening can lead to unconscious bias in hiring.''')

        st.subheader("Purpose of the Project ")
        st.write('''• To automate and optimize the recruitment process using AI-driven algorithms.''')
        st.write('''• To provide accurate job recommendations for candidates based on their profiles.''')
        st.write('''• To enable employers to quickly identify the best-fit candidates.''')
        st.write('''• To enhance data-driven decision-making in hiring.''')
        st.write('''• To minimize bias and increase fairness in the recruitment process.''')

        st.subheader("Functional Requirements")
        st.write('''1. Resume Parsing & Analysis – Extract key skills, experience, and qualifications from resumes.''')
        st.write('''2. Job Matching Algorithm – AI-based matching of candidates with job postings.''')
        st.write('''3. Job Posting & Management – Employers can create, edit, and manage job listings.''')
        st.write('''4. Recommendation System – Personalized job recommendations for candidates.''')
        st.write('''5. Feedback & Review System – Employers can provide feedback on applications.''')

        st.subheader("System Modules")
        st.write('''1. AI Job Matching Module – NLP-based resume analysis and job compatibility scoring.''')
        st.write('''2. Application Module – candidate applications and employer responses.''')
        st.write('''3. Recommendation System – Provides job suggestions based on user behavior and data.''')

        st.subheader("System Requirements")
        st.write('''Hardware Requirements:''')
        st.write('''        • Processor: Intel i5 or higher''')
        st.write('''        • RAM: 8GB minimum''')
        st.write('''        • Storage: 250GB SSD or more''')
        st.write('''        • Internet Connectivity: Stable broadband connection''')

        st.write('''Software Requirements:''')
        st.write('''        • Operating System: Windows''')
        st.write('''        • Pycharm , python''')
        st.write('''        • Required AI Libraries''')

        st.subheader("Front End and Back End of System")
        st.write('''• Front End (Client-Side): StreamLit''')
        st.write('''• Back End (Server-Side): Python , Machine Learning Models , AI models''')

        st.subheader("Download Pdf of Project Overview")
         # File path of the PDF to be shared
        pdf_file_path = "AI-Driven Intelligent Skill-Based Role Recommendation.pdf"  # Change this to your PDF file path

        # Open the file in binary mode
        with open(pdf_file_path, "rb") as file:
            pdf_data = file.read()

        # Create a download button
        st.download_button(
            label="Download PDF",
            data=pdf_data,
            file_name="AI-Driven Intelligent Skill-Based Role Recommendation.pdf",
            mime="application/pdf"
        )

# logout navigation
def logout(sidebar):
    if sidebar=="Logout":
        if st.button("Log Out"):
            st.session_state.logged_in = False
            st.session_state.page = "login"
            st.query_params.clear()
            process_bar()
            employee_data()
            st.rerun()

# profile data form
@st.dialog("Add Data")
def Add_New_Profile_Data():
    with st.form(key="form3"):
        name = st.text_input("Name :")
        number = st.text_input("Phone Number :")
        email = st.text_input("Email Id :")
        gender = st.selectbox("Gender :", gender_group)
        bdate=st.date_input("Birth Date :",min_value=date(1990, 1, 1),max_value=date(2030, 12, 31))
        education = st.selectbox("Higher Education :", education_group)
        marks_10 = st.number_input("10th Percentage :",step=0.25)
        marks_12 = st.number_input("12th Percentage :",step=0.25)
        marks_clg = st.number_input("Graduation CGPA :",step=0.05)
        technology = st.selectbox("Technology which you like to or work on :", technology_group)
        skills = st.multiselect("Skills :", skill_group)
        location = st.multiselect("City You Like To Do Work :", place_group, default=None)
        experience = st.number_input("Experience :", min_value=0, max_value=10, step=1)
        current_position = st.text_input("Your Current Position (Mention fresher if you do not have any) :")
        linkedin_link = st.text_input("LinkeIn Linke :")
        github_link = st.text_input("GitHub Link :")
        profile_picture = st.file_uploader("Upload Profile Picture",type=["jpg", "jpeg", "png"])
        resume = st.file_uploader("Latest resume(file formate must be pdf)", type=["pdf"])
        submit3 = st.form_submit_button("Submit")

        if submit3:
            if name=="":
                st.error("Enter Name First!!")
            elif number=="":
                st.error("Enter Number!!")
            elif email=="":
                st.error("Enter Email!!")
            elif gender=="":
                st.error("Select Gender!!")
            elif bdate=="":
                st.error("Enter Birth Date!!")
            elif education=="":
                st.error("Select Education!!")
            elif technology=="":
                st.error("Select Technology!!")
            elif skills=="":
                st.error("Select Skills!!")
            elif location=="":
                st.error("Select Place!!")
            elif marks_10=="":
                st.error("Enter 10th Marks!!")
            elif marks_12=="":
                st.error("Enter 12th Marks!!")
            elif marks_clg=="":
                st.error("Enter CGPA!!")
            elif experience=="":
                st.error("Enter Experience!!")
            elif linkedin_link=="":
                st.error("Enter LinkedIn Link!!")
            elif github_link=="":
                st.error("Enter GitHUb Link!!")
            elif profile_picture is None:
                st.error("Upload Profile Picture!!")
            # elif resume is None:
            #     st.error("Upload Resume!!")
            else:
                # Ensure the directory exists
                upload_folder = f"Dataset/{st.session_state.user}/{st.session_state.username}"
                if not os.path.exists(upload_folder):
                    os.makedirs(upload_folder)

                if profile_picture is not None:
                    with open(os.path.join(upload_folder, f"Profile_picture_{st.session_state.username}.jpg"), "wb") as f:
                        f.write(profile_picture.getbuffer())

                if resume is not None:
                    # Save the uploaded file
                    with open(os.path.join(upload_folder,f"Resume_{st.session_state.username}.pdf"), "wb") as f:
                        f.write(resume.getbuffer())
                add_profile_data(name,number,email,gender,bdate,location,education,marks_10,marks_12,marks_clg,technology,skills,experience,current_position,linkedin_link,github_link)
                # st.session_state.profile_data_entry=True
                profile_data_entry()
                st.success("Successfully Uploaded Data.")
                st.rerun()

            # except AttributeError and ValueError:
            #     st.error("Fill All Details First")

# data entry csv file
def add_profile_data(name,number,email,gender,bdate,location,education,marks_10,marks_12,marks_clg,technology,skills,experience,current_position,linkedin_link,github_link):
    columns = ["Candidate ID","Name", "Number", "Email", "Gender", "Birth Date","Location", "Education", "10th", "12th", "CGPA", "Technology","Skills","Experience", "Current Position", "LinkedIn Link", "GitHub Link"]

    df = pd.DataFrame(columns=columns)
    file_path = f"Dataset/{st.session_state.user}/{st.session_state.username}/profile_{st.session_state.username}.csv"

    new_data = pd.DataFrame(
        [{'Candidate ID':candidate_id,'Name': name, 'Number': int(number),'Email':email,'Gender':gender,'Birth Date':bdate,"Education":education,'Location':location,"10th":marks_10,"12th":marks_12,
          "CGPA":marks_clg,'Technology':technology,'Skills':skills,'Experience':experience,'Current Position':current_position,'LinkedIn Link':linkedin_link,'GitHub Link':github_link}])

    # Append and save
    df = pd.concat([df, new_data], ignore_index=True)
    df.to_csv(file_path, index=False)

    # data entry in main file
    file_path_new=f"Dataset/DATA/Main_Employee.csv"
    if os.path.exists(file_path_new):
        main_df=pd.read_csv(file_path_new)

        if candidate_id in main_df['Candidate ID'].values:
            main_df.loc[main_df["Candidate ID"]==candidate_id,["Name", "Number", "Email", "Gender", "Birth Date","Location", "Education", "10th", "12th", "CGPA", "Technology","Skills","Experience", "Current Position", "LinkedIn Link", "GitHub Link"]]=[name,number,email,gender,bdate,location,education,marks_10,marks_12,marks_clg,technology,skills,experience,current_position,linkedin_link,github_link]
        else:
             main_df=pd.concat([main_df,new_data],ignore_index=True)
             main_df.to_csv(file_path_new,index=False)
    else:
        main_df=pd.DataFrame(columns=["Candidate ID","Name", "Number", "Email", "Gender", "Birth Date","Location", "Education", "10th", "12th", "CGPA", "Technology","Skills","Experience", "Current Position", "LinkedIn Link", "GitHub Link","Project Count"],index=False)
        if candidate_id in main_df['Candidate ID'].values:
            main_df.loc[
                main_df["Candidate ID"] == candidate_id, ["Name", "Number", "Email", "Gender", "Birth Date", "Location",
                                                          "Education", "10th", "12th", "CGPA", "Technology", "Skills",
                                                          "Experience", "Current Position", "LinkedIn Link",
                                                          "GitHub Link"]] = [name, number, email, gender, bdate,
                                                                             location, education, marks_10, marks_12,
                                                                             marks_clg, technology, skills, experience,
                                                                             current_position, linkedin_link,
                                                                             github_link]
        else:
            main_df = pd.concat([main_df, new_data], ignore_index=True)
            main_df.to_csv(file_path_new, index=False)

# data entry on dictionary
def profile_data_entry():
    df=pd.read_csv(f"Dataset/{st.session_state.user}/{st.session_state.username}/profile_{st.session_state.username}.csv")
    my_dic["username"]=st.session_state.username
    my_dic["name"]=df.at[0, 'Name']
    my_dic["number"]=df.at[0,"Number"]
    my_dic["email"]=df.at[0,"Email"]
    my_dic["gender"]=df.at[0,"Gender"]
    my_dic["bdate"]=df.at[0,"Birth Date"]
    my_dic["location"]=df.at[0,"Location"]
    my_dic["education"]=df.at[0,"Education"]
    my_dic["10th"]=df.at[0,"10th"]
    my_dic["12th"]=df.at[0,"12th"]
    my_dic["CGPA"]=df.at[0,"CGPA"]
    my_dic["technology"]=df.at[0,"Technology"]
    my_dic["skills"]=df.at[0,"Skills"]
    my_dic["experience"]=df.at[0,"Experience"]
    my_dic["current_position"]=df.at[0,"Current Position"]
    my_dic["linkedin_link"]=df.at[0,"LinkedIn Link"]
    my_dic["github_link"]=df.at[0,"GitHub Link"]

@st.dialog("Add Data")
def add_new_project_data():
    columns_project = ["Project ID", "Project Name", "Project Description", "Project Status",
                       "Project Technology", "Project Link"]
    project_df = pd.DataFrame(columns=columns_project)
    project_df.to_csv(
        f"Dataset/{st.session_state.user}/{st.session_state.username}/Project_{st.session_state.username}.csv")
    with st.form(key="form3"):
        project_name=st.text_input("Project Name",max_chars=20)
        project_description=st.text_input("Project Description")
        project_status=st.selectbox("Project Status",["Finished","Progress","Pending","Hold","Issue"])
        project_technology=st.multiselect("Technology",technology_group)
        project_link=st.text_input("Project Link")
        project_submit=st.form_submit_button("Submit Project")

        if project_submit:
            if not project_name:
                st.error("Enter Project Name!!")
            elif not project_description:
                st.error("Enter Project Description")
            elif not project_status:
                st.error("Enter Project Status")
            elif not project_technology:
                st.error("Enter Used Technology Used In Project")
            else:
                add_project_data(project_name,project_description,project_status,project_technology,project_link)
                st.success("Successfully Uploaded Data.")
                st.rerun()

def add_project_data(project_name,project_description,project_status,project_technology,project_link):
    file_path=f"Dataset/{st.session_state.user}/{st.session_state.username}/Project_{st.session_state.username}.csv"
    project_df = pd.read_csv(file_path)
    rows , cols = project_df.shape
    new_data = pd.DataFrame(
        [{'Project ID':project_df.shape[0]+1,'Project Name':project_name,'Project Description':project_description,'Project Status':project_status,'Project Technology':project_technology,'Project Link':project_link}])
    # Append and save
    df = pd.concat([project_df, new_data], ignore_index=True)
    df.to_csv(file_path, index=False)

# loading bar
def process_bar():
    progress_bar = st.progress(0)
    for percent in range(1, 100,15):
        time.sleep(0.2)  # Simulate loading
        progress_bar.progress(percent)

def employee_data():
    if os.path.exists(f"Dataset/{st.session_state.user}/{st.session_state.username}/Project_{st.session_state.username}.csv") and os.path.exists(f"Dataset/{st.session_state.user}/{st.session_state.username}/profile_{st.session_state.username}.csv"):

        profile_df=pd.read_csv(f"Dataset/{st.session_state.user}/{st.session_state.username}/profile_{st.session_state.username}.csv")

        project_df=pd.read_csv(f"Dataset/{st.session_state.user}/{st.session_state.username}/Project_{st.session_state.username}.csv")
        rows , cols = project_df.shape
        project_count=rows

        main_df=pd.read_csv(f"Dataset/DATA/Main_Employee.csv")
        # if st.session_state.username in main_df["User Name"].values:
        main_df=pd.concat([main_df,profile_df],ignore_index=True)
        main_df["User Name"]=st.session_state.username
        main_df["Project Count"]=project_count
        main_df.to_csv(f"Dataset/DATA/Main_Employee.csv")

def recommendation(sidebar):
    if sidebar=="Role Recommendation":
        options=["Role Recommendation","Role Recommendation based on your profile"]
        role_recommendation_x , role_recommendation_y = st.tabs(options)
        with role_recommendation_x:
            role_recommendation()
        with role_recommendation_y:
            profile_role_rocommendation()

def role_recommendation():
    # Load dataset
    df = pd.read_csv("Dataset/DATA/final_curated_job_dataset - Copy.csv")  # Replace with your actual dataset file
    # Preprocessing
    le_edu = LabelEncoder()
    df['Encoded_Education'] = le_edu.fit_transform(df['Required Education'])

    vectorizer = TfidfVectorizer(tokenizer=lambda x: x.split(', '))
    skills_matrix = vectorizer.fit_transform(df['Required Skills'])

    education_matrix = df[['Encoded_Education']].values
    combined_features = hstack([skills_matrix, education_matrix])

    job_titles = df['Job Title'].tolist()

    # --- Skills list (can be expanded with all known skills)
    unique_skills = set()
    for skill_str in df['Required Skills']:
        for skill in skill_str.split(', '):
            unique_skills.add(skill.strip())
    skill_options = sorted(unique_skills)

    # Role Recommendation Function
    def recommend_role(user_education, user_skills_list):
        try:
            edu_encoded = le_edu.transform([user_education])[0]
        except:
            return "❌ Education not found in training data."

        user_skills = ', '.join(user_skills_list)
        skills_vector = vectorizer.transform([user_skills])
        user_vector = hstack([skills_vector, [[edu_encoded]]])
        similarities = cosine_similarity(user_vector, combined_features)
        top_index = similarities.argmax()
        return job_titles[top_index]

    st.header("Role Recommendation")
    st.markdown("Get job recommendations based on your **Education** and **Skills**.")

    with st.form("recommendation form"):
        # Education input
        education_input = st.selectbox("Select your Education", sorted(df['Required Education'].unique()))
        # Skills input (multiselect)
        skills_input = st.multiselect("Select your Skills", options=skill_options)
        submit_role=st.form_submit_button("Recommend Job Role")

    if submit_role:
        if skills_input:
            result = recommend_role(education_input, skills_input)
            process_bar()
            st.success(f"✅ Recommended Job Role: **{result}**")
        else:
            st.warning("⚠️ Please select at least one skill.")

def profile_role_rocommendation():
    # Load dataset
    df = pd.read_csv("Dataset/DATA/final_curated_job_dataset - Copy.csv")  # Replace with your actual dataset file
    df_profile=pd.read_csv(f"Dataset/{st.session_state.user}/{st.session_state.username}/profile_{st.session_state.username}.csv")
    # Preprocessing
    le_edu = LabelEncoder()
    df['Encoded_Education'] = le_edu.fit_transform(df['Required Education'])

    vectorizer = TfidfVectorizer(tokenizer=lambda x: x.split(', '))
    skills_matrix = vectorizer.fit_transform(df['Required Skills'])

    education_matrix = df[['Encoded_Education']].values
    combined_features = hstack([skills_matrix, education_matrix])

    job_titles = df['Job Title'].tolist()

    # --- Skills list (can be expanded with all known skills)
    unique_skills = set()
    for skill_str in df['Required Skills']:
        for skill in skill_str.split(', '):
            unique_skills.add(skill.strip())
    skill_options = sorted(unique_skills)

    # Role Recommendation Function
    def recommend_role(user_education, user_skills_list):
        try:
            edu_encoded = le_edu.transform([user_education])[0]
        except:
            return "❌ Education not found in training data."

        user_skills = ', '.join(user_skills_list)
        skills_vector = vectorizer.transform([user_skills])
        user_vector = hstack([skills_vector, [[edu_encoded]]])
        similarities = cosine_similarity(user_vector, combined_features)
        top_index = similarities.argmax()
        return job_titles[top_index]

    st.header("Role Recommendation Based On Your Profile")
    st.markdown("Get job recommendations based on your **Education** and **Skills**.")

    if st.button("role recommendation"):
        result = recommend_role(df_profile.at[0,"Education"],df_profile.at[0,"Skills"])
        process_bar()
        st.success(f"✅ Recommended Job Role: **{result}**")





