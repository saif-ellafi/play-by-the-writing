### 3.11
* UPDATED: SUM v7
* FIXED: pull command was not working

### 3.10
Overview: Performance boosts! PlayBTW now is compiled differently, so it works faster than ever
NOTE: This update will leave behind files inside espanso/scripts folder that won't be needed anymore. Feel free to cleanup before installing this version.

* CHANGED: Build changes reduces storage and CPU usage significantly when running
* CHANGED: Build scripts are way snappier now, faster to compile
* CHANGED: Made pull function snappier, so it doesn't take so many resources
* CHANGED: no-AI option allows building PbtW without AI support (lightweight build)

### 3.02
Overview: This update makes PlayBTW slightly faster by making the scripts lighter

* FIXED: Smaller executables help in faster PlayBTW response
* FIXED: Faster build from source by removing redundant steps
* CHANGED: Used a faster dice roller library, syntax may change
* DEPRECATED: Mythic script now is part of "Core"

### 3.01
Overview: This update is pure credit to the community who reported issues here and in the Discord server. Special thanks to Jeremy (@jeremy-w) for fixing these as I was going through life stuff! Thank you so much!

* FIXED: Broken cards commands (Thank you @jeremy-w)
* FIXED: Broken weighted tables commands (Thank you @jeremy-w)
* FIXED: Broken BOLD Waylay table (Thank you @jeremy-w)
* FIXED: Improved Waylay table expression

### 3.00
Overview: Essentially, from now on, PlayBTW will store player specific tables and configurations in $HOME/PlayBTW folder, this gives space to the user for customization in the future, plus not breaking files upon updates. Users can more easily fiddle with custom tables and lists without worrying about updates. For example, users can now override default tables content with own content, without touching the original table. Espanso folder's data should no longer be altered.

* FEATURE: PlayBTW now stores configuration tables in $HOME directory
* FEATURE: my_tables folder in config folder allows for random tables
* FEATURE: list_tables folder stores player lists for mythic and pum
* FEATURE: Pull command now checks for updates and gives update notes
* FEATURE: Mythic Focus table is now a configurable list_table
* FEATURE: Simpler lists and plot nodes commands (:mlists and :pnodes)
* FEATURE: OpenAI Key setup now introduced via prompt
* UPDATED: Updated to latest PUM V8-1
* UPDATED: Prompty Questions tables now included
* FIXED: User list_tables like plot nodes yield default lists when unset
* FIXED: Mythic Fate Check wrong probabilities
* FIXED: Broken weighted lists (Mythic focus)
* DEPRECATED: Deprecated :list commands in favor of Espanso's search
* DEPRECATED: Unwrappable tables of type u{{}} (just use normal)

### 2.11
* Fixed failing AI commands (:aistart)

### 2.10
* Always show all rolled dice in formulas when rolling for example 2d6+2: [2, 6] = 10
* Added new command :update which pulls latest tables from the internet without having to download a new version
* Removed command :rr - now there is only one dice roll command which is :r<formula>

### 2.09
* Build for MacOS available
* Fixed an issue on output with non-english characters
* Fixed a typo in a table name

### 2.08
* More table typos and mistakes I'm afraid

### 2.07
* Fixed wrong table name in PUM
* Shifted :myth to :mythic

### 2.06
* Added Genesys RPG dice (:genesys or :gend)
* Updated to PUM v8

### 2.05
* Updated to latest OpenAI Python API (AI commands were broken)

### 2.04
* Updated to PUM v7-8
* Added support for custom decks (in text form)
* Documented ALT+SPACE command which shows all available commands
* Added labels so all tables can be used with ALT+SPACE
* Added new command `:aicall` that shows all AI related commands
* Improved error message for when a user list is not defined

### 2.03
* Updated to PUM v7-7

### 2.02
* New commands for Conjecutre games (CRGE, UNE, BOLD)
* Added missing GUM setup commands
* Small corrections here and there

### 2.01
#### THE ONLY COMMANDS YOU NEED TO LEARN NOW!
* New command :mel - Browse all mythic element tables
* New command :pum - Browse all PUM tables
* New command :gum - Browse all GUM tables
* New command :sum - Browse all SUM tables
* New command :mune - Browse all MUNE tables
* New command :opse - Browse all OPSE tables
* Fixed Mythic descriptors command :mde
* Fixed ChatGPT error with ugly characters (thanks @BapKing)
* Support for user defined nested tables
* Simplified some SUM commands

### 2.00
* Mythic GME updated to 2e
* PUM updated to v7
* SUM updated to v6
* GUM updated to v2
* Added MUNE to the oracles
* ChatGPT updated to latest API
* Dall-E updated to v3
* Dall-E new settings (image size, quality, styles)
* Dall-E can now return b64 into the result
* ChatGPT deprecated completion
* ChatGPT now allows isolated questions
* New list browser allows filtered search (:list.mythic.)
* User defined lists supported (Character lists, thread lists, plot nodes, etc.)
* Cleanup code and deprecations of old oracle versions

### 1.33
* Updated to GUM V2 (Rev5)
* Updated inner dependencies

### 1.32
* Updated to GUM Rev5
* Basic and advanced dice rolls now have the same output style

### 1.31
* Support for GUM Extended

### 1.30
* OpenAI GPT-4 and GPT-3.5 Support
* Game Unfolding Machine (GUM) rules support

### 1.22
* OpenAI GPT Support
* GPT with Memory
* AI with UI Box prompt
* Options to use AI memory

### 1.19
* Updated to SUM v5.5

### 1.18
* Updated to SUM v4 (corrected)

### 1.17
* Updated to PUM v5.3
* Updated to SUM v4.0-Preview
* Fixed :mre command (Mythic random event)
* Fixed: added missing -8 variants to Mythic checks
* Fixed: clarified meaning of 'Yes favorable'
* Fixed: PUM :person to :people to match rules
* Fixed: Added back :tt.<table>. and :wt.<wtable>. commands again

### 1.13
* Updated to PUM v4
* Updated to SUM v2.2

### 1.12
* Added poker deck functions (persists, non-replacement)
* Simplified and cleaned up unnecessary scripts
* Updated PUM to V3.2 and SUM to V2

#### 1.11
* Added support for nested tables
* Support spaces in table lists and names
* Updated PUM to V3