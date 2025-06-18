cmake_minimum_required(VERSION 3.30)

project(SoftServeExampleCBinding C)

set(CMAKE_C_STANDARD 11)

find_package(OpenSSL REQUIRED)

add_subdirectory(lib)