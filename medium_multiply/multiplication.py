import numpy as np
class Multiplication:
    """
    Instantiate a multiplicaton operation
    Numbers will multiplied by given multiplier
    
    :param multiplier: The multiplier.
    :type multiplier: int
    """
    
    def __init__(self, multiplier):
        self.multiplier = multiplier
        
    def multiply(self, number):
        """
        Multiply a given number by the multiplier.
        
        :param number: The number to multiply.
        :type number: int
    
        :return: The result of the multiplication.
        :rtype: int
        """
        return np.dot(number, self.multiplier)
    
# Instantiate a Multiplication object
multiplication = Multiplication(2)

# Call the multiply method
print(multiplication.multiply(5))