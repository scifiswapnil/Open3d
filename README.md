<p align="center">
<img src="docs/_static/open3d_logo_horizontal.png" width="320" />
</p>

# Open3D: A Modern Library for 3D Data Processing

<h4>
    <a href="http://www.open3d.org">open3d.org</a> |
    <a href="http://www.open3d.org/docs">Documentation</a> |
    <a href="http://www.open3d.org/docs/release/getting_started.html">Quick Start</a> |
    <a href="http://www.open3d.org/docs/release/compilation.html">Build from Source</a> |
    <a href="http://www.open3d.org/docs/release/index.html#python-api-index">Python API</a> |
    <a href="http://www.open3d.org/docs/release/cpp_api/index.html">C++ API</a> |
    <a href="http://www.open3d.org/docs/release/contribute.html">Contribute</a> |
    <a href="https://www.youtube.com/watch?v=I3UjXlA4IsU">Demo</a> |
    <a href="https://forum.open3d.org">Forum</a>
</h4>

Open3D is an open-source library that supports rapid development of software that deals with 3D data. The Open3D frontend exposes a set of carefully selected data structures and algorithms in both C++ and Python. The backend is highly optimized and is set up for parallelization. We welcome contributions from the open-source community.

---
## Home Work Assignments :
- C++ function open3d::geometry::TriangleMesh::IdenticallyColoredConnectedComponents :heavy_check_mark:
- Python binding foropen3d.geometry.TriangleMesh.identically_colored_connected_components :heavy_check_mark:
- "Open3D/examples/Cpp/solution.cpp" :heavy_check_mark:
- "Open3D/examples/Python/Basic/solution.py" :heavy_check_mark:
- "results.txt" shall be formatted the same way as specified in the "Example triangle mesh" section :heavy_check_mark:
- C++ and Python unit tests integrated with Open3D's unit test system :heavy_check_mark:
- Document your code, the algorithm used, how to build and run, and etc :heavy_check_mark:

---
## Build steps
- `git clone --recursive https://github.com/scifiswapnil/Open3d-homeWork Open3d`
- `cd Open3d`
- dependencies setup 
	- for ubuntu : ` .util/scripts/install-deps-ubuntu.sh`
	- for macOS  :  `util/scripts/install-deps-os` 
- `mkdir build && cd build`
- `cmake -DCMAKE_INSTALL_PREFIX=<open3d_install_directory> -DPYTHON_EXECUTABLE=<python_executable_directory> -DPYTHON_LIBRARIES=<python_library_directory> ..`
- make 
	- for ubuntu : `make-j$(nproc)`
	- for macOS : `make -j$(sysctl -n hw.physicalcpu)`
- `sudo make install`
- For python-pip package use `make install-pip-package`

---
## Function implementation, bindings and algorithm used 
- [C++ function defination ](https://github.com/scifiswapnil/Open3d-homeWork/blob/7424ba31e42c8119f54d2836f335c7cde1931a2c/src/Open3D/Geometry/TriangleMesh.h#L89)
- [C++ function implementation](https://github.com/scifiswapnil/Open3d-homeWork/blob/7424ba31e42c8119f54d2836f335c7cde1931a2c/src/Open3D/Geometry/TriangleMesh.cpp#L1231) 
- [Python binding](https://github.com/scifiswapnil/Open3d-homeWork/blob/7424ba31e42c8119f54d2836f335c7cde1931a2c/src/Python/open3d_pybind/geometry/trianglemesh.cpp#L163) 

#### Algorithm used : 
```
- getConnectComponentSearch()
	- read the mesh file
	- check the size and color of vertices in mesh file 
	- initialize an array 'visited' of size as same vertices in mesh file and set every element to false
	- traverse each element 'v' in the array and do :
		- if 'v' is not visited before, call DepthFirstSearchConnectedComponentSearch(v,vertex_color(v)) 
		- sort the results of DFSCCSearch(v,vertex_color(v)) and pushback to result
	- return result

- DFSCCSearch(v,vertex_color(v))
	- Mark 'v' as visited.
	- pusback element to queue
	- get the adjacent elements 
	- visit each adjacent elements and check the color as of root element
	- If adjacent elements is not visited, then recursively call DFSCCSearch(v,vertex_color(v))
```

---
## Example solution usage

- [solution.cpp](https://github.com/scifiswapnil/Open3d-homeWork/blob/master/examples/Cpp/solution.cpp)
	- Usage :
	```
		- cd  ~/Open3D/build/bin/examples
		- ./solution 
		or 
		- ./solution <input_mesh_file> <output_result_file>
	```
- [solution.py](https://github.com/scifiswapnil/Open3d-homeWork/blob/master/examples/Python/Basic/solution.py)
	- Usage :
	```
		- cd  ~/Open3D/examples/Python/Basic
		- python solution .py
		or 
		- python solution .py <input_mesh_file> <output_result_file>

#### Note : 
- If you directly run the executable without any arguments the code fetchs the [test_mesh.ply](https://github.com/scifiswapnil/Open3d-homeWork/blob/master/examples/TestData/test_mesh.ply) form `~/Open3d/examples/TestData` and writes the `results.txt` in the same directory.  
- C++ solution code is added to build system, after build use the above steps to run the solution code for cpp and python. 


---		
## Unit tests 

- [C++ unit tests](https://github.com/scifiswapnil/Open3d-homeWork/blob/7424ba31e42c8119f54d2836f335c7cde1931a2c/src/UnitTest/Geometry/TriangleMesh.cpp#L849)
	- unit tests are added to the build system and can be directly used once built
	- usage `./Open3d/build/bin/unitTests`

- [python unit tests](https://github.com/scifiswapnil/Open3d-homeWork/blob/master/src/UnitTest/Python/test_identicallyColoredConnectedComponents.py)
	- usage `pytest ~/Open3d/src/UnitTest/Python `

#### Note :
- C++ and python unit tests are added to the existing build system. 
- You need to set `BUILD_UNIT_TESTS` flag to true during the cmake for the build system to make the executables
---
## Citation
Please cite [our work](https://arxiv.org/abs/1801.09847) if you use Open3D.

```
@article{Zhou2018,
	author    = {Qian-Yi Zhou and Jaesik Park and Vladlen Koltun},
	title     = {{Open3D}: {A} Modern Library for {3D} Data Processing},
	journal   = {arXiv:1801.09847},
	year      = {2018},
}
```
