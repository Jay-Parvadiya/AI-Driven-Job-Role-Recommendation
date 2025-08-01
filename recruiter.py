from streamlit import columns
from streamlit_option_menu import option_menu
import streamlit as st
import time
from datetime import date
import os
import pandas as pd

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

skills_group= [
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

mode_group = ["Full-time", "Part-time", "Internship", "Freelance"]

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
    "experience":"",
    "company_name":"",
    "company_size":"",
    "company_industry":"",
    "positions_hiring":"",
    "location":"",
    "company_website":"",
    "linkedId_link":"",
}

def main_recruiter():
    st.session_state.select_user = "Recruiter"
    with st.sidebar:
        sidebar = option_menu("Recruiter", ["Home", "Profile", "Job Post", "Employee Search","Visualization", "Contact Us",
                              "About Project", "Logout"], default_index=0, menu_icon="pie-chart",
                              icons=["house", "person", "star", "search", "bar-chart-fill", "phone",
                              "bell", "lock"], orientation="vertical")

    home(sidebar)
    profile(sidebar)
    jobpost(sidebar)
    contact(sidebar)
    employee_search(sidebar)
    About_Project(sidebar)
    logout(sidebar)

# home navigation
def home(sidebar):
    if sidebar=="Home":
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

# logout navigation
def logout(sidebar):
    if sidebar=="Logout":
        if st.button("Log Out"):
            st.session_state.logged_in = False
            st.session_state.page = "login"
            st.query_params.clear()
            process_bar()
            st.rerun()

def contact(sidebar):
    if sidebar=="Contact Us":
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

# loading bar
def process_bar():
    progress_bar = st.progress(0)
    for percent in range(1, 100,15):
        time.sleep(0.1)  # Simulate loading
        progress_bar.progress(percent)

# profile navigation
def profile(sidebar):
    if sidebar == "Profile":
        st.caption("Recruiter")
        file_path = f"Dataset/{st.session_state.user}/{st.session_state.username}/profile_{st.session_state.username}.csv"
        if os.path.exists(file_path):
            profile_pic_path=f"Dataset/{st.session_state.user}/{st.session_state.username}/Profile_picture_{st.session_state.username}.jpg"
            profile_data_entry()
            col1 , col2 =st.columns(2,gap="small",vertical_alignment="center")
            with col1:
                st.image(profile_pic_path,width=200)
            with col2:
                st.title(my_dic['name'].upper())
                st.caption(my_dic["company_name"])
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
    st.write(f"Experience  :  **{my_dic['experience']}**")

    st.divider()

    st.caption("Company :")
    st.write(f"Company Name  :  **{my_dic['company_name']}**")
    st.write(f"Company Size  :  **{my_dic['company_size']}**")
    st.write(f"Company Industry  :  **{my_dic['company_industry']} **")
    st.write(f"Position Hiring  :  **{my_dic['positions_hiring']} **")
    st.write(f"Location :  **{my_dic['location']} **")

    st.divider()

    st.caption("Contact :")
    st.write(f"Phone Number  :  **{my_dic['number']}**")
    st.write(f"Email ID  :  **{my_dic['email']}**")
    st.write(f"Company Website : **{my_dic['company_website']}**")
    st.write(f"LinkedIN Link  :  **{my_dic['linkedId_link']}**")

