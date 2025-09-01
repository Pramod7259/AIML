class Student :
    def __init__(self):
        self.name =" "
        self.regno =0
        self.age =0
        
    def set_values(self , n , r , a):
        self.name =n
        self.regno =r
        self.age =a    
   
    def display(self):
       print("The name , regno , age of the student is ")    
       print("Name :",self.name)
       print("RegNo :",self.regno)
       print("Age :",self.age)

Student s1= new Student( )
s1.set_values ("Pramod",123,19)
s1.display()