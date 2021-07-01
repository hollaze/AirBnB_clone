# AirBnB_clone v1 - File storage / Console

The purpose of this project is to recreate the AirBnB site, from the back-end data management to the front-end user interface.

This repo contains the first part of the project which consists in :

*    put in place a parent class (called BaseModel) to take care of the initialization, serialization and deserialization of your future instances
*    create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
*    create all classes used for AirBnB (User, State, City, Place…) that inherit from BaseModel
*    create the first abstracted storage engine of the project: File storage
*    create all unittests to validate all our classes and storage engine

![Alt text](https://imagizer.imageshack.com/v2/1257x669q90/924/Aebfet.png "The part of this project: v1")

# Command interpreter


## Installation

Clone this repositary:

    $ git clone https://github.com/hollaze/AirBnB_clone.git 

Access the folder:

    $ cd AirBnB_clone

## How tu use it

You can access the console via two modes.

Interactive mode:

    $ ./console.py

Non-interactive mode:

    $ echo "<command>" | ./console.py

## Examples

### Authors

-[Etienne Brun](https://github.com/EtienneBrJ)

-[Alrick Deperiers](https://github.com/hollaze)
