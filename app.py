import streamlit as st
from utils import build_story

st.set_page_config(page_title="Story Lens", layout="wide")

st.title("🎬 Story Lens")
st.markdown("Turn your movie idea into a visual storyboard powered by local AI.")

prompt = st.text_input("Enter your movie idea:", "A sci-fi adventure through time")
num_scenes = st.slider("Number of scenes", min_value=1, max_value=10, value=5)

if st.button("Generate Storyboard"):
    with st.spinner("Generating scenes..."):
        story = build_story(prompt, num_scenes)
        for scene in story:
            st.subheader(scene.title)
            st.image(scene.image, use_column_width=True)
            st.write(scene.description)
