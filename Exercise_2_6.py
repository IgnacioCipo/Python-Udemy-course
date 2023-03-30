# Exercise 2.5 from python OOP Udemy course

class Fraction():
    def __init__(self, nr, dr=1):
        self._nr = nr
        self._dr = dr
        if self._dr < 0:
            self._dr *= -1
            self._nr *= -1
    
    def show(self):
        print(self._nr, "/", self._dr)

fraction1 = Fraction(2, -3)
fraction1.show()