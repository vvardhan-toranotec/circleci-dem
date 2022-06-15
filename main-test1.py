# Import the Add function, and assert that it works correctly.
from main import Multiplication

def TestMultiplication():
        assert Multiplication(5,5) == 25
        print("Multiplication Function works correctly")

if __name__ == '__main__':
        TestMultiplication()