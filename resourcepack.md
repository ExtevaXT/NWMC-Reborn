## [❮ Back](/readme.md)
## Resource pack Introduction
Unbreakable items with different durability are
[linked with json models](Resourcepack\original\assets\minecraft\models\item\diamond_pickaxe.json)
and this models then linked to png textures.

### diamond_pickaxe.json
```json
{"predicate": {"damaged": 0, "damage": 0.000640204865557}, "model": "item/naruto/fireblast"}
```
### fireblast.json
```json
{
    "parent": "item/custom/icon",
    "textures": {
        "particle": "item/naruto/icons/jutsu/fireblast",
        "texture": "item/naruto/icons/jutsu/fireblast"
    }
}
```
### fireblast.png
<img src="Resourcepack\original\assets\minecraft\textures\item\naruto\jutsu\fireblast.png" alt="fireblast" width="128"/>

## Notes

[Script for making json links according to png](Resourcepack\original\assets\minecraft\models\item\naruto\\.script.py)

[Script for making disabled icon (brightness 0.5, blur 5)](Resourcepack\original\assets\minecraft\textures\item\naruto\jutsu_disabled\\.script.py)

- [Pickaxe](Resourcepack\original\assets\minecraft\models\item\diamond_pickaxe.json) have all spells and wands
- [Hoe](Resourcepack\original\assets\minecraft\models\item\diamond_hoe.json) have all armorstand models
- [Sword](Resourcepack\original\assets\minecraft\models\item\diamond_sword.json) have all custom item models

Pickaxe should be changed with hoe, and sword merged with hoe too

**Diamond pickaxe should NOT be used for wands, because it can break blocks**

[Icons](Resourcepack\original\assets\minecraft\mcpatcher\cit) for stackable items can be made with Optifine using hidden enchantments. Prefer to avoid it
