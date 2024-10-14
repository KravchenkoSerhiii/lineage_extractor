def extract_lineage(root):
    db_objects = {}
    informatica_objects = {}
    column_lineage = []

    for source in root.findall(".//SOURCE"):
        db_name = source.attrib["NAME"]
        db_type = source.attrib["DATABASETYPE"]

        if db_name not in db_objects:
            db_objects[db_name] = {}

        columns = {}
        for field in source.findall(".//SOURCEFIELD"):
            column_name = field.attrib["NAME"]
            column_id = len(columns) + 1
            columns[column_name] = {"id": column_id}
        db_objects[db_name].update({'columns': columns})

    for mapping in root.findall(".//MAPPING"):
        mapping_name = mapping.attrib["NAME"]
        informatica_objects[mapping_name] = {}

        for transformation in mapping.findall(".//TRANSFORMATION"):
            transform_name = transformation.attrib["NAME"]
            transform_fields = {}
            for field in transformation.findall(".//TRANSFORMFIELD"):
                transform_fields[field.attrib["NAME"]] = {'id': len(transform_fields) + 1}
            informatica_objects[mapping_name][transform_name] = transform_fields

    for connector in root.findall(".//CONNECTOR"):
        from_field = connector.attrib["FROMFIELD"]
        to_field = connector.attrib["TOFIELD"]
        column_lineage.append((from_field, to_field))

    return db_objects, informatica_objects, column_lineage
