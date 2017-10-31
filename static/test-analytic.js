(function(){
	var O=window,
		M=document;
	var qa = function(a) {// return true if string * not undefine
        return void 0 != a && -1 < (a.constructor + "").indexOf("String")},
        sa=function(a) {//remove whitespace at begin and end string
        return a ? a.replace(/^[\s\xa0]+|[\s\xa0]+$/g, "") : ""
    	};
    var fq=[]; //function queque
    fq['create'] = function(a){
    	var tam = 1;
    	tam+=1;
    }
	var gb = qa(window.FsoftAnalyticsObject) && sa(window.FsoftAnalyticsObject) || "fsa";
	O[gb]=function(a){

		fq[a](arguments);


	};

    // return "http://127.0.0.1:8000/"
})(window);




// (function(i, s, o, g, r, a, m) {
//     i['FsoftAnalyticsObject'] = r;
//     i[r] = i[r] || function() {
//         (i[r].q = i[r].q || []).push(arguments)
//     }
//     ,
//     i[r].l = 1 * new Date();
//     a = s.createElement(o),
//     m = s.getElementsByTagName(o)[0];
//     a.async = 1;
//     a.src = g;
//     m.parentNode.insertBefore(a,m)
    
// }
// )(window, document, 'script', 'http://127.0.0.1:8000/static/test-analytic.js', 'fsa');