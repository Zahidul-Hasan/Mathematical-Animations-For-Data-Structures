



def Strlen(s):
	if s == "":
		return 0
	else:
		return 1 + Strlen(s[1:])


def Fibonacci(n):
	if n == 0 or n == 1:
		return 1
	else:
		return Fibonacci(n-1) + Fibonacci(n-2)

s = "abcdefg"

#print(Strlen(s))
print(Fibonacci(5))