# profile data form
@st.dialog("Add Data")
def Add_New_Profile_Data():
    with st.form(key="form3"):
        full_name = st.text_input("Full Name :")
        number = st.text_input("Phone Number :")
        email = st.text_input("Email Id :")
        gender = st.selectbox("Gender :", gender_group)
        experience = st.number_input("Your Experience :", min_value=0, max_value=10, step=1)
        company_name = st.text_input("Company Name :")
        company_size = st.slider("Company Size :",min_value=1,max_value=1000,value=100)
        company_industry = st.multiselect("Industries Which Has Company Work On:",industries)
        positions_hiring=st.multiselect("Type of Positions Hiring",mode_group ,default=None)
        location = st.multiselect("Company Location:",place_group, default=None)
        company_website=st.text_input("Company Website Link :")
        linkedin_link = st.text_input("Company LinkeIn Link :")
        profile_picture = st.file_uploader("Upload Profile Picture",type=["jpg", "jpeg", "png"])
        submit5 = st.form_submit_button("Submit")

    if submit5:
        if full_name=="":
            st.error("Enter Full Name First!!")
        elif number=="":
            st.error("Enter Number!!")
        elif email=="":
            st.error("Enter Email!!")
        elif gender=="":
            st.error("Select Gender!!")
        elif experience=="":
            st.error("Enter Experience!!")
        elif company_name=="":
            st.error("Enter Company Name!!")
        elif company_size=="":
            st.error("Enter Company Size!!")
        elif company_industry=="":
            st.error("Select Industries Where Company Work On!!")
        elif location=="":
            st.error("Select Company Location!!")
        elif positions_hiring=="":
            st.error("Enter Positions Hiring!!")
        elif company_website=="":
            st.error("Enter Company Website Link!!")
        elif linkedin_link=="":
            st.error("Enter Company LinkedIn Link!!")
        elif profile_picture is None:
            st.error("Upload Profile Picture!!")
        else:
            # Ensure the directory exists
            upload_folder = f"Dataset/{st.session_state.user}/{st.session_state.username}"
            if not os.path.exists(upload_folder):
                os.makedirs(upload_folder)

            if profile_picture is not None:
                with open(os.path.join(upload_folder, f"Profile_picture_{st.session_state.username}.jpg"), "wb") as f:
                    f.write(profile_picture.getbuffer())

            columns = ["User Name","Name", "Number", "Email", "Gender", "Experience", "Company Name", "Company Size", "Company Industry", "Positions Hiring",
                       "Location", "Company Website", "Company LinkedIn Link"]

            df = pd.DataFrame(columns=columns)
            file_path = f"Dataset/{st.session_state.user}/{st.session_state.username}/profile_{st.session_state.username}.csv"

            new_data = pd.DataFrame(
                [{'User Name': st.session_state.username, 'Name': full_name, 'Number': int(number), 'Email': email,
                  'Gender': gender,'Experience':experience,'Company Name':company_name,'Company Industry':company_industry,'Position Hiring':positions_hiring,
                  'Location':location,'Company Website':company_website,'Company LinkedIn Link':linkedin_link}])

            # Append and save
            df = pd.concat([df, new_data], ignore_index=True)
            df.to_csv(file_path, index=False)

            # st.session_state.profile_data_entry=True
            profile_data_entry()
            st.success("Successfully Uploaded Data.")
            st.rerun()

            # except AttributeError and ValueError:
            #     st.error("Fill All Details First")

# data entry on dictionary
def profile_data_entry():
    df=pd.read_csv(f"Dataset/{st.session_state.user}/{st.session_state.username}/profile_{st.session_state.username}.csv")
    my_dic["username"]=df.at[0,'User Name']
    my_dic["name"]=df.at[0, 'Name']
    my_dic["number"]=df.at[0,"Number"]
    my_dic["email"]=df.at[0,"Email"]
    my_dic["gender"]=df.at[0,"Gender"]
    my_dic["experience"]=df.at[0,"Experience"]
    my_dic["company_name"]=df.at[0,"Company Name"]
    my_dic["company_size"]=df.at[0,"Company Size"]
    my_dic["company_industry"]=df.at[0,"Company Industry"]
    my_dic["positions_hiring"]=df.at[0,"Positions Hiring"]
    my_dic["location"]=df.at[0,"Location"]
    my_dic["company_website"]=df.at[0,"Company Website"]
    my_dic["linkedId_link"]=df.at[0,"Company LinkedIn Link"]


