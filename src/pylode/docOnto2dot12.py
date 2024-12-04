import pylode
from pathlib import Path

# html = pylode.MakeDocco(
#     input_data_file=input_file_path,
#     outputformat="html",
#     profile="ontdoc"
# ).document()


#input_data_file=Path('/home/dev/workdir/s2c2/qvas.ttl')
input_data_file='/home/dev/workdir/s2c2/qvas.ttl'
pylode.MakeDocco(input_data_file,outputformat="html",profile="ontdoc",).document()
pylode.MakeDocco(input_data_file,outputformat="md",profile="ontdoc",).document()
