var G3 = {

    game: null,

    // elements
    el: {

    },

    // events
    ev: {
        // of the form
        // eventName elQuery: functionInG3.f
        'click .playButton': 'playGame',
        'click .pauseButton': 'pauseGame',
        'click .stopButton': 'stopGame',
        'click .restartButton': 'restartGame',

        'keypress': 'interpretKeyboardEvent',
    },

    // functions
    f: {

        interpretKeyboardEvent(evt) {
            switch (evt.keyCode) {
                case 32:
                  G3.f.playPause();
                  break;
                case 37:
                  G3.f.sendCommandToGame('left');
                  break;
                case 38:
                  G3.f.sendCommandToGame('up');
                  break;
                case 39:
                  G3.f.sendCommandToGame('right');
                  break;
                case 40:
                  G3.f.sendCommandToGame('down');
                  break;
                case 82:
                  G3.f.restartGame();
                  break;
            }
        },

        sendCommandToGame(cmd) {
            G3.game.gameQueue.push(cmd);
        },

        playPause() {
            if (G3.game.playing) {
                G3.f.pauseGame();
            } else {
                G3.f.playGame();
            }
        },

        playGame() {
            G3.game.play();
        },

        pauseGame() {
            G3.game.pause();
        },

        stopGame() {
            G3.game.pause();
        },

        restartGame() {
            G3.game = new Game();
        },

    },

    // messages
    m: {

    },

};

G3.init = function() {

    // instantiate game objects, etc.
    G3.game = new Game();

    // add event listeners
    Object.keys(G3.ev).forEach(function(identifier) {
        var eventName = identifier.split(' ')[0],
            selector = identifier.split(' ').splice(1).join(' '),
            fn = G3.f[G3.ev[identifier]];

        G3Utils.eventAdder(selector, eventName, fn);
    });

    // serviceWorker check
    // if ('serviceWorker' in navigator) {
    //     navigator.serviceWorker.register('sw.js').then(function(registration) {
    //         console.log('Service worker registration successful');
    //     }).catch(function(err) {
    //         console.error('Service worker registration failed', err);
    //     });
    // }

    console.info('G3 initialized');

    // start the requestAnimationFrame loop here

};

G3.init();
