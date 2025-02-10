from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans


def extract_colours(image_path, n_clusters=6):
    """
    Extracts dominant colors from an image using KMeans clustering
    :param image_path: Path to the image
    :param n_clusters: Number of clusters for KMeans
    :return: List of HEX codes for the dominant colors
    """
    # Reload the image
    image = Image.open(image_path).convert("RGB")

    # Resize for faster processing
    image = image.resize((150, 150))
    image_np = np.array(image).reshape(-1, 3)

    # Use KMeans clustering to find dominant colors
    kmeans = KMeans(n_clusters=n_clusters, random_state=42, n_init=10)
    kmeans.fit(image_np)
    dominant_colors = kmeans.cluster_centers_.astype(int)

    # Convert to HEX
    hex_colors = ['#{:02x}{:02x}{:02x}'.format(*color) for color in dominant_colors]

    return hex_colors,dominant_colors


    


