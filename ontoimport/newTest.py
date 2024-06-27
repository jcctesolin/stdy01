from owlready2 import *

filename = "ScenarioNewWithHint"

FILE_PATH = os.path.dirname(os.path.abspath(__file__))

def create(): 
    try:
        mil_onto = get_ontology("https://raw.githubusercontent.com/jcctesolin/stdy01/dev/ontoimport/onto/miscon-r.rdf").load()
        nwk_base_onto =  get_ontology("https://raw.githubusercontent.com/jcctesolin/stdy01/dev/ontoimport/onto/hintv3-r.rdf").load() # ontologia de rede (Julio)
        msr_base_onto =  get_ontology("https://raw.githubusercontent.com/jcctesolin/stdy01/dev/ontoimport/onto/qvas-r.rdf").load() # ontologia de rede (Julio)
    except Exception as e:
        print(f"Exceção é: {e}")

    new_onto = get_ontology(f"file://{FILE_PATH}/{filename}.owl")
    new_onto.imported_ontologies.append(mil_onto)
    new_onto.imported_ontologies.append(nwk_base_onto)
    new_onto.imported_ontologies.append(msr_base_onto)

    # Instances
    with new_onto:    
        mp= mil_onto.MilitaryPerson("m1")
        cd= nwk_base_onto.CommDevice("cd01")
        meas = msr_base_onto.SQVA("sqva01")
        mp.carries.append(cd)
        sync_reasoner_pellet(infer_property_values=True, infer_data_property_values = True)
    
    new_onto.save(format = "rdfxml")
    
def load():
    print("\n\n\n\n\n-------------> LENDO ARQUIVOS <--------------------")
    current_instance_file = get_ontology(f"{FILE_PATH}/{filename}.owl").load()
    
    with current_instance_file:
        for property in current_instance_file.imported_ontologies: # AQUI da pra filtrar por tudo que quiseres consultar
            print(property)
            
create()
load()