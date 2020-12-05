let kek = [0,10,12,-54,-23,14,5,1,2,3];
let lol = kek.filter(function(elem, index) {
	if ((elem * index) < 30) {
		return true;
	} else {
		return false;
	}
});
document.write(lol);