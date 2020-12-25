<<<<<<< HEAD
def bouncingDiagonals(matrix):
	mapping = {}
	n = len(matrix)
	for i in range(0, n):
		mapping[matrix[i][0]] = 0;
	for i in range(0, n):
		x = i
		y = 0
		for j in range(i,0,-1):
			# print("J is", j)
			# print("X is", x)
			# print("Y is", y)
			mapping[matrix[i][0]]+= matrix[x][y]
			x -= 1
			y += 1
		for j in range(i,n):
			# print("J is", j)
			# print("X is", x)
			# print("Y is", y)
			mapping[matrix[i][0]]+= matrix[x][y]
			x += 1
			y += 1
	sorted_keys = sorted(mapping)
	mapping2 = {}
	for key in sorted_keys:
		mapping2[key] = mapping[key]
	sorted_mapping = sorted((value, key) for (key,value) in mapping2.items())
	result = []
	for i in range(0, n):
		result.append(sorted_mapping[i][1])
	print (result)
X = [[2,3,2], 
     [0,2,5], 
     [1,0,1]]
=======
def bouncingDiagonals(matrix):
	mapping = {}
	n = len(matrix)
	for i in range(0, n):
		mapping[matrix[i][0]] = 0;
	for i in range(0, n):
		x = i
		y = 0
		for j in range(i,0,-1):
			# print("J is", j)
			# print("X is", x)
			# print("Y is", y)
			mapping[matrix[i][0]]+= matrix[x][y]
			x -= 1
			y += 1
		for j in range(i,n):
			# print("J is", j)
			# print("X is", x)
			# print("Y is", y)
			mapping[matrix[i][0]]+= matrix[x][y]
			x += 1
			y += 1
	sorted_keys = sorted(mapping)
	mapping2 = {}
	for key in sorted_keys:
		mapping2[key] = mapping[key]
	sorted_mapping = sorted((value, key) for (key,value) in mapping2.items())
	result = []
	for i in range(0, n):
		result.append(sorted_mapping[i][1])
	print (result)
X = [[2,3,2], 
     [0,2,5], 
     [1,0,1]]
>>>>>>> 6a511d70a9044aa21ff457120200837581634c3b
bouncingDiagonals(X)