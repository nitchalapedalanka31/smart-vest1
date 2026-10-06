
from datetime import datetime

def show_normal_status():
    print("\n--- SAFETY STATUS ---")
    print("Temperature: 36.8 C (simulated)")
    print("Movement: Normal (simulated)")
    print("GPS: Not connected")
    print("Status: SAFE")

def show_emergency_alert():
    print("\n--- EMERGENCY ALERT ---")
    print("Possible safety incident detected!")
    print("Time:", datetime.now().strftime("%d-%m-%Y %H:%M:%S"))
    print("Demo only: No real alert was sent.")

while True:
    print("\nSMART VEST SAFETY MONITORING")
    print("1. Normal Condition")
    print("2. Emergency Condition")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        show_normal_status()
    elif choice == "2":
        show_emergency_alert()
    elif choice == "3":
        print("System closed.")
        break
    else:
        print("Invalid choice.")