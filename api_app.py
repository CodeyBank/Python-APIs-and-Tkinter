from tkinter import *
from PIL import ImageTk, Image
import requests
import json

root = Tk()
root.title("api")
root.iconbitmap('icon.ico')
root.geometry("400x150")

zipcode_entry = Entry(root, width=20)
zipcode_entry.grid(row=0, column=0, padx=20, ipady=6)

global default
default = "90210"


def ziplookup():
    default = zipcode_entry.get()
    print(default)

    try:
        api_request = requests.get(
            "http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=" + default + "&distance=5&API_KEY=F41098F5-7512-4528-9BE0-98D80B2F97B9")
        # load content of the api request in a json variable
        api = json.loads(api_request.content)
        city = api[0]['ReportingArea']
        quality = api[0]['AQI']
        category = api[0]['Category']['Name']
        weather_color = ''

        if category == "Good":
            weather_color = "#00e400"
        elif category == "Moderate":
            weather_color = "#ffff00"
        elif category == "Unhealthy for Sensitive Groups":
            weather_color = "ff7e00"
        elif category == "Unhealthy":
            weather_color = "#ff0000"
        elif category == "Very Unhealthy":
            weather_color = "#8f3f97"
        elif category == "Hazardous":
            weather_color = "#7e0023"

        root.config(bg=weather_color)
        mylabel = Label(root,
                        text="City: " + city + "\n " + "Air Quality: " + str(quality) + "\n " + "Category: " + category,
                        font=("Gothic", 20), bg=weather_color)
        mylabel.grid(row=1, column=0, columnspan=2)

    except Exception as e:
        api = "Error..."


# print(default)
# api_request = requests.get(
#     "http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode="+default+"&distance=5&API_KEY=F41098F5-7512-4528-9BE0-98D80B2F97B9")
# api = json.loads(api_request.content)
# city = api[0]['ReportingArea']
# quality = api[0]['AQI']
# category = api[0]['Category']['Name']
# weather_color = ''
#
# if category == "Good":
#     weather_color = "#00e400"
# elif category == "Moderate":
#     weather_color = "#ffff00"
# elif category == "Unhealthy for Sensitive Groups":
#     weather_color = "ff7e00"
# elif category == "Unhealthy":
#     weather_color = "#ff0000"
# elif category == "Very Unhealthy":
#     weather_color = "#8f3f97"
# elif category == "Hazardous":
#     weather_color = "#7e0023"
#
# root.config(bg=weather_color)
# mylabel = Label(root,
#                 text="City: " + city + "\n " + "Air Quality: " + str(quality) + "\n " + "Category: " + category,
#                 font=("Gothic", 20), bg=weather_color)
# mylabel.grid(row=1, column=0, columnspan=2)


# control = LabelFrame(root).grid(row=0, column=0)
zipButton = Button(root, text="Lookup Zipcode", bg="white", font=("Gothic", 14), command=ziplookup)
zipButton.grid(row=0, column=1)

# data_frame = LabelFrame(root).pack()

root.mainloop()
