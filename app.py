import streamlit as st
from PIL import Image, ImageDraw
from ultralytics import YOLO

# Load the YOLO model
model = YOLO('best.pt')

# Define a function to perform object detection on the uploaded image
def detect_objects(image):
    # Perform object detection
    results = model(image)
    
    # Assume the first result is the one we want
    return results[0]

# Define the Streamlit app
def main():
    st.title("Shelf Object Detection")

    # Allow the user to upload an image
    uploaded_image = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

    if uploaded_image is not None:
        # Display the uploaded image
        image = Image.open(uploaded_image)
        st.image(image, caption='Uploaded Image', use_column_width=True)

        # Perform object detection
        results = detect_objects(image)
        num_objects = len(results)
        st.write(f"Number of objects detected: {num_objects}")

        # Draw bounding boxes on the image for detected objects
        annotated_image = image.copy()
        draw = ImageDraw.Draw(annotated_image)
        for box in results.boxes:
            x1, y1, x2, y2 = box.xyxy[0]
            draw.rectangle([x1, y1, x2, y2], outline="red", width=3)

        # Display the annotated image with detected objects
        st.image(annotated_image, caption='Detected Objects', use_column_width=True)

if __name__ == "__main__":
    main()
