// G3 object definitions

const GAME_SETTINGS = {
    GIFT_COUNT: 5,
    GRAVITY: 5, // d.i.pixels per rAP frame
    COLLISION_DIST: 100, // pixels
    POINTS_PER_GIFT: 3,

    JUMP: 12, // d.i.pixels per rAP frame
    SLIDE: 8, // d.i.pixels per rAP frame
};

class Game {

    constructor(options) {
        // initialize game
        this.geometry = {
            y: options.geometry.y || window.innerHeight,
            x: options.geometry.x || window.innerWidth
        };
        this.score = options.startScore || 0;
        this.time = options.startTime || 0;
        this.commandQueue = [];
        this.playing = false;
        this.GIFT_COUNT = options.GIFT_COUNT || GAME_SETTINGS.GIFT_COUNT; // max number of gifts on screen at once

        this.animator = null; // rAP variable

        // initialize characters and game objects
        this.scoreboard = new GameScoreBoard({
            game: this
        });
        this.grinch = new Grinch({
            position: {
                x: this.geometry.x / 2,
                y: 0
            },
            game: this
        });
        this.gifts = [];
        for (let i = 0; i < this.GIFT_COUNT; i ++) {
            this.gifts.push(
                new Gift({
                    game: this
                })
            )
        }

        // initial render of all game objects
        // TODO: initial render
    }

    step() {
        // a single step in the game loop
        this.time ++;
        this.scoreboard.step();
        this.grinch.step();
        this.gifts.forEach(g => g.step());

        this.commandQueue = [];
    }

    animate(go) {
        this.step();
        this.render();
        if (go) window.requestAnimationFrame(this.animate.bind(this));
    }

    play() {
        this.playing = true;
        this.animate();
    }

    pause() {
        this.playing = false;
        this.animate(false);
    }

    render() {
        // draw game
    }

}

class GameScoreBoard {

    constructor(options) {
        this.game = options.game;
    }

    step() {
        // do-nothing
    }

    render() {
        // do something with this.game.score
    }

}

class GameObject {

    constructor(options) {
        this.game = options.game;
        this.position = Object.assign({}, options.position);
        this.GRAVITY = GAME_SETTINGS.GRAVITY;
    }

    step() {
        // gravity
        this.position.y = this.position > this.GRAVITY ? this.position - this.GRAVITY : 0;
    }

    render() {
        // use positions
    }

}

class Grinch extends GameObject {

    constructor() {
        super();
        this.JUMP = GAME_SETTINGS.JUMP;
    }

    step() {
        super.step();
        const c = this.game.commandQueue.slice(0);

        c.forEach(comm => {
            switch (comm) {
                case 'up':
                    this.position.y += this.JUMP;
                    break;
                case 'down':
                    this.position.y -= this.JUMP;
                    break;
                case 'right':
                    this.position.x += this.SLIDE;
                    break;
                case 'left':
                    this.position.x -= this.SLIDE;
                    break;
            }
        });
    }

}

class Gift extends GameObject {

    constructor() {
        super();
    }

    step() {
        super.step();
        if (this.distanceToGrinch(this.game.grinch) < GAME_SETTINGS.COLLISION_DIST) {
            this.collide();
        }
    }

    distanceToGrinch(grinch) {
        const dx = grinch.position.x - this.position.x;
        const dy = grinch.position.y - this.position.y;
        const ds = Math.sqrt(Math.pow(dx, 2) + Math.pow(dy, 2));
        return ds;
    }

    collide() {
        // add points
        this.game.score += GAME_SETTINGS.POINTS_PER_GIFT;

        // respawn gift
        this.respawn();
    }

    respawn() {
        this.position.y = this.game.geometry.y;
        this.position.x = Math.random() * this.game.geometry.x;
    }

}
