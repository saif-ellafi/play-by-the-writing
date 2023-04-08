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
There's a price tag on it to justify the compilation, building and installer effort, but even if you can on your own, your support is appreciated.

To use it, you will have to install [Espanso](https://espanso.org/) (free) and then run the installer available here, 
which will automatically point to your Espanso user folder, and run immediately.

## Open Source Version

The installable is compilable from the source code available [HERE](https://github.com/saif-ellafi/play-by-the-writing).
If you know some Python and want to fiddle with Espanso, you can find this program in there for **FREE**
(The installable version is priced to justify the time it takes me to compile, build and make it installable)

Follow the instructions in BUILD.md to compile the Python scripts into an executable that you can run, then place the dist
files inside Espanso user directory (not the install directory!).

# What is included?

- **Example kit**: Test before you buy. Once installed, by writing `:example` you should see a happy output.
- **Core kit**: Includes dice rolling, random tables, weighted tables, [Mythic GM Emulator](https://www.drivethrurpg.com/product/20798/Mythic-Game-Master-Emulator), [Plot Unfolding Machine (PUM)](https://jeansenvaars.itch.io/plot-unfolding-machine), [Game Unfolding Machine (GUM)](https://jeansenvaars.itch.io/game-unfolding-machine), [Scene Unfolding Machine (PUM)](https://jeansenvaars.itch.io/scene-unfolding-machine) and [One Page Solo Engine (OPSE)]((https://inflatablestudios.itch.io/one-page-solo-engine)) keywords
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
3. If using default paths, this should just work: `unzip ~/Downloads/PlayBTW_v1_31_base_with_ai.zip -d ~/.config/espanso/`

### AI Complete errors

If you get any errors when using `aicomplete` keyword, it may be due to missing clipboard mechanisms.
Install `xclip` or learn more about it here: https://pyperclip.readthedocs.io/en/latest/index.html#not-implemented-error

That’s it. See the keywords list below in this document.

# Customization

## Match files

There are many files with `.yml` extension inside the `match` folder. Open with a text editor and change the lines 
that start with `:` in order to change their command keyword.

Some entries point to `table` (or `wtable` for weighted tables) which follow with a table name. This table name 
is the file name within the folder `tables`, and you can append with comma more than one, i.e. `table1,table2`

Understanding this, will allow you to copy these segments to create your own commands with your own tables!

## Table customization

There are two types of tables. Ones ending in `.txt` (simple tables) and others in `.psv` (weighted tables). Check
the ones available in the folder `tables` for examples of each.

## Nested tables

You can nest table rolls within others, by utilizing the format `{{table_simple_name}}` or `w{{weighted_table_name}}`
where the table name refers to the file name. You can use these however you like, and even build sentences with more
than one of them, i.e. `Hello {{table_1}}, I hope you had a great {{table_2}}!`

# Keywords List

The keyword column is what you simply write in your keyboard, to get it replaced with an output (usually, at random).

**Note:** There are some `.` Surrounding certain commands. These represent user input and must be written down to denote the ending.

## Core Keywords

| Name                      | keyword                       | Output | Information                                                                                                                           | 
|---------------------------|-------------------------------|--------|---------------------------------------------------------------------------------------------------------------------------------------|
| Dice                      | `:dd`                         | 🎲 | Just fancy dice                                                                                                                       |
| Arrow                     | `:arr`                        | → | Just an arrow                                                                                                                         |
| Roll simple dice          | `:r1d6.`                      | 1d6: 6 | Replace the red part with your own. Only works with this type of expression.                                                          |
| Roll complex dice         | `:rr3d6x.`                    | 3d6x: [1, 3, 1] | Replace the red part with your own formula. Example has exploding dice. Find more here: https://github.com/borntyping/python-dice     |
| Roll fudge dice           | `:df.`                        | ( ) (+) (-) (-) + (0) = -1 | Fudge dice for FATE                                                                                                                   |
| Roll fudge dice with bons | `:df+3.`                      | ( ) ( ) (-) (-) + (3) = 1 | Fudge dice for FATE with a bonus                                                                                                      |
| Roll Random Table         | `:tt.example.`                |  [Third result] | Roll from a table in .txt format placed in the tables folder. See the example table.                                                  |
| Roll Weighted Table       | `:wt.example_w.`              | [Next quarter] | Roll from a weighted table in .psv format. There is an example file in the tables folder. It is to roll from tables with dice ranges. |
| Shuffle Poker Deck        | `:shuffle`                    |
| Draw from Poker Deck      | `:draw`                       |
| Roll from random list     | `:list` `:+list` `:++list`    | ... | Display all available tables in the directory, and roll from there                                                                    |
| Roll from weighted list   | `:wlist` `:+wlist` `:++wlist` | ... | Display all available w-tables in the directory, and roll from there                                                                  |

## Mythic GM Emulator Keywords

Play with Mythic Game Master Emulator: https://www.drivethrurpg.com/product/20798/Mythic-Game-Master-Emulator

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

| Name                | keyword                  |
|---------------------|--------------------------|
| Yes or No Question  | `:qq` `:+qq` `:-qq`      |
| Scene Prompt        | `:scene`                 |
| Expectation Checker | `:check` `:expectation`  |
| Challenge           | `:challenge` or `:skill` |
| Discovery           | `:discovery`             |
| Risk                | `:risk`                  |
| Subject             | `:subject`               |
| Catalyst            | `:catalyst`              |
| Complication        | `:complication`          |
| Circumstance        | `:circumstance`          |
| Kind of item        | `:item`                  |
| Kind of ability     | `:ability`               |
| Kind of people      | `:people`                |
| Kind of enemy       | `:enemy`                 |
| Kind of danger      | `:danger`                |
| Who?                | `:who`                   |
| Intent              | `:intent`                |
| Activity            | `:activity`              |
| Reason              | `:reason`                |
| Describe Area       | `:area`                  |
| Describe NPC        | `:someone`               |
| Describe Object     | `:object`                |

## SUM Keywords

These are meant to be played with https://jeansenvaars.itch.io/scene-unfolding-machine

| Name             | keyword                         |
|------------------|---------------------------------|
| GM Action        | `:gma` or `:+gma` or `:-gma`    |
| GM Feedback      | `:gmf` or `:+gmf` or `:-gmf`    |
| GM World         | `:gmw` or `:+gmw` or `:-gmw`    |
| NPC Contribution | `:npcc` or `:+npcc` or `:-npcc` |
| NPC Behavior     | `:npcb` or `:+npcb` or `:-npcb` |
| NPC Opinion      | `:npco` or `:+npco` or `:-npco` |
| NPC Answer       | `:npca` or `:+npca` or `:-npca` |
| Action Prompt    | `:sumac`                        |
| Subject Prompt   | `:sumsu`                        |
| Adjective Prompt | `:sumad`                        |

## GUM Keywords

These are meant to be played with https://jeansenvaars.itch.io/game-unfolding-machine

| Name                         | keyword                                    |
|------------------------------|--------------------------------------------|
| Oracle (GM)                  | `:gqgm` or `:+gqgm` or `:-gqgm`            |
| Oracle (PC)                  | `:gqpc` or `:+gqpc` or `:-gqpc`            |
| Oracle (NPC)                 | `:gqnpc` or `:+gqnpc` or `:-gqnpc`         |
| Grand Oracle (Basic)         | `:gob`                                     |
| Grand Oracle (Rich)          | `:gor`                                     |
| Grand Oracle (Subject)       | `:gos`                                     |
| Grand Oracle (Description)   | `:god`                                     |
| Unfold the scene             | `:gscene`                                  |
| Challenge skill test         | `:gskill`                                  |
| Combat (Random)              | `:gcombat` or `:gconflict`                 |
| Plan check (Safe to Explode) | `:gpc` or `:+gpc` or `:++gpc` or `:+++gpc` |
| GM Intervention              | `:ginterv`                                 |
| Location identity (Random)   | `:glocid`                                  |
| Location detail (Random)     | `:glocdet`                                 |
| NPC identity (Random)        | `:gnpcid`                                  |
| NPC detail (Random)          | `:gnpcdet`                                 |
| Motive (Good)                | `:gmotivegood`                             |
| Motive (Evil)                | `:gmotiveevil`                             |
| Action (Good)                | `:gactgood`                                |
| Action (Evil)                | `:gactevil`                                |
| NPC (Who?)                   | `:gwho` or `:gnpcwho`                      |
| Game setup (Location)        | `:gsetlocation`                            |
| Game setup (Problem)         | `:gsetproblem`                             |
| Game setup (Hook)            | `:gsethook`                                |
| Game setup (Mission)         | `:gsetmission`                             |
| Game setup (Consider)        | `:gsetconsider`                            |
| Game setup (Lead)            | `:gsetlead`                                |
| Game setup (Full)            | `:gsetfull`                                |
| Extended - Prober World      | `:gprobew`                                 |
| Extended - Prober Scene      | `:gprobes`                                 |
| Extended - Discovery         | `:gdisc`                                   |
| Extended - Discovery Past    | `:gpast`                                   |
| Extended - Discovery Future  | `:gfuture`                                 |
| Extended - Discovery Clues   | `:gclue` or `:ginfo`                       |
| Extended - Discovery Reasons | `:greason`                                 |
| Extended - NPC Interaction   | `:ginteract`                               |
| Extended - NPC Behavior      | `:gbehav`                                  |
| Extended - NPC Contribution  | `:gcontrib`                                |
| Extended - NPC Response      | `:gresponse`                               |
| Extended - NPC Request       | `:grequest`                                |
| Extended - Enemy Action      | `:genemy`                                  |
| Extended - Enemy Insight     | `:gfeel` or `:ginsight`                    |
| Extended - Enemy Risks       | `:grisk`                                   |
| Extended - Enemy Events      | `:gevent`                                  |
| Extended - Enemy Threat      | `:gthreat`                                 |


## OPSE Keywords

These are meant to be played with https://inflatablestudios.itch.io/one-page-solo-engine

| Name                         | keyword             |
|------------------------------|---------------------|
| Oracle (Yes/No)              | `:qa` `:+qa` `:-qa` |
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

| Name                               | keyword                                     | Output                                                                | 
|------------------------------------|---------------------------------------------|-----------------------------------------------------------------------|
| AI Text GPT-3 Completion Prompt    | `:text` `:aitext` `:aicomplete` `:aiprompt` | An AI response to your prompt                                         |
| AI Text GPT-3 Show Memory          | `:aimemory` `:aiknow`                       | Bring AI accumulated knowledge memory                                 |
| AI Text GPT-3 Forget Memory        | `:aiforget` `:aierase` `:aiclear`           | Delete AI memories (saves costs)                                      |
| AI Chat GPT-4 New Instruction      | `:aisys` `:aiinit` `:aistart`                | Initialize a new AI Chat-GPT interaction with an instruction          |
| AI Chat GPT-4 Continue Interaction | `:chat` `:aichat`                           | Chat with the AI with the given instruction (needs instruction first) |
| AI Image Dall-E                    | `:aiimg` `:aiimage` `:dall-e`               | An AI generated image                                                 |

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