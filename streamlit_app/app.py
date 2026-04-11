import streamlit as st
import time

# 1. Page Configuration
st.set_page_config(page_title="PhysiPy", page_icon="⚛️")

# 2. Custom Styling
st.markdown("""
<style>
.card {
    background: rgba(255, 255, 255, 0.05);
    padding: 25px;
    border-radius: 12px;
    box-shadow: 0 4px 10px rgba(0,0,0,0.1);
    max-width: 450px;
    margin: auto;
}
</style>
""", unsafe_allow_html=True)

# 3. Header Section
st.title("⚛️ PhysiPy")
st.subheader("🍎 Newton's Second Law Calculator")

# 4. Main Calculator Card
st.markdown('<div class="card">', unsafe_allow_html=True)
st.write("### 🧮 Calculator")
mass = st.text_input("⚖️ Enter mass (kg)", placeholder="e.g. 10")
a = 9.8  # Constant acceleration
if st.button("🚀 Calculate Force"):
    if mass:
        try:
            m = float(mass)
            
            # Animation: Spinner gives the "Calculating" feel
            with st.spinner('⚙️ Physics Engine Computing...'):
                time.sleep(1.2)  # Short delay for visual effect
                force = m * a
            
            st.success(f"💪 Force = {force:.2f} N")
            st.balloons()
        except ValueError:
            st.error("❌ Please enter a valid number")
    else:
        st.warning("⚠️ Please enter a mass value first")
st.markdown('</div>', unsafe_allow_html=True)

# 5. Educational Content Section
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
    st.divider()
    st.caption("👩‍💻 Created by Vedika Apte | PhysiPy | M.Sc. Physics")
