from flask import Flask, jsonify, request
import numpy as np
from loguru import logger
from time import sleep

app = Flask(__name__)

train_status = "not training"

def _train():
    global train_status
    logger.info("train started")
    train_status = 'training'

    sleep(10)

    logger.info("train finished")
    train_status = 'not training' 
    
@app.route("/")
def hello_world():
    return jsonify({"Hello": "World"})

@app.route("/status")
def status():
    return jsonify({"status": train_status})

@app.route("/predict_v1/<age>/<salary>")
def predict_v1(age, salary):
    # this is an example of a GET request with url unnamed params

    try:
       age = int(age)
       salary = float(salary)
    except Exception as e:
       return jsonify({'error': str(e)})
 
    prediction = np.random.randint(2)*age + salary
    logger.info(f"prediction for age {age} and salary {salary} is {prediction}")
    return jsonify({"prediction": prediction})

@app.route("/predict_v2")
def predict_v2():

    age = request.args.get('age')
    salary = request.args.get('salary')

    prediction = np.random.randint(2)*age + salary
    logger.info(f"prediction for age {age} and salary {salary} is {prediction}")

    return jsonify({"prediction": prediction})

@app.route("/predict_v3", methods=['POST'])
def predict_v3():

    age = request.json.get('age')
    salary = request.json.get('salary')

    print ("yyyy", age, salary)

    prediction = np.random.randint(2)*age + salary
    logger.info(f"prediction for age {age} and salary {salary} is {prediction}")

    return jsonify({"prediction": prediction})

@app.route("/train")
def train():
    if train_status == 'training':
       return  jsonify({"error": "already training"})

    _train()
    return jsonify({'result': 'training finished successfully'})
 
if __name__ == "__main__":
    app.run(debug=True)
