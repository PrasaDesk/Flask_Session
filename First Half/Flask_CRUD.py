from flask import Flask, jsonify, request #import objects from the Flask model
app = Flask(__name__) #define app using Flask

languages = [{'id': 1,'name' : 'JavaScript'}, {'id': 2,'name' : 'Python'}, {'id': 1,'name' : 'Ruby'}]


@app.route('/', methods=['GET'])
def test():
	return jsonify({'message' : 'It works!'})


@app.route('/lang', methods=['GET'])
def returnAll():
	return jsonify({'languages' : languages})


@app.route('/lang/<string:id>', methods=['GET'])
def returnOne(id):
	langs = [language for language in languages if language['id'] == int(id)]
	return jsonify({'language' : langs[0]})


@app.route('/lang', methods=['POST'])
def addOne():
	print(request.json)
	language = {'id': request.json['id'], 'name' : request.json['name']}

	languages.append(language)
	return jsonify({'msg': 'Language has been added.!'})


@app.route('/lang/<string:id>', methods=['PUT'])
def editOne(id):
	langs = [language for language in languages if language['id'] == int(id)]
	langs[0]['name'] = request.json['name']
	return jsonify({'language' : langs[0]})


@app.route('/lang/<string:id>', methods=['DELETE'])
def removeOne(id):
	lang = [language for language in languages if language['id'] == int(id)]
	languages.remove(lang[0])
	return jsonify({'languages' : languages})

if __name__ == '__main__':
	app.run(debug=True, port=8080) #run app on port 8080 in debug mode
