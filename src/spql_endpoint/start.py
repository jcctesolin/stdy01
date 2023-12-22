import flask

from owlready2 import *
from owlready2.sparql.endpoint import *

# Load one or more ontologies
go = get_ontology("http://purl.obolibrary.org/obo/go.owl").load() # (~ 170 Mb), can take a moment!

app = flask.Flask("Owlready_sparql_endpoint")
endpoint = EndPoint(default_world)
app.route("/sparql", methods = ["GET"])(endpoint)

# Run the server with Werkzeug; you may use any other WSGI-compatible server
import werkzeug.serving
werkzeug.serving.run_simple("localhost", 5000, app)