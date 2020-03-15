

class Converter:
    
    def __init__(self):
        _dict = dict()
        _dict[(None, 'RUB')] = 1
        _dict[(None, 'GBP')] = 1
        _dict[(None, 'EUR')] = 1
        _dict[(None, 'USD')] = 1
        _dict[(None, 'JPY')] = 1
        _dict[('RUB', 'RUB')] = 1
        _dict[('GBP', 'GBP')] = 1
        _dict[('EUR', 'EUR')] = 1
        _dict[('USD', 'USD')] = 1
        _dict[('JPY', 'JPY')] = 1
        _dict[('GBP', 'RUB')] = 89.4576
        _dict[('EUR', 'RUB')] = 77.3875
        _dict[('USD', 'RUB')] = 68.5630
        _dict[('JPY', 'RUB')] = 0.6506
        _dict[('RUB', 'GBP')] = 1 / _dict[('GBP', 'RUB')]
        _dict[('RUB', 'EUR')] = 1 / _dict[('EUR', 'RUB')]
        _dict[('RUB', 'USD')] = 1 / _dict[('USD', 'RUB')]
        _dict[('RUB', 'JPY')] = 1 / _dict[('JPY', 'RUB')]
        _dict[('EUR', 'USD')] = 1.1309
        _dict[('EUR', 'GBP')] = 0.8685
        _dict[('EUR', 'JPY')] = 118.9050
        _dict[('USD', 'EUR')] = 1 / _dict[('EUR', 'USD')]
        _dict[('GBP', 'EUR')] = 1 / _dict[('EUR', 'GBP')]
        _dict[('JPY', 'EUR')] = 1 / _dict[('EUR', 'JPY')]
        _dict[('USD', 'GBP')] = 0.7664
        _dict[('USD', 'JPY')] = 105.3800
        _dict[('GBP', 'USD')] = 1 / _dict[('USD', 'GBP')]
        _dict[('JPY', 'USD')] = 1/ _dict[('USD', 'JPY')]
        _dict[('GBP', 'JPY')] = 137.4946
        _dict[('JPY', 'GBP')] = 1 / _dict[('GBP', 'JPY')]
        self._dict = _dict

    def convert(self, from_, to_):
        return self._dict[(from_, to_)]
    
    def __repr__(self):
        return self._dict.__repr__()


class Money:
    
    def _switcher(self, argument):
        currencies = {"RUB" : "₽", "USD" : "$", "EUR" : "€", "GBP" : "£", "JPY" : "¥"}
        return currencies[argument]
    
    def __init__(self, converter, amount, currency = None):
        self.converter = converter
        self.amount = amount
        self.currency = currency
        self.valuta = ''
        if (currency != None):
            if (self._switcher(currency) == None):
                raise Exception("Unknown currency!")
            self.valuta = self._switcher(currency)
            
    def _convert(self, from_, to_):
        return self.converter.convert(from_, to_)
    
    def __add__(self, other):
        if ((type(other) == float or type(other) == int) and self.currency != None):
            return Money(self.converter, self.amount + other, self.currency)
        if (self.currency == None and other.currency == None or (type(other) == float or type(other) == int) and self.currency == None):
            raise Exception("Both operands have no currency defined")
        if (self.currency == None):
            first = other
            second = self
        else:
            first = self
            second = other
        result_amount = first.amount + first._convert(second.currency, first.currency) * second.amount
        result_currency = first.currency
        return Money(first.converter, result_amount, result_currency)
        
    def __str__(self):
        return str(self.amount) + self.valuta
    
    def __repr__(self):
        return str(self)



def main(): 
    converter = Converter()
    dollars = Money(converter, 5, "USD")
    euro = Money(converter, 8, "EUR")
    money = Money(converter, 1)
    print(dollars + euro)
    print(dollars + money)
    print(euro + 19)
    try:
        print(money + money)
    except Exception:
        print("Something's wrong")


        
if __name__ == "__main__":
    main()