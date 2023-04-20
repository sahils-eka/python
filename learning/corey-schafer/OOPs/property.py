class Celsius(object):
    def __init__(self,val=0):
        self.temperature = val

    @property
    def temperature(self):
        print("Getting value...")
        return self.temp

    @temperature.setter
    def temperature(self,value):
        print("Setting value...")
        self.temp = value
    
    def to_fahr(self):
        return (self.temperature * 1.8) + 32
    
human1 = Celsius(37)

print(human1.temperature)
##(Above) the getter function will be called

# Now let's change the value
human1.temperature = 35

## (Above) The temperature setter function will be called.

print(human1.temperature)

##Now here, the getter is used to get the value and then the optns are done on it.
## Notice the 'Getting value...' string in the output
print(human1.to_fahr())