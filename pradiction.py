import streamlit as st
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from scipy.sparse import hstack

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

# --- Streamlit UI ---
st.set_page_config(page_title="AI Role Recommender", layout="centered")

st.title("🎯 AI-Driven Role Recommendation System")
st.markdown("Get job recommendations based on your **Education** and **Skills**.")

# Education input
education_input = st.selectbox("📘 Select your Education", sorted(df['Required Education'].unique()))

# Skills input (multiselect)
skills_input = st.multiselect("💡 Select your Skills", options=skill_options)

if st.button("🔍 Recommend Job Role"):
    if skills_input:
        result = recommend_role(education_input, skills_input)
        st.success(f"✅ Recommended Job Role: **{result}**")
    else:
        st.warning("⚠️ Please select at least one skill.")
