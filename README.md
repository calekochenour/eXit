# eXit

The ascii styled BBS game on the TV series Mr. Robot.

This repo is a fork of DasAutoIngenieur's repo (https://github.com/DasAutoIngenieur/eXit), which itself is a fork of sinfulz's original repo (https://github.com/sinfulz/eXit).

## Requirements
* pathlib
* sys

See environment.yml file for Python version this workflow was tested on.

## Usage
Create and activate the Conda environment, then run the `eXit.py` script.

Create Conda environment:
```commandline
conda env create -f environment.yml
```

Activate Conda environment:
```commandline
conda activate eXit
```

Run script:
```commandline
(eXit) > python eXit.py
```

## Files

### `eXit.py`
Contains the code to play the game.

### `utilities/ascii.py`
Contains all visuals used in `eXit.py`, in ASCII characters.

### `environment.yml`
Contains the recipe to create the Conda environment.

## Changelog
* Version 0.1, 19/04/2020 - Release day!
* Version 1, 15/7/2024 - Replaced for with while loops
* Version 2, September 8, 2024
  * Added steps to take multiple paths through the game (path 1 - leave for a new world, path 2 - stay with your friend) to emulate the sequence in episode 4x11 "eXit"
  * Added ASCII images/visuals displaying various steps throughout the game (tunnel, boat, etc.) to complement the text portion of the game

## Disclaimer:
This piece of software has no affiliation with the Mr. Robot brand or the USA Network.
