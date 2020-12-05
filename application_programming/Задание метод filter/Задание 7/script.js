let kek = [345, -345, 231, -345, 123, -234, -23456, -346, -321, 345];
let lol = kek.filter(function(elem){
	if(elem < 0 ) {
		return true;
	} else {
		return false;
	}
});
document.write(lol.length);