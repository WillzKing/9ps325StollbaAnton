let kek = ['Kek','Billy','Harington','Welcom','club','Return'];
let lol = kek.filter(function(elem){
	if(elem.length > 5) {
		return true;
	} else {
		return false;
	}
});
document.write(lol);