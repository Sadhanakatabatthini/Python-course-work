from abc import ABC, abstractmethod

class payment(ABC):
    def source(self):
        print("Scanner/upiid/Mobile Number")
    def amount(self):
        print("Enter the amount")
    def bank(self):
        print("Select the bank")    
    def pin(self):
        print("Select the pin")
        
    @abstractmethod    
    def paymentprocess(self):
        pass
    def paymentstatus(self):
        print("Payment is Success/Fail")  
        
class HDFC(payment):
    def paymentprocess(self):
        print("Payment is processed from HDFC bank")
        
class ICICI(payment):
    def paymentprocess(self):
            print("Payment is processed from ICIC bank")    
            
class SBI(payment):
    def paymentprocess(self):
            print("Payment is processed from SBI bank")  
            
class Canara(payment):
    def paymentprocess(self):
            print("Payment is processed from Canara bank")                            
         
                  
harsha = HDFC() 
harsha.source()   
harsha.amount()           
harsha.bank()       
harsha.pin()       
harsha.paymentprocess()       
harsha.paymentstatus() 
print()      
                
Lohitha = ICICI() 
Lohitha.source()   
Lohitha.amount()           
Lohitha.bank()       
Lohitha.pin()       
Lohitha.paymentprocess()       
Lohitha.paymentstatus()
print()   

Jenni = SBI()    
Jenni.source()   
Jenni.amount()           
Jenni.bank()       
Jenni.pin()       
Jenni.paymentprocess()       
Jenni.paymentstatus() 
print()         

Karthik = SBI()    
Karthik.source()   
Karthik.amount()           
Karthik.bank()       
Karthik.pin()       
Karthik.paymentprocess()       
Karthik.paymentstatus() 
print()