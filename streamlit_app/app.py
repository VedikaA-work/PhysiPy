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

with st.expander("🧠 Learn the Physics Behind This"):
    st.markdown("""
**Newton's Second Law**

F = m × a

F → Force (N)  
m → Mass (kg)  
a → Acceleration (m/s²)
""")

st.caption("👩‍💻 Created by Vedika Apte | PhysiPy")
