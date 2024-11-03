import streamlit as st
from utils.aria_helper import AriaHelper
import os

# Initialize Aria Helper
aria = AriaHelper()

# Set page config
st.set_page_config(
    page_title="Story Illustrator",
    page_icon="📚",
    layout="wide"
)

# Title and description
st.title("✨ Story Illustrator")
st.markdown("Transform your stories into visual experiences using AI")

# Story input
story_text = st.text_area("Enter your story:", height=200)

# Generate button
if st.button("Generate Illustrations", type="primary"):
    if story_text:
        with st.spinner("Analyzing your story..."):
            try:
                # Get scene suggestions
                analysis = aria.analyze_story(story_text)
                
                # Display results
                st.subheader("Story Analysis")
                st.write(analysis)
                
                # Here we'll add image generation in the next step
                st.info("Image generation feature coming in next update!")
                
            except Exception as e:
                st.error(f"An error occurred: {str(e)}")
    else:
        st.warning("Please enter a story first!")

# Add footer
st.markdown("---")
st.markdown("Built with ❤️ using Aria AI")
