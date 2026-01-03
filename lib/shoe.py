#!/usr/bin/env python3

class Shoe:
    def __init__(self,brand,size):
        self.brand = brand
        self.size = size

    def cobble(self):
        self.condition = "New"
        print("Your shoe is as good as new!")

    
    @property
    def size(self):
        return self._size

    @size.setter
    def size(self,size):
        if isinstance(size, int):
            self._size = size
        else:
            print("size must be an integer")
    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, brand):
         self._brand = brand

stan_smith = Shoe("Adidas", 9)
stan_smith.brand = "Nike"
print(stan_smith.brand)

