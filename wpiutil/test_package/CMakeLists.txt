cmake_minimum_required(VERSION 3.15)
project(WpiUtilTest CXX)

find_package(wpiutil CONFIG REQUIRED)

add_executable(wpiutiltest src/test.cpp)
target_link_libraries(wpiutiltest wpiutil::wpiutil)