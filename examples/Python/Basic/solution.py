# Open3D: www.open3d.org
# The MIT License (MIT)
# See license file or visit www.open3d.org for details

# examples/Python/Basic/solution.py

import numpy as np
import os
import open3d as o3d
import sys

results_file = ""
ply_path = ""

if len(sys.argv) > 2 and len(sys.argv) < 4 :
    ply_path = sys.argv[1]
    results_file = sys.argv[2]
else :
    pwd = os.path.dirname(os.path.realpath(__file__))
    data_dir = os.path.join(pwd, os.pardir, os.pardir, os.pardir, "examples","TestData")
    ply_path = os.path.join(data_dir, "test_mesh.ply")
    results_file = os.path.join(data_dir, "results.txt")

mesh = o3d.io.read_triangle_mesh(ply_path)
resultFile = open(results_file, "w") 
result = np.array(mesh.identically_colored_connected_components())
for i in range(0,len(result)):
    resultFile.write(' '.join(map(str, result[i])))
    resultFile.write('\n')
resultFile.close()


