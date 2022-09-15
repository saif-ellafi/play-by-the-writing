# Play by the Writing (Play-btw)
### by JeansenVaars

Play by the writing is a small application powered by [Espanso](https://espanso.org/) that enables rolling dice, 
random tables and some solo RPG systems directly when writing with your keyboard. Just write down the magic 
keywords (listed below) and they will be replaced with the result of such command.

To put it in plain words, for example, when you write down “:qq” it will be replaced with an Oracle Yes/No question 
“[No]” , basically with an answer that could also be “[Yes, but]”. That’s it!

[Check YouTube explanation video](https://youtu.be/UeV63Iyi5_s)

# How to use?

## Installable Version

If you are a casual Windows user, I have put the installable version available to download [HERE](https://jeansenvaars.itch.io/play-by-the-writing)

To use it, you will have to install [Espanso](https://espanso.org/) (free) and learn where Espanso's user folder 
is located. In such folder you will be extracting the zipped download and execute Espanso so this plugin is loaded. 
Step by step instructions included.

## Open Source Version

Follow the instructions in README.md to compile the Python scripts into an executable that you can run, then place the dist
files inside Espanso user directory (not the install directory!).

# What is included?

- **Example kit**: Test before you buy. Once installed, by writing `:example` you should see a happy output.
- **Core kit**: Includes dice rolling, random tables, weighted tables, [Mythic GM Emulator](https://www.drivethrurpg.com/product/20798/Mythic-Game-Master-Emulator) (tables not included, user to upload them), [Plot Unfolding Machine (PUM)](https://jeansenvaars.itch.io/plot-unfolding-machine), [Scene Unfolding Machine (PUM)](https://jeansenvaars.itch.io/scene-unfolding-machine) and [One Page Solo Engine (OPSE)]((https://inflatablestudios.itch.io/one-page-solo-engine)) keywords
- **AI kit (Paying 5+ EUR)**: Includes Core kit + [OpenAI integration](https://beta.openai.com/playground) 
- auto-completes text for you based on context, using artificial intelligence/

# What is inside?

- Espanso’s files that make this application work with Espanso
- An executable (Windows or Linux) that is run by Espanso to support advanced functions
- Random Tables as included or used by any of the Play-btw modules
- Instructions in PDF format (README, INSTALL, KEYWORDS, LICENSE)

# Is this safe?
- Espanso is an open source application. I only wrote the logic to roll dice and random tables with Espanso.
- If you are a software developer, you can go ahead and learn Espanso. I recommend it. This package is for the out-of-the-box experience.
- Executables for Windows and Linux, meant to be of ease of use
- I am an indie developer; I do most of my stuff for [free and open source](https://github.com/saif-ellafi) - Including Mythic GME Tools for Foundry VTT
- I do this for love. But this took me quite a bunch of hours to get it right. This is why this time I decide to put a minimum price-gap for it 😊 Take it as a contribution and a coffee for me

# How to install

Play by the Writing (Play-btw) files go inside the Espanso's user config directory. **IMPORTANT:** Config directory is **NOT** the same as installation directory.

For example, if you install Espanso on the F:/ drive, the **config** directory will still be on the Windows installation drive, where your Documents and user files are located.

The installer will identify this location automatically, so normally you don't have to switch the path installation of Play by the writing.

## Windows

### Installer

1. Make sure Espanso works fine in your system and starts correctly.
2. Download the Windows installer executables
3. Follow the installer instructions. By default, the installer should point to Espanso config folder: 
`C:\Users\USERNAME\AppData\Roaming\espanso\`. Adjust if it is different.

## Linux

1. Make sure your Espanso installation is valid and espanso starts correctly
2. Download the Zip packages for Linux (either base or base with AI)
3. If using default paths, this should just work: `unzip ~/Downloads/PlayBTW_v1_11_base_with_ai.zip -d ~/.config/espanso/`

### AI Complete errors

If you get any errors when using `aicomplete` keyword, it may be due to missing clipboard mechanisms.
Install `xclip` or learn more about it here: https://pyperclip.readthedocs.io/en/latest/index.html#not-implemented-error

That’s it. See the keywords list below in this document.

# Keywords List

The keyword column is what you simply write in your keyboard, to get it replaced with an output (usually, at random).

**Note:** There are some `.` Surrounding certain commands. These represent user input and must be written down to denote the ending.

## Core Keywords

| Name                                                                                                                                                                                   | keyword          | Output | Information| 
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------|--------|------------|
| Dice | `:dd`            | 🎲 | Just fancy dice                                                                                                                                                            |
| Arrow | `:arr`           | → | Just an arrow                                                                                                                                                             |
| Roll simple dice | `:r1d6.`         | 1d6: 6 | Replace the red part with your own. Only works with this type of expression.                                                                            |
| Roll complex dice | `:rr3d6x.`       | 3d6x: [1, 3, 1] | Replace the red part with your own formula. Example has exploding dice. Find more here: https://github.com/borntyping/python-dice           |
| Roll fudge dice | `:df.`           | ( ) (+) (-) (-) + (0) = -1 | Fudge dice for FATE                                                                                                                    |
| Roll fudge dice with bons | `:df+3.`         | ( ) ( ) (-) (-) + (3) = 1 | Fudge dice for FATE with a bonus                                                                                            |
| Roll Random Table | `:tt.example.`   |  [Third result] | Roll from a table in .txt format placed in the tables folder. See the example table.                                                    |
| Roll Weighted Table | `:wt.example_w.` | [Next quarter] | Roll from a weighted table in .psv format. There is an example file in the tables folder. It is to roll from tables with dice ranges. |
| List all available tables | `:list`          | … | This will print all your available random tables to roll from. Usually just for checking.                                                            |

## Mythic GM Emulator Keywords

Play with Mythic Game Master Emulator: https://www.drivethrurpg.com/product/20798/Mythic-Game-Master-Emulator

**IMPORTANT!** Tables are not included. After installation, go to Espanso user directory
(default `C:\Users\username\AppData\Roaming\espanso\tables`) and replace the content of the tables
`mythic_action_1.txt` `mythic_action_2.txt` `mythic_description_1.txt` `mythic_description_2.txt` and `mythic_focus.psv`
on top of that you can add your own focus tables with format `.psv` following the same format as `mythic_focus.psv`.

Find the tables here: [https://github.com/rpg-tips/obsidian_goodies/blob/main/GM%20Emulation/Mythic_GME.md](https://github.com/rpg-tips/obsidian_goodies/blob/main/GM%20Emulation/Mythic_GME.md)

| Name                  | keyword                                                                   |
|-----------------------|---------------------------------------------------------------------------|
| Fate Check (prompted) | `:mmfc`                                                                   |
| Fate Check (per bias) | `:mfc4`, `:+mfc4`, `:++mfc4`, `:+++mfc4`, `:-mfc4`, `:--mfc4`, `:---mfc4` |
| Scene Alteration      | `:malt4`                                                                  |
| Random Event          | `:mre`                                                                    |
| Action Question       | `:mac`                                                                    |
| Description Question  | `:mde`                                                                    |
| Focus roll            | `:mfoc`                                                                   |
| Focus roll (custom)   | `:mfo.my_focus_table.`                                                    |

## PUM Keywords

These are meant to be played with https://jeansenvaars.itch.io/plot-unfolding-machine

| Name                 | keyword             |
|----------------------|---------------------|
| Yes or No Question   | `:qq` `:+qq` `:-qq` |
| Scene Prompt         | `:scene`            |
| Skill                | `:skill`            |
| High Stakes          | `:stakes`           |
| Goal                 | `:goal`             |
| Risk                 | `:risk`             |
| Expectation Checker  | `:check`            |
| Subject              | `:subject`          |
| Revelation           | `:revelation`       |
| Combat               | `:combat`           |
| Kind of item         | `:item`             |
| Kind of ability      | `:ability`          |
| Kind of person       | `:person`           |
| Kind of enemy        | `:enemy`            |
| Event                | `:event`            |
| Who?                 | `:who`              |
| Intent               | `:intent`           |
| Activity             | `:activity`         |
| Reason               | `:reason`           |
| Property             | `:property`         |
| Describe Area        | `:area`             |
| Describe NPC         | `:someone`          |
| Describe Object      | `:object`           |

## SUM Keywords

These are meant to be played with https://jeansenvaars.itch.io/scene-unfolding-machine

| Name                   | keyword                               |
|------------------------|---------------------------------------|
| GM Action (Score)      | `:gma` `:+gma` `:++gma` `:+++gma`     |
| NPC Action (Score)     | `:npca` `:+npca` `:++npca` `:+++npca` |
| NPC Disposition (Good) | `:npcg`                               |
| NPC Disposition (Bad)     | `:npcb`                               |
| Action Prompt          | `:sumac`                              |
| Subject Prompt         | `:sumsu`                              |
| Adjective Prompt       | `:sumad`                              |

## OPSE Keywords

These are meant to be played with https://inflatablestudios.itch.io/one-page-solo-engine

| Name                         | keyword             |
|------------------------------|---------------------|
| Oacle (Yes/No)               | `:qa` `:+qa` `:-qa` |
| Set the Scene (Complication) | `:setscene`         |
| Set the Scene (Alteration)   | `:setalt`           |
| GM Moves (Pacing)            | `:pacemove`         |
| GM Moves (Failure)           | `:failmove`         |
| Oracle (How)                 | `:opsehow`          |
| Random Event                 | `:opsere`           |
| Action Focus                 | `:afocus`           |
| Detail Focus                 | `:dfocus`           |
| Topic Focus                  | `:tfocus`           |
| Plot Hook Generator          | `:opsehook`         |
| NPC Generator                | `:opsenpc`          |
| Dungeon Crawler              | `:opsedungeon`      |
| Hex Crawler                  | `:opsehex`          |

## AI Keywords (OpenAI)

This experimental functionality relies on OpenAI: https://openai.com for using Artificial Intelligence to autocomplete a prompt. For this to function:
1. Go to openai and create an account (for free)
2. Go to your account settings and copy the API Key
3. Go to espanso settings folder inside the config folder
4. Paste the API Key in the file called openai.txt

| Name         | keyword      | Output | Information                                                       | 
|--------------|--------------|-------|-------------------------------------------------------------------|
| Autocomplete | `:aicomplete`  | ...   | You have to copy (CTRL+C) a piece of text that represents context |

# License - Service Level Agreement of Purchased Installable version
- This software is provided as-is, I provide support to users on good-will and listen to feedback and ideas, but cannot commit to eternal promises.
- This software is only available on itch.io – For your safety, only download from there
- Currently working only in Microsoft Windows and Linux (MacOS eventually. Not on mobile.)
- This software is purely and entirely recreational, and it should not cause any harm to your system. I cannot be held responsible for misuses or damage caused to your system.
- For users that have paid, they shall receive all future updates for free. However, new content may be sold separately.
- No refunds! Sorry – Use the example package to test this software before you buy

# License - Open Source Code
This application has been made to have fun, and I am not a large company. 
You can do whatever you would like to with this software, but be kind and share!