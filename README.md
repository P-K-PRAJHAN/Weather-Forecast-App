# Weather Forecast Web Application

A modern, responsive weather forecasting application with two versions:
1. **Web Version**: Built with HTML, CSS, and Vanilla JavaScript
2. **Streamlit Version**: Built with Python and Streamlit

Both versions provide current weather conditions and a 7-day forecast using the OpenWeatherMap API.

## 🌟 Features

- **Search by City**: Enter any city name to get current weather and forecast
- **Location Detection**: Automatically detect user's location for local weather
- **Current Weather Display**: 
  - Temperature and weather condition
  - Humidity percentage
  - Wind speed
  - Sunrise and sunset times
  - Weather icon visualization
- **7-Day Forecast**: Detailed forecast for the upcoming week
- **Responsive Design**: Works on mobile, tablet, and desktop devices
- **Loading Animation**: Visual feedback during data fetching
- **Error Handling**: Graceful handling of invalid cities or network issues
- **Modern UI**: Glass-morphism design with smooth animations

## 🛠️ Tech Stack

- **Python**: Core programming language
- **Streamlit**: Web application framework
- **Requests**: HTTP library for API calls
- **Pandas**: Data processing (for forecast data)
- **OpenWeatherMap API**: Weather data source

## 📁 Project Structure

```
/weather-forecast-app
│
├── weather_app.py      # Streamlit application
├── requirements.txt    # Python dependencies
├── README.md           # Project documentation
└── API_KEY_INSTRUCTIONS.md # API key setup instructions
```

## ⚙️ Setup Instructions

1. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Obtain an API Key**:
   - Visit [OpenWeatherMap](https://openweathermap.org/api)
   - Sign up for a free account
   - Navigate to the API keys section
   - Generate a new API key (or use the default free tier key)
   - Copy your API key
   - For detailed instructions, see `API_KEY_INSTRUCTIONS.md`

3. **Configure the API Key**:
   - Open `weather_app.py` in a text editor
   - Replace `'YOUR_API_KEY_HERE'` with your actual API key:
   ```python
   API_KEY = 'your_actual_api_key_here'
   ```

4. **Run the Application**:
   ```bash
   streamlit run weather_app.py
   ```
   - The app will open automatically in your browser at `http://localhost:8501`
   
   **Alternative method (if the above doesn't work)**:
   ```bash
   python -m streamlit run weather_app.py
   ```

## 🚀 How to Use

1. **Search by City**:
   - Enter a city name in the sidebar input
   - Select temperature unit (Celsius/Fahrenheit)
   - Click "Get Weather" button

2. **View Weather Data**:
   - Current weather conditions appear in the main panel
   - 7-day forecast displays below the current weather

## 🎨 UI/UX Features

- **Glass-morphism Design**: Modern frosted glass effect cards
- **Responsive Layout**: Adapts to all screen sizes
- **Smooth Animations**: Hover effects and transitions
- **Intuitive Icons**: Visual representation of weather conditions
- **Loading States**: Spinner animation during data fetch
- **Error Messages**: Clear feedback for user actions

## 🔧 API Integration

This application uses two OpenWeatherMap APIs:

1. **Current Weather API**: 
   ```
   api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}
   ```

2. **5-Day Forecast API**:
   ```
   api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={API key}
   ```

## 📱 Responsive Design

The application is fully responsive and adapts to:
- **Mobile Devices**: Single column layout with larger touch targets
- **Tablets**: Optimized spacing and layout adjustments
- **Desktops**: Full-width design with expanded elements

Media queries adjust the layout at:
- 768px breakpoint for tablets
- 480px breakpoint for mobile devices

## 🐛 Troubleshooting

**API Key Issues**:
- Ensure your API key is correctly placed in `weather_app.py`
- Check that your API key is active in your OpenWeatherMap account
- Verify you haven't exceeded the free tier request limits (typically 1,000 calls/day)
- Make sure you've replaced the placeholder `YOUR_API_KEY_HERE` with your actual API key

**Location Not Working**:
- Note: Streamlit version does not support direct geolocation
- Ensure location services are enabled on your device

**Styling Issues**:
- Make sure all files are in the same directory
- For Streamlit version, ensure you're using a compatible browser

**Streamlit Command Not Found**:
- If `streamlit run weather_app.py` doesn't work, try `python -m streamlit run weather_app.py`
- This happens when Streamlit is not in your system PATH but is installed in your Python environment

## 📄 License

This project is open source and available under the MIT License.

## 🤝 Contributing

Contributions are welcome! Feel free to submit issues or pull requests to improve the application.

---

**Note**: This is a frontend-only application. All data is fetched directly from the OpenWeatherMap API in the browser.