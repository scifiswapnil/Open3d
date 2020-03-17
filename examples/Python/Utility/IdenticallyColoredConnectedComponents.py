import open3d as open3d
import numpy as np
mesh = open3d.io.read_triangle_mesh("../../TestData/test_mesh.ply")
mesh.compute_adjacency_list()

print("number of vertices : " + str(len(np.asarray(mesh.vertices))))
print("lenght of adjacency list : " + str(len(mesh.adjacency_list[:])))
V = [0] * len(np.asarray(mesh.vertices)) 
array_size = len(np.asarray(mesh.vertices))


def DFSUtil(temp, v, visited,color): 
	visited[v] = 1
	temp.append(v)
	connected_elements = mesh.adjacency_list[v]
	for j in range(0, len(connected_elements)):
		if (visited[list(connected_elements)[j]] == 0 and mesh.vertex_colors[list(connected_elements)[j]].all() == color.all() ):	
			temp = DFSUtil(temp, list(connected_elements)[j], visited,mesh.vertex_colors[list(connected_elements)[j]]) 
	return temp 

def connectedComponents(): 
	visited = [] 
	result = []
	for i in range(0,len(V)): 
		visited.append(0) 
	for v in range(0,len(V)): 
		if visited[v] == 0: 
			temp = [] 
			result.append(DFSUtil(temp, v, visited, mesh.vertex_colors[v])) 
	return result

print connectedComponents()
