class cat:
   def __init__(self,name, age):
      self.name = name
      self.age = age

   def info(self):
         print(f"I am a cat. my name is {self.name}.I am {self.age} years old.")

   def make_sound(self):
            print("Meow")


class Dog:
   def __init__(self,name, age):
      self.name = name
      self.age = age

   def info(self):
         print(f"I am a dog. my name is {self.name}.I am {self.age} years old.")

   def make_sound(self):
            print("bark")
cat1=cat("cecillia", 5)
dog1=Dog("bingo", 7)
for animal in (cat1, dog1):
     animal.make_sound()
     animal.info()