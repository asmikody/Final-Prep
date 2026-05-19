class Parent:
    @staticmethod
    def show():
        print("Static method in Parent")

class Child(Parent):
    @staticmethod
    def show():
        print("Static method in Child")

# Method hiding example
print("Calling via class:")
Parent.show()  # Calls Parent's method
Child.show()   # Calls Child's method

# Casting and runtime behavior
print("\nCalling via instance:")
parent_obj = Parent()
child_obj = Child()

parent_obj.show()  # Calls Parent's method
child_obj.show()   # Calls Child's method

# Upcasting (Casting Child to Parent type)
print("\nUpcasting Child to Parent:")
upcasted_obj = child_obj  # Still treated as Child
upcasted_obj.show()  # Calls Child's method (static method does not follow polymorphism)
