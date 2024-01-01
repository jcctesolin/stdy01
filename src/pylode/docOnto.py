from pathlib import Path
from pylode import OntPub

onto_file=Path.cwd().joinpath('composedLink8v2.ttl')
html_file=Path.cwd().joinpath('composedLink8v2.html')
print(onto_file)
OntPub(onto_file).make_html(destination=html_file)