import json
import os
import logging
from jsonschema import validators, validate

with open("schema.json", "r") as f:
    schema_data = json.load(f)
validators.validator_for(schema_data).check_schema(schema_data)

if "exemple-valide.json" in os.listdir():
    with open("exemple-valide.json", "r") as f:
        data = json.load(f)
    validate(instance=data, schema=schema_data)

else:
    logging.warning('No example file to validate, consider adding one')
