import RandData
import time

#Bubble Sort
def Bubble_Sort(list):
	TL = len(list)-2
	for k in range(len(list)):
		for i in range(TL+1):
			j = i+1
			if list[i] >= list[j]:
				list[i], list[j] = list[j], list[i]
	return list

#Insert Sort
def Insert_Sort(list):
	for i in range(len(list)-1):
		for j in list[:i+1]:
			if list[i+1] <= j:
				list.insert(list.index(j), list.pop(i+1))
				break
	return list

#Shell Sort
def Shell_Sort(list):
	global i
	LN = len(list)/2
	while LN > 0:
		for i in range(LN, len(list)):
			while i >= LN:
				if list[i-LN] >= list[i]:
					list[i-LN], list[i] = list[i], list[i-LN]
				i -= LN
		LN = LN/2
	return list

#Merge Sort
def Merge_Sort(list):
	def DivideSort(list):
		if len(list) <= 1:
			return list
		num = len(list)/2
		Left = Merge_Sort(list[:num])
		Right = Merge_Sort(list[num:])
		return Merge(Left, Right)

	def Merge(Left, Right):
		NewSpace = []
		while len(Left) > 0 and len(Right) > 0:
			if Left[0] <= Right[0]:
				NewSpace.append(Left[0])
				Left.pop(0)
			elif Left[0] > Right[0]:
				NewSpace.append(Right[0])
				Right.pop(0)
		if len(Left) > 0:
			for i in Left:
				NewSpace.append(i)
		elif len(Right) > 0:
			for i in Right:
				NewSpace.append(i)
		return NewSpace

	return DivideSort(list)

#Heap Sort
def Heap_Sort(list):
	def Heap(list):
		if (len(list) - 1) % 2 == 0:
			num = len(list) / 2 - 1
			for i in range(num, -1, -1):
				if list[2 * i + 1] == min(list[i], list[2 * i + 1], list[2 * i + 2]):
					list[i], list[2 * i + 1] = list[2 * i + 1], list[i]
				elif list[2 * i + 2] == min(list[i], list[2 * i + 1], list[2 * i + 2]):
					list[i], list[2 * i + 2] = list[2 * i + 2], list[i]
				else:
					continue
		else:
			num = (len(list)-1) / 2
			for i in range(num, -1, -1):
				if i < num:
					if list[2 * i + 1] == min(list[i], list[2 * i + 1], list[2 * i + 2]):
						list[i], list[2 * i + 1] = list[2 * i + 1], list[i]
					elif list[2 * i + 2] == min(list[i], list[2 * i + 1], list[2 * i + 2]):
						list[i], list[2 * i + 2] = list[2 * i + 2], list[i]
					else:
						continue
				else:
					if list[i] <= list[2 * i + 1]:
						continue
					else:
						list[i], list[2 * i + 1] = list[2 * i + 1], list[i]
		return list

	def Sort(list):
		for i in range(len(list)-2):
			temp = Heap(list[i:])
			list[i:] = temp
		return list

	list = Heap(list)
	Sort(list)
	return list


TestList = [2, 3, 5, 8, 90, 4, 2, 5, 0]

print '/nStart generate randam data...'
list=RandData.randata()
print 'Data generation finished.'

a = list
print '/nStart internal sort...'
t1=time.clock()
a.sort()
t2=time.clock()
print 'Internal sort finisehd. Time used=%fs'%(t2-t1)
print a

a = list
print '/nStart bubble sort...'
t1=time.clock()
Bubble_Sort(a)
t2=time.clock()
print 'Bubble sort finished. Time used=%fs'%(t2-t1)
print a

a = list
print '/nStart insert sort...'
t1=time.clock()
Insert_Sort(a)
t2=time.clock()
print 'Insert sort finished. Time used=%fs'%(t2-t1)
print a

a = list
print '/nStart shell sort...'
t1=time.clock()
Shell_Sort(a)
t2=time.clock()
print 'Shell sort finished. Time used=%fs'%(t2-t1)
print a

a = list
print '/nStart merge sort with new space...'
t1=time.clock()
Merge_Sort(a)
t2=time.clock()
print 'Merge sort with new space finished. Time used=%fs'%(t2-t1)
print a

a = list
print '/nStart heap sort without new space...'
t1=time.clock()
Heap_Sort(a)
t2=time.clock()
print 'Merge sort without new space finished. Time used=%fs'%(t2-t1)
print a

#print Heap_Sort(RandData.randata())
