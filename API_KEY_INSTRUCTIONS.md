# How to Get Your OpenWeatherMap API Key

Follow these steps to obtain your free API key from OpenWeatherMap:

## Step 1: Sign Up for an Account
1. Go to [OpenWeatherMap](https://home.openweathermap.org/users/sign_up)
2. Fill in the registration form with your details
3. Check your email for a confirmation message
4. Click the activation link in the email

## Step 2: Access Your API Keys
1. Log in to your OpenWeatherMap account
2. Navigate to the [API Keys page](https://home.openweathermap.org/api_keys)
3. You'll see your default API key in the table
4. If you don't have one, click "Generate" to create a new API key

## Step 3: Configure Your Application
1. Open `weather_app.py` in a text editor
2. Find the line: `API_KEY = 'YOUR_API_KEY_HERE'  # <-- REPLACE THIS WITH YOUR ACTUAL API KEY`
3. Replace `'YOUR_API_KEY_HERE'` with your actual API key
4. Save the file

## Step 4: Test Your Application
1. Run your application: `streamlit run weather_app.py` or `python -m streamlit run weather_app.py`
2. Try searching for a city like "London" or "New York"
3. You should now see weather data instead of the authorization error

## API Key Tips
- Your API key may take a few minutes to activate after creation
- The free tier allows up to 1,000 API calls per day
- Keep your API key secret and don't share it publicly
- If you exceed the rate limit, you'll need to wait until the next day or upgrade to a paid plan

## Troubleshooting
If you still get authorization errors:
1. Double-check that you've copied the API key correctly (no extra spaces)
2. Make sure you're using the correct API key from your account
3. Wait 10-15 minutes for the key to become active if it's newly created
4. Check that you've saved the file after making changes

If you get command not found errors when running the Streamlit app:
1. Try using `python -m streamlit run weather_app.py` instead of `streamlit run weather_app.py`
2. This happens when Streamlit is installed but not in your system PATH