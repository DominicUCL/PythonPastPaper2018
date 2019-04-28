import pytest
from simplemaths.simplemaths import SimpleMaths as sm
import math

class TestSimpleMaths():
    #Test Constructor   
    def test_only_accept_right_values_in_constructor(self):
        with pytest.raises(TypeError):
            sm("i")
    
    def test_only_accept_positive_values_in_constructor(self):
        with pytest.raises(ValueError):
            sm(-5)    
    def test_correct_number_stored(self):
        assert sm(3).number==3
   
    def test_constructor_creates_object(self):
        a =sm(1)
        assert a
    
    def test_no_value(self):
        with pytest.raises(Exception) as error:
            sm() 
   
    #Test Sqaure Function   
    def test_square(self):
        a =sm(3)    
        assert a.square()== 3**2
    
    #Test Factorial
    def test_factorial(self):
        a =sm(3)    
        assert a.factorial()== 6

    
    #Test Power
    def test_power_default_value(self):
        a=sm(2)
        assert a.power()==8
    
    def test_power_different_value(self):
        a=sm(2)
        assert a.power(2)==4
        
    #Test odd_or_even
    def test_odd_values(self):
        a=sm(3)
        assert a.odd_or_even()=="Odd"
    def test_even_values(self):
        a=sm(2)
        assert a.odd_or_even()=="Even"
    def test_zero_value(self):
        a=sm(0)
        assert a.odd_or_even()=="Even"
        
    #Test square_root
    def test_compare_with_math(self):
        a=sm(10)
        assert a.square_root()==pytest.approx(math.sqrt(10))

        
