let km = ['джентельмены','шесть','чувство','theboys'];
let noug = km.map(function(elem) {
	return elem.split('').reverse().join('')
});
let i = 0;
let kekw = noug.length;
for (i = 0; i < kekw; i++){
     alert(noug[i]);
}
document.write(noug);