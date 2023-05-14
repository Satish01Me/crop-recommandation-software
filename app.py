from flask import Flask, render_template, redirect, jsonify, request, url_for
import pickle
import sklearn
import datetime as dt
date_details = dt.datetime.now()
day = date_details.weekday()
import csv

app = Flask(__name__)
model = pickle.load(open('static/model.pkl', 'rb'))

# labels
crop_list={1:'apple',2:'banana',3:'blackgram',4:'chickpea',5:'coconut',6:'coffee',7:'cotton',8:'grapes',9:'jute',10:'kidneybeans',
11:'lentil',12:'maize',13:'mango',14:'mothbeans',15:'mungbean',16:'muskmelon',17:'orange',18:'papaya',19:'pigeonpeas',
20:'pomegranate',21:'rice',22:'watermelon',}
days = ["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY",
        "FRIDAY", "SATURDAY", "SUNDAY"]


@app.route("/")
def home():
    global day, days
    return render_template("index.html",time=days[day])


@app.route("/Recommand_crop.html",methods=['POST','GET'])
def Recommand_crop():
    global model,crop_list
    b=1
    crop=""
    nitrogen=""
    phosphorus=""
    potassium=""
    temperature=""
    humidity=""
    ph=""
    rainfall=""
    predict=[]
    if request.method=='POST':
        nitrogen = float(request.form['nitrogen'])
        phosphorus = float(request.form['phosphorus'])
        potassium = float(request.form['potassium'])
        temperature = float(request.form['temperature'])
        humidity = float(request.form['humidity'])
        ph = float(request.form['ph'])
        rainfall = float(request.form['rainfall'])
        predict = model.predict([[nitrogen,phosphorus,potassium,temperature,humidity,ph,rainfall]])
        predict=crop_list[predict[0]]
    else:
        pass
    # # for _ in predict:
    return render_template("Recommand_crop.html",nitrovalue=predict,nitrogen=nitrogen,
                           phosphorus=phosphorus,potassium=potassium,temperature=temperature,humidity=humidity,
                           ph=ph,rainfall=rainfall)


@app.route("/contact_us.html",methods=['POST','GET'])
def contact_us():
    name=''
    email=''
    message=''
    if request.method=='POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        with open('static/contact.csv', 'a',newline="") as file:
            writer = csv.writer(file)
            writer.writerow([name,email,message])
    else:
        pass      
    return render_template('contact_us.html')  



if __name__ == "__main__":
    app.run(host='127.0.0.1',port=5000,debug=True)
