from flask import Flask,request, render_template
import pickle
app=Flask(__name__)

@app.route('/')
def index():
    return render_template('HAM.html')

@app.route('/test')
def test():
    return render_template('index.html')

@app.route('/get_data', methods = ['POST'])
def model_prediction():
    data = request.form 
    print(data)

    model = pickle.load(open(r'model1.pkl','rb'))
    print(model)

    user_data = [[float(data['age']),
                  float(data['sex']),
                  float(data['cp']),
                  float(data['trtbps']),
                  float(data['chol']),
                  float(data['fbs']),
                  float(data['restecg']),
                  float(data['thalachh'])
                  ]]
    
    print(user_data)


    result = model.predict(user_data)

    print(result)

    target = ['Less Chance of Heart Attack','More Chance of Heart Attack']

    print(f"prediction = {target[result[0]]}")

    prediction_result_backend=target[result[0]]


    return render_template('HAM.html', prediction_result=prediction_result_backend)


if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=False,port=8080)
