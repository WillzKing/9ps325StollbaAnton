let arr = [126797, 5435, 2, 124, 345];
let lol = arr.map(function(elem) {
	return Math.sqrt(elem)
});
let i = 0;
let kekw = lol.length;
for (i = 0; i < kekw; i++){
     alert(lol[i]);
}
document.write(lol);