import requests
from datetime import datetime
import smtplib
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

print("🛰️ ISS OVERHEAD NOTIFIER PROJECT")
print("="*50)

# YOUR COORDINATES (Change these to your actual location)
MY_LAT = 28.6139   
MY_LONG = 77.2090  

# EMAIL CONFIGURATION (You need to setup your email)
MY_EMAIL = "your_email@gmail.com" 
MY_PASSWORD = "your_app_password" 
TO_EMAIL = "recipient@gmail.com"  

print(f"📍 Monitoring location: Latitude {MY_LAT}, Longitude {MY_LONG}")
print(f"📧 Email notifications: {MY_EMAIL} → {TO_EMAIL}")

# STEP 1: CHECK ISS POSITION

def is_iss_overhead():
    """
    STEP 1: Check if ISS is overhead your location
    - Gets current ISS position from API
    - Compares with your coordinates
    - Returns True if ISS is within +5/-5 degrees
    """
    print("\n🛰️ Checking ISS position...")
    
    try:
        response = requests.get(url="http://api.open-notify.org/iss-now.json")
        response.raise_for_status()
        data = response.json()

        iss_latitude = float(data["iss_position"]["latitude"])
        iss_longitude = float(data["iss_position"]["longitude"])
        
        print(f"   ISS Current Position:")
        print(f"   📍 Latitude: {iss_latitude}°")
        print(f"   📍 Longitude: {iss_longitude}°")
        print(f"   📍 Your Position: {MY_LAT}°, {MY_LONG}°")

       
        # ISS is overhead if it's within +5 or -5 degrees of your position
        lat_match = MY_LAT - 5 <= iss_latitude <= MY_LAT + 5
        long_match = MY_LONG - 5 <= iss_longitude <= MY_LONG + 5
        
        if lat_match and long_match:
            print("   ✅ ISS IS OVERHEAD! 🛰️")
            return True
        else:
            print("   ❌ ISS is not overhead")
            lat_diff = abs(iss_latitude - MY_LAT)
            long_diff = abs(iss_longitude - MY_LONG)
            print(f"   📏 Distance: {lat_diff:.1f}° lat, {long_diff:.1f}° long")
            return False
            
    except Exception as e:
        print(f"   ❌ Error checking ISS position: {e}")
        return False

# ==================== STEP 2: CHECK IF IT'S NIGHT ====================

def is_night():
    """
    STEP 2: Check if it's nighttime at your location
    - Gets sunrise/sunset times from API
    - Compares with current time
    - Returns True if it's currently night (ISS visible)
    """
    print("\n🌙 Checking if it's nighttime...")
    
    try:
        parameters = {
            "lat": MY_LAT,
            "lng": MY_LONG,
            "formatted": 0,
        }

        response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
        response.raise_for_status()
        data = response.json()
        
        # Parse sunrise and sunset times (UTC)
        sunrise_utc = data["results"]["sunrise"]
        sunset_utc = data["results"]["sunset"]
        
        # Convert to datetime objects
        sunrise_time = datetime.fromisoformat(sunrise_utc.replace('Z', '+00:00'))
        sunset_time = datetime.fromisoformat(sunset_utc.replace('Z', '+00:00'))
        
        # Get current UTC time
        current_utc = datetime.utcnow().replace(tzinfo=sunrise_time.tzinfo)
        
        print(f"   🌅 Sunrise (UTC): {sunrise_time.strftime('%H:%M:%S')}")
        print(f"   🌇 Sunset (UTC): {sunset_time.strftime('%H:%M:%S')}")
        print(f"   🕐 Current (UTC): {current_utc.strftime('%H:%M:%S')}")
        
        # Check if current time is after sunset OR before sunrise (nighttime)
        if current_utc < sunrise_time or current_utc > sunset_time:
            print("   ✅ IT'S NIGHTTIME! 🌙 (ISS will be visible)")
            return True
        else:
            print("   ❌ It's daytime ☀️ (ISS not visible)")
            return False
            
    except Exception as e:
        print(f"   ❌ Error checking time: {e}")
        return False

# ==================== STEP 3: SEND EMAIL NOTIFICATION ====================

def send_notification():
    """
    STEP 3: Send email notification
    - Creates email with ISS overhead alert
    - Sends to specified email address
    - Includes current time and location info
    """
    print("\n📧 Sending email notification...")
    
    try:
        # Create email message
        msg = MIMEMultipart()
        msg['From'] = MY_EMAIL
        msg['To'] = TO_EMAIL
        msg['Subject'] = "🛰️ ISS IS OVERHEAD! Look Up! 🌟"
        
        # Email body
        body = f"""
🛰️ INTERNATIONAL SPACE STATION ALERT! 🛰️

The ISS is currently overhead your location!

📍 Your Location: {MY_LAT}°, {MY_LONG}°
🕐 Current Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
🌙 It's nighttime - ISS is visible!

👀 GO OUTSIDE AND LOOK UP AT THE SKY! 👀

The ISS appears as a bright moving star and is visible for a few minutes.
It's the third brightest object in the sky after the Sun and Moon!

🚀 This message was sent automatically by your ISS Tracker.

Happy stargazing! ✨
        """
        
        msg.attach(MIMEText(body, 'plain'))
        
        # Send email (Gmail SMTP)
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(MY_EMAIL, MY_PASSWORD)
            server.send_message(msg)
        
        print("   ✅ Email notification sent successfully! 📧")
        return True
        
    except Exception as e:
        print(f"   ❌ Error sending email: {e}")
        print("   💡 Note: You need to configure email settings to send notifications")
        return False

