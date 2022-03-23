from django.shortcuts import render,redirect
from django.views.generic import TemplateView
import pickle
import pandas as pd
# Create your views here.
carModel = pickle.load(open("/Users/user/Negi/Django/Pridiction_proj/price/car.pkl", "rb"))


class Home(TemplateView):
    template_name = "price/index.html"
    items = ["Car", "Bike", "House"]
    def post(self,request):
        selectedItem=request.POST["item"]
        if selectedItem=="Please select type...":
            return render(request, "price/index.html",{"error":"Please select type","items": self.items})
        else:
            print(selectedItem)
            return redirect("item/"+selectedItem)
    def get(self,request):
        return render(request, "price/index.html", {"items": self.items})

class InputPage(TemplateView):
    template_name = "price/input_page.html"
    fuel_type=["Diesel","LPG","Petrol"]
    vehiclename=['Audi', 'BMW', 'Chevrolet', 'Datsun', 'Fiat', 'Force', 'Ford',
     'Hindustan', 'Honda', 'Hyundai', 'Jaguar', 'Jeep', 'Land',
     'Mahindra', 'Maruti', 'Mercedes', 'Mini', 'Mitsubishi', 'Nissan',
     'Renault', 'Skoda', 'Tata', 'Toyota', 'Volkswagen', 'Volvo']
    model=[2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021]
    def get(self, request, item, *args, **kwargs):
        return render(request,"price/input_page.html",
                      {"item":item,
                       "vehiclename":self.vehiclename,
                       "fuel_type":self.fuel_type,
                       "models":self.model
                       })

    def post(self,request,item):
        print(request.POST)
        if request.POST["name"]=="Select Vehicle Name" or   request.POST["fuel"]=="Select Fuel Type" or request.POST["model"]=="Select Model" or not request.POST["kms_driven"] :
            return render(request, "price/input_page.html",
                          {"error": "Please fill all fields",
                            "item": item,
                           "vehiclename": self.vehiclename,
                           "fuel_type": self.fuel_type,
                           "models": self.model})
        else:
            data=pd.DataFrame.from_dict([{"company": request.POST["name"], "year": int(request.POST["model"]), "kms_driven": int(request.POST["kms_driven"]), "fuel_type":request.POST["fuel"]}])
            print(data)
            prediction=carModel.predict(data)
            print(prediction[0][0])
            successMsg="Market price will be arround "+str(int(prediction[0][0]))
            return render(request, "price/input_page.html",
                          {"item": item,
                           "vehiclename": self.vehiclename,
                           "fuel_type": self.fuel_type,
                           "models": self.model,
                           "successMsg":successMsg
                           })