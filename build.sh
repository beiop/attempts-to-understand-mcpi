#!/bin/sh

#sudo apt install ninja-build  <-- dunno what this is, but maybe install it?


#set -e # Exit immediately if a command exits with a non-zero status.

# Create Output Directory
cd "$(dirname "$0")" #
ROOT="$(pwd)"           #I think this is the working folder??
#OUT="${ROOT}/out"
#rm -rf "${OUT}"
#mkdir -p "${OUT}"

# Build
build() {
    cd "${ROOT}/$1"
    # Build
    rm -rf build
    mkdir build
    cd build
    cmake -GNinja ..
    cmake --build .
    # Copy Result
    #cp lib*.so "${OUT}"
    #rm /home/$USER/.minecraft-pi/mods/lib*.so
    cp lib*.so /home/$USER/.minecraft-pi/mods -r
}
#build chat-commands
#build expanded-creative
#build recipes
build cake
build doubleStoneSlab
build edibleStoneSlab
