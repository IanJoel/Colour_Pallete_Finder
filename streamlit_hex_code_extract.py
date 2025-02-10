import streamlit as st
import os
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image

from extracting_hex_codes import extract_colours


# Define the directory for file uploads
UPLOAD_DIR = "uploaded_files"
os.makedirs(UPLOAD_DIR, exist_ok=True)

def file_uploader_page():
    st.title("File Uploader")
    uploaded_file = st.file_uploader("Upload a file", type=["png", "jpg", "jpeg"])
    
    if uploaded_file is not None:
        file_path = os.path.join(UPLOAD_DIR, uploaded_file.name)
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        st.success(f"File '{uploaded_file.name}' has been uploaded successfully!")

def plot_viewer_page():
    st.title("Colour Palette Finder")
    files = os.listdir(UPLOAD_DIR)
    
    if not files:
        st.warning("No files found in the directory. Please upload a file first.")
        return
    
    selected_file = st.selectbox("Select a file to use", files)
    number_colors = st.slider("Number of colors to extract", 1, 10, 6)
    
    if selected_file:
        file_path = os.path.join(UPLOAD_DIR, selected_file)
        
        # Load the data (assuming CSV for now, modify for other formats)
        try:
            image = Image.open(file_path).convert("RGB")
            st.image(image, caption="Preview Of The Uploaded Image", use_container_width=True)
            
        except Exception as e:
            st.error(f"Error loading file: {e}")
            
        # Extract the dominant colors
        hex_colors, dominant_colors = extract_colours(file_path,n_clusters=number_colors)
        
        # Show the extracted colors
        plt.figure(figsize=(8, 2))
        for i, color in enumerate(hex_colors):
            plt.subplot(1, number_colors, i+1)
            plt.axis("off")
            plt.imshow([[dominant_colors[i] / 255]])
            plt.text(0.5, -0.2, hex_colors[i], ha='center', va='center', transform=plt.gca().transAxes)
        
        st.write("Colour Palette")
        st.pyplot(plt)
        
            
        

# Sidebar navigation
st.sidebar.title("Colour Finder")
page = st.sidebar.radio("Go to", ["Upload File", "View Plot"])

if page == "Upload File":
    file_uploader_page()
elif page == "View Plot":
    plot_viewer_page()
