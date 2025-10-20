# ==================== WEATHER & NEWS DASHBOARD ====================
# Mini API Project using: HTTP Requests, JSON Parsing, Error Handling, User Interface

import requests
import json
from datetime import datetime

print("🌤️📰 WEATHER & NEWS DASHBOARD")
print("="*50)

# ==================== API CONFIGURATION ====================
# Free API Keys - Get from respective websites
WEATHER_API_KEY = "your_openweather_api_key"  # Get from: https://openweathermap.org/api
NEWS_API_KEY = "your_news_api_key"            # Get from: https://newsapi.org/

# API Endpoints
WEATHER_BASE_URL = "http://api.openweathermap.org/data/2.5/weather"
NEWS_BASE_URL = "https://newsapi.org/v2/top-headlines"

print("📋 API Configuration:")
print(f"   🌤️ Weather API: {'✅ Configured' if WEATHER_API_KEY != 'your_openweather_api_key' else '❌ Need API Key'}")
print(f"   📰 News API: {'✅ Configured' if NEWS_API_KEY != 'your_news_api_key' else '❌ Need API Key'}")

# ==================== WEATHER FUNCTIONS ====================

def get_weather_data(city_name):
    """
    Get current weather data for specified city
    Returns weather information or None if error
    """
    print(f"\n🌤️ Fetching weather data for {city_name}...")
    
    # API parameters
    params = {
        'q': city_name,
        'appid': WEATHER_API_KEY,
        'units': 'metric'  # Celsius temperature
    }
    
    try:
        # Make API request
        response = requests.get(WEATHER_BASE_URL, params=params)
        
        if response.status_code == 200:
            data = response.json()
            print("   ✅ Weather data fetched successfully!")
            return data
        elif response.status_code == 401:
            print("   ❌ Invalid API key! Please check your Weather API key.")
            return None
        elif response.status_code == 404:
            print("   ❌ City not found! Please check the city name.")
            return None
        else:
            print(f"   ❌ Error: {response.status_code}")
            return None
            
    except requests.exceptions.ConnectionError:
        print("   ❌ No internet connection!")
        return None
    except requests.exceptions.RequestException as e:
        print(f"   ❌ Request error: {e}")
        return None

def display_weather_info(weather_data):
    """
    Display formatted weather information
    """
    if not weather_data:
        return
    
    # Extract weather information
    city = weather_data['name']
    country = weather_data['sys']['country']
    temp = round(weather_data['main']['temp'])
    feels_like = round(weather_data['main']['feels_like'])
    humidity = weather_data['main']['humidity']
    description = weather_data['weather'][0]['description'].title()
    
    # Display weather info
    print(f"\n🌤️ WEATHER INFORMATION FOR {city.upper()}")
    print("="*50)
    print(f"📍 Location: {city}, {country}")
    print(f"🌡️  Temperature: {temp}°C (feels like {feels_like}°C)")
    print(f"☀️  Condition: {description}")
    print(f"💧 Humidity: {humidity}%")
    
    # Weather-based recommendations
    print(f"\n💡 RECOMMENDATIONS:")
    get_weather_recommendations(temp, description.lower())

def get_weather_recommendations(temperature, condition):
    """
    Provide clothing and activity suggestions based on weather
    """
    # Clothing suggestions
    if temperature >= 30:
        clothing = "👕 Light clothes, sunhat, stay hydrated!"
    elif temperature >= 20:
        clothing = "👔 Comfortable clothes, light jacket optional"
    elif temperature >= 10:
        clothing = "🧥 Jacket or sweater recommended"
    else:
        clothing = "🧥❄️ Warm clothes, heavy jacket, gloves"
    
    # Activity suggestions  
    if "rain" in condition or "drizzle" in condition:
        activity = "☔ Indoor activities, carry umbrella if going out"
    elif "snow" in condition:
        activity = "❄️ Great for winter sports or cozy indoor time"
    elif "clear" in condition and 15 <= temperature <= 25:
        activity = "🌟 Perfect weather for outdoor activities!"
    elif temperature > 35:
        activity = "🔥 Stay indoors during peak hours, plenty of water"
    else:
        activity = "🚶 Good weather for moderate outdoor activities"
    
    print(f"   👕 CLOTHING: {clothing}")
    print(f"   🎯 ACTIVITY: {activity}")

