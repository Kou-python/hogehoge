import mediapipe as mp
import cv2

print("OpenCV version:")

# ハンドトラッキングモジュールの初期化
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

# カメラキャプチャの初期化
cap = cv2.VideoCapture(0)

with mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=1,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5,
) as hands:
    while cap.isOpened():
        ret, frame = cap.read()

        # フレームが正常に読み込まれなかった場合、現在のループをスキップ
        if not ret:
            continue

        # フレームをRGBに変換
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # ハンドトラッキングを実行
        results = hands.process(image)

        # 手のマークを処理
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                # 座標の出力と描画
                for landmark in hand_landmarks.landmark:
                    x = landmark.x
                    y = landmark.y
                    z = landmark.z
                    print(f"X: {x}, Y: {y}, Z: {z}")

                mp_drawing.draw_landmarks(
                    image, hand_landmarks, mp_hands.HAND_CONNECTIONS
                )

        # RGBからBGRに変換して表示
        cv2.imshow("MediaPipe Hands", cv2.cvtColor(image, cv2.COLOR_RGB2BGR))

        if cv2.waitKey(10) & 0xFF == ord("q"):
            break

cap.release()
cv2.destroyAllWindows()
