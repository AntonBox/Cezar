
function codeText(){
	rotate = document.getElementById('rotate').value;
	write = document.getElementById('write').value;
	dataToSend = JSON.stringify({code: write, rotate: rotate});
	$.post('/code/', dataToSend, pasteCodedText, "json").error(function() { alert("Введите корректное число 0-26"); });
}

function uncodeText(){
	rotate = document.getElementById('rotate').value;
	write = document.getElementById('write').value;
	dataToSend = JSON.stringify({code: write, rotate: rotate});
	$.post('/uncode/', dataToSend, pasteCodedText, "json").error(function() { alert("Введите корректное число 0-26"); });
}

function pasteCodedText(data){
	document.getElementById("read").innerHTML = data;
}