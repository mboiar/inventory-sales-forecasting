from flask import Flask, request, render_template
import pandas as pd
import joblib

app = Flask(__name__)

model = None

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict', methods=['POST'])
def predict():
    year_week = request.form['year_week']
    product_number = request.form['product_number']
    
    data = pd.DataFrame({'year_week': [year_week], 'product_number': [int(product_number)]})

    train_df = pd.read_csv('dataset/train.csv')
    product_mapping = train_df[['product_number', 'prod_category', 'segment', 'specs', 'display_size']].drop_duplicates()
    data_complete = data.merge(product_mapping, on='product_number', how = 'left')
    # prediction = model.predict(data_complete)
    
    return render_template('result.html', prediction=None)

if __name__ == '__main__':
    app.run(debug=True)