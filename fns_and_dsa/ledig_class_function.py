trade_volume = int(input("Enter the trade volume: "))
if trade_volume < 30000:  # Less than $30,000 in trade volume
    print("Trade volume is low, please contact support at hello@ledig.io for assistance.")

else:
    print("Trade volume is sufficient, please visit  www.ledig.io to request a business account.")     

class ledig:
    def __init__(self, trade_volume):
        self.trade_volume = trade_volume

    def check_trade_volume(self):
        if self.trade_volume < 30000:  # Less than $30,000 in trade volume
            return "Trade commission would be charged at a rate lower than 0.3%."
        else:
            return "Trade commission would be charged at a rate of 0.2%."
    try:
        trade_volume = int(input("Enter the trade volume: "))
        ledig_instance = ledig(trade_volume)
        print(ledig_instance.check_trade_volume())
    except ValueError:
        print("Invalid input. Please enter a valid integer for trade volume.")
        print("An error occurred while processing the trade volume.")
        print("Please ensure you enter a numeric value.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}") 
    finally:
        print("Thank you for using the ledig trade volume checker.")    