from django.shortcuts import render,redirect
from django.views.generic import TemplateView
import pickle
import pandas as pd
# Create your views here.

bikeModel = pickle.load(open("price/bike.pkl", "rb"))
carModel= pickle.load(open("price/car.pkl", "rb"))

class Home(TemplateView):
    template_name = "price/index.html"
    items = ["Bike", "Car", "House"]
    def post(self,request):
        selectedItem=request.POST["item"]
        if selectedItem=="Please select type...":
            return render(request, "price/index.html",{"error":"Please select type","items": self.items})
        elif selectedItem==self.items[0]:
            return redirect("bike/")
        elif selectedItem == self.items[1]:
            return redirect("car/")
        else:
            return redirect("house/")
    def get(self,request):
        return render(request, "price/index.html", {"items": self.items})



class Bike(TemplateView):
    template_name = "price/bike.html"
    owner=["First Owner","Second Owner","Third Owner","Fourth Owner Or More"]
    brand=['Bajaj', 'Hero', 'Royal Enfield', 'Yamaha', 'Honda', 'Suzuki', 'TVS',
       'KTM', 'Harley-Davidson', 'Kawasaki', 'Hyosung', 'Benelli', 'Mahindra',
       'Triumph', 'Ducati', 'BMW', 'Jawa', 'MV', 'Indian', 'Ideal', 'Rajdoot',
       'LML', 'Yezdi']
    age=[1,2,3,4,5,6,7,8,9,10,11,12]

    def get(self, request, *args, **kwargs):
        return render(request,"price/bike.html",
                      {
                       "owner":self.owner,
                       "brand":self.brand,
                       "age":self.age
                       })

    def post(self,request):
        print(request.POST)
        if request.POST["owner"]=="Select Owner" or   request.POST["brand"]=="Select Brand Name" or request.POST["age"]=="Select Age" or not request.POST["kms_driven"] or not request.POST["power"]:
            return render(request, "price/bike.html",
                          {"error": "Please fill all fields",
                           "owner": self.owner,
                           "brand": self.brand,
                           "age": self.age})
        else:
            data=pd.DataFrame([{"kms_driven": int(request.POST["kms_driven"]),"owner": request.POST["owner"],"age":int(request.POST["age"]),  "power":int(request.POST["power"]), "brand": request.POST["brand"],}])
            print(data)
            prediction=bikeModel.predict(data)
            print(prediction)
            successMsg="Market price will be around "+str(int(prediction))
            return render(request, "price/bike.html",
                          {
                           "owner":self.owner,
                            "brand":self.brand,
                             "age":self.age,
                             "successMsg":successMsg
                           })




class Car(TemplateView):
    template_name = "price/car.html"
    fuel_type=["Diesel","LPG","Petrol"]
    vehiclename=['Audi', 'BMW', 'Chevrolet', 'Datsun', 'Fiat', 'Force', 'Ford',
     'Hindustan', 'Honda', 'Hyundai', 'Jaguar', 'Jeep', 'Land',
     'Mahindra', 'Maruti', 'Mercedes', 'Mini', 'Mitsubishi', 'Nissan',
     'Renault', 'Skoda', 'Tata', 'Toyota', 'Volkswagen', 'Volvo']
    model=[2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021]
    def get(self, request, *args, **kwargs):
        return render(request,"price/car.html",
                      {
                       "vehiclename":self.vehiclename,
                       "fuel_type":self.fuel_type,
                       "models":self.model
                       })

    def post(self,request):
        print(request.POST)
        if request.POST["name"]=="Select Vehicle Name" or   request.POST["fuel"]=="Select Fuel Type" or request.POST["model"]=="Select Model" or not request.POST["kms_driven"] :
            return render(request, "price/car.html",
                          {"error": "Please fill all fields",
                           "vehiclename": self.vehiclename,
                           "fuel_type": self.fuel_type,
                           "models": self.model})
        else:
            data=pd.DataFrame([{"company": request.POST["name"], "year": int(request.POST["model"]), "kms_driven": int(request.POST["kms_driven"]), "fuel_type":request.POST["fuel"]}])
            print(data)
            prediction=carModel.predict(data)
            print(prediction)
            successMsg="Market price will be around "+str(int(prediction))
            return render(request, "price/car.html",
                          {
                           "vehiclename": self.vehiclename,
                           "fuel_type": self.fuel_type,
                           "models": self.model,
                           "successMsg":successMsg
                           })

class House(TemplateView):
    template_name = "price/house.html"


