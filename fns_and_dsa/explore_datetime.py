from datetime import datetime, timedelta

def display_current_datetime():
    """
    Displays the current date and time in 'YYYY-MM-DD HH:MM:SS' format.
    
    Returns:
        datetime: The current date and time
    """
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_date}")
    return current_date

def calculate_future_date(days):
    """
    Calculates the date after adding the specified number of days to the current date.
    
    Args:
        days (int): Number of days to add
    
    Returns:
        datetime: The future date
    """
    current_date = datetime.now()
    future_date = current_date + timedelta(days=days)
    formatted_future_date = future_date.strftime("%Y-%m-%d")
    print(f"Future date after {days} days: {formatted_future_date}")
    return future_date

def main():
    # Display current date and time
    current_date = display_current_datetime()
    
    # Prompt for number of days and validate input
    try:
        days = input("Enter the number of days to add to the current date: ").strip()
        days = int(days)
        if days < 0:
            print("Please enter a non-negative number of days.")
            return
        # Calculate and display future date
        future_date = calculate_future_date(days)
    except ValueError:
        print("Invalid input. Please enter a valid integer for the number of days.")

if __name__ == "__main__":
    main()