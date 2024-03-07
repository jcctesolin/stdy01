import owlready2 as owlr

#onto = owlr.get_ontology("http://test.org/onto.owl")
#o_hint = owlr.get_ontology("file:///home/dev/workdir/stdy01/ontoimport/onto/hint-r.rdf").load()
o_hint = owlr.get_ontology("https://purl.org/s2c2/hint").load()
#o_qvas = owlr.get_ontology("file:///home/dev/workdir/stdy01/ontoimport/onto/qvas-r.rdf").load()
#o_miscon = owlr.get_ontology("file:///home/dev/workdir/stdy01/ontoimport/onto/owlBase03112023.owl").load()
#o_gufo = owlr.get_ontology("file:///home/dev/workdir/stdy01/ontoimport/onto/gufo-r.rdf").load()
#o_gufo = owlr.get_ontology("http://purl.org/nemo/gufo").load()

#o_hint.name = "hint"
#o_qvas.name="qvas"
#o_miscon.name = "miscon"
#o_gufo.name = "gufo"
#print(o_hint.name)

#onto.imported_ontologies.append(o_hint)
#owlr.sync_reasoner_pellet()

print(list(o_gufo.imported_ontologies))
#print(list(onto.classes()))
#print(list(o_miscon.classes()))
#print(list(o_hint.classes()))
#print(list(o_qvas.classes()))
#print(o_gufo.name)
print(list(o_gufo.classes()))
