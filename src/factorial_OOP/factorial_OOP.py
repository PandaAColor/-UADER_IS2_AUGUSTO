import sys

class factorial_OOP:

    def __init__(self, min, max):
        self.min = int(min)
        self.max = int(max)

    def run(self):
        def factorial(num): 
            if num < 0: 
                print("Factorial de un número negativo no existe")
                return 0
            elif num == 0: 
                return 1
                
            else: 
                fact = 1
                while(num > 1): 
                    fact *= num 
                    num -= 1
                return fact 
        min = self.min
        max = self.max
        if min >max:
            a = max
            max = min
            min = a

        for i in range(min, max+1): #imprime el factorial desde el min hasta el max incluido
            print("Factorial ",i,"! es ", factorial(i))
        
