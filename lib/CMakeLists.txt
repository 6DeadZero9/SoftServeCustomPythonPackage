file(GLOB_RECURSE SOURCES *.c)

add_library(${CMAKE_PROJECT_NAME} SHARED ${SOURCES})

set_target_properties(${CMAKE_PROJECT_NAME} PROPERTIES LINKER_LANGUAGE C)

target_include_directories(${CMAKE_PROJECT_NAME} PUBLIC ${CMAKE_CURRENT_SOURCE_DIR}/inc)

target_link_libraries(${CMAKE_PROJECT_NAME} openssl::openssl)