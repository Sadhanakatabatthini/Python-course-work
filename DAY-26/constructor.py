# Constructor - A constructor is a special method that is automatically called when an object is created. 
# It is mainly used to initialize the object's data.

class Instagram:
    def __init__(self,name,password):
        self.name = name
        self.password = password
        print(f'Welcome to Instagram , {self.name}')

sadhana = Instagram('Sadhana','12345')
