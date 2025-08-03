class BankAccount:
    def __init__(self, initial_balance=0):
        """
        Initialize a BankAccount with an optional initial balance.
        
        Args:
            initial_balance (float): Starting balance, defaults to 0
        """
        self._account_balance = float(initial_balance) if initial_balance >= 0 else 0
    
    def deposit(self, amount):
        """
        Deposit a positive amount to the account balance.
        
        Args:
            amount (float): Amount to deposit
        """
        if isinstance(amount, (int, float)) and amount > 0:
            self._account_balance += amount
        else:
            print("Invalid deposit amount. Must be positive.")
    
    def withdraw(self, amount):
        """
        Withdraw an amount if sufficient funds are available.
        
        Args:
            amount (float): Amount to withdraw
            
        Returns:
            bool: True if withdrawal succeeds, False otherwise
        """
        if isinstance(amount, (int, float)) and amount > 0:
            if amount <= self._account_balance:
                self._account_balance -= amount
                return True
            else:
                return False
        else:
            print("Invalid withdrawal amount. Must be positive.")
            return False
    
    def display_balance(self):
        """
        Display the current account balance in a user-friendly format.
        """
        print(f"Current Balance: ${self._account_balance:.2f}")