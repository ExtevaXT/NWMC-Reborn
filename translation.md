## [❮ Back](/readme.md)
## Translation with Triton 
### Magic spells
[localize.py](Scripts\localize.py) for fixing formatting of spells and replacing 'name' and 'description' 
with translation placeholders `"[lang]magic.spells.basic.wind{index}.name[/lang]"` in Magic
then it creates translation file with EN and RU lines for Triton.

[Triton docs for this](https://triton.rexcantor64.com/concepts/placeholders.html#placeholder-syntax)

### Localization

All lines in RU need to be changed with this `[lang]` tags.
Keys like `plugin.category.subcategory.etc` used just for convenience.

