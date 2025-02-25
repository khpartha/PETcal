# PET Cup Calculator
A simple and efficient C++ program that estimates the amount of PET (Polyethylene Terephthalate) required to manufacture a plastic cup with user-defined dimensions. This project demonstrates practical applications of geometry, volume calculations, and material density conversion—all wrapped in an easy-to-use command-line interface.

Table of Contents
Overview
Features
Project Structure
Requirements
Installation and Build
Usage
Code Overview
Contributing
License
Contact
Acknowledgements

Overview
The PET Cup Calculator estimates the volume and mass of PET needed to manufacture a plastic cup given its dimensions. The cup is modeled as a combination of a hollow cylinder (the main body), a bottom disk, and a small cylindrical handle. By accepting user inputs for the cup's diameter and height, the program dynamically calculates:

Volume of the cup walls: Modeled as a hollow cylindrical shell.
Volume of the bottom: Modeled as a solid disk.
Volume of the handle: Approximated as a simple cylinder.
These volumes are then used to estimate the total weight of PET needed based on a preset density.

Features
User Input: Dynamically accepts cup dimensions (diameter and height).
Accurate Calculation: Uses geometric formulas for a hollow cylinder, a disk, and a cylindrical handle.
Modular Design: Clear separation of calculation functions for enhanced readability and maintenance.
Unit Conversion: Automatically converts the computed weight from pounds to grams.
Project Structure
mathematica
Copy
PET-Cup-Calculator/
├── README.md
└── pet_cup_calculator.cpp
README.md: This file, providing an overview, instructions, and details about the project.
pet_cup_calculator.cpp: The main C++ source file containing the implementation of the calculator.
Requirements
Compiler: A C++ compiler (e.g., g++, clang++)
Operating System: Cross-platform (tested on Linux, Windows, macOS)
Basic Knowledge: Familiarity with command-line operations
