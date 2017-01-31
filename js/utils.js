var $ = document.querySelector.bind(document),
    $$ = document.querySelectorAll.bind(document);

var G3Utils = {

    eventAdder: function(selector, eventName, callback) {
        var targets = $$(selector) || [],
            tLength = targets.length;

        for (i = 0; i < tLength; i++) {
            targets[i].addEventListener(eventName, callback);
        }

        return targets;
    },

    extendObject: function(obj, el) {

        Object.keys(el).forEach(function(key) {
            obj[key] = el[key];
        });

        return obj;

    },

    getLocation: function(el) {

        var boundingClientRect = el.getBoundingClientRect();

        extendObject(boundingClientRect, {
            width: boundingClientRect.right - boundingClientRect.left,
            height: boundingClientRect.bottom - boundingClientRect.top
        });

        return boundingClientRect;

    },

    getNodeArray: function(identifier) {
        return Array.prototype.slice.apply(document.querySelectorAll(identifier));
    }

};
