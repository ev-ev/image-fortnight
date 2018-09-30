
class Image:
    def __init__(self,real_part,imag_part):
        self.rp=real_part
        self.ip=imag_part 
    def __str__(self):
        if self.ip == 0:
            return str(self.rp)
        elif self.rp == 0:
            return str(self.ip)+'i'
        elif self.ip>0:
            if self.ip == 1:
                return str(self.rp) + '+' + 'i'
            else:
                return str(self.rp) + '+' + str(self.ip) + 'i'
        else:
            if self.ip == -1:
                return str(self.rp) + '-' + 'i'
            else:
                return str(self.rp) + '-' + str(-self.ip) + 'i'
     
    #ADDITION BLOCK
    def __add__(self,other):
        #print('Add')
        #print('Other:',other)
        #print('Self: ',self)
        if isinstance(other, Image):
            return Image(self.rp+other.rp,self.ip+other.ip)
        else:
            return Image(self.rp+other,self.ip)
    def __radd__(self,other):
        #print('Radd')
        #print('Other:',other)
        #print('Self: ',self)
        if isinstance(other, Image):
            return Image(self.rp+other.rp,self.ip+other.ip)
        else:
            return Image(self.rp+other,self.ip)
    def __iadd__(self,other):
        #print('iAdd')
        #print('Other:',other)
        #print('Self: ',self)
        if isinstance(other, Image):
            return Image(self.rp+other.rp,self.ip+other.ip)
        else:
            return Image(self.rp+other,self.ip)
    #ADDITION BLOCK END
    
    #SUBTRACTION BLOCK
    def __sub__(self,other):
        if isinstance(other, Image):
            return Image(self.rp-other.rp,self.ip-other.ip)
        else:
            return Image(self.rp-other,self.ip)
            
    def __rsub__(self,other):
        if isinstance(other, Image): #will never happen
            print('wtf?')
        else:
            return Image(other-self.rp,-self.ip)
    def __isub__(self,other):
        if isinstance(other, Image):
            return Image(self.rp-other.rp,self.ip-other.ip)
        else:
            return Image(self.rp-other,self.ip)
    #SUBTRACTION BLOCK END
    
    #MULTIPLICATION BLOCK
    def __mul__(self,other):
        if isinstance(other, Image):
            return self.multiply(self,other)
        else:
            return Image(self.rp*other,self.ip*other)
            
    def __rmul__(self,other):
        if isinstance(other, Image): #will never happen
            print('wtf?')
        else:
            return Image(self.rp*other,self.ip*other)
    def __imul__(self,other):
        if isinstance(other, Image):
            return self.multiply(self,other)
        else:
            return Image(self.rp*other,self.ip*other)
    def multiply(self,i1,i2):
        x=i1.rp
        y=i1.ip
        a=i2.rp
        b=i2.ip
        rp=x*a-b*y
        ip=x*b+y*a
        return Image(rp,ip)
    #MULTIPLICATION BLOCK END
    
    #DIVISION BLOCK
    def __truediv__(self,other): #When the image is divided by something + Both are images
        if isinstance(other, Image):
            return self.divide_images(self,other)
        else:
            return self.divide_image_by_normal(self,other)
    def __rtruediv__(self,other): #When something is divided by the image
        if isinstance(other, Image):
            return self.divide_images(other,self)
        else:
            return self.divide_images(Image(other,0),self)
    def __itruediv__(self,other): #When the image is divided by sth + Both are images
        if isinstance(other, Image):
            return self.divide_images(self,other)
        else:
            return self.divide_image_by_normal(self,other)
    def divide_image_by_normal(self,i,n):
        rp=i.rp/n
        ip=i.ip/n
        return Image(rp,ip)
    def divide_images(self,i1,i2):
        x=i1.rp
        y=i1.ip
        a=i2.rp
        b=i2.ip
        denom=a**2+b**2
        num=Image(x*a+y*b,a*y-x*b)
        return self.divide_image_by_normal(num,denom)
    #DIVISION BLOCK END
    