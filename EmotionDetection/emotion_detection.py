import requests


def emotion_detector(text_to_analyze):

    url = "https://sn-watson-emotion.labs.coursera.org/emotion"

    myobj = {
        "raw_document": {
            "text": text_to_analyze
        }
    }

    response = requests.post(url, json=myobj)

    formatted_response = response.json()

    anger = formatted_response["emotionPredictions"][0]["emotion"]["anger"]
    disgust = formatted_response["emotionPredictions"][0]["emotion"]["disgust"]
    fear = formatted_response["emotionPredictions"][0]["emotion"]["fear"]
    joy = formatted_response["emotionPredictions"][0]["emotion"]["joy"]
    sadness = formatted_response["emotionPredictions"][0]["emotion"]["sadness"]

    emotions = {
        "anger": anger,
        "disgust": disgust,
        "fear": fear,
        "joy": joy,
        "sadness": sadness
    }

    dominant_emotion = max(emotions, key=emotions.get)

    return {
        "anger": anger,
        "disgust": disgust,
        "fear": fear,
        "joy": joy,
        "sadness": sadness,
        "dominant_emotion": dominant_emotion
    }