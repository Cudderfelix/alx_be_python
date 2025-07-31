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
        