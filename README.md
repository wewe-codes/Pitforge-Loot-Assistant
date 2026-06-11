# ⛏️ Pitforge Loot Assistant

> A simple automation and quality-of-life tool for the Minecraft server Pitforge.
>
> Built while learning Python and experimenting with Minescript.

---

## ✨ Features

###  Auto Loot

Automatically loots valuable items from chests.

Default loot:

*  Nether Stars
*  Experience Bottles (dragon breath)
*  Prismarine Crystals
*  Creeper Spawn Eggs

Loot items can easily be changed inside `pfg.py`.

### 📈 XP Tracking

Tracks collected experience bottles and calculates:

* 25 XP
* 50 XP
* 100 XP
* 250 XP
* 500 XP

View your total XP gained during the current session.

### 👀 Auto Near

Automatically executes:

```text
/near
```

at configurable intervals.

Useful for detecting nearby players while looting.

### ⌨️ Hotkeys

| Key | Action             |
| --- | ------------------ |
| F5  | Toggle Auto Near   |
| F6  | Toggle Auto Loot   |
| F8  | Show XP Statistics |

---

## 🚀 Installation

### Requirements

* Minecraft Java Edition
* Python 3.10+
* Minescript

### 1️⃣ Install Minescript

Follow the official installation guide:

https://minescript.net

### 2️⃣ Download This Repository

Clone the repository:

```bash
git clone https://github.com/wewe-codes/Pitforge-Loot-Assistant.git
```

or download pfg.py manually.

### 3️⃣ Download lib_inv

This project uses **lib_inv** by SmaertBoty.

Download:

https://github.com/SmaertBoty/Minescript/tree/main/lib_inv

### 4️⃣ Copy Files

Place both files into your Minescript folder:

```text
.minecraft/
└── minescript/
    ├── pfg.py
    └── lib_inv.py
```

### 5️⃣ Launch Minecraft

Start Minecraft and run:

```text
\pfg
```

---

## 📊 Example Output

```text
Auto Near ON

Auto Loot ON

Total XP: 4250
3 Capture Points = 14025 XP
```

---

## ❤️ Credits

Special thanks to **SmaertBoty** for creating the `lib_inv` library used for inventory interaction and quick item movement.

Repository:

https://github.com/SmaertBoty/Minescript/tree/main/lib_inv

---

## 👤 Author

**Kevin / LEKEVIN**

🌍 https://lekevin.de
