#day21_Challenge

class Queue:
	def __init__(self):
		self.a1 = []
		self.a2 = []

	def enQueue(self, x):
		
		while len(self.a1) != 0:
			self.a2.append(self.a1[-1])
			self.a1.pop()

		self.a1.append(x)

		while len(self.a2) != 0:
			self.a1.append(self.a2[-1])
			self.a2.pop()

	# Dequeue an item from the queue
	def deQueue(self):
		
			# if first stack is empty
		if len(self.a1) == 0:
			print("Q is Empty")

		x = self.a1[-1]
		self.a1.pop()
		return x

if __name__ == '__main__':
	q = Queue()
	q.enQueue(10)
	q.enQueue(11)
	q.enQueue(12)

	print(q.deQueue())
	print(q.deQueue())
	print(q.deQueue())
