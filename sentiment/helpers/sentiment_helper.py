import os
import pickle
import joblib

# load vectorizer and classifier
vectorizer_path = os.path.join(os.path.dirname(__file__), '../../utils/vectorizers/TFIDFvec.pickle')
classifier_path = os.path.join(os.path.dirname(__file__), '../../utils/models/MultinomialNBModel.joblib')

vectorizer = pickle.load(open(vectorizer_path,"rb"))
classifier = joblib.load(classifier_path)

def predict(text):
    test = []
    test.append(text)

    vect = vectorizer.transform(test)
    predicted = classifier.predict(vect)
    sentiment = ' '.join(predicted)
    
    return sentiment

def orderLabel(label):
    if label == '2-negative':
        return "negative"
    elif label == '1-neutral':
        return "neutral"
    elif label == '3-positive':
        return "positive"