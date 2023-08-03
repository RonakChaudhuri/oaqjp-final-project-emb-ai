''' Executing this function initiates the application of sentiment
    analysis to be executed over the Flask channel and deployed on
    localhost:5000.
'''
# Import Flask, render_template, request from the flask pramework package :
# Import the emotion_detector function from the package created:
# Initiate the flask app :
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emt_detector():
    ''' This code receives text from the HTML interface and 
        runs emotion detection over it using emotion_dection()
        function. The output returned shows the different emotion
        scores for the text provided
    '''
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    anger_score = response['anger']
    disgust_score = response['disgust']
    fear_score = response['fear']
    joy_score = response['joy']
    sadness_score = response['sadness']
    dominant_emotion = response['dominant_emotion']
    if anger_score is None:
        return "Invalid text! Please Try again."
    return "For the given statement, the system response is 'anger': {:.9f}, 'disgust': {:.9f}, 'fear': {:.9f}, 'joy': {:.9f}, and 'sadness': {:.9f}. The dominant emotion is {}.".format(anger_score, disgust_score, fear_score, joy_score, sadness_score, dominant_emotion)

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
