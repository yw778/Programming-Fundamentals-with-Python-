class Parent():
	def __init__(self, last_name, eye_color):
		print("Parent Constructor Called")
		self.last_name = last_name
		self.eye_color = eye_color
	def show_info(self):
		print(self.last_name + " " + self.eye_color)

class Child(Parent):
	def __init__(self, last_name, eye_color, num_of_toyes):
		print("Child Constructor Called")
		Parent.__init__(self, last_name, eye_color)		
		self.num_of_toyes = num_of_toyes
	def show_info(self):
		print(self.last_name + " " + self.eye_color + " " + str(self.num_of_toyes))

# parent = Parent("yu", "blue")
# print(parent.last_name) 
# parent.show_info()
child = Child("yu", "blue", 5)
# print(child.last_name) 
# print(child.num_of_toyes) 
child.show_info()