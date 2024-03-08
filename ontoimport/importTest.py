import owlready2 as owlr

print(list(owlr.onto_path))

o_sim = owlr.get_ontology("http://example.org/ex01")
o_hint = owlr.get_ontology("file:///home/dev/workdir/stdy01/ontoimport/onto/hintv3-r.rdf").load()

#o_hint = owlr.get_ontology("https://raw.githubusercontent.com/jcctesolin/stdy01/dev/ontoimport/onto/hintv3-r.rdf").load()
#o_qvas = owlr.get_ontology("file:///home/dev/workdir/stdy01/ontoimport/onto/qvas-o.owl").load()
o_miscon = owlr.get_ontology("file:///home/dev/workdir/stdy01/ontoimport/onto/miscon-r.rdf").load()
o_gufo = owlr.get_ontology("file:///home/dev/workdir/stdy01/ontoimport/onto/gufo-r.rdf").load()
#o_gufo = owlr.get_ontology("https://raw.githubusercontent.com/jcctesolin/stdy01/dev/ontoimport/onto/gufo-o.owl").load()

o_hint.name = "hint"
#o_qvas.name = "qvas"
o_miscon.name = "miscon"
o_gufo.name = "gufo"
#print(o_hint.name)

#onto.imported_ontologies.append(o_hint)
#o_miscon.imported_ontologies.append(o_hint)
o_sim.imported_ontologies.append(o_gufo)
o_sim.imported_ontologies.append(o_miscon)
o_sim.imported_ontologies.append(o_hint)
#owlr.sync_reasoner_pellet()

#print(list(o_hint.imported_ontologies))
print(list(o_sim.imported_ontologies))
#print(list(onto.classes()))
print(list(o_sim.classes()))
#print(list(o_hint.classes()))
#print(list(o_qvas.classes()))
#print(o_gufo.name)
#print(list(o_gufo.classes()))
#print(o_hint.SelectedBond.ancestors())
o_sim.save(file = "/home/dev/workdir/stdy01/ontoimport/onto/ex01.rdf", format = 'rdfxml')