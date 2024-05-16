import scipy.io
import numpy as np
import pandas as pd

# Step 3: Load .mat File
mat_file_path = './Test/img_0334_ann.mat'
mat_contents = scipy.io.loadmat(mat_file_path)

# Step 4: Access Data

# for item in mat_contents:
#     print(item)
variable_name = 'annPoints'
data = mat_contents[variable_name]
# Step 5: Data Conversion (Optional)
print(data)
print(data[1][0])


from PIL import Image, ImageDraw

def place_dot(image_path, pixel_coords, dot_color=(255, 0, 0), dot_radius=3):
    # Open the image
    image = Image.open(image_path)

    # Create a drawing context
    draw = ImageDraw.Draw(image)

    # Extract coordinates
    x, y = pixel_coords

    # Define bounding box for the dot
    bounding_box = [(x - dot_radius, y - dot_radius), (x + dot_radius, y + dot_radius)]

    # Draw the dot
    draw.ellipse(bounding_box, fill=dot_color)

    # Save the modified image
    image.save("./modified_image.jpg")
    print("Dot placed on pixel coordinates:", pixel_coords)

# Example usage:
image_path = "./modified_image.jpg"  # Provide your image file path
for dot in data:
    print(dot)
    pixel_coords = (dot[0], dot[1])  # Coordinates of the pixel to place the dot on
    place_dot(image_path, pixel_coords)



# Step 6: Use Data in Computer Vision Project
# Your computer vision project code goes here..