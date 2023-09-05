from flask import Flask, request, render_template

import pickle

# load the model
with open('model2.pkl','rb') as file:
    model_rf = pickle.load(file)

# create the server
app = Flask(__name__)

@app.route('/',methods=['GET'])
def root():
    return render_template('index1.html')

@app.route("/predict", methods=["POST"])
def predict():
    # get input from user

    Delivery_person_Age = float(request.form.get("Delivery_person_Age"))
    Delivery_person_Ratings = float(request.form.get("Delivery_person_Ratings"))
    distance_km = float(request.form.get("distance_km"))
    avg_speed_kmph = float(request.form.get("avg_speed_kmph"))
    Road_traffic_density_High = float(request.form.get("Road_traffic_density_High"))
    Road_traffic_density_Jam = float(request.form.get("Road_traffic_density_Jam"))
    Road_traffic_density_Low = float(request.form.get("Road_traffic_density_Low"))
    Road_traffic_density_Medium = float(request.form.get("Road_traffic_density_Medium"))
    Type_of_order_Buffet = float(request.form.get("Type_of_order_Buffet"))
    Type_of_order_Drinks = float(request.form.get("Type_of_order_Drinks"))
    Type_of_order_Meal = float(request.form.get("Type_of_order_Meal"))
    Type_of_order_Snack = float(request.form.get("Type_of_order_Snack"))
    Festival_Yes = float(request.form.get("Festival_Yes"))
 

    algo = request.form.get("algo")
    x = [Delivery_person_Age, Delivery_person_Ratings, distance_km, avg_speed_kmph, Road_traffic_density_High, Road_traffic_density_Jam, Road_traffic_density_Low, Road_traffic_density_Medium,
         Type_of_order_Buffet, Type_of_order_Drinks, Type_of_order_Meal, Type_of_order_Snack, Festival_Yes]
    if algo == 'model2.pkl':
        prediction = model_rf.predict([x])


    return render_template(
        "result1.html",
        prediction=prediction,
        Delivery_person_Age =Delivery_person_Age,Delivery_person_Ratings=Delivery_person_Ratings,distance_km=distance_km,avg_speed_kmph=avg_speed_kmph,Road_traffic_density_High=Road_traffic_density_High,Road_traffic_density_Jam=Road_traffic_density_Jam,Road_traffic_density_Low=Road_traffic_density_Low,Road_traffic_density_Medium=Road_traffic_density_Medium,Type_of_order_Buffet=Type_of_order_Buffet,Type_of_order_Drinks=Type_of_order_Drinks,
         Type_of_order_Meal=Type_of_order_Meal, Type_of_order_Snack=Type_of_order_Snack, Festival_Yes = Festival_Yes, algo=algo)


# start the server
app.run(port=4006,debug=True,host='0.0.0.0')