# ==================== NEWS FUNCTIONS ====================

def get_news_headlines(country='in', category=None):
    """
    Get latest news headlines
    Returns news data or None if error
    """
    print(f"\n📰 Fetching latest news headlines...")
    
    # API parameters
    params = {
        'apiKey': NEWS_API_KEY,
        'country': country,
        'pageSize': 5  # Get top 5 headlines
    }
    
    if category:
        params['category'] = category
    
    try:
        # Make API request
        response = requests.get(NEWS_BASE_URL, params=params)
        
        if response.status_code == 200:
            data = response.json()
            print("   ✅ News data fetched successfully!")
            return data
        elif response.status_code == 401:
            print("   ❌ Invalid API key! Please check your News API key.")
            return None
        else:
            print(f"   ❌ Error: {response.status_code}")
            return None
            
    except requests.exceptions.ConnectionError:
        print("   ❌ No internet connection!")
        return None
    except requests.exceptions.RequestException as e:
        print(f"   ❌ Request error: {e}")
        return None

def display_news_headlines(news_data):
    """
    Display formatted news headlines
    """
    if not news_data or 'articles' not in news_data:
        return
    
    articles = news_data['articles']
    
    print(f"\n📰 TOP NEWS HEADLINES")
    print("="*60)
    
    for i, article in enumerate(articles, 1):
        title = article.get('title', 'No title')
        source = article.get('source', {}).get('name', 'Unknown source')
        description = article.get('description', 'No description available')
        published_at = article.get('publishedAt', '')
        
        # Format published time
        if published_at:
            try:
                pub_time = datetime.fromisoformat(published_at.replace('Z', '+00:00'))
                time_str = pub_time.strftime('%H:%M, %d %b')
            except:
                time_str = 'Unknown time'
        else:
            time_str = 'Unknown time'
        
        print(f"\n📖 {i}. {title}")
        print(f"   📺 Source: {source}")
        print(f"   🕐 Published: {time_str}")
        if description and len(description) > 0:
            # Truncate description if too long
            desc = description[:150] + "..." if len(description) > 150 else description
            print(f"   📝 {desc}")

# ==================== DEMO MODE (When API keys not available) ====================

def demo_weather():
    """
    Demo weather data when API key not available
    """
    print("\n🧪 DEMO MODE - Sample Weather Data")
    print("="*40)
    
    demo_data = {
        'name': 'Delhi',
        'sys': {'country': 'IN'},
        'main': {
            'temp': 28.5,
            'feels_like': 32.1,
            'humidity': 65
        },
        'weather': [{'description': 'clear sky'}]
    }
    
    display_weather_info(demo_data)

def demo_news():
    """
    Demo news data when API key not available
    """
    print("\n🧪 DEMO MODE - Sample News Headlines")
    print("="*40)
    
    demo_data = {
        'articles': [
            {
                'title': 'Sample News Headline 1',
                'source': {'name': 'Demo News'},
                'description': 'This is a sample news description for demonstration purposes.',
                'publishedAt': '2024-10-20T10:30:00Z'
            },
            {
                'title': 'Sample Technology Update',
                'source': {'name': 'Tech Times'},
                'description': 'Latest developments in technology sector.',
                'publishedAt': '2024-10-20T09:15:00Z'
            },
            {
                'title': 'Sample Weather Update',
                'source': {'name': 'Weather Channel'},
                'description': 'Weather conditions across major cities.',
                'publishedAt': '2024-10-20T08:45:00Z'
            }
        ]
    }
    
    display_news_headlines(demo_data)

# ==================== MAIN MENU FUNCTIONS ====================

def get_weather():
    """
    Weather information menu option
    """
    city = input("\n🌤️ Enter city name: ").strip()
    
    if not city:
        print("❌ Please enter a valid city name!")
        return
    
    if WEATHER_API_KEY == "your_openweather_api_key":
        print("⚠️ Weather API key not configured. Showing demo data...")
        demo_weather()
    else:
        weather_data = get_weather_data(city)
        display_weather_info(weather_data)

