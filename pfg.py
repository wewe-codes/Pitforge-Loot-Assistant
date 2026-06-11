import minescript as mc
import time
import threading
import lib_inv as li


# ==========================================
# Settings
# ==========================================

loot_items = {
    "minecraft:nether_star",
    "minecraft:dragon_breath",
    "minecraft:prismarine_crystals",
    "minecraft:creeper_spawn_egg"
}


# ==========================================
# Globals
# ==========================================

lowXP = 0
NormalXP = 0
HighXP = 0
VeryHighXP = 0
UltraXP = 0

neartoggle = False
GUItoggle = False

last_near = 0


# ==========================================
# Auto Near
# ==========================================

def NearToggle():
    global last_near

    while True:

        if neartoggle and time.time() - last_near > 10.5:
            mc.execute("/near")
            last_near = time.time()

        time.sleep(0.2)


# ==========================================
# Auto Loot
# ==========================================

def GUI():
    global lowXP, NormalXP, HighXP, VeryHighXP, UltraXP

    while True:

        if not GUItoggle:
            time.sleep(1)
            continue
        if mc.screen_name() != "Chest":
            time.sleep(0.2)
            continue
        for item in mc.container_get_items():

            if item.slot >= 27:
                continue

            if item.item not in loot_items:
                continue

            if item.nbt:
                if "500 Experience" in item.nbt:
                    UltraXP += 500

                elif "250 Experience" in item.nbt:
                    VeryHighXP += 250

                elif "100 Experience" in item.nbt:
                    HighXP += 100

                elif "50 Experience" in item.nbt:
                    NormalXP += 50

                elif "25 Experience" in item.nbt:
                    lowXP += 25

            li.quickmove(item.slot, 1)

        time.sleep(0.4)


# ==========================================
# Threads
# ==========================================

threading.Thread(target=GUI, daemon=True).start()
threading.Thread(target=NearToggle, daemon=True).start()


# ==========================================
# Hotkeys
# ==========================================

with mc.EventQueue() as q:

    q.register_key_listener()

    print("Pitforge Loot Assistant")
    print("")
    print("Hotkeys:")
    print("F5) Auto Near | Toggle")
    print("F6) Auto Loot | Toggle")
    print("F8) Show XP Statistics")

    while True:

        e = q.get()

        # F5
        if e.key == 294 and e.action == 1:

            neartoggle = not neartoggle

            if neartoggle:
                mc.echo_json(
                    '{"text":"Auto Near ON","color":"green"}'
                )
            else:
                mc.echo_json(
                    '{"text":"Auto Near OFF","color":"red"}'
                )

        # F6
        elif e.key == 295 and e.action == 1:

            GUItoggle = not GUItoggle

            if GUItoggle:
                mc.echo_json(
                    '{"text":"Auto Loot ON","color":"green"}'
                )
            else:
                mc.echo_json(
                    '{"text":"Auto Loot OFF","color":"red"}'
                )

        # F8
        elif e.key == 297 and e.action == 1:

            totalXP = (
                lowXP
                + NormalXP
                + HighXP
                + VeryHighXP
                + UltraXP
            )

            print(f"Total XP: {totalXP}")
            print(
                f"3 Capture Points = {totalXP * 3.3:.0f} XP (x3.3)"
            )