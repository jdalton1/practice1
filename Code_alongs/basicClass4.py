class Person:
    def __init__(self, full_name):
        self.full_name = full_name
        self.restaurants = []

    def add_restaruants(self, restaurant):
        self.restaurants.append(restaurant)

    def get_restaurants(self):
        return self.restaurants

    def get_favorite_restaurant(self):
        best = -1
        favorite = Restaurant("", "", "$", -1)
        for r in self.restaurants:
            break





class Restaurant:

    def __init__(self, name="", cuisine="", price="", rating=-1):
        self.name = name
        self.cuisine = cuisine
        self.price = price
        self.rating = rating

    def __str__(self):
        return self.name

