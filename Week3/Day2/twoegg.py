import math
def minAttempts(eggs,floors):
	num1 = floors * 2
	num2 = math.sqrt((1^2) + (4*1*num1))
	num3 = (-1 + num2)/2
	num4 = (-1 - num2)/2
    
	return math.ceil(max(num3,num4))
floors = 100
eggs = 2
print(minAttempts(eggs,floors))
