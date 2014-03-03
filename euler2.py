#Text of challenge: "Each new term in the Fibonacci sequence is generated by adding
#the previous two terms. By starting with 1 and 2, the first 10 terms will be:
#1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
#By considering the terms in the Fibonacci sequence whose values do not exceed four
#million,find the sum of the even-valued terms."


number = 1
last = 0
before_last = 0
answer = 0

while number < 4000000:
	before_last = last
	last = number
	number = before_last + last
	
	if number % 2 == 0:
		answer += number
		
print answer