def jobpost(sidebar):
    if sidebar=="Job Post":
        file_path=f"Dataset/{st.session_state.user}/{st.session_state.username}/Jobs_{st.session_state.username}.csv"
        if os.path.exists(file_path):
            options = ["Existing Jobs Post","Add Jobs","Delete Job Post", "Job Post Status"]
            existing_jobs , add_jobs,delete_job_post, job_post_status = st.tabs(options)

            with add_jobs:
                with st.form("add job"):
                    st.subheader("Add Job Post")
                    company_name = st.text_input("Company Name")
                    job_title = st.selectbox("Job Title", technology_group)
                    job_description = st.text_input("Job Description")
                    required_education = st.multiselect("Required Education", education_group)
                    required_skills = st.multiselect("Required Skills", skills_group)
                    min_experience = st.slider("Minimum Experience", min_value=0, max_value=30, value=2)
                    job_location = st.multiselect("Job Location", place_group)
                    job_industry = st.selectbox("Job Industry", industries)
                    salary_range = st.slider("Salary Range", min_value=10000, max_value=5000000,
                                             value=(200000, 500000))
                    job_mode = st.selectbox("Mode", mode_group)
                    submit_job = st.form_submit_button("Submit Job")
                    if submit_job:
                        file_path = f"Dataset/{st.session_state.user}/{st.session_state.username}/Jobs_{st.session_state.username}.csv"
                        if not os.path.exists(file_path):
                            job_columns = ["Job ID", "Required Education", "Required Skills", "Min Experience",
                                           "Max Experience",
                                           "Job Location", "Industry", "Salary Range", "Job Description", "Mode",
                                           "Company Name", "Post Date", "Job Title"]
                            df = pd.DataFrame(columns=job_columns)
                            df.to_csv(file_path, index=False)

                        if os.path.exists(file_path):
                            df = pd.read_csv(file_path)
                            row, col = df.shape
                            today = date.today()

                            new_row = [{'Job ID': row + 1, "Required Education": required_education,
                                        "Required Skills": required_skills, "Min Experience": min_experience,
                                        "Job Location": job_location, "Industry": job_industry,
                                        "Salary Range to": salary_range[0], "Salary Range From": salary_range[1],
                                        "Job Description": job_description, "Mode": job_mode,
                                        "Company Name": company_name, "Post Date": today, "Job Title": job_title}]
                            # Convert to DataFrame
                            new_df = pd.DataFrame(new_row)
                            # Append to existing CSV without writing headers again
                            new_df.to_csv(file_path, mode='a', header=False, index=False)
                            process_bar()
                            st.success("Successfully Add Job Post")

            with delete_job_post:
                file_path = f"Dataset/{st.session_state.user}/{st.session_state.username}/Jobs_{st.session_state.username}.csv"
                project_df = pd.read_csv(file_path)
                rows, cols = project_df.shape
                list_of_jobs = []
                for i in range(0, rows):
                    list_of_jobs.append(project_df.at[i, "Job Title"])

                if list_of_jobs == []:
                    st.info("No Job Post Found !!")
                else:
                    with st.form(key="add projects"):
                        st.subheader("Delete Job Post")
                        job_title = st.selectbox("Select Job Title Which You Want To Delete", list_of_jobs)
                        job_title_submit = st.form_submit_button("Delete")

                        if job_title_submit:
                            if not job_title:
                                st.error("Enter Job Title Name!!")
                            else:
                                # Append and save
                                df = project_df[project_df['Job Title'] != job_title]
                                df.to_csv(file_path, index=False)
                                process_bar()
                                st.success("Data Deleted")

            with job_post_status:
                #show apply candidates
                pass

            with existing_jobs:
                file_path = f"Dataset/{st.session_state.user}/{st.session_state.username}/Jobs_{st.session_state.username}.csv"
                df = pd.read_csv(file_path)
                rows, cols = df.shape
                if rows==0:
                    st.info("There Is No Job Post Yet !!!")
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
                            <h4>{df.at[i, 'Job Title']}</h4>
                            <p>{df.at[i, 'Job Description']}</p>
                            <p>{df.at[i, 'Post Date']}</p>
                            <p>{df.at[i, 'Mode']}</p>
                            <p>{df.at[i, 'Job Location']}</p>
                        </div>
                        """,
                        unsafe_allow_html=True
                    )
        else:
            st.info("You Dont Have Upload Jobs Yet!!")
            job_add=st.button("Add Job")
            if job_add:
                add_job_form()

@st.dialog("ADD JOBS")
def add_job_form():
    with st.form("add job"):
        company_name=st.text_input("Company Name")
        job_title=st.selectbox("Job Title",technology_group)
        job_description=st.text_input("Job Description")
        required_education=st.multiselect("Required Education",education_group)
        required_skills=st.multiselect("Required Skills",skills_group)
        min_experience=st.slider("Minimum Experience",min_value=0,max_value=30,value=2)
        job_location=st.multiselect("Job Location",place_group)
        job_industry=st.selectbox("Job Industry",industries)
        salary_range=st.slider("Salary Range",min_value=10000,max_value=5000000,value=(200000,500000))
        job_mode=st.selectbox("Mode",mode_group)
        submit_job=st.form_submit_button("Submit Job")
        if submit_job:
            file_path = f"Dataset/{st.session_state.user}/{st.session_state.username}/Jobs_{st.session_state.username}.csv"
            if not os.path.exists(file_path):
                job_columns = ["Job ID", "Required Education", "Required Skills", "Min Experience", "Max Experience",
                               "Job Location", "Industry", "Salary Range", "Job Description", "Mode",
                               "Company Name", "Post Date", "Job Title"]
                df = pd.DataFrame(columns=job_columns)
                df.to_csv(file_path,index=False)

            if os.path.exists(file_path):
                df=pd.read_csv(file_path)
                row,col =df.shape
                today = date.today()

                new_row = [{'Job ID':row+1,"Required Education":required_education,"Required Skills":required_skills,"Min Experience":min_experience,"Job Location":job_location,"Industry":job_industry,"Salary Range to":salary_range[0],"Salary Range From":salary_range[1],"Job Description":job_description,"Mode":job_mode,"Company Name":company_name,"Post Date":today,"Job Title":job_title}]
                # Convert to DataFrame
                new_df = pd.DataFrame(new_row)
                # Append to existing CSV without writing headers again
                new_df.to_csv(file_path, mode='a', header=False, index=False)
                st.success("Successfully Add Job Post")
                process_bar()
                st.rerun()


def employee_search(sidebar):
    if sidebar=="Employee Search":
        option=["Search Employee","Filter"]

        employee_search , filter = st.tabs(option)

        with employee_search:
            # Specify the path
            path = 'Dataset/Employee/'  # Current directory, or replace with your target path
            # List all folders in the path
            folders = [name for name in os.listdir(path) if os.path.isdir(os.path.join(path, name))]
            folder_name=[]
            # Print the folders
            for folder in folders:
                folder_name.append(folder)
            with st.form("employee_search"):
                st.subheader("Search For Employee")
                employee_name=st.selectbox("Search By Employee Name",folder_name)
                submit_employee = st.form_submit_button("Search")

            if submit_employee:
                file_path = f"Dataset/Employee/{employee_name}/profile_{employee_name}.csv"
                employee_profile_show(file_path,employee_name)

            with filter:
                pass


@st.dialog("Employee Profile")
def employee_profile_show(file_path,employee_name):
    df=pd.read_csv(file_path)
    st.caption("Employee")
    if os.path.exists(file_path):
        profile_pic_path = f"Dataset/Employee/{employee_name}/Profile_picture_{employee_name}.jpg"
        profile_data_entry()
        col1, col2 = st.columns(2, gap="small", vertical_alignment="center")
        with col1:
            st.image(profile_pic_path, width=200)
        with col2:
            st.title(df.at[0,"Name"].upper())
            st.write(df.at[0,"Gender"])
            st.write(df.at[0,"Location"].upper())
        st.divider()

        st.caption("Education :")
        st.write(f"Higher Education  :  **{df.at[0,'Education']}**")
        st.write(f"CGPA  :  **{df.at[0,'CGPA']}**")
        st.write(f"10th  :  **{df.at[0,'10th']} %**")
        st.write(f"12th  :  **{df.at[0,'12th']} %**")

        st.divider()

        st.caption("Professional :")
        st.write(f"Technology  :  **{df.at[0,'Technology']}**")
        st.write(f"Skills  :  **{df.at[0,'Skills']}**")
        st.write(f"Experience  :  **{df.at[0,'Experience']}**")
        st.write(f"Current Status  :  **{df.at[0,'Current Position']}**")

        st.divider()

        st.caption("Contact :")
        st.write(f"LinkedIN Link  :  **{df.at[0,'LinkedIn Link']}**")
        st.write(f"GitHub Link  :  **{df.at[0,'GitHub Link']}**")
    else:
        print("File does not exist.")
        st.error("File Not Found")


# def Filter(side_bar_select):
#     if side_bar_select=="Filter":
#         directory_path = r"C:\Users\DAKSH\PycharmProjects\PythonProject\new_project\DataScience_Internship\Week 8\Day 37\uploaded_file"
#         if os.path.exists(directory_path):
#
#
#         # Applying multiple filters at once
#         filtered_df = df[
#             ((df["Age"]>=age_range[0]) & (df["Age"]<=age_range[1])) &
#             ((df["Experience"]>=experience_range[0])&(df["Experience"]<=experience_range[1])) &
#             (df["Gender"].isin(select_gender)) &
#             (df["Education"].isin(select_education)) &
#             (df["Technology"].isin(select_technology)) &
#             (df["Place"].isin(select_place)) &
#             (df["Mode"].isin(select_mode)) &
#             (df["Current Position"].isin(select_current_position)) &
#             (df["Skills"].apply(lambda x: all(skill in x for skill in select_skills)))
#             ]
#
#         st.dataframe(filtered_df,hide_index=True)