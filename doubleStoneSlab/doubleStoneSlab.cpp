#include <libreborn/libreborn.h>
#include <symbols/minecraft.h>

#include <mods/feature/feature.h>
#include <mods/init/init.h>
#include <mods/misc/misc.h>
#include <mods/bucket/bucket.h>

static Tile *doubleStoneSlab = nullptr;

#define doubleStoneSlab_LEN 0.0F

// Description
static std::string doubleStoneSlab_getDescriptionId(__attribute__((unused)) Tile *tile) {
    return "tile.doubleStoneSlab";
}

// Textures
static int doubleStoneSlab_getTexture2(__attribute__((unused)) Tile *tile, int face, __attribute__((unused)) int data) {
    if (face == 1) {
        // Top texture
        return 6;
    } 
    /*
    else if (face == 0) {
        // Bottom texture
        return 5;
    }
    */
    // Side texture
    return 6;
}
 /* 
static int doubleStoneSlab_getTexture3(__attribute__((unused)) Tile *tile, LevelSource *level, int x, int y, int z, int face) {
    // Eaten face
    if (face == 3) {
        int data = level->getData(x, y, z);
        if (data != 0 && data < 6) {
            // Sliced texture
            return 123 + 32 + 16;
        }
    }
    // Normal
    return doubleStoneSlab_getTexture2(tile, face, 0);
}
*/
// Rendering
static bool doubleStoneSlab_isSolidRender(__attribute__((unused)) Tile *tile) {
    // Stop it from turning other blocks invisable
    return 0;
}

static int doubleStoneSlab_getRenderLayer(__attribute__((unused)) Tile *tile) {
    // Stop weird transparency issues
    return 1;
}

static bool doubleStoneSlab_isCubeShaped(__attribute__((unused)) Tile *tile) {
    return false;
}

// Size
/*
static void doubleStoneSlab_updateDefaultShape(Tile *tile) {
    // Set the default shape
    tile->setShape(
        doubleStoneSlab_LEN,       0.0, doubleStoneSlab_LEN,
        1.0 - doubleStoneSlab_LEN, 0.5, 1.0 - doubleStoneSlab_LEN
    );
}
*/
/*
static AABB *doubleStoneSlab_getAABB(Tile *tile, Level *level, int x, int y, int z) {
    // Get the size of the slices
    int data = level->getData(x, y, z);
    if (data >= 6) data = 0;
    float slice_size = (1.0 / 7.0) * (float) data;

    // Corner 1
    AABB *aabb = &tile->aabb;
    aabb->x1 = (float) x + doubleStoneSlab_LEN;
    aabb->y1 = (float) y;
    aabb->z1 = (float) z + doubleStoneSlab_LEN;

    // Corner 2
    aabb->x2 = (float) x + (1.0 - doubleStoneSlab_LEN);
    aabb->y2 = (float) y + 0.5;
    aabb->z2 = (float) z + (1.0 - doubleStoneSlab_LEN) - slice_size;

    return aabb;
}

static void doubleStoneSlab_updateShape(Tile *tile, LevelSource *level, int x, int y, int z) {
    // Set doubleStoneSlab
    int data = level->getData(x, y, z);
    if (data >= 6) data = 0;
    // Get slice amount
    float slice_size = (1.0 / 7.0) * (float) data;
    tile->setShape(
        doubleStoneSlab_LEN,       0.0, doubleStoneSlab_LEN,
        1.0 - doubleStoneSlab_LEN, 0.5, (1.0 - doubleStoneSlab_LEN) - slice_size
    );
}

// Eating
static int doubleStoneSlab_use(__attribute__((unused)) Tile *tile, Level *level, int x, int y, int z, Player *player) {
    // Eat
    player->foodData.eat(3);
    // Set the new tile
    int data = level->getData(x, y, z);
    if (data >= 5) {
        // Remove the doubleStoneSlab, it has been completely gobbled up
        level->setTileAndData(x, y, z, 0, 0);
    } else {
        // Remove a slice
        level->setTileAndData(x, y, z, 104, data + 1);
    }
    return 1;
}
*/
// Makes the doubleStoneSlabs
static void make_doubleStoneSlab() {
    // Construct
    doubleStoneSlab = new Tile;
    ALLOC_CHECK(doubleStoneSlab);
    int texture = 122;
    doubleStoneSlab->constructor(104, texture, Material::dirt);
    doubleStoneSlab->texture = texture;

    // Set VTable
    doubleStoneSlab->vtable = dup_Tile_vtable(Tile_vtable_base);
    ALLOC_CHECK(doubleStoneSlab->vtable);

    // Set shape
    doubleStoneSlab->setShape(
        doubleStoneSlab_LEN,       0.0, doubleStoneSlab_LEN,
        1.0 - doubleStoneSlab_LEN, 1.0, 1.0 - doubleStoneSlab_LEN
    );

    // Modify functions
    doubleStoneSlab->vtable->getDescriptionId = doubleStoneSlab_getDescriptionId;
    //doubleStoneSlab->vtable->getTexture3 = doubleStoneSlab_getTexture3;
    doubleStoneSlab->vtable->getTexture2 = doubleStoneSlab_getTexture2;
    doubleStoneSlab->vtable->isSolidRender = doubleStoneSlab_isSolidRender;
    doubleStoneSlab->vtable->getRenderLayer = doubleStoneSlab_getRenderLayer;
    doubleStoneSlab->vtable->isCubeShaped = doubleStoneSlab_isCubeShaped;
    //doubleStoneSlab->vtable->updateShape = doubleStoneSlab_updateShape;
    //doubleStoneSlab->vtable->updateDefaultShape = doubleStoneSlab_updateDefaultShape;
    //doubleStoneSlab->vtable->getAABB = doubleStoneSlab_getAABB;
    //doubleStoneSlab->vtable->use = doubleStoneSlab_use;

    // Init
    doubleStoneSlab->init();
    doubleStoneSlab->setDestroyTime(1.0f);
    doubleStoneSlab->setExplodeable(20.0f);
    doubleStoneSlab->category = 4;
    std::string name = "doubleStoneSlab";
    doubleStoneSlab->setDescriptionId(&name);
}

