import streamlit as st
import requests
import datetime
import pandas as pd

# API Configuration
# IMPORTANT: Replace 'YOUR_API_KEY_HERE' with your actual OpenWeatherMap API key
API_KEY = '4ee07ce55229e87e169ea03e15a608c9'  # <-- REPLACE THIS WITH YOUR ACTUAL API KEY
BASE_URL = 'https://api.openweathermap.org/data/2.5'

# Set page config
st.set_page_config(
    page_title="Weather Forecast App",
    page_icon="🌤️",
    layout="wide"
)

# Custom CSS for styling
st.markdown("""
<style>
    .stApp {
        background: linear-gradient(135deg, #1a2a6c, #b21f1f, #1a2a6c);
        background-size: 400% 400%;
        animation: gradientBG 15s ease infinite;
    }
    
    @keyframes gradientBG {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    
    .weather-card {
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(10px);
        border-radius: 20px;
        padding: 30px;
        margin: 20px 0;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.2);
        border: 1px solid rgba(255, 255, 255, 0.18);
    }
    
    .forecast-card {
        background: rgba(255, 255, 255, 0.05);
        border-radius: 15px;
        padding: 20px;
        text-align: center;
        transition: all 0.3s ease;
        margin: 10px 0;
    }
    
    .forecast-card:hover {
        background: rgba(255, 255, 255, 0.1);
        transform: translateY(-5px);
    }
    
    .metric-card {
        background: rgba(255, 255, 255, 0.05);
        border-radius: 15px;
        padding: 15px;
        text-align: center;
        margin: 10px 0;
    }
    
    .temperature {
        font-size: 4rem;
        font-weight: 700;
        text-shadow: 0 0 10px rgba(255, 255, 255, 0.5);
    }
    
    .weather-icon {
        width: 100px;
        height: 100px;
    }
    
    .title {
        text-align: center;
        color: white;
        text-shadow: 0 2px 10px rgba(0, 0, 0, 0.3);
    }
    
    .footer {
        text-align: center;
        padding: 20px;
        margin-top: 20px;
        font-size: 0.9rem;
        opacity: 0.8;
        color: white;
    }
</style>
""", unsafe_allow_html=True)

# Title
st.markdown("<h1 class='title'>🌤️ Weather Forecast App</h1>", unsafe_allow_html=True)

# Sidebar for inputs
with st.sidebar:
    st.header("📍 Location Settings")
    
    # Unit selection
    unit = st.radio("Temperature Unit", ["Celsius", "Fahrenheit"], index=0)
    unit_param = "metric" if unit == "Celsius" else "imperial"
    temp_symbol = "°C" if unit == "Celsius" else "°F"
    wind_unit = "m/s" if unit == "Celsius" else "mph"
    
    # Location input
    city_name = st.text_input("Enter City Name", "London")
    
    # Geolocation button
    use_geolocation = st.checkbox("Use My Location")
    
    # Submit button
    submit = st.button("Get Weather")

# Function to fetch current weather
def fetch_current_weather(city_name, unit_param):
    try:
        url = f"{BASE_URL}/weather?q={city_name}&appid={API_KEY}&units={unit_param}"
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching current weather data: {e}")
        return None

# Function to fetch forecast
def fetch_forecast(lat, lon, unit_param):
    try:
        url = f"{BASE_URL}/forecast?lat={lat}&lon={lon}&appid={API_KEY}&units={unit_param}"
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching forecast data: {e}")
        return None

# Function to get weather by coordinates
def fetch_weather_by_coordinates(lat, lon, unit_param):
    try:
        url = f"{BASE_URL}/weather?lat={lat}&lon={lon}&appid={API_KEY}&units={unit_param}"
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching weather data for your location: {e}")
        return None

# Function to process forecast data
def process_forecast_data(forecast_data):
    daily_forecasts = {}
    
    for item in forecast_data['list']:
        date = datetime.datetime.fromtimestamp(item['dt'])
        day_key = date.strftime('%Y-%m-%d')
        day_name = date.strftime('%A')
        date_str = date.strftime('%b %d')
        
        if day_key not in daily_forecasts:
            daily_forecasts[day_key] = {
                'day': day_name,
                'date': date_str,
                'icon': item['weather'][0]['icon'],
                'temp_max': item['main']['temp_max'],
                'temp_min': item['main']['temp_min'],
                'description': item['weather'][0]['description']
            }
        else:
            # Update max/min temps
            daily_forecasts[day_key]['temp_max'] = max(daily_forecasts[day_key]['temp_max'], item['main']['temp_max'])
            daily_forecasts[day_key]['temp_min'] = min(daily_forecasts[day_key]['temp_min'], item['main']['temp_min'])
    
    # Convert to list and limit to 7 days
    forecast_list = list(daily_forecasts.values())[:7]
    return forecast_list

