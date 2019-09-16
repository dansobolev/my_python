class Automobile:

    def __init__(self, client, mark, model, year):
        self.client = client
        self.mark = mark
        self.model = model
        self.year = year



    def price(self):
        if self.mark == "BMW" and self.model =="Cross":
            return f"{self.year * 0.25} USD"
        elif self.mark == "BMW" and self.model =="SUV":
            return self.year * 0.30
        elif self.mark == "Mercedes" and self.model =="Cross":
            return self.year * 0.35
        elif self.mark == "Mercedes" and self.model =="SUV":
            return self.year * 0.41
        elif self.mark == "Porshe" and self.model=="Sport":
            return self.year * 0.55
        elif self.mark == "Porshe" and self.model =="SUV":
            return self.year * 0.60


class Client:

    def __init__(self, name, number, adress):
        self.name = name
        self.number = number
        self.adress = adress

print(Automobile("Ivan", "Porshe", "Sport", 2019).price())