cmake_minimum_required(VERSION 3.15)
project(test_exec CXX)

if(MSVC)
    add_compile_options("/Zc:preprocessor")
endif()

find_package(pathplanner CONFIG REQUIRED)

add_executable(test_exec src/test.cpp)
target_link_libraries(test_exec pathplanner::pathplanner)