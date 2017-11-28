class Cat:
    def __init__(self, name):
        self.name = name

    def meow(self):
        print(self.name + ' Meow!')

    def __str__(self):
        return 'Cat: ' + self.name

pusheen = Cat('Pusheen')
pusheen.meow()
print(pusheen)
