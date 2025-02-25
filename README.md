# PET Production Calculator

The PET Cup Calculator is a Python-based tool designed to estimate the amount of PET (Polyethylene Terephthalate) required to manufacture a cup. The calculator takes the cup's diameter and height as user inputs and computes the PET needed, including a simplified handle model.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [How It Works](#how-it-works)
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
   git clone https://github.com/khpartha/pet_calculator.git
 
``` 
## Usage
Run the Python script from the command line:

 ```bash
  python pet_cup_calculator.py
```

You will be prompted to enter the cup's diameter and height (both in inches). The program will then output the estimated amount of PET required in grams.

**Example Interaction**
 ```python
Enter the diameter of the cup (in inches): 6
Enter the height of the cup (in inches): 6
The estimated amount of PET required: 72 grams
```
## How It Works
- **1. User Input:** The script prompts the user for the cup's diameter and height. 
- **2. User Input:** The cup is modeled as a hollow cylinder for the body.
   
- **3. Weight Estimation:** The total volume is calculated and then converted to weight using the density of PET (approx. 0.050 lb/in³).
Finally, the weight is converted from pounds to grams.
  
The clear modular structure of the code allows for easy maintenance and future expansion of features.

## Contact 
For any questions, suggestions, or contributions, please feel free to contact me at 4khundrakpampartha@gmail.com.




