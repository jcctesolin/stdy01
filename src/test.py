import owlready2

# go = owlready2.get_ontology("http://purl.obolibrary.org/obo/go.owl").load() # (~ 170 Mb), can take a moment!


list(owlready2.default_world.classes())

#list(owlready2.default_world.sparql("""
#           SELECT (COUNT(?x) AS ?nb)
#           { ?x a owl:Class . }
#    """))
