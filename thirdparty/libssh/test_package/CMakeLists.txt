cmake_minimum_required(VERSION 3.15)
project(test_package LANGUAGES CXX)

find_package(Threads REQUIRED)
find_package(libssh CONFIG REQUIRED)

add_executable(${PROJECT_NAME} test_package.cpp)

if(WIN32)
    target_link_libraries(${PROJECT_NAME} wldap32 ws2_32 Crypt32.lib Wldap32)
endif()

target_link_libraries(
    ${PROJECT_NAME}
    Threads::Threads
    libssh::libssh
    ${CMAKE_DL_LIBS}
)
