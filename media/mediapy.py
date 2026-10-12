import cv2
import mediapipe as mp
import subprocess

mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils

hands = mp_hands.Hands(
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)

cap = cv2.VideoCapture(0)

numbers = [3, 2, 1]
index = 0
mic_on = False

while True:
    ret, frame = cap.read()

    if not ret:
        break

    frame = cv2.flip(frame, 1)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb)

    if result.multi_hand_landmarks:
        hand = result.multi_hand_landmarks[0]
        lm = hand.landmark

        fingers = 0

        if lm[8].y < lm[6].y:
            fingers += 1

        if lm[12].y < lm[10].y:
            fingers += 1

        if lm[16].y < lm[14].y:
            fingers += 1

        if lm[20].y < lm[18].y:
            fingers += 1

        if fingers == numbers[index]:
            index += 1

            if index == len(numbers):
                subprocess.run(
                    ["pactl", "set-source-mute", "@DEFAULT_SOURCE@", "0"]
                )
                mic_on = True
                index = 0

        mp_draw.draw_landmarks(
            frame,
            hand,
            mp_hands.HAND_CONNECTIONS
        )

        cv2.putText(
            frame,
            f"Fingers: {fingers}",
            (20, 50),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 0),
            2
        )

    cv2.putText(
        frame,
        f"Step: {index + 1}/3",
        (20, 90),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (255, 255, 255),
        2
    )

    if mic_on:
        cv2.putText(
            frame,
            "Microphone ON",
            (20, 130),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 0),
            2
        )

    cv2.imshow("Camera", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()