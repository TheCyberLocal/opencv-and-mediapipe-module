import cv2
import mediapipe as mp

mp_drawing = mp.solutions.drawing_utils
mp_holistic = mp.solutions.holistic

cap = cv2.VideoCapture(1)
with mp_holistic.Holistic(min_detection_confidence=0.6, min_tracking_confidence=0.6) as holistic:
    while cap.isOpened():
        ret, frame0 = cap.read()
        frame1 = frame0.copy()
        image = cv2.cvtColor(frame0, cv2.COLOR_BGR2RGB)

        results = holistic.process(image)
        # print(results.face_landmarks)
        # print(results.pose_landmarks)

        mp_drawing.draw_landmarks(frame1, results.face_landmarks, mp_holistic.FACEMESH_CONTOURS,
                                  mp_drawing.DrawingSpec(color=(255, 0, 0), thickness=1, circle_radius=1),  # landmarks
                                  mp_drawing.DrawingSpec(color=(255, 255, 255), thickness=2, circle_radius=2)   # lines
                                  )
        # mp_drawing.draw_landmarks(frame1, results.face_landmarks, mp_holistic.FACEMESH_TESSELATION)
        # mp_drawing.draw_landmarks(frame1, results.pose_landmarks, mp_holistic.POSE_CONNECTIONS)
        mp_drawing.draw_landmarks(frame1, results.right_hand_landmarks, mp_holistic.HAND_CONNECTIONS,
                                  mp_drawing.DrawingSpec(color=(255, 0, 0), thickness=-1, circle_radius=5),  # landmarks
                                  mp_drawing.DrawingSpec(color=(255, 255, 255), thickness=2, circle_radius=2)   # lines
                                  )
        mp_drawing.draw_landmarks(frame1, results.left_hand_landmarks, mp_holistic.HAND_CONNECTIONS,
                                  mp_drawing.DrawingSpec(color=(255, 0, 0), thickness=-1, circle_radius=5),  # landmarks
                                  mp_drawing.DrawingSpec(color=(255, 255, 255), thickness=2, circle_radius=2)   # lines
                                  )

        cv2.imshow('frame1', frame1)
        # cv2.imshow('frame', frame0)

        if cv2.waitKey(1) == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
