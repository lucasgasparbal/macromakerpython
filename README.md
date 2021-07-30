# Macromaker

A console based python program made for easy creation of /cast macro for World of Warcraft, with template saving functionality.

<br>

<br>


## Index

<br>

 1. [What is a /cast macro?](#whatis)
 2. [Anatomy of the /cast macro](#anatomy)
    1. [Statements](#statements)
    2. [Condition Blocks](#condition-blocks)
 3. [How to use Macromaker](#howto)
    1. [An example](#howto-example)
    2. [Some general usage rules](#howto-rules)
    3. [Conditions](#howto-conditions)
    4. [Commands](#howto-commands)
   

<br>

<br>

## What is a /cast macro? <a name="whatis"></a>

> In the World of Warcraft, a macro is a grouping of several slash commands that execute together when you click a button. 

[Source: Wowpedia](https://wowpedia.fandom.com/wiki/Macro)

A /cast macro is a specific type of macro that casts a spell in World of Warcraft. A /cast macro can be useful for making a button cast different spells depending on the target or by changing the target of a spell based on if additional keys are pressed.

This program works by transforming simplified user input into a working /cast macro to be pasted into World of Warcraft.

<br>

<br>

## Anatomy of the /cast macro <a name="anatomy"></a>

A World of Warcraft /cast macro may look something like this:
```
#showtooltip
/cast [@player, mod:alt][@mouseover, exists, help] Chain Heal; [@mouseover, exists, harm] Chain Lightning
```

The example above casts Chain Heal on the player if the alt key is held; Or it casts it on an ally, if the cursor is over them or they are the target. If the target or the unit hovered by the cursor is an enemy it instead casts Chain Lightning.


The line `#showtooltip` makes it so when you hover your cursor over the macro button the tooltip of the spell to be cast is displayed.

`/cast` is the slash command to be executed.

<br>

### Statements <a name="statements"></a>


An statement is a group of condition blocks paired with a spell. In the previous example we have two statements:
`[@player, mod:alt][@mouseover, exists, help] Chain Heal` and `[@mouseover, exists, harm] Chain Lightning`

 We can take a look at the first statement's structure:<br>
`[@player, mod:alt][@mouseover, exists, help]` are the statement's condition blocks and `Chain Heal` is the spell to be cast.


Macros can have more than one statement, separated by a semicolon (;). In this case the game will first check if it should cast Chain Heal based on the first statement's conditions, if these first conditions aren't met it will then go on to check the second statemet's conditions.

<br>

### Condition Blocks <a name="condition-blocks"></a>

A condition block is a group of conditions, each separated by a comma (,) and all of them encased between brackets ([ ]).They are always part of a statement. World of Warcraft checks these conditions to figure out if the statement should be cast. A statement can have more than one condition block, in this case World of Warcraft checks them from first to last, starting on the leftmost one. If at least one of them is true the statement's spell will be cast.

Condition blocks can also include the specific target of a macro if one desires to have one, noted with the `@` prefix. 


in the example we have various condition blocks, we will look at the first statement's: <br>
`[@player, mod:alt][@mouseover, exists, help]`

`[@player, mod:alt]` checks if the "alt" key is held on the keyboard, if it is the spell (in this case Chain Heal" will be cast on the player (denoted by `@player`)

`[@mouseover, exists, help]`<br> 
`exists` is a condition that checks if the desired target of the condition block exists. It is always used if the target may not exist currently in the game; In this case there might not be a target under the cursor, so the game would check to see if there is one before executing the macro. by pairing it with the `help` condition it will also check if the target under the cursor is a friendly character.


It is useful to note that the empty condition block `[]` always returns true.

<br>

<br>

## How to use Macromaker <a name="howto"></a>

Macromaker is meant to make cast macros without having to bother learning too much about their syntax. It supports a number of targets and conditions and it can also save any macro syntax you make into a file, so the next time you want to use it you only need to load the template and use it with the spells you desire.

<br>

### An example <a name="howto-example"></a>

Inputing this: `player alt / mouseover ally "Chain Heal"; mouseover enemy "Chain Lightning"` will result in the previously shown macro:

```
#showtooltip
/cast [@player, mod:alt][@mouseover, exists, help] Chain Heal; [@mouseover, exists, harm] Chain Lightning
```

<br>

### Some general usage rules <a name="howto-rules"></a>

 - **Separators**
      - You must separate statements using a semicolon **(;)** 
      - For condition blocks, separate them with a forward slash **(/)**
    
 - All Statements must have a spell, enclosed by double quotation marks(" ")
        Example: "Chain Heal" 
        
 - There can only be one target per condition block.
 
 - If one or more given conditions conflict with each other (for example, both mouseover and player are passed as targets in the same condition block) then the first one is selected.
 
 - You can have more than one modifier key, up to alt+ctrl+shift.

<br>

### Conditions <a name="howto-conditions"></a>

<br>

Use the macromaker keys to add the desired condition to the macro. If the condition has more than one Macromaker key you only need to use one of the keys listed.

<br>

#### Target Standing

- Macromaker keys: help or ally
 <br> Macro value: help
 <br> Description: Casts the macro if its target is an ally.


- Macromaker keys: harm or enemy
  <br> Macro value: harm
  <br> Description: Casts the macro if its target is an enemy.


#### Target Status

 - Macromaker keys: nodead or alive
   <br> Macro value: nodead
   <br> Description: Casts the macro if its target is alive.

 - Macromaker keys: dead
  <br> Macro value: dead
  <br> Description: Casts the macro if its target is dead.


#### Key Modifiers


 - Macromaker keys: alt
  <br> Macro value: alt
  <br> Description: Casts the macro if the 'alt' key is held.


 - Macromaker keys: control or ctrl
  <br> Macro value: ctrl
  <br> Description: Casts the macro if the 'control' key is held.


 - Macromaker keys: shift
  <br> Macro value: shift
  <br> Description: Casts the macro if the 'shift' key is held.

#### Custom Targeting

 - Macromaker keys: player or self
  <br> Macro value: player
  <br> Description: Makes your character the target of the spell.


 - Macromaker keys: focus
  <br> Macro value: focus, exists
  <br >Description: Casts the spell on your focus if you have one, otherwise casts it on the default target


 - Macromaker keys: mouse or mouseover
  <br> Macro value: mouseover, exists
  <br> Description: Casts the spell only if there is a target on your cursor

<br>

### Commands <a name="howto-commands"></a>

<br>
**NOTE: parameters should be separated by a colon (:), as shown below**
<br>

 - add _[Template title] : [Macromaker macro syntax]_
  <br>Alternative calls: save, savetemplate
  <br>Description: Saves the given marco syntax as a template, to be accessed with the other commands using its title. the macro syntax follows  the same rules used in the macromaker program
  
  
 - load _[Template title] : [Spells]_
  <br>Alternative calls: loadtemplate
  <br> Description: Writes the given macro template with the given spell on the console. **The spell should be encased in double quotation marks (" ")**
  Keep in mind each template has a required number of spells

 - show _[Template title]_
  <br> Alternative calls: showtemplate
  <br> Description: Shows the given title's macro template on the console, without spells.

 - remove _[Template title]_
  <br> Alternative calls: removetemplate, delete, del, deletetemplate
  <br> Description: Removes the given template from the files

 - change _[Title to change] : [New title]_
  <br> Alternative calls: changetitle
  <br> Description: Changes the title of the first title's template with the second given title. If the second title
 is already in use, it won't change the title.

 - list
  <br> Alternative calls: templates
  <br> Description: Lists the titles of the currently saved templates.
