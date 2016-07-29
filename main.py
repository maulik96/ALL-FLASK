import ass,lin,loader,sim

x = []


def runass():
	ass.pass1(x)

def runlin():
	lin.linker(x)

def runload(offset=0):
	loader.loader(x, offset)
	sim.reg['PC'] = offset

def getSymTable():
	return ass.symTable

def getGlobTable():
	return ass.globTable

def getExtTable():
	return ass.extTable

def getifTable():
	return ass.ifTable

def runloader(file, offset=0):
	sim.load(file, offset)

def runSimulator():
	sim.callbackf()

def getRegisters():
	return sim.reg

def getStack():
	return sim.stack

def getMemlocs():
	return sim.memory