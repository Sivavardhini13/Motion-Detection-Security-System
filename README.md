Motion Detection Security System
Overview

A Python-based motion detection system that uses OpenCV to monitor live webcam footage. The application detects movement in real time, highlights moving objects with bounding boxes, and displays the motion status on the video feed.

Features
Real-time webcam monitoring
Motion detection using frame differencing
Bounding boxes around detected movement
Live status display ("Movement Detected" / "No Movement")
Multiple display windows for debugging (Security Feed, Threshold, Frame Delta)
Press Q to exit the application
Technologies Used
Python 3
OpenCV (cv2)
How It Works
Captures live video from the webcam.
Converts frames to grayscale and applies Gaussian blur.
Compares the current frame with the background.
Detects differences indicating motion.
Draws rectangles around moving objects.
Displays the motion status in real time.
Future Improvements
Record video when motion is detected.
Save snapshots automatically.
Send email or mobile notifications.
Detect only humans using AI (YOLO or MobileNet SSD).
Add date and time stamps to recordings.
