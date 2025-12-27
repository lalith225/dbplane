import cv2
from fer import FER

# Dictionary mapping emotions to song recommendations
emotion_songs = {
    'happy': ['Happy by Pharrell Williams', 'Good Vibrations by The Beach Boys'],
    'sad': ['Someone Like You by Adele', 'Fix You by Coldplay'],
    'angry': ['Killing in the Name by Rage Against the Machine', 'Break Stuff by Limp Bizkit'],
    'surprise': ['Surprise by The Style Council', 'Uptown Funk by Mark Ronson'],
    'neutral': ['Chill by Alan Walker', 'Weightless by Marconi Union'],
    'fear': ['Happy by Pharrell Williams', 'Good Vibrations by The Beach Boys'],
}


# Main function to run emotion detection and song suggestion
def main():
    cap = cv2.VideoCapture(0)  # Use 0 for the primary camera
    detector = FER()
    EMOTION_DETECTED = 0

    while EMOTION_DETECTED == 0:
        ret, frame = cap.read()
        if not ret:
            break

        # Detect emotions
        emotions = detector.detect_emotions(frame)


        if emotions:
            # Get the dominant emotion
            dominant_emotion = emotions[0]['emotions']
            emotion = max(dominant_emotion, key=dominant_emotion.get)

            print(f'Detected Emotion: {emotion}')

            # Suggest songs based on detected emotion
            suggested_songs = emotion_songs.get(emotion, [])
            if suggested_songs:
                print("Suggested Songs:")
                for song in suggested_songs:
                    print(f"- {song}")
                    EMOTION_DETECTED = 1
        # Display the frame
        cv2.imshow('Emotion Detection', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
