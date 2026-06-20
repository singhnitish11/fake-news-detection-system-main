from flask import Flask, render_template, request
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline

app = Flask(__name__)

# Your model code (the same as you have)
# Load datasets and train your model
true_df = pd.read_csv('True.csv')
true_df['label'] = 0
fake_df = pd.read_csv('Fake.csv')
fake_df['label'] = 1
df = pd.concat([true_df, fake_df], ignore_index=True)
X_train, X_test, y_train, y_test = train_test_split(df['text'], df['label'], test_size=0.2, random_state=42)
model = make_pipeline(TfidfVectorizer(), MultinomialNB())
model.fit(X_train, y_train)

# Default route to serve the index.html
@app.route('/')
def index():
    return render_template('index.html')  # This will load 'index.html' from the 'templates' folder

# Add the predict route here if you need to make predictions
@app.route('/predict', methods=['POST'])
def predict():
    user_input = request.form['news_article']  # Get the news article from the form input
    prediction = model.predict([user_input])

    if prediction[0] == 0:
        result = "The news is likely to be true."
    else:
        result = "The news is likely to be fake."

    return render_template('index.html', prediction_result=result)

if __name__ == '__main__':
    app.run(debug=True)

