cmake_minimum_required(VERSION 3.15)
project(test_exec CXX)

find_package(wpilibnewcommands CONFIG REQUIRED)

if(MSVC)
    add_compile_options("/Zc:preprocessor")
endif()

add_executable(test_exec src/test.cpp)
target_link_libraries(test_exec wpilibnewcommands::wpilibnewcommands)