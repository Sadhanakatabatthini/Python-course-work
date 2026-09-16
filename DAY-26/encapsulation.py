'''
Public attritube - 
private attribute - add double underscore infront of the variable
protected attribute - single underscore 


class Instagram:
    def __init__(self,name,password):
        self.name = name #public
        self.__password = password #private
        self._post = []          #protected
        print(f'Welcome to Instagram , {self.name}')

    def getpassword(self):
        return self.__password

    @property
    def accesspoint(self):
        return self._post
    
sadhana = Instagram('sadhana','12345')
print(sadhana.name)
print(sadhana.getpassword())
print(sadhana.accesspoint)

'''
class Instagram:
    def __init__(self,name,password):
        self.name = name #public
        self.__password = password #private
        self._post = []          #protected

    def getpassword(self):
        return self.__password

    def setpassword(self,newpassword):
        self.__password = newpassword

    @property
    def accesspost(self):
        return self._post

    @accesspost.setter
    def accesspost(self,newpost):
        self._post.append(newpost)
    
sadhana = Instagram('sadhana','12345')
print(sadhana.name)
print(sadhana.getpassword())
print(sadhana.accesspost)

sadhana.name = "sadhana_123"
print(sadhana.name)

sadhana.setpassword("sadha@123")
print(sadhana.getpassword())


