cmake_minimum_required(VERSION 3.15)
project(test_package LANGUAGES CXX)

find_package(wpiutil CONFIG REQUIRED)
find_package(wpimath CONFIG REQUIRED)
find_package(apriltaglib CONFIG REQUIRED)
find_package(apriltag CONFIG REQUIRED)

add_executable(${PROJECT_NAME} test_package.cpp)
target_link_libraries(${PROJECT_NAME} wpiutil::wpiutil wpimath::wpimath apriltaglib::apriltaglib apriltag::apriltag)