# ==================== STEP 4: MAIN MONITORING LOGIC ====================

def check_iss_and_notify():
    """
    STEP 4: Main logic - Check ISS position and time, send notification if both conditions met
    """
    print(f"\n🔄 ISS Check at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("-" * 50)
    
    # Check both conditions
    iss_overhead = is_iss_overhead()
    night_time = is_night()
    
    print(f"\n📊 CONDITIONS CHECK:")
    print(f"   🛰️ ISS Overhead: {'✅ YES' if iss_overhead else '❌ NO'}")
    print(f"   🌙 Nighttime: {'✅ YES' if night_time else '❌ NO'}")
    
    # If both conditions are true, send notification
    if iss_overhead and night_time:
        print(f"\n🎉 PERFECT CONDITIONS! Sending notification...")
        send_notification()
        return True
    else:
        print(f"\n⏳ Conditions not met. Will check again in 60 seconds...")
        return False

# ==================== STEP 5: CONTINUOUS MONITORING ====================

def start_monitoring():
    """
    STEP 5: Start continuous monitoring every 60 seconds
    """
    print("\n🚀 Starting ISS monitoring...")
    print("Press Ctrl+C to stop monitoring")
    print("="*50)
    
    notification_sent = False
    check_count = 0
    
    try:
        while True:
            check_count += 1
            print(f"\n📡 Check #{check_count}")
            
            # Check ISS and send notification if needed
            if check_iss_and_notify():
                notification_sent = True
                print(f"\n🎯 Notification sent! Pausing for 1 hour to avoid spam...")
                time.sleep(3600)  # Wait 1 hour before checking again
                notification_sent = False
            
            print(f"\n⏰ Waiting 60 seconds before next check...")
            time.sleep(60)  # Check every 60 seconds
            
    except KeyboardInterrupt:
        print(f"\n\n🛑 Monitoring stopped by user")
        print(f"📊 Total checks performed: {check_count}")
        print("👋 Thank you for using ISS Overhead Notifier!")

# ==================== DEMO MODE ====================

def demo_mode():
    """
    Demo mode - Just check once without continuous monitoring
    """
    print("\n🧪 DEMO MODE - Single Check")
    print("="*30)
    check_iss_and_notify()

# ==================== MAIN PROGRAM ====================

def main():
    """
    Main program with user options
    """
    print("\nISS OVERHEAD NOTIFIER")
    
    print("1. Start Continuous Monitoring")
    print("2. Single Check (Demo)")
    print("3. Test Email Configuration")
    print("4. Exit")
    
    while True:
        choice = input("\nChoose option (1-4): ").strip()
        
        if choice == '1':
            start_monitoring()
            break
        elif choice == '2':
            demo_mode()
            break
        elif choice == '3':
            print("\n📧 Testing email configuration...")
            send_notification()
            break
        elif choice == '4':
            print(" Goodbye!")
            break
        else:
            print(" Invalid choice! Please enter 1-4.")

# ==================== SETUP INSTRUCTIONS ====================

print("\n SETUP INSTRUCTIONS:")
print("1. Update YOUR coordinates (MY_LAT, MY_LONG)")
print("2. Configure email settings if you want notifications")
print("3. For Gmail, use App Password instead of regular password")
print("4. Run the program and choose monitoring option")

if __name__ == "__main__":
    main()

# ==================== PROJECT SUMMARY ====================
print("""
🛰️ ISS OVERHEAD NOTIFIER PROJECT

PURPOSE:
- Track the International Space Station (ISS) in real-time
- Notify you when ISS is visible from your location
- Automatically check every 60 seconds
- Send email alerts when conditions are perfect

HOW IT WORKS:
1. 📡 Gets ISS position from API
2. 🌙 Checks if it's nighttime (ISS visible)
3. 📍 Compares ISS location with yours
4. 📧 Sends notification if ISS is overhead at night
5. ⏰ Repeats every 60 seconds

TECHNOLOGIES USED:
✅ REST API calls (requests)
✅ JSON data parsing
✅ Date/time operations
✅ Email sending (SMTP)
✅ Error handling
✅ Continuous monitoring loops
✅ Geographic calculations

REAL-WORLD APPLICATION:
- Space enthusiasts can spot ISS easily
- Educational tool for astronomy
- Automated monitoring system
- Email notification system
""")



