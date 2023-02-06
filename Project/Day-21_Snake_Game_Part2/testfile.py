class Dog:
    def __init__(self):
        self.temp = "angry"


class Lambrador(Dog):
    def __init__(self):
        super().__init__()
        # self.temp = "ramah"


molly = Lambrador()
print(molly.temp)
