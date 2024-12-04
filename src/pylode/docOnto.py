from pathlib import Path
from pylode import OntPub

#onto_file=Path.cwd().joinpath('composedLink8v2.ttl')
onto_file=Path('/home/dev/workdir/s2c2/miscon.ttl')
#onto_file=Path('/home/dev/workdir/s2c2/*.ttl')
html_file=Path('/home/dev/workdir/stdy01/src/pylode/miscon.html')
print(onto_file)
OntPub(onto_file).make_html(destination=html_file,include_css=False)