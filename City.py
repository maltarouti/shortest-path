
class City:
    def __init__(self,
                 city_name: str,
                 cost: float,
                 previous_city=None):
        self.city_name = city_name
        self.cost = cost
        self.previous_city = previous_city
