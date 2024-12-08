import time
from picamera2 import Picamera2

# Create a Picamera2 object
picam2 = Picamera2()

# Generate a preview configuration and configure the camera
preview_config = picam2.create_preview_configuration()
picam2.configure(preview_config)

# Start the camera
picam2.start()

# Wait for 2 seconds
time.sleep(2)

# Capture an image and save it with a timestamp in the filename
file_name = f"first_python_image.jpeg"
picam2.capture_file(file_name)

# Stop the camera and preview
picam2.stop()

print("Image captured and saved to:", file_name)
