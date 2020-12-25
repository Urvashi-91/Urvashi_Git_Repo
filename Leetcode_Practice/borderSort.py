<<<<<<< HEAD
def sort_layer(matrix,layer):
    border = []
    size = len(matrix) - layer -1
    for i in range(layer+1, size):
        border.append(matrix[i][layer])
        border.append(matrix[i][size])
        
    border.extend(matrix[layer][layer:size+1])
    border.extend(matrix[size][layer: size+1])
    border.sort()
    
    pointer = 0
    
    for i in range(layer, size+1):
        matrix[layer][i] = border[pointer]
        pointer+=1
      
    for i in range(layer+1, size):
        matrix[i][size] = border[pointer]
        pointer+=1
    
    for i in range(size, layer-1, -1):
        matrix[size][i] = border[pointer]
        pointer+=1
        
    for i in range(size-1, layer, -1):
        matrix[i][layer] = border[pointer]
        pointer+=1
        
def border_sort(matrix):
    for row in matrix:
        print(row)
        
    layers = len(matrix)//2
    for layer in range(layers):
        sort_layer(matrix,layer)
        
    print()
    print (matrix)
    
=======
def sort_layer(matrix,layer):
    border = []
    size = len(matrix) - layer -1
    for i in range(layer+1, size):
        border.append(matrix[i][layer])
        border.append(matrix[i][size])
        
    border.extend(matrix[layer][layer:size+1])
    border.extend(matrix[size][layer: size+1])
    border.sort()
    
    pointer = 0
    
    for i in range(layer, size+1):
        matrix[layer][i] = border[pointer]
        pointer+=1
      
    for i in range(layer+1, size):
        matrix[i][size] = border[pointer]
        pointer+=1
    
    for i in range(size, layer-1, -1):
        matrix[size][i] = border[pointer]
        pointer+=1
        
    for i in range(size-1, layer, -1):
        matrix[i][layer] = border[pointer]
        pointer+=1
        
def border_sort(matrix):
    for row in matrix:
        print(row)
        
    layers = len(matrix)//2
    for layer in range(layers):
        sort_layer(matrix,layer)
        
    print()
    print (matrix)
    
>>>>>>> 6a511d70a9044aa21ff457120200837581634c3b
    