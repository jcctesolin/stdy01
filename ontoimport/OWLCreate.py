from owlready2 import *

owl_file_instance_name = "newScenario"

FILE_PATH = os.path.dirname(os.path.abspath(__file__))

def create_instance_file(instanciate_items:list): 
    try:
        #base_onto = get_ontology("https://raw.githubusercontent.com/jcctesolin/stdy01/dev/ontoimport/onto/miscon-r2.rdf").load()
        base_onto = get_ontology("https://raw.githubusercontent.com/jcctesolin/s2c2/main/rdfxml/miscon").load()
        network_base_onto =  get_ontology("https://raw.githubusercontent.com/jcctesolin/s2c2/main/rdfxml/hint").load() # ontologia de rede (Julio)
        measure_base_onto =  get_ontology("https://raw.githubusercontent.com/jcctesolin/s2c2/main/rdfxml/qvas").load() # ontologia de rede (Julio)
    except Exception as e:
        print(f"Exceção é: {e}")

    new_onto = get_ontology(f"file://{FILE_PATH}/{owl_file_instance_name}.owl") #Create OWL

    new_onto.imported_ontologies.append(base_onto)
    new_onto.imported_ontologies.append(network_base_onto)
    new_onto.imported_ontologies.append(measure_base_onto)

    # Instances 
    with new_onto:
        
        for item in instanciate_items:
            if 'nameOverlord' in item: # MO Root
                print(item)
                mo = getattr(base_onto, item['typeMO'])(item['nameMO'])
                
                if item['nameOverlord'] != 'Nobody': # MO not root
                    mo.isSubordinateTo = [getattr(new_onto, item['nameOverlord'])]
                
            else:
                if 'plataform_id' in item: # Platform
                    platform = getattr(base_onto, item['typePlatform'])(item['typePlatform']+str(item['plataform_id']))
                    platform.belongsTo = [getattr(new_onto, item['nameMO'])]
                    
                else: # Military
                    device = network_base_onto.CommDevice("cd01") ## Adicionar interfaces para o primeiro militar de cada OM.
                    
                    if 'byFoot' in item:
                        military = base_onto.MilitaryPerson(item['id'])
                        military.militaryPersonHasMilitaryOrganization = [getattr(new_onto, item['nameMO'])]
                        
                        
                        if item['byFoot'] == False:
                            military.isLocatedIn = [getattr(new_onto, (item['typePlatform']+str(item['platformId'])))]
                            
                        else:
                            continue
                                         
            
    sync_reasoner_pellet(infer_property_values=True, infer_data_property_values = True)
    new_onto.save(format = "rdfxml")
    
def load(owl_file_name: str) -> list:
    print("\n\n\n\n\n-------------> LENDO ARQUIVOS <--------------------")
    current_instance_file = get_ontology(f"{FILE_PATH}/{owl_file_instance_name}.owl").load()
    
    with current_instance_file:
        for property in current_instance_file.imported_ontologies: # AQUI da pra filtrar por tudo que quiseres consultar
            print(property)
            
if __name__ == "__main__":        
    create_instance_file(
         [
         {'nameMO': '1PL', 'typeMO': 'Platoon', 'nameOverlord': 'Nobody', 'typeOverlord': 'Nobody', 'nMilitary': 20},
         {'nameMO': '2PL', 'typeMO': 'Platoon', 'nameOverlord': 'Nobody', 'typeOverlord': 'Nobody', 'nMilitary': 20},
         {'nameMO': '1BT', 'typeMO': 'BattleGroup', 'nameOverlord': '1PL', 'typeOverlord': 'Platoon', 'nMilitary': 5},
         {'nameMO': '2BT', 'typeMO': 'BattleGroup', 'nameOverlord': '1PL', 'typeOverlord': 'Platoon', 'nMilitary': 5},
         {'nameMO': '3BT', 'typeMO': 'BattleGroup', 'nameOverlord': '1PL', 'typeOverlord': 'Platoon', 'nMilitary': 5},
         {'nameMO': '4BT', 'typeMO': 'BattleGroup', 'nameOverlord': '2PL', 'typeOverlord': 'Platoon', 'nMilitary': 5},
         {'nameMO': '5BT', 'typeMO': 'BattleGroup', 'nameOverlord': '2PL', 'typeOverlord': 'Platoon', 'nMilitary': 5},
         {'nameMO': '6BT', 'typeMO': 'BattleGroup', 'nameOverlord': '1PL', 'typeOverlord': 'Platoon', 'nMilitary': 5},
         {'nameMO': '8BTW3', 'typeMO': 'BattleGroup', 'nameOverlord': '2PL', 'typeOverlord': 'Platoon', 'nMilitary': 3},
         {'plataform_id': 0, 'nameMO': '1BT', 'typeMO': 'BattleGroup', 'typePlatform': 'Urutu', 'nInsidePlatform': 3, 'nOutsidePlatform': 0},
         {'plataform_id': 1, 'nameMO': '1BT', 'typeMO': 'BattleGroup', 'typePlatform': 'Urutu', 'nInsidePlatform': 2, 'nOutsidePlatform': 0},
         {'plataform_id': 2, 'nameMO': '6BT', 'typeMO': 'BattleGroup', 'typePlatform': 'Guarani', 'nInsidePlatform': 4, 'nOutsidePlatform': 1},
         {'plataform_id': 3, 'nameMO': '8BTW3', 'typeMO': 'BattleGroup', 'typePlatform': 'Urutu', 'nInsidePlatform': 2, 'nOutsidePlatform': 0},
         {'id': 0, 'nameMO': '1BT', 'typeMO': 'BattleGroup', 'typePlatform': 'Urutu', 'platformId': 0, 'byFoot': False},
         {'id': 1, 'nameMO': '1BT', 'typeMO': 'BattleGroup', 'typePlatform': 'Urutu', 'platformId': 0, 'byFoot': False},
         {'id': 2, 'nameMO': '1BT', 'typeMO': 'BattleGroup', 'typePlatform': 'Urutu', 'platformId': 0, 'byFoot': False},
         {'id': 3, 'nameMO': '1BT', 'typeMO': 'BattleGroup', 'typePlatform': 'Urutu', 'platformId': 1, 'byFoot': False},
         {'id': 4, 'nameMO': '1BT', 'typeMO': 'BattleGroup', 'typePlatform': 'Urutu', 'platformId': 1, 'byFoot': False},
         {'id': 5, 'nameMO': '6BT', 'typeMO': 'BattleGroup', 'typePlatform': 'Guarani', 'platformId': 2, 'byFoot': False},
         {'id': 6, 'nameMO': '6BT', 'typeMO': 'BattleGroup', 'typePlatform': 'Guarani', 'platformId': 2, 'byFoot': False},
         {'id': 7, 'nameMO': '6BT', 'typeMO': 'BattleGroup', 'typePlatform': 'Guarani', 'platformId': 2, 'byFoot': False},
         {'id': 8, 'nameMO': '6BT', 'typeMO': 'BattleGroup', 'typePlatform': 'Guarani', 'platformId': 2, 'byFoot': False},
         {'id': 9, 'nameMO': '6BT', 'typeMO': 'BattleGroup', 'typePlatform': 'Guarani', 'platformId': 2, 'byFoot': True},
         {'id': 10, 'nameMO': '8BTW3', 'typeMO': 'BattleGroup', 'typePlatform': 'Urutu', 'platformId': 3, 'byFoot': False},
         {'id': 11, 'nameMO': '8BTW3', 'typeMO': 'BattleGroup', 'typePlatform': 'Urutu', 'platformId': 3, 'byFoot': False},
         ]
     )
    load(owl_file_instance_name)