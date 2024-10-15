
## Description

The ETL Lineage Extractor is a program that extracts technical lineage from an XML file containing data exported from the Informatica PowerCenter ETL tool. The program creates a structure of database objects and Informatica objects, as well as tracks relationships between columns in these objects.

## Functionality

- Extracts database objects (tables and their columns) from the XML file.
- Extracts Informatica objects (transformations and their fields) from the XML file.
- Extracts relationships (lineage) between columns from database objects and Informatica objects.
- Saves the results in JSON format in output files.

## Requirements

- Python 3.x
- Libraries:
  - `xml.etree.ElementTree`
  - `json`
  - `pytest`

## If you are using PyCharm - it may propose you to automatically create venv for your project and install requirements in it, but if not:

    python -m venv venv
    venv\Scripts\activate (on Windows)
    source venv/bin/activate (on macOS)
    pip install -r requirements.txt

## Usage
Ensure that the input.XML file is located in the root directory of the project.
The results will be saved in JSON format in the output folder.

Run the program:
```bash
python main.py
