import owlready2 as owlr

o_miscon = owlr.get_ontology("https://raw.githubusercontent.com/jcctesolin/stdy01/dev/ontoimport/onto/miscon-r.rdf").load()

o_miscon.name = "miscon"

print(list(o_miscon.imported_ontologies))

print(list(o_miscon.classes()))
