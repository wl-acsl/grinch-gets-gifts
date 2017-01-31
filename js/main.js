var G3 = {

    // elements
    el: {

    },

    // events
    ev: {
        // of the form
        // eventName elQuery: functionInG3.f
    },

    // functions
    f: {

    },

    // messages
    m: {

    }

};

G3.init = function() {

    // add event listeners
    Object.keys(G3.ev).forEach(function(identifier) {
        var eventName = identifier.split(' ')[0],
            selector = identifier.split(' ').splice(1).join(' '),
            fn = G3.f[G3.ev[identifier]];

        G3Utils.eventAdder(selector, eventName, fn);
    });

    // serviceWorker check
    if ('serviceWorker' in navigator) {
        navigator.serviceWorker.register('sw.js').then(function(registration) {
            console.log('Service worker registration successful');
        }).catch(function(err) {
            console.error('Service worker registration failed', err);
        });
    }

    console.info('G3 initialized');

};

G3.init();
