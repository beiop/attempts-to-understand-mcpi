# attempts-to-understand-mcpi

Time to prove whether or not average joe can mod mcpi

if you can read this, i have succeded in linking vs to github

minecraft.h is meant for the compiler. I would recommend learning the syntax for the symbol definition files and reading them.

## - TheBrokenRail

### Ok, so how to run it

(this will download all mods, compile them for your last run version of mcpi, and move all of them to the mods directory.)

```sh
# remove any old version
rm attempts-to-understand-mcpi -r -f

# download it
git clone https://github.com/beiop/attempts-to-understand-mcpi

# make it able to do things
chmod +x attempts-to-understand-mcpi/build.sh

# do the things!
attempts-to-understand-mcpi/build.sh

```
