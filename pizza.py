class Pizza():
    def __init__(self,name,price):
        self.name = name
        self.price = price
        print "Pizza created: {} (${})".format(self.name, self.price)

    def make(self, quantity = 1):
        print "Made {} {} pizza(s)".format(quantity, self.name)

    def eat(self, quantity = 1):
        print "Ate {} {} pizza(s)".format(quantity, self.name)

pizza_01 = Pizza("artichoke", 15)
pizza_01.make()
pizza_01.eat()


pizza_02 = Pizza("margherita",12)
pizza_02.make(2)
pizza_02.eat()

#https://www.digitalocean.com/community/tutorials/how-to-use-logging-in-python-3

# above code has an init method that define the name and price of an object of the pizza class
# has two methods - make, eat. these two methods take in the quantity parameter, that is set at 1

