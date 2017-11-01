(function(){
	var O=window,
		M=document;
	var qa = function(a) {// return true if string * not undefine
        return void 0 != a && -1 < (a.constructor + "").indexOf("String")},
        sa=function(a) {//remove whitespace at begin and end string
        return a ? a.replace(/^[\s\xa0]+|[\s\xa0]+$/g, "") : ""
    	};
    var $core=function(a){
        this.f=[];
        this.f_imp=[];
        this.inf={};
    }
    $core.prototype.set=function(a){
        this.f.push(a);
        console.log("insertd:"+a);
        console.log(this.f);
    }
    // /// first intialize
    $core.prototype.check=function(a,func){
        return this.f.includes(a);
    }
    core = new $core;
    function setCookie(){
    	// document.cookie = "username=John Doe; expires=Thu, 18 Dec 2013 12:00:00 UTC; path=/";
    	m_path=M.location.pathname;
    	expiration_date = new Date();
    	expiration_date.setFullYear(expiration_date.getFullYear()+2);
    	
    	document.cookie="_fsa=1."+M.location.host.match(/\./g).length+"."+Math.floor(Date.now() / 1000)+"; expires="+expiration_date.toUTCString()+";path=/";
    }
    function createImage(){
    	var img = new Image,
    	url = encodeURIComponent(M.location.pathname),
      	title = encodeURIComponent(M.title),
      	ref = encodeURIComponent(M.referrer);
      	img.src = 'http://127.0.0.1:8000/a.gif?url=' + url + '&t=' + title + '&ref=' + ref +'&tid='+core.inf['tid'];
    }
    // create function
    // just simple with tracking id & 
    core.set('create');
    core.f_imp['create']=function(a){
    	if (arguments.length<2){
    		return;
    	}
    	core.inf['tid']=arguments[1]
    	if(void 0 !=arguments[2] && arguments[2]=='auto'){
    		setCookie.apply(core,arguments);
    	}
    	
    }
    
    core.set('send');
    core.f_imp['send']=function(a){
    	// use basic with pageview
    	createImage();
    	
    }
    ////
	var gb = qa(window.FsoftAnalyticsObject) && sa(window.FsoftAnalyticsObject) || "fsa";
	O[gb]=function(a){
        if (core.check(a)){
            core.f_imp[a].apply(core.f_imp[a],arguments);
        };
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