import cv2

# Open webcam
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

background = None

while True:
    ret, frame = cap.read()

    if not ret:
        print("Failed to grab frame.")
        break

    # Resize for faster processing (optional)
    frame = cv2.resize(frame, (640, 480))

    # Convert to grayscale and blur
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (21, 21), 0)

    # Initialize background
    if background is None:
        background = gray.astype("float")
        continue

    # Update background slowly
    cv2.accumulateWeighted(gray, background, 0.05)

    # Compute difference
    frame_delta = cv2.absdiff(gray, cv2.convertScaleAbs(background))

    # Threshold
    thresh = cv2.threshold(frame_delta, 25, 255, cv2.THRESH_BINARY)[1]
    thresh = cv2.dilate(thresh, None, iterations=2)

    # Find contours
    contours, _ = cv2.findContours(
        thresh,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE
    )

    status = "No Movement"

    for contour in contours:
        if cv2.contourArea(contour) < 500:
            continue

        (x, y, w, h) = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        status = "Movement Detected"

    cv2.putText(
        frame,
        f"Status: {status}",
        (10, 30),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (0, 0, 255),
        2,
    )

    cv2.imshow("Security Feed", frame)
    cv2.imshow("Threshold", thresh)
    cv2.imshow("Frame Delta", frame_delta)

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
