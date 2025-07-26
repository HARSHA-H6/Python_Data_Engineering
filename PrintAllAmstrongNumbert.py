
# Create the class NumberMystery as mentioned in problem statement
class NumberMystery:
    """
    In this program we are print all 
    the amstrong numbers for 100 till 999
    """

    # Check if the given number is amstrong number or not 
    def is_amstrong(self, number:int)->bool:
        temp = number
        sum = 0
        while(temp!=0):
            d = temp%10
            sum += d**3
            temp //= 10

        return sum == number
    
    # Check what are the numbers for 100 to 999 are amstrong number
    def find_all(self):
        
        for i in range(100,999):

            if obj1.is_amstrong(i) == True:
                print(i)
            

# create the object to the class
obj1 = NumberMystery()
# call the function using the object
obj1.find_all()           


