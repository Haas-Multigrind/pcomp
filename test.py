import json
from jsonschema import validate

schema_str = open('pcomp_schema.json','r').read()
schema = json.loads(schema_str)

path = '.'
file = 'Tannenbaumfraeser12_grinddate'


j_str = open(f'{path}/{file}.json', 'r').read()
pcomp = json.loads(j_str)

validate(instance=pcomp,schema=schema)
## hier ggf. echten UnitTest

NrOfPoints = pcomp['NominalValues']['NrOfPoints']

if NrOfPoints!=len(pcomp['NominalValues']['Values']):
    raise Exception("NrOfPoints in Nominal Values does not fit!")


for key,val in pcomp['ActualValues'].items():
    if NrOfPoints!=len(val['Values']):
        raise Exception(f"NrOfPoints in {key} AcutalValues does not fit!")


print(f'json-file {file} ok!')