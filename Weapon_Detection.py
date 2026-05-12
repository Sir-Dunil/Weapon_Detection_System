import cv2
from ultralytics import YOLO

# =====================================
# LOAD MODEL
# =====================================
Weapon_Detection = YOLO('YOLO_Weights/Weapon_Detection.pt')

# =====================================
# THREAT LEVEL COLORS
# Different colors per class
# =====================================
CLASS_COLORS = {
    'gun':              (0, 0, 255),    # Red
    'knife':            (0, 165, 255),  # Orange
    'person_with_mask': (0, 255, 255),  # Yellow
}

# =====================================
# THREAT LEVEL LABELS
# =====================================
THREAT_LEVEL = {
    'gun':              'HIGH THREAT',
    'knife':            'THREAT DETECTED',
    'person_with_mask': 'SUSPICIOUS',
}


# =====================================
# DRAW DETECTIONS
# Returns highest threat type found
# =====================================
def draw_detections(frame, results):

    # Track highest threat found
    # weapon > suspicious > none
    highest_threat = None

    for result in results:
        for box in result.boxes:

            # Get confidence and class
            conf  = float(box.conf[0])
            cls   = int(box.cls[0])
            label = Weapon_Detection.names[cls]

            # Get box coordinates
            x1, y1, x2, y2 = map(int,
                box.xyxy[0].tolist())

            # Get color and threat label
            color  = CLASS_COLORS.get(
                label, (255, 255, 255))
            threat = THREAT_LEVEL.get(
                label, 'DETECTED')

            # Draw bounding box
            cv2.rectangle(frame,
                (x1, y1), (x2, y2),
                color, 2)

            # Draw label background
            cv2.rectangle(frame,
                (x1, y1-30), (x2, y1),
                color, -1)

            # Draw label text
            cv2.putText(frame,
                f"{label} {conf:.0%}",
                (x1+5, y1-8),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6, (0, 0, 0), 2)

            # Draw threat level
            cv2.putText(frame,
                threat,
                (x1, y2+25),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7, color, 2)

            # Assign threat type
            # Weapon always overrides suspicious
            if label in ['gun', 'knife']:
                highest_threat = "weapon"
            elif label == 'person_with_mask' \
                and highest_threat != "weapon":
                highest_threat = "suspicious"

    return frame, highest_threat


# =====================================
# DRAW ALERT BANNER
# Different banners per threat level
# =====================================
def draw_alert_banner(frame, threat_type):
    h, w, _ = frame.shape

    if threat_type == "weapon":
        # Red banner for weapons
        cv2.rectangle(frame,
            (0, 0), (w, 50),
            (0, 0, 255), -1)
        cv2.putText(frame,
            "⚠ WEAPON DETECTED ⚠",
            (w//2 - 180, 35),
            cv2.FONT_HERSHEY_SIMPLEX,
            1, (255, 255, 255), 2)

    elif threat_type == "suspicious":
        # Yellow banner for mask
        cv2.rectangle(frame,
            (0, 0), (w, 50),
            (0, 215, 255), -1)
        cv2.putText(frame,
            "⚠ SUSPICIOUS PERSON ⚠",
            (w//2 - 190, 35),
            cv2.FONT_HERSHEY_SIMPLEX,
            1, (0, 0, 0), 2)

    return frame


# =====================================
# MAIN PROGRAM
# =====================================
Web_Cam = cv2.VideoCapture('Test_Files/Crime_Footage_3 .mov')

# Track consecutive detections
# to reduce flickering
detection_counter  = 0
DETECTION_THRESHOLD = 3

while True:
    success, frame = Web_Cam.read()
    if not success:
        break

    frame = cv2.flip(frame, 1)

    # Run detection with tracking
    weapon_result = Weapon_Detection.predict(
        source=frame,
        conf=0.7,
        verbose=False,
        tracker="bytetrack.yaml"
    )

    # Draw detections and get threat type
    frame, threat_type = draw_detections(
        frame, weapon_result)

    # Count consecutive detections
    # to reduce flickering
    if threat_type:
        detection_counter += 1
    else:
        detection_counter = 0

    # Only show banner after consistent
    # detections across multiple frames
    if detection_counter >= DETECTION_THRESHOLD:
        frame = draw_alert_banner(
            frame, threat_type)

    # Status text and color
    # based on current threat type
    if threat_type == "weapon":
        status_text  = "THREAT DETECTED"
        status_color = (0, 0, 255)      # Red
    elif threat_type == "suspicious":
        status_text  = "SUSPICIOUS"
        status_color = (0, 215, 255)    # Yellow
    else:
        status_text  = "ALL CLEAR"
        status_color = (0, 255, 0)      # Green

    # Draw status text
    cv2.putText(frame,
        f"Status: {status_text}",
        (10, 30),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7, status_color, 2)

    cv2.imshow("Weapon Detection System", frame)

    if cv2.waitKey(1) == ord('q'):
        break

Web_Cam.release()
cv2.destroyAllWindows()