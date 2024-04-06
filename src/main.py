import streamlit as st

# Using object notation
add_selectbox = st.sidebar.selectbox(
    "How would you like to be contacted?",
    ("Email", "Home phone", "Mobile phone")
)

# Using "with" notation
with st.sidebar:
    add_radio = st.radio(
        "Choose a shipping method",
        ("Standard (5-15 days)", "Express (2-5 days)")
    )
    
st.write("You selected:", add_selectbox)
st.write("You selected:", add_radio)

st.video('https://www.youtube.com/watch?v=TEKyEQL-S8o&list=RDTEKyEQL-S8o&start_radio=1')
