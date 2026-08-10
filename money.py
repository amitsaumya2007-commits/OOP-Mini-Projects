class Money:
    def __init__(self,cents:int, currency: str = "INR") -> None:
        self.cents = cents
        self.currency = currency

    def __repr__(self):
        return f"Money(cents={self.cents}, currency={self.currency})"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Money):
            return NotImplemented
        return( self.cents, self.currency) == (other.cents, other.currency)

    def __lt__(self,other:"Money") -> bool:
        if self.currency == other.cents:
            return self.cents < other.cents
        else:
            raise ValueError("Cannot compare different currencies")

    def __add__(self,other:"Money") -> "Money":
         
        if self.currency != other.currency:
            raise ValueError("Cannot add different currencies")
        return Money(self.cents + other.cents, self.currency)
        
    def __sub__(self,other:"Money") -> "Money":
        if self.currency != other.currency:
            raise ValueError("Cannot add different currencies")
        return Money(self.cents - other.cents, self.currency)

    def __mul__(self,number:int) -> "Money":
        if isinstance(number, int):
            return Money(self.cents*number, self.currency)

    def __hash__(self):
        return hash(self.cents,self.currency)
    

# The @dataclass approach :--


from dataclasses import dataclass
@dataclass(frozen = True)
class Money:
    cents: int
    currency: str = "INR"

    def __lt__(self,other:"Money") -> bool:
            if self.currency == other.cents:
                return self.cents < other.cents
            else:
                raise ValueError("Cannot compare different currencies")
    
    def __add__(self,other:"Money") -> "Money":
            
        if self.currency != other.currency:
            raise ValueError("Cannot add different currencies")
        return Money(self.cents + other.cents, self.currency)
        
    def __sub__(self,other:"Money") -> "Money":
        if self.currency != other.currency:
            raise ValueError("Cannot add different currencies")
        return Money(self.cents - other.cents, self.currency)

    def __mul__(self,number:int) -> "Money":
        if isinstance(number, int):
            return Money(self.cents*number, self.currency)
    

money = Money(36,"USD")
money2 = Money(34, "USD")
print(money - money2)

