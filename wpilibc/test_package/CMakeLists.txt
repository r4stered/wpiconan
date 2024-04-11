cmake_minimum_required(VERSION 3.15)
project(test_package LANGUAGES CXX)

find_package(wpiutil CONFIG REQUIRED)
find_package(ntcore CONFIG REQUIRED)
find_package(opencv CONFIG REQUIRED)
find_package(cscore CONFIG REQUIRED)
find_package(cameraserver CONFIG REQUIRED)
find_package(wpilibc CONFIG REQUIRED)
find_package(hal CONFIG REQUIRED)
find_package(nilibraries CONFIG)

if(MSVC)
    add_compile_options(/Zc:preprocessor)
endif()

add_executable(${PROJECT_NAME} test_package.cpp)

if(${nilibraries_FOUND})
    target_link_libraries(${PROJECT_NAME} nilibraries::nilibraries)
endif()

target_link_libraries(
    ${PROJECT_NAME}
    wpiutil::wpiutil
    wpimath::wpimath
    hal::hal
    wpinet::wpinet
    ntcore::ntcore
    opencv::opencv
    cscore::cscore
    cameraserver::cameraserver
    wpilibc::wpilibc
)
