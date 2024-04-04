cmake_minimum_required(VERSION 3.15)
project(test_package LANGUAGES CXX)

find_package(googletest CONFIG REQUIRED)
find_package(Threads REQUIRED)

enable_testing()

add_executable(${PROJECT_NAME} test_package.cpp)
target_link_libraries(${PROJECT_NAME} Threads::Threads googletest::googletest ${CMAKE_DL_LIBS})

include(GoogleTest)
gtest_discover_tests(${PROJECT_NAME})