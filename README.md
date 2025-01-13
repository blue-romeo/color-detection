# color-detection# Color Detection 
## Overview
This project is a real-time color detection application built using Python, OpenCV, and Pillow. It specifically detects the color **yellow** from live webcam feed. The webcam feed is captured using the **IP Webcam** app, which allows a smartphone to act as a network-based camera.

## Features
- Real-time yellow color detection.
- Uses OpenCV for image processing.
- Leverages Pillow for additional image manipulation.
- Works with webcam feeds streamed over a network.

## Requirements
### Software
- Python 3.8 or higher
- IP Webcam app (available on Android)

### Python Libraries
The following libraries are required for the project:
- OpenCV
- Pillow
- NumPy

To install the necessary libraries, run:
```bash
pip install opencv-python, pillow, numpy
```

## Setup Instructions

1. **Install IP Webcam on your smartphone:**
   - Download and install the [IP Webcam app](https://play.google.com/store/apps/details?id=com.pas.webcam) from the Google Play Store.
   - Open the app and start the server. Note the IP address and port displayed on the screen (e.g., `http://192.168.0.101:8080`).

2. **Clone this repository:**
   ```bash
   git clone https://github.com/blue-romeo/color-detection
   cd color-detection
   ```

3. **Update the script:**
   - Edit the script to include the correct IP Webcam URL (replace `YOUR_IP_ADDRESS` with your phone's IP and port):
     ```python
     url = 'http://YOUR_IP_ADDRESS/video'
     ```

4. **Run the script:**
   ```bash
   main.py
   ```

5. **View the detection:**
   - The script will display a live video feed with yellow areas highlighted.

## Code Explanation

1. **Video Stream:**
   The video stream is captured from the IP Webcam URL using OpenCV’s `VideoCapture`.

2. **Color Detection:**
   - Convert the frames to HSV (Hue, Saturation, Value) color space.
   - Define the range for detecting yellow color.
   - Create a mask to isolate yellow areas in the frame.

3. **Display:**
   - Highlight the detected yellow areas on the original video feed.
   - Display the output in real time using OpenCV's `imshow`.

## Output
When yellow objects are detected in the webcam feed, they are highlighted in the video frame with a green bounding box.


## Future Improvements
- Add support for detecting multiple colors.
- Include a graphical user interface (GUI).
- Optimize for different lighting conditions.

## Contributing
Contributions are welcome! Feel free to open issues or submit pull requests to improve the project.

## License
This project is licensed under the Apache 2.0 License. See the `LICENSE` file for more details.

## Acknowledgments
- [OpenCV Documentation](https://docs.opencv.org/)
- [Pillow Documentation](https://pillow.readthedocs.io/)
- [IP Webcam App](https://play.google.com/store/apps/details?id=com.pas.webcam)

