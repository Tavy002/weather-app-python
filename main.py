import tkinter as tk
from tkinter import ttk, messagebox
import requests
from PIL import Image, ImageTk

# Replace with your actual API key
API_KEY = "0d176dfcdb438794e56ff3b68ff6f0f6"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"


# Function to fetch weather
def get_weather(city):
    params = {"q": city, "appid": API_KEY, "units": "metric"}
    response = requests.get(BASE_URL, params=params)
    data = response.json()

    if response.status_code == 200:
        return {
            "city": data["name"],
            "temperature": data["main"]["temp"],
            "humidity": data["main"]["humidity"],
            "condition": data["weather"][0]["main"],
        }
    else:
        return None


# Function to update UI
def fetch_weather():
    city = city_entry.get()
    weather = get_weather(city)

    if weather:
        temp_label.config(text=f"{weather['temperature']}°C")
        condition_label.config(text=weather['condition'])
        humidity_label.config(text=f"Humidity: {weather['humidity']}%")
        update_icon(weather['condition'])
        update_background(weather['condition'])
    else:
        messagebox.showerror("Error", "City not found")


# Function to update weather icon
def update_icon(condition):
    icons = {
        "Clear": "sun.png",
        "Clouds": "cloud.png",
        "Rain": "rain.png",
        "Snow": "snow.png",
        "Mist": "mist.png",
    }
    icon_path = icons.get(condition, "default.png")
    img = Image.open(icon_path)
    img = img.resize((100, 100))
    img = ImageTk.PhotoImage(img)
    icon_label.config(image=img)
    icon_label.image = img


# Function to update background color
def update_background(condition):
    colors = {
        "Clear": "#FFD700",  # Gold for sunny
        "Clouds": "#D3D3D3",  # Light gray for cloudy
        "Rain": "#4682B4",  # Steel blue for rain
        "Snow": "#ADD8E6",  # Light blue for snow
        "Mist": "#B0C4DE",  # Light steel blue for mist
    }
    bg_color = colors.get(condition, "#87CEEB")  # Default sky blue
    root.config(bg=bg_color)
    temp_label.config(bg=bg_color)
    condition_label.config(bg=bg_color)
    humidity_label.config(bg=bg_color)
    icon_label.config(bg=bg_color)


# GUI Setup
root = tk.Tk()
root.title("Weather App")
root.geometry("400x500")
root.config(bg="#87CEEB")

city_entry = ttk.Entry(root, font=("Arial", 14))
city_entry.pack(pady=20)

fetch_button = ttk.Button(root, text="Get Weather", command=fetch_weather)
fetch_button.pack()

icon_label = tk.Label(root, bg="#87CEEB")
icon_label.pack()

temp_label = tk.Label(root, font=("Arial", 24, "bold"), bg="#87CEEB")
temp_label.pack()

condition_label = tk.Label(root, font=("Arial", 18), bg="#87CEEB")
condition_label.pack()

humidity_label = tk.Label(root, font=("Arial", 14), bg="#87CEEB")
humidity_label.pack()

root.mainloop()
