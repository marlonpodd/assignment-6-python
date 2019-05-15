itt = int(input( "Type in number of itterations: "))+1

sign = (-1)

answer = 0

for loop in range( 1, itt, 1):
	sign = sign * (-1)
	answer = answer+4/(loop*2-1)*sign


print(answer)