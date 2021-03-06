import os
from flask import Flask, render_template, request, json,redirect, url_for, send_from_directory
import main

app = Flask(__name__)


@app.route('/')
def searchpage():
	return render_template('index.html')


@app.route('/load_ajax', methods=["GET", "POST"])
def load_ajax():
	if request.method == "POST":
		data =  request.get_json()
		fileNames = data['files']
		fileNames = [str(i) for i in fileNames]
		filedata = {}
		for file in fileNames:
			with open(file, 'r') as f:
				filedata[file] = f.read()
		main.x = fileNames
		main.runass()
		main.runlin()
		symTable = main.getSymTable()
		globTable = main.getGlobTable()
		extTable = main.getExtTable()
		pass1 = {}
		pass2 = {}
		iftable = main.getifTable()
		# print 'lol'
		# print iftable
		for file in fileNames:
			file = file.split('.')[0]
			with open(file+'.l') as f:
				pass1[file] = f.read()
			with open(file+'.li') as f:
				pass2[file] = f.read()
		with open(fileNames[0].split('.')[0]+'.ls') as f:
			lin = f.read()

		return json.dumps({'status':'OK' ,'pass1':pass1, 'pass2':pass2, 'lin':lin, 'symTable':symTable, 'globTable':globTable, 'extTable':extTable , 'ifTable': iftable, 'filedata':filedata})

@app.route('/loadSimulator', methods=["GET", "POST"])
def loadSimulator():
	if request.method == "POST":
		data = request.get_json()
		fileName = data['file']
		print data
		offset = data['offset']
		main.runload(int(offset))
		fileName = fileName+'.8085'
		main.runloader(fileName, offset)
		reg = main.getRegisters()
		memory = main.getMemlocs()
		stack = main.getStack()
		print stack
		return json.dumps({'status':'OK', 'reg':reg, 'memory':memory , 'stack':stack})


@app.route('/runSimulator', methods=["GET", "POST"])
def runSimulator():
	if request.method == "POST":
		main.runSimulator()
		reg = main.getRegisters()
		memory = main.getMemlocs()
		stack = main.getStack()
		print stack
		return json.dumps({'status':'OK', 'reg':reg, 'memory':memory , 'stack':stack})

if __name__=="__main__":
	app.run(host='0.0.0.0', debug=True)
