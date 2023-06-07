import streamlit as st

# Header and Introduction
st.title("Career Recommendation System")
st.write("Welcome to the Career Recommendation System. This app will help you discover the best-fit career option based on your profile and skill ratings.")

# User Input Section
st.header("User Profile")
name = st.text_input("Name")
age = st.number_input("Age", min_value=1, max_value=100)
education_level = st.selectbox("Education Level", ["High School", "Bachelor's Degree", "Master's Degree", "Ph.D."])
areas_of_interest = st.multiselect("Areas of Interest", ["Technology", "Business", "Art", "Healthcare", "Science"])
programming_skill = st.slider("Programming Skill (1-10)", 1, 10, 5)
communication_skill = st.slider("Communication Skill (1-10)", 1, 10, 5)
problem_solving_skill = st.slider("Problem Solving Skill (1-10)", 1, 10, 5)

# Recommendation Results
st.header("Recommendation Results")
# Perform your recommendation model's prediction based on the user's inputs
# Store the recommended career path in a variable called 'recommended_career'
recommended_career = "Software Engineer"  # Replace this with the actual recommendation

st.success(f"Based on your profile and skill ratings, we recommend a career in {recommended_career}.")

# Alternative Career Options
st.header("Alternative Career Options")
# List a few alternative career options along with brief descriptions
alternative_careers = {
    "Data Analyst": "Analyzing and interpreting complex data to help businesses make informed decisions.",
    "Digital Marketer": "Developing and implementing online marketing strategies to promote products or services.",
    "Graphic Designer": "Creating visual concepts using computer software to communicate ideas that inspire, inform, and captivate consumers."
}
for career, description in alternative_careers.items():
    st.write(f"**{career}**: {description}")

# Additional Resources
st.header("Additional Resources")
st.write("Here are some additional resources to explore and further enhance your career exploration:")
st.write("- [Website 1](https://www.example.com)")
st.write("- [Website 2](https://www.example.com)")
st.write("- [Online Course 1](https://www.example.com)")
st.write("- [Online Course 2](https://www.example.com)")

# Footer
st.write("Your app's footer or any necessary disclaimers can be placed here.")
