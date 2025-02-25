# PET Cup Calculator

The PET Cup Calculator is a Python-based tool designed to estimate the amount of PET (Polyethylene Terephthalate) required to manufacture a cup. The calculator takes the cup's diameter and height as user inputs and computes the PET needed, including a simplified handle model.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [How It Works](#how-it-works)
- [Contributing](#contributing)
- [Contact](#contact)

## Overview

This project provides a quick and easy way to calculate the material requirements for a PET cup based on user-defined dimensions. It is ideal for those interested in material estimation, design optimization, or simply exploring a practical Python application.

## Features

- **User Input:** Dynamically accepts the cup's diameter and height.
- **Accurate Calculations:** Estimates the volume of the cup's walls, bottom, and handle.
- **Material Estimation:** Converts the calculated volume to weight (grams) using the density of PET.
- **Extensible Code:** Clean and well-documented code that can be easily modified or extended.

## Installation

 **Clone the repository:**

   ```bash
   git clone https://github.com/Partha/pet-cup-calculator.git
   cd pet-cup-calculator

## Usage

 **Run the Python script from the command line:**

   ```bash
   python pet_cup_calculator.py

*You will be prompted to enter the cup's diameter and height (both in inches). The program will then output the estimated amount of PET required in grams.*
 # Example Interaction
 ```python
   Enter the diameter of the cup (in inches): 6
   Enter the height of the cup (in inches): 6
   The estimated amount of PET required: 72 grams
