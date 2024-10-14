from parser import parse_xml
from extractor import extract_lineage
from saver import save_json


def main():
    source_data = parse_xml("input.xml")

    db_objects, informatica_objects, column_lineage = extract_lineage(source_data)

    save_json("output/db_objects.json", db_objects)
    save_json("output/informatica_objects.json", informatica_objects)
    save_json("output/column_lineage.json", column_lineage)


if __name__ == "__main__":
    main()
