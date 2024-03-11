from owlready2 import *

owl_file_instance_name = "ScenarioNewWithHint"

def create(): 
    try:
        base_onto = get_ontology("https://raw.githubusercontent.com/ProjetoS2C2Redes/S2C2-TestReferenceFiles/main/owlBase03112023.owl").load()
        network_base_onto =  get_ontology("https://raw.githubusercontent.com/ProjetoS2C2Redes/S2C2-TestReferenceFiles/main/hint.owl").load() # ontologia de rede (Julio)
        measure_base_onto =  get_ontology("https://raw.githubusercontent.com/ProjetoS2C2Redes/S2C2-TestReferenceFiles/main/qvas.owl").load() # ontologia de rede (Julio)
    except Exception as e:
        print(f"Exceção é: {e}")

    
    new_onto = get_ontology(f"file://{owl_file_instance_name}.owl") #CRIA o novo arquivo de ontologia nesse path, trocar para qual quiseres utilizar.

    new_onto.imported_ontologies.append(base_onto)
    new_onto.imported_ontologies.append(network_base_onto)
    new_onto.imported_ontologies.append(measure_base_onto)

    with new_onto:
        
        mp = base_onto.MilitaryPerson("m1")
        sync_reasoner_pellet(infer_property_values=True, infer_data_property_values = True)

    new_onto.save(format = "rdfxml")
    
def load():
    print("\n\n\n\n\n-------------> LENDO ARQUIVOS <--------------------")
    current_instance_file = get_ontology(f"{owl_file_instance_name}.owl").load()
    
    with current_instance_file:
        for property in current_instance_file.imported_ontologies: # AQUI da pra filtrar por tudo que quiseres consultar
            print(property)
            
create()
load()