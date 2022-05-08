from xml.etree.ElementTree import C14NWriterTarget


class complex:
    def __init__(self,real,imag):
        self.real=real
        self.imag=imag
    def show(self):
        print("the real part is {} and imag part is{}".format(self.real,self.imag))
    def __add__ (self,other):
        real=self.real+other.real
        imag=self.imag+other.imag
        return complex(real,imag)
    
c1=complex(3,4)
c2=complex(6,7)
c3=c1+c2
c1.show()
c2.show()
c3.show()