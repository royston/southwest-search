class Flight:
    def __init__(self, origin, destination, month, fare, currency, fare_type, date):
        self.origin = origin
        self.destination = destination
        self.month = month
        self.fare = fare
        self.currency = currency
        self.fare_type = fare_type
        self.date = date

    def __str__(self):
        return self.origin + self.destination + self.month + self.fare + self.currency + self.fare_type + self.date

