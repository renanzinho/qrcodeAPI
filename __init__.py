from flask import Flask
from consulta import parsing
import json

app = Flask(__name__)

@app.route('/<code>/<location>')
def consulta(code, location):
	location = ', '.join(location.split(' '))
	parsed = parsing(code,location)
	return json.dumps(parsed, indent=2, separators=(',', ': '))


if __name__ == '__main__':
    app.run(debug=True)

