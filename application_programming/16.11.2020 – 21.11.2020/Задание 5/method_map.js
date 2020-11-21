let arbidol = [312387, 376, 9123,];
let valerik = arbidol.map(function(elem, index) {
	return elem * index;
});
let i = 0;
let kekw = valerik.length;
for (i = 0; i < kekw; i++){
     alert(valerik[i]);
}
document.write(valerik);