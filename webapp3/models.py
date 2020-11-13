from django.db import models
from django.db.models import F
from datetime import datetime

class company(models.Model):
    name=models.CharField(max_length=15, unique=True)
    gst=models.CharField(max_length=15)
def __str__(self):
    return self.name

class product(models.Model):
     productname= models.CharField(max_length=15, unique=True)
     companies = models.ForeignKey('company', on_delete=models.CASCADE,default=True)
     cost= models.IntegerField(default=10,blank=True)

def __str__(self): 
    return self.productname

class order(models.Model):
   
    companies = models.ForeignKey('company', on_delete=models.CASCADE,default=True)
    productname=  models.ForeignKey('Product', on_delete=models.CASCADE,default=True)
    cost= models.IntegerField(default=10,blank=True)
    quantity= models.IntegerField(default=1)
    totalprice=models.IntegerField(default=10, blank=True)
    order_no =models.IntegerField(default=1)
    purchased_ON=models.DateField(null=True)   
    purchase_details=models.CharField(blank=True,max_length=50)
       
    
    def calculate_price(self):
        totalprice=self.cost*self.quantity
        return totalprice
        

            
    def calculate_order(self):
        cur_y = date.today().year
        
        y=self.purchased_ON.year
        z=int(y)
        if cur_y != z:
           b=order.objects.filter('purchased_on=z').last()
           self.order_no=self.order_no+1
           return self.order_no 

        aws=order.objects.order_by('purchase_details').last()
        if aws is None:
           return 1
        else:
             a= aws.purchase_details.split('/')[-1]
             self.order_no=int(a)
             self.order_no=self.order_no + 1
             return self.order_no   
               
       
       

    def generate_transaction_number(self):
        purchase_details=f"{self.purchased_ON}/{int(self.order_no)}"
        return purchase_details
    
    def save(self,*args,**kwargs):
        self.totalprice = str(self.calculate_price())
        self.order_no = str(self.calculate_order())
        self.purchase_details = str(self.generate_transaction_number())
        super().save(*args, **kwargs)
     
           
         
            
            
                
        
  


    

def __str__(self):
    return self.purchase_details
