// ----------------------------------------------------------------------------
// -                        Open3D: www.open3d.org                            -
// ----------------------------------------------------------------------------
// The MIT License (MIT)
//
// Copyright (c) 2018 www.open3d.org
//
// Permission is hereby granted, free of charge, to any person obtaining a copy
// of this software and associated documentation files (the "Software"), to deal
// in the Software without restriction, including without limitation the rights
// to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
// copies of the Software, and to permit persons to whom the Software is
// furnished to do so, subject to the following conditions:
//
// The above copyright notice and this permission notice shall be included in
// all copies or substantial portions of the Software.
//
// THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
// IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
// FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
// AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
// LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
// FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
// IN THE SOFTWARE.
// ----------------------------------------------------------------------------
// examples/Cpp/solution.cpp


#include <iostream>
#include <fstream>
#include "Open3D/Open3D.h"

int main(int argc, char const *argv[])
{
    using namespace open3d;
    geometry::TriangleMesh mesh;
    std::string ply_file,result_loc;

    if (argc <=2 || argc > 3){
        ply_file = "../../../examples/TestData/test_mesh.ply";
        result_loc = "../../../examples/TestData/results.txt";
    }
    else{
        ply_file = argv[1];
        result_loc = argv[2];
    }
    
    io::ReadTriangleMesh(ply_file,mesh);
    std::vector<std::vector<int>> result = mesh.IdenticallyColoredConnectedComponents();
    std::ofstream result_file;
    result_file.open(result_loc);
    for (size_t i = 0 ; i < result.size() ; i++){
    for (size_t j = 0 ; j < result[i].size(); j++)
        result_file << result[i][j] << " ";
    result_file << std::endl ;
    }
    result_file.close();
    return 0;
}
