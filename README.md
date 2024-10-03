# RIB Files Generator

This repository helps automate the creation of RIBs (Router-Interactor-Builder) in your project. It generates files for both platform and shared layers with the appropriate naming conventions.

## Features

- Automatically generates files based on the provided RIB name.
- Supports both platform and shared file generation.
- Helps maintain consistent naming conventions across RIBs.

## Prerequisites

- Python 3.x installed on your machine.
- Ensure you have the necessary permissions to create files in the target directories.

## Usage

### 1. Clone the Repository

```bash
git clone https://github.com/Kovvuri-Chandra-Kiran-Reddy/newRibCreator.git
```

### 2. Navigate to the Cloned Directory
```bash
cd newRibCreator
```

### 3. Run the RIB Files Generator
```bash
python3 main.py
```

### 4. Enter the Required Information
- **Package Name** : When prompted, enter the package name for the RIB. If no specific package is required, just press Enter. ( if package name is empty => all files will be created in the folder path provided in next inputs).
- **RIB Name** : Enter the RIB name in UpperCamelCase like CancelTrip. This rib name will be used as a prefix for the generated files (e.g., CancelTripInteractor, CancelTripBuilder, etc.).
- **Platform Path** : Provide the absolute path where the platform-specific RIB files should be generated.
- **Shared Path** : Provide the absolute path where the shared RIB files should be generated.

### 5. Changes to be made from the user
- make sure you change the ***ProductFlow*** value in ***event identifiers file.***

<br/>
<div align="center"> <img src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNmJtbWExMXJiaGc1amJteXZ5YW1iOGM2Y3FjOHpyNWFpaWFpcWFiZyZlcD12MV9naWZzX3NlYXJjaCZjdD1n/3bu85lsWhBTlWcOMN6/giphy.gif" alt="Coding Animation"> </div>
