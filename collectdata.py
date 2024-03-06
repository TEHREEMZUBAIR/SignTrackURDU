import os
import cv2

cap = cv2.VideoCapture(0)
directory = 'Image/'

# Create directories for Urdu signs
urdu_signs = ['Alif','Bey','Che','Daal','Dhaal','Fe','Gaaf','Ghain','Haa','Hamza','He','J','Khe','Laam','Meem','Noon','Qaaf','Re','Rey','Saad','Se','Seen','Sheen','Te','Waw','Ye','Ze','Zhaad','Zhe','Zoye']
for sign in urdu_signs:
    os.makedirs(os.path.join(directory, sign), exist_ok=True)

while True:
    _, frame = cap.read()

    count = {sign.lower(): len(os.listdir(os.path.join(directory, sign))) for sign in urdu_signs}

    row, col, _ = frame.shape
    cv2.rectangle(frame, (0, 40), (300, 400), (255, 255, 255), 2)
    cv2.imshow("data", frame)
    cv2.imshow("ROI", frame[40:400, 0:300])
    roi = frame[40:400, 0:300]

    interrupt = cv2.waitKey(10)

    # Capture images for Urdu signs
    for sign in urdu_signs:
        if isinstance(sign, str) and len(sign) >= 1 and interrupt & 0xFF == ord(sign[0].lower()):
            cv2.imwrite(os.path.join(directory, sign.lower(), f"{count[sign.lower()]}.png"), roi)

    if interrupt & 0xFF == 27:  # Esc key to exit
        break

cap.release()
cv2.destroyAllWindows()