import streamlit as st

st.set_page_config(page_title="PhysiPy", page_icon="⚛️")

# Simple card styling
st.markdown("""
<style>
.card {background:white;padding:25px;border-radius:12px;
box-shadow:0 4px 10px rgba(0,0,0,0.1);max-width:450px;margin:auto;}
</style>
""", unsafe_allow_html=True)

st.title("⚛️ PhysiPy")
st.subheader("📦 Newton's Second Law Calculator")

st.markdown('<div class="card">', unsafe_allow_html=True)

mass = st.text_input("⚖️ Enter mass (kg)")
a = 9.8

if st.button("🚀 Calculate Force"):
    try:
        m = float(mass)
        st.success(f"💪 Force = {m*a} N")
        st.balloons()
    except:
        st.error("Enter a valid number")

st.markdown('</div>', unsafe_allow_html=True)

with st.expander("🧠 Learn the Physics & Logic"):
    st.markdown("""
    ### 🧪 Scientific Overview
    Newton's Second Law states that the acceleration of an object depends on the mass of the object and the amount of force applied.
    
    **The Formula:**
    $$F = m \\times a$$
    
    * **Force ($F$):** Measured in Newtons ($N$).
    * **Mass ($m$):** Measured in Kilograms ($kg$).
    * **Acceleration ($a$):** The rate of change of velocity ($m/s^2$).
    
    ---
    ### 💻 Implementation Details
    This calculator is built with robust programming practices:
    * **Standard Constants:** Defaults to Earth's gravity ($9.8 \, m/s^2$).
    * **Input Validation:** Uses `try-except` blocks to ensure only numeric data is processed.
    * **Modular Design:** Written for easy integration into larger physics simulations.
    """)
    st.caption("👩‍💻 Created by Vedika Apte | PhysiPy")
