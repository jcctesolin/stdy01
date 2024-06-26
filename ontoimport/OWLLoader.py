from owlready2 import *
import os

FILE_PATH = os.path.dirname(os.path.abspath(__file__))

def loadOwlInstancesFile(filename):
    
    ref_onto = get_ontology(f"{FILE_PATH}/{filename}").load()
    ref_onto_imported = ref_onto.imported_ontologies[0]
    
    militaryList = []
    indvs = []

    land_speed = []
    water_speed = []
    sight = []
    Type = []
    Range = []
    num_nodes = 0

    for ind in ref_onto.individuals():
        if(ind.is_a[0]._name == "MilitaryPerson"):
            num_nodes += 1                          # Count military
            
            if(ind.isLocatedIn):
                military = {
                    "id" : ind.name,
                    "land_speed" : 95,
                    "water_speed" : 9,
                    "sight" : 1000,
                    "communicationDevice" : ind.operates[0]._name,
                    "interface" : ind.operates[0].hasInterface[0]._name,
                    "interfacePowerType" : ind.operates[0].hasInterface[0].hasInterfPowerType[0]._name,
                    "txPower" : ind.operates[0].hasInterface[0].hasInterfPowerType[0].Txpower[0],
                    "frequency" : ind.operates[0].hasInterface[0].hasInterfPowerType[0].Frequency[0],
                    "vehicleId" : ind.isLocatedIn[0]._name,
                    "belongsTo" : ind.isLocatedIn[0].belongsTo[0]._name,
                    "hasMOPowerType" : ind.isLocatedIn[0].belongsTo[0].hasMOPowerType[0]._name,
                    "subordinateTo" : ind.isLocatedIn[0].belongsTo[0].hasMOPowerType[0].MOTypeIsSubordinateTo[0]._name,
                }
                militaryList.append(military)
                
            else:
                military = {
                    "id": ind.name,
                    "land_speed": 95,
                    "water_speed": 9,
                    "sight": 1000,
                    "communicationDevice" : ind.operates[0]._name,
                    "interface" : ind.operates[0].hasInterface[0]._name,
                    "interfacePowerType" : ind.operates[0].hasInterface[0].hasInterfPowerType[0]._name,
                    "txPower" : ind.operates[0].hasInterface[0].hasInterfPowerType[0].Txpower[0],
                    "frequency" : ind.operates[0].hasInterface[0].hasInterfPowerType[0].Frequency[0],      
                }
                militaryList.append(military)
                

    print("\nPrinting all instances\n")
    for node in militaryList:
        print(node, "\n")
    

    return num_nodes, land_speed, water_speed, sight, Type, Range

# def load(filepath):
#     current_instance_file = get_ontology(filepath).load()
#     reference_ontology = get_ontology(current_instance_file.imported_ontologies[0].base_iri).load()
#     print(current_instance_file.imported_ontologies[1])
#     with current_instance_file:
#         print(reference_ontology)
#         vehicle = reference_ontology.Guarani(['1'])
                
#         sync_reasoner_pellet(infer_property_values=True, infer_data_property_values = True)

#         current_instance_file.save(format = "rdfxml")
            

if __name__ == "__main__":
    loadOwlInstancesFile("newScenario.owl")