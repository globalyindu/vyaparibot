import streamlit as st
from utils.generator import generate_social_posts
import json

st.title("VyapariBot 🧠 – AI for Social Media Marketing")

st.subheader("Enter your business info:")

business_info = {
    'type': st.text_input("Business Type (e.g., Boutique, Cafe)"),
    'city': st.text_input("City"),
    'products': st.text_area("What do you sell?"),
    'tone': st.selectbox("Tone", ['Trendy', 'Professional', 'Desi Fun']),
    'language': st.selectbox("Language", ['English', 'Hindi']),
    'audience': st.text_input("Your target audience (e.g., college students, working women)"),
    'offers': st.text_input("Current offers (optional)")
}

if st.button("Generate 15-Day Plan"):
    with st.spinner("Generating..."):
        output = generate_social_posts(business_info)
        st.success("Here is your content plan:")
        st.json(json.loads(output))