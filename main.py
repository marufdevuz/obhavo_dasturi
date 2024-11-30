import requests
import json
from datetime import datetime
from colorama import init, Fore, Back, Style
import time
import os

# Colorama initialization
init()

# OpenWeatherMap API key (siz o'z API kalitingizni kiritishingiz kerak)
API_KEY = "-----"

# O'zbekiston viloyatlari
CITIES = {
    "Toshkent": {"lat": 41.2995, "lon": 69.2401},
    "Samarqand": {"lat": 39.6547, "lon": 66.9597},
    "Buxoro": {"lat": 39.7747, "lon": 64.4286},
    "Andijon": {"lat": 40.7827, "lon": 72.3442},
    "Namangan": {"lat": 41.0011, "lon": 71.6673},
    "Farg'ona": {"lat": 40.3834, "lon": 71.7870},
    "Qarshi": {"lat": 38.8603, "lon": 65.7889},
    "Nukus": {"lat": 42.4671, "lon": 59.6103},
    "Xiva": {"lat": 41.3775, "lon": 60.3619},
    "Jizzax": {"lat": 40.1158, "lon": 67.8422},
    "Navoiy": {"lat": 40.0844, "lon": 65.3792},
    "Termiz": {"lat": 37.2242, "lon": 67.2783}
}

def get_weather(lat, lon):
    """Berilgan koordinatalar uchun ob-havo ma'lumotlarini olish"""
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}&units=metric&lang=uz"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
hfwefhuwifuwiwiuehwiehwiufehiuwfehiuwehiuwhfeiuwfehiuweh
cowhfecwefcwef
cowhfecwefcwef
cowhfecwefcwef
cowhfecwefcwef
cowhfecwefcwef
cowhfecwefcwef
cowhfecwefcwef
cowhfecwefcwef
cowhfecwefcwef
cowhfecwefcwef
cowhfecwefcwef
cowhfecwefcwef
cowhfecwefcwef
cowhfecwefcwef
cowhfecwefcwef
cowhfecwefcwef
cowhfecwefcwef
cowhfecwefcwef
cowhfecwefcwef
cowhfecwefcwef
cowhfecwefcwef
cowhfecwefcwef
cowhfecwefcwef
cowhfecwefcwef
cowhfecwefcwef
cowhfecwefcwef
cowhfecwefcwef
cowhfecwefcwef
cowhfecwefcwef
cowhfecwefcwef
cowhfecwefcwef
cowhfecwefcwef
cowhfecwefcwef
cowhfecwefcwef
    except requests.RequestException as e:
        print(f"{Fore.RED}Xatolik yuz berdi: {e}{Style.RESET_ALL}")
        return None

def display_weather(city_name, weather_data):
    """Ob-havo ma'lumotlarini chiroyli formatda ko'rsatish"""
    if not weather_data:
        return
    
    # Asosiy ma'lumotlarni olish
    temp = weather_data['main']['temp']
    feels_like = weather_data['main']['feels_like']
    humidity = weather_data['main']['humidity']
    wind_speed = weather_data['wind']['speed']
    description = weather_data['weather'][0]['description']
    
    # Harorat rangini aniqlash
    temp_color = Fore.RED if temp > 25 else Fore.BLUE if temp < 10 else Fore.GREEN
    
    # Ramka yaratish
    print(f"\n{Fore.YELLOW}{'='*50}{Style.RESET_ALL}")
    print(f"{Fore.CYAN}📍 {city_name.upper()}{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}{'='*50}{Style.RESET_ALL}")
    
    # Ma'lumotlarni ko'rsatish
    print(f"🌡️  Harorat: {temp_color}{temp:.1f}°C{Style.RESET_ALL}")
    print(f"🤔 His qilinishi: {temp_color}{feels_like:.1f}°C{Style.RESET_ALL}")
    print(f"💧 Namlik: {Fore.BLUE}{humidity}%{Style.RESET_ALL}")
    print(f"💨 Shamol tezligi: {Fore.GREEN}{wind_speed} m/s{Style.RESET_ALL}")
    print(f"📝 Holat: {Fore.MAGENTA}{description}{Style.RESET_ALL}")
    
    # Vaqtni ko'rsatish
    current_time = datetime.now().strftime("%H:%M:%S")
    print(f"\n⏰ So'nggi yangilanish: {Fore.YELLOW}{current_time}{Style.RESET_ALL}")

def main():
    """Asosiy dastur"""
    while True:
        try:
            # Ekranni tozalash
            os.system('cls' if os.name == 'nt' else 'clear')
            
            print(f"{Fore.CYAN}O'ZBEKISTON VILOYATLARI OB-HAVO MA'LUMOTLARI{Style.RESET_ALL}")
            print(f"{Fore.YELLOW}{'='*50}{Style.RESET_ALL}\n")
            
            # Har bir shahar uchun ob-havo ma'lumotlarini olish va ko'rsatish
            for city, coords in CITIES.items():
                weather_data = get_weather(coords['lat'], coords['lon'])
                display_weather(city, weather_data)
            
            print(f"\n{Fore.YELLOW}Ma'lumotlar har 5 daqiqada yangilanadi.{Style.RESET_ALL}")
            print(f"{Fore.RED}Dasturni to'xtatish uchun Ctrl+C bosing.{Style.RESET_ALL}")
            
            # 5 daqiqa kutish
            time.sleep(300)
            
        except KeyboardInterrupt:
            print(f"\n{Fore.GREEN}Dastur to'xtatildi. Xayr!{Style.RESET_ALL}")
            break
        except Exception as e:
            print(f"\n{Fore.RED}Kutilmagan xatolik yuz berdi: {e}{Style.RESET_ALL}")
            break

if __name__ == "__main__":
    main()