static void Tile_initTiles_injection() {
    make_doubleStoneSlab();
}

// Add doubleStoneSlab to creative inventory
static void Inventory_setupDefault_FillingContainer_addItem_call_injection(FillingContainer *filling_container) {
    ItemInstance *doubleStoneSlab_instance = new ItemInstance;
    ALLOC_CHECK(doubleStoneSlab_instance);
    doubleStoneSlab_instance->count = 255;
    doubleStoneSlab_instance->auxiliary = 0;
    doubleStoneSlab_instance->id = 104;
    filling_container->addItem(doubleStoneSlab_instance);
}

// Recipe (only when buckets are enabled)
static void Recipes_injection(Recipes *recipes) {
    // Sugar
    Recipes_Type sugar = {
        .item = 0,
        .tile = 0,
        .instance = {
            .count = 1,
            .id = 353,
            .auxiliary = 0
        },
        .letter = 's'
    };
    // Wheat
    Recipes_Type wheat = {
        .item = 0,
        .tile = 0,
        .instance = {
            .count = 1,
            .id = 296,
            .auxiliary = 0
        },
        .letter = 'w'
    };
    // Eggs
    Recipes_Type eggs = {
        .item = 0,
        .tile = 0,
        .instance = {
            .count = 1,
            .id = 344,
            .auxiliary = 0
        },
        .letter = 'e'
    };
    // Milk
    Recipes_Type milk = {
        .item = 0,
        .tile = 0,
        .instance = {
            .count = 1,
            .id = 325,
            .auxiliary = 1
        },
        .letter = 'm'
    };
    // doubleStoneSlab
    ItemInstance doubleStoneSlab_item = {
        .count = 1,
        .id = 104,
        .auxiliary = 0
    };
    // Add
    std::string line1 = "mmm";
    std::string line2 = "ses";
    std::string line3 = "www";
    std::vector<Recipes_Type> ingredients = {milk, sugar, wheat, eggs};
    recipes->addShapedRecipe_3(&doubleStoneSlab_item, &line1, &line2, &line3, &ingredients);
}
__attribute__((constructor)) static void init_doubleStoneSlab() {
    // Add doubleStoneSlab
    misc_run_on_tiles_setup(Tile_initTiles_injection);
    misc_run_on_creative_inventory_setup(Inventory_setupDefault_FillingContainer_addItem_call_injection);
}
