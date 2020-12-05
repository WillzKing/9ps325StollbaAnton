let kek = [2, [12,5], 100, 543, [234,12], 2345];
let lol = kek.filter(function(elem){
	if(Array.isArray(elem)) {
		return false;
	} else {
		return true;
	}
});
document.write(lol);