# Excel-SQLite converter

This repository is showcasing a very simple script to make importing Excel(Like the [Test Excel table](./Test_Excel.xlsx) provided in the repository) to a SQLite database easier. The python script creates a simple GUI any user can use to import any Excel table to a SQLite database.

## Table of Contents

- [Introduction](#introduction)
- [Project Structure](#project-structure)
- [Technologies Used](#technologies-used)
- [Setup](#setup)
- [Usage](#usage)
- [Contributing](#contributing)

## Introduction

The Excel-SQLite converter is a Python script that allows users to easily import Excel data into a SQLite database. It provides a user-friendly interface to select an Excel file, specify the database name, and import the data into the SQLite database.

## Project Structure

```bash
├── Excel-SQLite-Converter.py            # Main Python script
├── Test_excel.xlsx                      # Sample Excel file
├── requirments.txt                      # Python dependencies
└── README.md
```
- `Excel-SQLite-Converter.py`: Contains the script, which is the main file that contains the code for the Excel-SQLite converter.
- `Test_excel.xlsx`: Sample Excel file to test the script.
- `requirements.txt`: Cointains the dependencies required for the script to run.


## Technologies Used

- **python**
- **pandas**
- **sqlite3**
- **tkinter** (plus **tkinter.filedialog** and **tkinter.messagebox**)

## Setup

**Clone the repository:**
```bash
git clone https://github.com/pitukepe/excel-sqlite_converter.git
```
**Install the required packages:**
```bash
pip install -r requirements.txt
```

## Usage

### Running the script:
Python Scripts: Run the scripts in the scripts/ directory to launch the GUI for Importin Excel to SQLite.
Example:
```bash
python3 ds_salaries_messy.py
```

### Executable file:
You can also create a simple executable file using the pyinstaller package.
```bash
pip install pyinstaller
pyinstaller --onefile --windowed Excel-SQLite-Converter.py
```

### MacOs Executable file:
You can also create a simple executable file with .command extension.
```bash
cd /Path/to/your/script
touch app.command
nano app.command
```
Then, in the app.command file, write the following:
```bash
cd "$(dirname "$0")"
python3 "$(dirname "$0")/Excel-SQLite_converter.py"
echo "App Ran Successfully!"
osascript -e 'tell application "Terminal" to close front window'
```
Save with ^X and close the file. Next, Run:
```bash
chmod +x app.command
```
You can now run the app.command file by cicking on it.


## Contributing

Contributions are welcome! Feel free to submit a pull request or open an issue if you find a bug or have a suggestion.
