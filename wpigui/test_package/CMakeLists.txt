cmake_minimum_required(VERSION 3.15)
project(test_package LANGUAGES CXX)

find_package(imgui CONFIG REQUIRED)
find_package(wpigui CONFIG REQUIRED)

add_executable(${PROJECT_NAME} test_package.cpp)
target_link_libraries(${PROJECT_NAME} imgui::imgui wpigui::wpigui)
