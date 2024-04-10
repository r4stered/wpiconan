cmake_minimum_required(VERSION 3.15)
project(test_package LANGUAGES CXX)

find_package(wpiutil CONFIG REQUIRED)
find_package(ntcore CONFIG REQUIRED)
find_package(opencv CONFIG REQUIRED)
find_package(cscore CONFIG REQUIRED)
find_package(cameraserver CONFIG REQUIRED)

add_executable(${PROJECT_NAME} test_package.cpp)
target_link_libraries(
    ${PROJECT_NAME}
    wpiutil::wpiutil
    ntcore::ntcore
    opencv::opencv
    cscore::cscore
    cameraserver::cameraserver
)
