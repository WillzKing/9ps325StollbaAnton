let kek = [-12364, -2346, 11, 265, 3345, -23485, 2345];
let lol = kek.filter(function(elem) {
	if (elem > 0) {
		return true;
	} else {
		return false;
	}
});
document.write(lol);