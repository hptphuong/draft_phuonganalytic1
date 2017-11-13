	(function() {
	    var O = window,
	        M = document;

	    var qa = function(a) { // return true if string * not undefine
	            return void 0 != a && -1 < (a.constructor + "").indexOf("String")
	        },
	        sa = function(a) { //remove whitespace at begin and end string
	            return a ? a.replace(/^[\s\xa0]+|[\s\xa0]+$/g, "") : ""
	        };
	    if (!O['FsoftAnalyticsObject']) return void!0;
	    var ee = function() {
	        this.keys = [];
	        this.values = {};
	        this.m = {}
	    };
	    ee.prototype.set = function(a, b, c) {
	        this.keys.push(a);
	        c ? this.m[":" + a] = b : this.values[":" + a] = b
	    };
	    ee.prototype.get = function(a) {
	        return this.m.hasOwnProperty(":" + a) ? this.m[":" + a] : this.values[":" + a]
	    };
	    ee.prototype.map = function(a) {
	        for (var b = 0; b < this.keys.length; b++) {
	            var c = this.keys[b],
	                d = this.get(c);
	            d && a(c, d)
	        }
	    }

	    // Declare $fsaCore
	    $fsaCore = function() {
	        var fName = [];
	        var fImp = [];
	        var trackers = [];


	        this.createFunc = function(f_name, f_imp) {
	            if (typeof f_name != "string" || typeof f_imp != "function") return void!0;
	            fName.push(f_name);
	            fImp[':' + f_name] = f_imp;
	        }
	        this.getF = function(f_name) {
	            if (fName.includes(f_name))
	                return fImp[":" + f_name];
	        }
	        this.setTracker = function(tracker) {
	            trackers.push(tracker);
	        };
	        this.getTrackerAll = function() {
	            return trackers;
	        }


	    }
	    fsaCore = new $fsaCore;

	    fsaCore.createFunc("create", function() {

	        if (arguments.length < 2) {
	            return;
	        }
	        tracker = new ee;
	        // fsaCore.inf['tid'] = arguments[1]
	        if (arguments[2] == 'auto' || arguments[2] == void!0)
	            m_name = "t0";
	        tracker.set("name", m_name);
	        tracker.set("tid", arguments[1]);
	        fsaCore.setTracker(tracker);
	        // if (void 0 != arguments[2] && arguments[2] == 'auto') {
	        //     createFsa_Fsid.apply(fsaCore, arguments);
	        //     return
	        // }


	    })

	    // var gb = qa(window.FsoftAnalyticsObject) && sa(window.FsoftAnalyticsObject) || "fsa";
	    // // Get queues for first instance
	    // if (O[gb].q) queues = O[gb].q;

	    // O[gb] = function(a) {
	    //     if (fsaCore.check(a)) {
	    //         fsaCore.f_imp[a].apply(fsaCore.f_imp[a], arguments);
	    //     };
	    // };

	    // for (i = 0; i < queues.length; i++) {
	    //     O[gb].apply(O[gb], queues[i]);
	    // }



	})(window);