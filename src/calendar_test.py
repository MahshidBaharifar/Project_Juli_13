import sys
import os

# Get the path to the 'src' directory
src_directory = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "src")

# Add 'src' directory to the Python path
sys.path.append(src_directory)

# Now you can import your classes from the 'src' directory
from my_calendar import Calendar
def main():
    # Step 1: Test Calendar functionality
    num_of_days = 30
    calendar = Calendar(num_of_days)

    all_booking_days = calendar.return_all_booking_days()
    available_date_range = calendar.return_available_date_range()

    print("All Booking Days:")
    print(all_booking_days)
    print("\nAvailable Date Range:")
    print("Check-in:", available_date_range[0])
    print("Check-out:", available_date_range[1])
    print("-----------------------------")


if __name__ == "__main__":
    main()