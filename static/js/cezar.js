
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

function graph(){
	// count each letter and convert in to arrays of objects
	write = document.getElementById('write').value;
	writeArray = write.split('');	
	var graphData = writeArray.reduce(function(acc, el) {
  		acc[el] = (acc[el] || 0) + 1;
  		return acc;
	}, {});

	graphDataPoint = []

for (key in graphData){
	graphDataPoint.push({y: graphData[key], label: key});
}
	// paint diagram

    var chart = new CanvasJS.Chart("chartContainer",
    {
      title:{
        text: "Частотная диаграмма символов"   
      },
      animationEnabled: true,
      axisY: {
        title: "Количество"
      },
      legend: {
        verticalAlign: "bottom",
        horizontalAlign: "center"
      },
      theme: "theme2",
      data: [

      {        
        type: "column",  
        showInLegend: true, 
        legendMarkerColor: "grey",
        legendText: "Символы",
        dataPoints: graphDataPoint
      }   
      ]
    });

    chart.render();
  }




