'''
Infix to postfix
'''

class Stack:
	def __init__(self):
		self.items = []
	def push(self, val):
		self.items.append(val)
	def pop(self):
		try:
			return self.items.pop()
		except IndexError:
			print("Stack is empty")
	def top(self):
		try:
			return self.items[-1]
		except IndexError:
			print("Stack is empty")
	def __len__(self):
		return len(self.items)
	def isEmpty(self):
		return self.__len__() == 0
	
def infix_to_postfix(infix):
	opstack = Stack()
	outstack = []
	token_list = infix.split()
		
		# 연산자의 우선순위 설정
	prec = {}
	prec['('] = 0
	prec['+'] = 3
	prec['-'] = 3
	prec['*'] = 2
	prec['/'] = 2
	prec['^'] = 1

	for token in token_list:
		if token == '(':# ( 괄호를 선두에 삽입.
			opstack.push(token)
		elif token == ')':
			while opstack.top() != '(':# opstack의 '(' 까지의 모든 연산자를 pop한다. ')'는 넣지 않음.
				outstack.append(opstack.pop())
			opstack.pop() # '('도 pop한다.
		elif token in '+-/*^': # opstack에 token보다 우선순위 높거나 같은 괄호를 제외한 연산자가 있다? -> 높거나 같은 우선순위가 없을 때 까지 pop하고 삽입.
			if len(opstack) != 0:
				while (len(opstack)!=0)and(opstack.top()in '+-/*^')and(prec.get(opstack.top()) <= prec.get(token)):
					outstack.append(opstack.pop())
			opstack.push(token)
		else: # operand일 때 그냥 push 
			outstack.append(token)
	while not opstack.isEmpty(): # opstack 에 남은 모든 연산자를 pop, outstack에 append
		outstack.append(opstack.pop())
	return " ".join(outstack)


infix_expr = input()
postfix_expr = infix_to_postfix(infix_expr)
print(postfix_expr)