def get_news():
    """
    News headlines menu option
    """
    print("\n📰 News Categories:")
    print("1. General (default)")
    print("2. Technology")
    print("3. Sports")
    print("4. Health")
    print("5. Entertainment")
    
    choice = input("Choose category (1-5) or press Enter for general: ").strip()
    
    category_map = {
        '2': 'technology',
        '3': 'sports', 
        '4': 'health',
        '5': 'entertainment'
    }
    
    category = category_map.get(choice, None)
    
    if NEWS_API_KEY == "your_news_api_key":
        print("⚠️ News API key not configured. Showing demo data...")
        demo_news()
    else:
        news_data = get_news_headlines(category=category)
        display_news_headlines(news_data)

def get_both():
    """
    Get both weather and news information
    """
    print("\n🌍 COMPREHENSIVE DASHBOARD")
    print("="*30)
    
    # Get weather
    city = input("🌤️ Enter city name for weather: ").strip()
    if city:
        if WEATHER_API_KEY == "your_openweather_api_key":
            demo_weather()
        else:
            weather_data = get_weather_data(city)
            display_weather_info(weather_data)
    
    # Get news
    if NEWS_API_KEY == "your_news_api_key":
        demo_news()
    else:
        news_data = get_news_headlines()
        display_news_headlines(news_data)

# ==================== MAIN PROGRAM ====================

def main():
    """
    Main program loop with menu
    """
    while True:
        print("\n" + "="*50)
        print("🌤️📰 WEATHER & NEWS DASHBOARD")
        print("="*50)
        print("1. 🌤️  Get Weather Information")
        print("2. 📰 Get Latest News Headlines")
        print("3. 🌍 Get Both (Weather + News)")
        print("4. ⚙️  Setup Instructions")
        print("5. 🚪 Exit")
        print("-"*50)
        
        choice = input("Choose an option (1-5): ").strip()
        
        if choice == '1':
            get_weather()
        elif choice == '2':
            get_news()
        elif choice == '3':
            get_both()
        elif choice == '4':
            show_setup_instructions()
        elif choice == '5':
            print("\n👋 Thank you for using Weather & News Dashboard!")
            print("🌟 Stay informed and weather-ready!")
            break
        else:
            print("❌ Invalid choice! Please enter 1-5.")

def show_setup_instructions():
    """
    Display API setup instructions
    """
    print("\n⚙️ API SETUP INSTRUCTIONS")
    print("="*30)
    print("""
🌤️ WEATHER API SETUP:
1. Go to: https://openweathermap.org/api
2. Sign up for free account
3. Go to API keys section
4. Copy your API key
5. Replace 'your_openweather_api_key' in code

📰 NEWS API SETUP:
1. Go to: https://newsapi.org/
2. Sign up for free account
3. Go to dashboard
4. Copy your API key
5. Replace 'your_news_api_key' in code

💡 BOTH APIs ARE FREE!
- Weather API: 1000 calls/day free
- News API: 500 requests/day free

🔄 After setup, restart the program to use real data!
    """)

# ==================== PROGRAM START ====================

if __name__ == "__main__":
    print("🚀 Welcome to Weather & News Dashboard!")
    print("="*50)
    print("📡 This app provides real-time weather and news information")
    print("🔑 API keys required for full functionality")
    print("🧪 Demo mode available without API keys")
    
    main()

# ==================== PROJECT SUMMARY ====================
print("\n🎯 PROJECT SUMMARY:")
print("="*20)
print("""
🌤️📰 WEATHER & NEWS DASHBOARD

FEATURES:
✅ Real-time weather data for any city
✅ Current temperature, humidity, conditions
✅ Weather-based clothing/activity recommendations
✅ Latest news headlines from multiple categories
✅ Beautiful formatted output with emojis
✅ Error handling for network/API issues
✅ Demo mode when API keys not available

TECHNOLOGIES USED:
✅ HTTP requests (requests library)
✅ JSON data parsing
✅ Error handling & validation
✅ Date/time operations
✅ String formatting & manipulation
✅ Menu-driven user interface
✅ External API integration

LEARNING OUTCOMES:
✅ REST API consumption
✅ HTTP status codes handling
✅ JSON data extraction
✅ User input validation
✅ Network error handling
✅ Data presentation formatting
✅ Real-world API usage patterns

APIS USED:
🌤️ OpenWeatherMap API (Free tier: 1000 calls/day)
📰 NewsAPI (Free tier: 500 requests/day)

NEXT STEPS:
1. Get free API keys from both services
2. Replace placeholder keys in code
3. Run program and test all features
4. Customize for your favorite cities/news categories
""")