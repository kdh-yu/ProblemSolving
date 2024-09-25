# Weave a linked list
import sys
class Node:
	def __init__(self, e, n=None):
		self.val = e
		self.next = n

class LinkedList:
	def __init__(self, l=[]):
		if not l:
			self.head = None
			self.size = 0
		else:
			self.head = Node(l[0])
			self.size = len(l)
			curr = self.head
			for x in l[1:]:
				curr.next = Node(x)
				curr = curr.next

	def __len__(self):
		return self.size

	def is_empty(self):
		return self.size == 0

	def append(self, d):
		end = Node(d)
		if not self.head:
			self.head = end
			return
		curr = self.head
		while curr.next:
			curr = curr.next
		curr.next = end

	def print(self, n=sys.maxsize):
		cnt = 0
		curr = self.head
		out = ""
		while curr and cnt < n:
			out += str(curr.val) + "->"
			curr = curr.next
			cnt += 1
		if out is not None:
			out = out[:-2]
		print(out)

def weave(head: Node) -> Node:
	p1 = head
	p2 = head
	while p2.next.next is not None:
		p1 = p1.next
		p2 = p2.next.next
	p2 = p1.next
	p1 = head
	while p2.next is not None:
		tmp = p2.next
		p2.next = p1.next
		p1.next = p2
		p1 = p2.next
		p2 = tmp
	p1.next = p2

if __name__ == '__main__':
	if len(sys.argv) > 1:
		l = LinkedList(sys.argv[1:])
		weave(l.head)
		l.print()
	else:
		nums = list(input().split())
		# nums = ['a1', 'a2' , 'b1', 'b2']
		l = LinkedList(nums)
		# l.print()
		weave(l.head)
		l.print()
