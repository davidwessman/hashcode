class Order:
	def __init__(self, l1, l2, l3, P):
		l = l1.split(" ");
		self.r = int(l[0])
		self.c = int(l[1])
		self.L = int(l2)
		self.prod = [0] * P
		l = l3.split(" ")
		for i in l:
			self.prod[int(i)] += 1
