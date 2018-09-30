
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
    