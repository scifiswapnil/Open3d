import open3d as open3d
import numpy as np
mesh = open3d.io.read_triangle_mesh("/home/scifiswapnil/Downloads/homework-task/test_mesh.ply")
mesh.compute_adjacency_list()

print("number of vertices : " + str(len(np.asarray(mesh.vertices))))
print("lenght of adjacency list : " + str(len(mesh.adjacency_list[:])))
V = [0] * len(np.asarray(mesh.vertices)) 
array_size = len(np.asarray(mesh.vertices))

def check_color(i):
	if (mesh.vertex_colors[i] == np.array([1,0,0])).all():
		return "Red"
	if (mesh.vertex_colors[i] == np.array([0,1,0])).all():
		return "Green"
	if (mesh.vertex_colors[i] == np.array([0,0,1])).all():
		return "Blue"

def DFSUtil(temp, v, visited,color): 
	visited[v] = 1
	temp.append(v)
	connected_elements = mesh.adjacency_list[v]
	for j in range(0, len(connected_elements)):
		if (visited[list(connected_elements)[j]] == 0 and check_color(list(connected_elements)[j]) == color ):	
			temp = DFSUtil(temp, list(connected_elements)[j], visited,check_color(list(connected_elements)[j])) 
	return temp 

def connectedComponents(): 
	visited = [] 
	result = []
	for i in range(0,len(V)): 
		visited.append(0) 
	for v in range(0,len(V)): 
		if visited[v] == 0: 
			temp = [] 
			result.append(DFSUtil(temp, v, visited,check_color(v))) 
	return result

print connectedComponents()
