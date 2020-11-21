let arr = ['123', '456', '789'];
let kek = arr.map(function(elem) {
	return elem.split('')
});
let i = 0;
let kekw = kek.length;
for (i = 0; i < kekw; i++){
     alert(kek[i]);
}
document.write(kek);