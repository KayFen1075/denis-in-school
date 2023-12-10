define audio.block = "audio/battle/skills/block.ogg"
define audio.fanfare = "audio/game/fanfare.ogg"
define sfx_whoosh = RandomBag(["audio/battle/whoosh1.ogg", "audio/battle/whoosh2.ogg", "audio/battle/whoosh3.ogg", "audio/battle/whoosh4.ogg", "audio/battle/whoosh5.ogg", "audio/battle/whoosh6.ogg", "audio/battle/whoosh7.ogg"])
define sfx_monsterdead = RandomBag(["audio/battle/monsterdead1.ogg", "audio/battle/monsterdead2.ogg", "audio/battle/monsterdead3.ogg"])

label battle_music:
    if bb == 1:
        play music battle1
    elif bb == 2:
        play music battle2
    elif bb == 3:
        play music battle3
    return
