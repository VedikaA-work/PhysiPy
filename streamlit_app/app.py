# PhysiPy - Newton's Second Law Calculator
# Author: Vedika Apte

import streamlit as st

# Page configuration
st.set_page_config(page_title="PhysiPy", page_icon="⚛️", layout="centered")

# Title
st.title("⚛️ PhysiPy")
st.markdown("### 📦 Newton's Second Law Calculator")

st.markdown("Use this tool to calculate the **force acting on a body**.")

st.markdown("---")

# Image for visual learning
st.image(
    "https://upload.wikimedia.org/wikipedia/commons/7/7f/Newton%27s_second_law.svg",
    caption="Force acting on an object",
    width=350
)

# Function from your original code
def Force(m, a):
    return m * a

# User input
mass = st.text_input("⚖️ Enter mass (kg)")

# Constant acceleration
a = 9.8

# Calculate button
if st.button("🚀 Calculate Force"):

    try:
        m = float(mass)

        if m == 0:
            st.error("❌ Error: Mass cannot be zero")

        else:
            F = Force(m, a)
            st.success(f"💪 Force acting on body = **{F} N**")
            st.balloons()

    except:
        st.error("❌ Please enter a numeric value")

st.markdown("---")

# Learn section (we will expand this with your README content)
with st.expander("🧠 Learn the Physics Behind This"):

    st.markdown("""
Newton's Second Law states that the **force acting on an object is equal to the product of its mass and acceleration**.

### Formula
**F = m × a**

Where:

- **F** → Force (Newton, N)
- **m** → Mass (kg)
- **a** → Acceleration (m/s²)

In this calculator we used **g = 9.8 m/s²**.
""")

st.markdown("---")

# Footer
st.markdown("#### 👩‍💻 Created by Vedika Apte | PhysiPy")

st.caption("Visitor Counter: 0001")
