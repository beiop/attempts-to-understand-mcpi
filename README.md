# beiop/attempts-to-understand-mcpi

Time to prove whether or not average joe can mod mcpi

if you can read this, i have succeded in linking vs to github

## What even

`doubleStoneSlab` adds the block to the game and makes it craftable

`edibleStoneSlab` adds the block to the game and makes it craftable

> I realise this is kinda redundant, but also cool formatting!

## Ok, so how to run it

this will download all mods, compile them for your last run version of mcpi, and move all of them to the mods directory.

do note that this probably will not work untill you install all the prerequisits that I will not tell you about because I don't even know them myself.

``` bash
# remove any old version
rm attempts-to-understand-mcpi -r -f

# download it
git clone https://github.com/beiop/attempts-to-understand-mcpi

# make it able to do things
chmod +x attempts-to-understand-mcpi/build.sh

# do the things!
attempts-to-understand-mcpi/build.sh

```
