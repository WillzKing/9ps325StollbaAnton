var cifri = [83,23841,347,12];
var kekw = 0;
cifri.forEach(function(element, index, array){
	array[index] = element* element;
	kekw += array[index]
});
alert(kekw);