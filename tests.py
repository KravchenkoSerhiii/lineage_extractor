import pytest
import json

from parser import parse_xml
from extractor import extract_lineage
from saver import save_json


@pytest.fixture
def xml_root():
    return parse_xml("input.XML")


def test_parse_xml():
    root = parse_xml("input.XML")
    assert root.tag == "POWERMART"


def test_extract_lineage(xml_root):
    db_objects, informatica_objects, column_lineage = extract_lineage(xml_root)

    assert "DimProduct" in db_objects
    assert "ProductKey" in db_objects["DimProduct"]["columns"]

    assert "m_refine_customersalesreport" in informatica_objects
    assert "SQ_FactInternetSales" in informatica_objects["m_refine_customersalesreport"]


def test_save_json(tmp_path):
    data = {"test_key": "test_value"}
    json_file_path = tmp_path / "test_output.json"
    save_json(json_file_path, data)

    with open(json_file_path) as f:
        loaded_data = json.load(f)
    assert loaded_data == data


if __name__ == "__main__":
    pytest.main()
