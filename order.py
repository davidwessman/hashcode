class Order:
	def __init__(self, l1, l2, l3):
		l = l1.split(" ");
		self.x = int(l[0])
		self.y = int(l[1])
		self.L = int(l2)
		self.prod = []
		l = l3.split(" ")
		for i in l:
			self.prod.append(int(i))
