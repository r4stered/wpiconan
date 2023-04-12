cmake_minimum_required(VERSION 3.15)
project(test_exec CXX)

find_package(wpiutil CONFIG REQUIRED)
find_package(wpinet CONFIG REQUIRED)

add_executable(test_exec src/test.cpp)
target_link_libraries(test_exec wpinet::wpinet wpiutil::wpiutil)