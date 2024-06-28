cmake_minimum_required(VERSION 3.16.0)

# Build For ARM
set(CMAKE_C_COMPILER arm-linux-gnueabihf-gcc)
set(CMAKE_CXX_COMPILER arm-linux-gnueabihf-g++)
set(CMAKE_SYSTEM_NAME "Linux")
set(CMAKE_SYSTEM_PROCESSOR "arm")

# Start Project
project(doubleStoneSlab)

# Include SDK
include("$ENV{HOME}/.minecraft-pi/sdk/lib/minecraft-pi-reborn/sdk/sdk.cmake")

# Build
add_library(doubleStoneSlab SHARED doubleStoneSlab.cpp)
target_link_libraries(doubleStoneSlab mods reborn-patch symbols)
