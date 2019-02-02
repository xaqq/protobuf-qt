cmake_minimum_required(VERSION 3.7)
project(protobufqt)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup(TARGETS)



set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++17")

# Compiler plugin

set(COMPILER_SRCS
        compiler/insertion_point_writer.cpp
        compiler/main.cpp
        compiler/protobuf_qt_generator.cpp
        )

add_executable(protoc-gen-qt ${COMPILER_SRCS})
target_link_libraries(protoc-gen-qt PUBLIC CONAN_PKG::protobuf)

install(TARGETS protoc-gen-qt  RUNTIME DESTINATION bin)
