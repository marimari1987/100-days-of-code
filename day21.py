class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breath(self):
        print("Inhale, exhale")


class Fish(Animal):
    def __init__(self):
        super().__init__()  # class inheritance

    def swim(self):
        print("moving in water.")

    def breath(self):
        super().breath()  # alles was breath kann
        print("doing this underwater")  # und zusätzlich das hier


nemo = Fish()
nemo.swim()
nemo.breath()
print(nemo.num_eyes)