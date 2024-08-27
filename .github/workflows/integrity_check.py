import json
from jsonschema import validators, validate

with open("schema.json", "r") as f:
    schema_data = json.load(f)
validators.validator_for(schema_data).check_schema(schema_data)

with open("exemple-valide.json", "r") as f:
    data = json.load(f)
validate(instance=data, schema=schema_data)