# Main content
if submit or use_geolocation:
    with st.spinner("Fetching weather data..."):
        if use_geolocation:
            # Note: Streamlit doesn't have direct geolocation access like browsers
            # We'll simulate this with a default city or prompt user to enter coordinates
            st.info("Geolocation is not directly available in Streamlit. Please enter a city name.")
            current_data = None
            forecast_data = None
        else:
            # Fetch current weather
            current_data = fetch_current_weather(city_name, unit_param)
            
            if current_data:
                # Fetch forecast using coordinates from current weather
                lat = current_data['coord']['lat']
                lon = current_data['coord']['lon']
                forecast_data = fetch_forecast(lat, lon, unit_param)

    if current_data and forecast_data:
        # Display current weather
        st.markdown("<div class='weather-card'>", unsafe_allow_html=True)
        st.subheader(f"{current_data['name']}, {current_data['sys']['country']}")
        
        col1, col2, col3 = st.columns([2, 1, 2])
        
        with col1:
            # Weather description
            st.markdown(f"<div class='temperature'>{round(current_data['main']['temp'])}{temp_symbol}</div>", unsafe_allow_html=True)
            st.write(current_data['weather'][0]['description'].title())
            
        with col2:
            # Weather icon
            icon_url = f"https://openweathermap.org/img/wn/{current_data['weather'][0]['icon']}@2x.png"
            st.image(icon_url, width=100, caption="")
            
        with col3:
            # Date
            today = datetime.datetime.now()
            st.write(today.strftime("%A, %B %d, %Y"))
            
        st.markdown("</div>", unsafe_allow_html=True)
        
        # Additional weather metrics
        st.markdown("<div class='weather-card'>", unsafe_allow_html=True)
        st.subheader("Weather Details")
        
        metric_cols = st.columns(3)
        
        with metric_cols[0]:
            st.markdown("<div class='metric-card'>", unsafe_allow_html=True)
            st.metric("Humidity", f"{current_data['main']['humidity']}%")
            st.markdown("</div>", unsafe_allow_html=True)
            
            st.markdown("<div class='metric-card'>", unsafe_allow_html=True)
            st.metric("Sunrise", datetime.datetime.fromtimestamp(current_data['sys']['sunrise']).strftime("%H:%M"))
            st.markdown("</div>", unsafe_allow_html=True)
            
            st.markdown("<div class='metric-card'>", unsafe_allow_html=True)
            st.metric("Pressure", f"{current_data['main']['pressure']} hPa")
            st.markdown("</div>", unsafe_allow_html=True)
            
        with metric_cols[1]:
            st.markdown("<div class='metric-card'>", unsafe_allow_html=True)
            st.metric("Wind Speed", f"{current_data['wind']['speed']} {wind_unit}")
            st.markdown("</div>", unsafe_allow_html=True)
            
            st.markdown("<div class='metric-card'>", unsafe_allow_html=True)
            st.metric("Sunset", datetime.datetime.fromtimestamp(current_data['sys']['sunset']).strftime("%H:%M"))
            st.markdown("</div>", unsafe_allow_html=True)
            
        with metric_cols[2]:
            st.markdown("<div class='metric-card'>", unsafe_allow_html=True)
            visibility_km = current_data['visibility'] / 1000
            st.metric("Visibility", f"{visibility_km:.1f} km")
            st.markdown("</div>", unsafe_allow_html=True)
            
        st.markdown("</div>", unsafe_allow_html=True)
        
        # Forecast section
        st.markdown("<div class='weather-card'>", unsafe_allow_html=True)
        st.subheader("7-Day Forecast")
        
        forecast_list = process_forecast_data(forecast_data)
        
        # Display forecast in columns
        forecast_cols = st.columns(7)
        for i, forecast in enumerate(forecast_list):
            with forecast_cols[i]:
                st.markdown("<div class='forecast-card'>", unsafe_allow_html=True)
                st.write(f"**{forecast['day']}**")
                st.write(f"{forecast['date']}")
                icon_url = f"https://openweathermap.org/img/wn/{forecast['icon']}.png"
                st.image(icon_url, width=60)
                st.write(f"{round(forecast['temp_max'])}{temp_symbol}/{round(forecast['temp_min'])}{temp_symbol}")
                st.write(forecast['description'].title())
                st.markdown("</div>", unsafe_allow_html=True)
                
        st.markdown("</div>", unsafe_allow_html=True)
    elif current_data is None and not use_geolocation:
        st.error("City not found. Please check the spelling and try again.")

# Welcome message when no data is displayed
else:
    st.info("👈 Enter a city name in the sidebar and click 'Get Weather' to see the forecast!")

# Footer
st.markdown("<div class='footer'>Weather Forecast App &copy; 2023 | Data provided by OpenWeatherMap</div>", unsafe_allow_html=True)