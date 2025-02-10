# Color Palette Finder

This is a Streamlit web app that extracts a color palette from an uploaded image using machine learning. It is useful for designers who want to find a harmonious color scheme based on an image.

## Features
- Upload an image
- Extract a dominant color palette using ML
- Display the color palette for design inspiration

## Installation

To run this app locally, follow these steps:

1. Clone the repository:
   ```sh
   https://github.com/IanJoel/Colour_Pallete_Finder.git
   cd Colour_Pallete_Finder
   ```

2. Create a virtual environment (optional but recommended):
   ```sh
   python -m venv .venv
   source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
   ```
   **Note:** This app was created using python version 3.10.16

3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Running the App

To start the Streamlit app, run:
```sh
streamlit run app.py
```

This will open the app in your default web browser. 

**Note:** The first time you run this app it may take a few extra seconds before it opens, this is due to the fact that the app needs to create a local directory where your uploaded images are stored.


## How It Works
1. Upload an image via the Streamlit UI.
2. The app processes the image and extracts a color palette using machine learning techniques (e.g., k-means clustering).
3. The extracted colors are displayed in a visually appealing format.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
This project is licensed under the MIT License.

