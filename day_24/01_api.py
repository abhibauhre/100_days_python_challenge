# ==================== WHAT IS API? ====================
# API = Application Programming Interface
# Simple Definition: A way for programs to talk to each other

print("🌐 WHAT IS API? - SIMPLE EXPLANATION")
print("=" * 50)

# ==================== API ANALOGY ====================
print("\n📞 REAL WORLD ANALOGY:")
print("-" * 30)
print("""
API is like ordering food from a restaurant:

🍽️ RESTAURANT ANALOGY:
   You (Program) → Waiter (API) → Kitchen (Server)
   
   1. You tell waiter what you want (Request)
   2. Waiter takes order to kitchen (API call)
   3. Kitchen prepares food (Server processes)
   4. Waiter brings food back (Response)
   5. You get your meal (Data)

💻 PROGRAMMING ANALOGY:
   Your Code → API → External Service
   
   1. Your code asks for data (HTTP Request)
   2. API forwards request (To server)
   3. Server processes request (Database/Logic)
   4. API sends data back (HTTP Response) 
   5. Your code receives data (JSON/XML)
""")

# ==================== BASIC API CONCEPTS ====================
print("\n🎯 KEY API CONCEPTS:")
print("-" * 30)
print("""
📡 REQUEST: What you ask for
   - URL: Where to send request
   - Method: GET (read), POST (create), PUT (update), DELETE (remove)
   - Parameters: Extra info you send

📥 RESPONSE: What you get back
   - Status Code: 200 (success), 404 (not found), 500 (error)
   - Data: Usually in JSON format
   - Headers: Extra information

🔗 ENDPOINT: Specific URL for specific data
   Example: https://api.weather.com/current
""")

# ==================== BASIC API PROGRAM ====================
print("\n💻 BASIC API PROGRAM - WEATHER DATA")
print("=" * 50)

import requests
import json

# ==================== EXAMPLE 1: Simple GET Request ====================
print("\n🌤️ EXAMPLE 1: Getting Weather Data")
print("-" * 40)

# Free weather API (no key required for this example)
# Using a mock API for demonstration
try:
    # This is a free API for testing
    url = "https://httpbin.org/json"
    
    print(f"📡 Making API request to: {url}")
    
    # Send GET request
    response = requests.get(url)
    
    print(f"📊 Status Code: {response.status_code}")
    
    if response.status_code == 200:
        # Convert response to JSON
        data = response.json()
        print("✅ API Response (JSON):")
        print(json.dumps(data, indent=2))
    else:
        print(f"❌ Error: {response.status_code}")
        
except requests.exceptions.RequestException as e:
    print(f"❌ Network Error: {e}")

# ==================== EXAMPLE 2: Real Weather API ====================
print("\n🌍 EXAMPLE 2: Real Weather API (Free)")
print("-" * 40)

try:
    # OpenWeatherMap free API (limited requests)
    # You can get free API key from openweathermap.org
    city = "London"
    # Using free service (no key required but limited)
    weather_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid=demo"
    
    print(f"🌆 Getting weather for: {city}")
    print(f"📡 API URL: {weather_url}")
    
    response = requests.get(weather_url)
    print(f"📊 Status Code: {response.status_code}")
    
    if response.status_code == 200:
        weather_data = response.json()
        print("🌤️ Weather Data:")
        print(json.dumps(weather_data, indent=2))
        
        # Extract specific information
        if "main" in weather_data:
            temp = weather_data["main"]["temp"]
            description = weather_data["weather"][0]["description"]
            print(f"\n📋 Summary:")
            print(f"   Temperature: {temp} K")
            print(f"   Description: {description}")
    else:
        print("❌ Could not get weather data (API key needed for full access)")
        
except Exception as e:
    print(f"❌ Error: {e}")

# ==================== EXAMPLE 3: Simple JSON Placeholder API ====================
print("\n📝 EXAMPLE 3: Getting User Data")
print("-" * 40)

try:
    # Free API for testing - JSONPlaceholder
    users_url = "https://jsonplaceholder.typicode.com/users/1"
    
    print(f"👤 Getting user data from: {users_url}")
    
    response = requests.get(users_url)
    print(f"📊 Status Code: {response.status_code}")
    
    if response.status_code == 200:
        user_data = response.json()
        print("👤 User Data:")
        print(json.dumps(user_data, indent=2))
        
        # Extract specific information
        print(f"\n📋 User Summary:")
        print(f"   Name: {user_data['name']}")
        print(f"   Email: {user_data['email']}")
        print(f"   City: {user_data['address']['city']}")
        print(f"   Company: {user_data['company']['name']}")
    else:
        print("❌ Could not get user data")
        
except Exception as e:
    print(f"❌ Error: {e}")

# ==================== EXAMPLE 4: Multiple Users ====================
print("\n👥 EXAMPLE 4: Getting Multiple Users")
print("-" * 40)

try:
    # Get all users
    all_users_url = "https://jsonplaceholder.typicode.com/users"
    
    print(f"👥 Getting all users from: {all_users_url}")
    
    response = requests.get(all_users_url)
    print(f"📊 Status Code: {response.status_code}")
    
    if response.status_code == 200:
        all_users = response.json()
        print(f"📊 Total Users: {len(all_users)}")
        
        print("\n👥 All Users:")
        for i, user in enumerate(all_users, 1):
            print(f"   {i}. {user['name']} ({user['email']})")
            
        # Find users from specific city
        print(f"\n🏙️ Users from 'Gwenborough':")
        for user in all_users:
            if user['address']['city'] == 'Gwenborough':
                print(f"   - {user['name']}")
    else:
        print("❌ Could not get users data")
        
except Exception as e:
    print(f"❌ Error: {e}")

# ==================== API BEST PRACTICES ====================
print("\n💡 API BEST PRACTICES:")
print("-" * 30)
print("""
✅ DO:
   • Always check status codes
   • Handle errors gracefully 
   • Use try-except blocks
   • Read API documentation
   • Respect rate limits
   • Store API keys securely

❌ DON'T:
   • Ignore error responses
   • Make too many requests quickly
   • Share API keys publicly
   • Assume API is always available
""")

# ==================== COMMON STATUS CODES ====================
print("\n📊 COMMON HTTP STATUS CODES:")
print("-" * 30)
print("""
✅ SUCCESS:
   200 - OK (Request successful)
   201 - Created (New resource created)
   
⚠️ CLIENT ERRORS:
   400 - Bad Request (Invalid request)
   401 - Unauthorized (Need authentication)
   404 - Not Found (Resource doesn't exist)
   
❌ SERVER ERRORS:
   500 - Internal Server Error (Server problem)
   503 - Service Unavailable (Server overloaded)
""")

# ==================== FOR ML APPLICATIONS ====================
print("\n🤖 APIs FOR MACHINE LEARNING:")
print("-" * 30)
print("""
📊 DATA COLLECTION:
   • Weather data for predictions
   • Stock prices for financial models
   • Social media data for sentiment analysis
   • News articles for NLP tasks

🚀 MODEL DEPLOYMENT:
   • Deploy your ML model as API
   • Other apps can use your predictions
   • Real-time predictions via HTTP requests

🔗 POPULAR APIs FOR ML:
   • Twitter API (text data)
   • Alpha Vantage (financial data) 
   • News API (articles)
   • REST Countries (country data)
""")

print("\n✅ API Tutorial Complete!")
print("🎯 Now you understand how programs talk to each other!")