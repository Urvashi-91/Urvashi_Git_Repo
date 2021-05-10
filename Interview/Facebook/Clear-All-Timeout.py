'''
let id = setTimeout(callback, delay);
clearTimeout(id);

setTimeout(callback, delay);
setTimeout(callback, delay);
setTimeout(callback, delay);
// implement clearAllTimeout();
'''
def seTimeout(callback, delay):
    pass

def clearTimeout(self,ID):
    pass

oldTimeout = window.setTimeout;
allTimeout = [];

window.setTimeout = function(callback, delay) {
	let id = oldTimeout(callback, delay);
	allTimeout.push(id);
	return id;
}

function creallAllTimeout() {
	allTimeout.forEach(id => clearTimeout(id));
	allTimeout = [];
}