cmake_minimum_required(VERSION 3.15)
project(test_package LANGUAGES CXX)

find_package(opencv CONFIG REQUIRED)
find_package(Threads REQUIRED)

add_executable(${PROJECT_NAME} test_package.cpp)
target_link_libraries(${PROJECT_NAME} Threads::Threads opencv::opencv ${CMAKE_DL_LIBS})