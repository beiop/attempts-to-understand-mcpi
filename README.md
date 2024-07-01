# beiop/attempts-to-understand-mcpi

Time to prove whether or not average joe can mod mcpi

if you can read this, i have succeded in linking vs to github

## What even

* `doubleStoneSlab` & `edibleStoneSlab` adds the block to the game and makes it craftable. Neither work
* [cuboid](<python scripts/cuboid.py>) & [line](<python scripts/line.py>) take the position of the block below you, then after you press enter in the terminal, another posiiton of another block below you and make a ___ between them out of the first position's block type.

> I realise this is kinda redundant, but also cool formatting!

## Ok, so how to run it (mods, python is python)

this will download all mods, compile them for your last run version of mcpi, and move all of them to the mods directory. Probably needs re-run when mcpi updates.

this also only supports being run on arm. I haven't figured out how to do anything else yet...

``` bash
# install every dependency I can think of. I probably missed a few and have one unessisary one
sudo apt install git make cmake gcc-arm-linux-gnueabihf g++-arm-linux-gnueabihf ninja-build

# remove any old version
rm attempts-to-understand-mcpi -r -f

# download it
git clone https://github.com/beiop/attempts-to-understand-mcpi

# make it able to do things
chmod +x attempts-to-understand-mcpi/build.sh

# do the things!
attempts-to-understand-mcpi/build.sh

```

there's no spell check in this...
