let kek = [-1345, 0, 1234, 2356, 3, 9, 1340, 100, 2, 5];
let lol = kek.filter(function(elem) {
	if (elem > 0  && elem < 10) {
		return true;
	} else {
		return false;
	}
});
document.write(lol);