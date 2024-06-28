#include <libreborn/libreborn.h>
#include <symbols/minecraft.h>

#include <mods/feature/feature.h>
#include <mods/init/init.h>
#include <mods/misc/misc.h>
#include <mods/bucket/bucket.h>

static Tile *edibleStoneSlab = nullptr;

#define edibleStoneSlab_LEN 0.0F
#define blockId 106
#353

// Description
static std::string edibleStoneSlab_getDescriptionId(__attribute__((unused)) Tile *tile) {
    return "tile.edibleStoneSlab";
}

// Textures
static int edibleStoneSlab_getTexture2(__attribute__((unused)) Tile *tile, int face, __attribute__((unused)) int data) {
    if (face == 1) {
        // Top texture
        return 6;
    } else if (face == 0) {
        // Bottom texture
        return 6;
    }
    // Side texture
    return 5;
}

static int edibleStoneSlab_getTexture3(__attribute__((unused)) Tile *tile, LevelSource *level, int x, int y, int z, int face) {
    // Eaten face
    if (face == 3) {
        int data = level->getData(x, y, z);
        if (data != 0 && data < 6) {
            // Sliced texture
            return 123 + 32 + 16;
        }
    }
    // Normal
    return edibleStoneSlab_getTexture2(tile, face, 0);
}

// Rendering
static bool edibleStoneSlab_isSolidRender(__attribute__((unused)) Tile *tile) {
    // Stop it from turning other blocks invisable
    return 0;
}

static int edibleStoneSlab_getRenderLayer(__attribute__((unused)) Tile *tile) {
    // Stop weird transparency issues
    return 1;
}

static bool edibleStoneSlab_isCubeShaped(__attribute__((unused)) Tile *tile) {
    return false;
}

// Size
static void edibleStoneSlab_updateDefaultShape(Tile *tile) {
    // Set the default shape
    tile->setShape(
        edibleStoneSlab_LEN,       0.0, edibleStoneSlab_LEN,
        1.0 - edibleStoneSlab_LEN, 0.5, 1.0 - edibleStoneSlab_LEN
    );
}

static AABB *edibleStoneSlab_getAABB(Tile *tile, Level *level, int x, int y, int z) {
    // Get the size of the slices
    int data = level->getData(x, y, z);
    if (data >= 6) data = 0;
    float slice_size = (1.0 / 7.0) * (float) data;

    // Corner 1
    AABB *aabb = &tile->aabb;
    aabb->x1 = (float) x + edibleStoneSlab_LEN;
    aabb->y1 = (float) y;
    aabb->z1 = (float) z + edibleStoneSlab_LEN;

    // Corner 2
    aabb->x2 = (float) x + (1.0 - edibleStoneSlab_LEN);
    aabb->y2 = (float) y + 0.5;
    aabb->z2 = (float) z + (1.0 - edibleStoneSlab_LEN) - slice_size;

    return aabb;
}

static void edibleStoneSlab_updateShape(Tile *tile, LevelSource *level, int x, int y, int z) {
    // Set edibleStoneSlab
    int data = level->getData(x, y, z);
    if (data >= 6) data = 0;
    // Get slice amount
    float slice_size = (1.0 / 7.0) * (float) data;
    tile->setShape(
        edibleStoneSlab_LEN,       0.0, edibleStoneSlab_LEN,
        1.0 - edibleStoneSlab_LEN, 0.5, (1.0 - edibleStoneSlab_LEN) - slice_size
    );
}

// Eating
static int edibleStoneSlab_use(__attribute__((unused)) Tile *tile, Level *level, int x, int y, int z, Player *player) {
    // Eat
    player->foodData.eat(3);
    // Set the new tile
    int data = level->getData(x, y, z);
    if (data >= 5) {
        // Remove the edibleStoneSlab, it has been completely gobbled up
        level->setTileAndData(x, y, z, 0, 0);
    } else {
        // Remove a slice
        level->setTileAndData(x, y, z, blockId, data + 1);
    }
    return 1;
}

// Makes the edibleStoneSlabs
static void make_edibleStoneSlab() {
    // Construct
    edibleStoneSlab = new Tile;
    ALLOC_CHECK(edibleStoneSlab);
    int texture = 122;
    edibleStoneSlab->constructor(blockId, texture, Material::dirt);
    edibleStoneSlab->texture = texture;

    // Set VTable
    edibleStoneSlab->vtable = dup_Tile_vtable(Tile_vtable_base);
    ALLOC_CHECK(edibleStoneSlab->vtable);

    // Set shape
    edibleStoneSlab->setShape(
        edibleStoneSlab_LEN,       0.0, edibleStoneSlab_LEN,
        1.0 - edibleStoneSlab_LEN, 0.5, 1.0 - edibleStoneSlab_LEN
    );

    // Modify functions
    edibleStoneSlab->vtable->getDescriptionId = edibleStoneSlab_getDescriptionId;
    edibleStoneSlab->vtable->getTexture3 = edibleStoneSlab_getTexture3;
    edibleStoneSlab->vtable->getTexture2 = edibleStoneSlab_getTexture2;
    edibleStoneSlab->vtable->isSolidRender = edibleStoneSlab_isSolidRender;
    edibleStoneSlab->vtable->getRenderLayer = edibleStoneSlab_getRenderLayer;
    edibleStoneSlab->vtable->isCubeShaped = edibleStoneSlab_isCubeShaped;
    edibleStoneSlab->vtable->updateShape = edibleStoneSlab_updateShape;
    edibleStoneSlab->vtable->updateDefaultShape = edibleStoneSlab_updateDefaultShape;
    edibleStoneSlab->vtable->getAABB = edibleStoneSlab_getAABB;
    edibleStoneSlab->vtable->use = edibleStoneSlab_use;

    // Init
    edibleStoneSlab->init();
    edibleStoneSlab->setDestroyTime(1.0f);
    edibleStoneSlab->setExplodeable(20.0f);
    edibleStoneSlab->category = 4;
    std::string name = "edibleStoneSlab";
    edibleStoneSlab->setDescriptionId(&name);
}

static void Tile_initTiles_injection() {
    make_edibleStoneSlab();
}

// Add edibleStoneSlab to creative inventory
static void Inventory_setupDefault_FillingContainer_addItem_call_injection(FillingContainer *filling_container) {
    ItemInstance *edibleStoneSlab_instance = new ItemInstance;
    ALLOC_CHECK(edibleStoneSlab_instance);
    edibleStoneSlab_instance->count = 255;
    edibleStoneSlab_instance->auxiliary = 0;
    edibleStoneSlab_instance->id = blockId;
    filling_container->addItem(edibleStoneSlab_instance);
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
    // edibleStoneSlab
    ItemInstance edibleStoneSlab_item = {
        .count = 1,
        .id = blockId,
        .auxiliary = 0
    };
    // Add
    std::string line1 = "mmm";
    std::string line2 = "ses";
    std::string line3 = "www";
    std::vector<Recipes_Type> ingredients = {milk, sugar, wheat, eggs};
    recipes->addShapedRecipe_3(&edibleStoneSlab_item, &line1, &line2, &line3, &ingredients);
}
__attribute__((constructor)) static void init_edibleStoneSlab() {
    // Add edibleStoneSlab
    misc_run_on_tiles_setup(Tile_initTiles_injection);
    misc_run_on_creative_inventory_setup(Inventory_setupDefault_FillingContainer_addItem_call_injection);
}
