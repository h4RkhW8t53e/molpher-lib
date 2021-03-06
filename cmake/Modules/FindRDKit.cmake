# FindRDKit.cmake
# Placed in the public domain by NextMove Software in 2013
# Try to find RDKit headers and libraries
# Defines:
#
#  RDKIT_FOUND - system has RDKit
#  RDKIT_INCLUDE_DIR - the RDKit include directory
#  RDKIT_LIBRARIES - Link these to use RDKit
#
# References:
#
#  https://raw.githubusercontent.com/jandom/shape-it-rdkit/master/cmake/modules/FindRdkit.cmake
#  http://nextmovesoftware.com/blog/2013/02/04/looking-for-a-c-cheminformatics-toolkit/
#  https://github.com/timvdm/MolDB/blob/master/cmake/modules/FindRDKit.cmake

if(RDKIT_INCLUDE_DIR AND RDKIT_LIBRARIES)
    # in cache already or user-specified
    set(RDKIT_FOUND TRUE)

else()

    set(LIB_SUFFIX "")
    if(RDKIT_LINK_STATIC)
        set(LIB_SUFFIX "_static")
    endif()

    if(NOT RDKIT_INCLUDE_DIR)
        if(WIN32)
            find_path(RDKIT_INCLUDE_DIR GraphMol/RDKitBase.h
                    PATHS
                    ${RDBASE}\\Code
                    $ENV{RDKIT_INCLUDE_DIR}
                    $ENV{RDKIT_INCLUDE_PATH}
                    $ENV{RDKIT_BASE}\\Code
                    $ENV{RDBASE}\\Code
                    C:\\RDKit\\include
                    C:\\RDKit\\Code
                    )
        else()
            find_path(RDKIT_INCLUDE_DIR GraphMol/RDKitBase.h
                    PATHS
                    ${RDBASE}/Code
                    $ENV{RDKIT_INCLUDE_DIR}
                    $ENV{RDKIT_INCLUDE_PATH}
                    $ENV{RDKIT_BASE}/Code
                    $ENV{RDBASE}/Code
                    /usr/local/rdkit/include/Code
                    /usr/local/rdkit/include
                    /usr/local/rdkit/Code
                    ~/rdkit/Code
                    ${CMAKE_PREFIX_PATH}/include/rdkit
                    )
        endif()
        if(RDKIT_INCLUDE_DIR)
            message(STATUS "Found RDKit include files at ${RDKIT_INCLUDE_DIR}")
        endif()
    endif()

    if(NOT RDKIT_LIBRARIES)
        find_library(GRAPHMOL_LIB NAMES "RDKitGraphMol${LIB_SUFFIX}"
                PATHS
                ${RDBASE}/lib
                $ENV{RDKIT_LIB_DIR}
                $ENV{RDKIT_LIB_PATH}
                $ENV{RDKIT_LIBRARIES}
                $ENV{RDKIT_BASE}/lib
                $ENV{RDBASE}/lib
                /usr/local/rdkit/lib
                ~/rdkit/lib
                $ENV{LD_LIBRARY_PATH}
                ${CMAKE_PREFIX_PATH}/lib/
                )
        if(GRAPHMOL_LIB)
            GET_FILENAME_COMPONENT(RDKIT_LIBRARY_DIR ${GRAPHMOL_LIB} PATH)
            message(STATUS "Found RDKit libraries at ${RDKIT_LIBRARY_DIR}")
            unset(GRAPHMOL_LIB CACHE)

            foreach(name ${RDKit_FIND_COMPONENTS})
                find_library(${name}_LIB NAMES "${name}${LIB_SUFFIX}"
                        HINTS ${RDKIT_LIBRARY_DIR})
                set(RDKIT_LIBRARIES ${RDKIT_LIBRARIES} ${${name}_LIB})
            endforeach()
            message(STATUS "RDKit libraries found: ${RDKIT_LIBRARIES}")

        endif()
    endif()

    if(RDKIT_INCLUDE_DIR AND RDKIT_LIBRARIES)
        set(RDKIT_FOUND TRUE)
    endif()

    mark_as_advanced(RDKIT_INCLUDE_DIR RDKIT_LIBRARIES)

    unset(LIB_SUFFIX)
endif()