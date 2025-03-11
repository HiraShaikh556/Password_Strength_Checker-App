import streamlit as st
import re

st.set_page_config(page_title="Password Strength Checker", page_icon="🔐")

st.title("🔐 Password Strength Checker")
st.markdown("""
## Welcome to the ultimate password strength checker! 👋🏻  
Use this simple tool to check your password strength and get suggestions on how to make it secure.  
We will give you helpful tips to create a **Strong Password** 🔐
""")

password = st.text_input("Enter your password here:", type="password")

# Initialize score and feedback list
score = 0
feedback = []

if password:
    # Check password length
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("⁉️ Password should be at least 8 characters long.")

    # Check uppercase & lowercase characters
    if any(c.isupper() for c in password) and any(c.islower() for c in password):
        score += 1
    else:
        feedback.append("⁉️ Password should contain both upper and lower case letters.")

    # Check for digits
    if any(c.isdigit() for c in password):
        score += 1
    else:
        feedback.append("⁉️ Password should contain at least one digit.")

    # Check for special characters
    if re.search(r'[!@#$%^&*()_+]', password):
        score += 1
    else:
        feedback.append("⁉️ Password should contain at least one special character (e.g., @, #, $, etc.).")

    # Strength assessment
    strength_messages = {
        4: "✅ Your password is **strong!** 💪🏻",
        3: "☑️ Your password is **moderate!** 👍🏻 Consider making it stronger.",
        2: "‼️ Your password is **weak!** 👎🏻 You should improve it.",
        1: "🚨 **Very weak password!** ❌ Change it immediately.",
        0: "⚠️ **Extremely weak password!** ❌ Use a stronger password."
    }

    # Calculate Strength Percentage
    strength_percentage = (score / 4) * 100

    st.subheader("🔎 Password Strength:")
    st.markdown(strength_messages[score])

    # Show Progress Bar
    st.progress(strength_percentage / 100)  # Convert % to a range (0-1)

    # Show Strength % 
    st.write(f"**Password Strength: {strength_percentage:.0f}%**")

    if feedback:
        st.markdown("### 🔹 Suggestions to Improve:")
        for tip in feedback:
            st.write(tip)
else:
    st.write("🔍 Please enter a password to check its strength.")
