svgTable = (function(){
    function mappedColor(color) {
        return color;
    }

    return {
        frame: null,
        sequence: [],
        d: function() {
            return this.frame.document;
        },
        $: function(id, doc) {
            if ( doc == null ) {
                doc = this.d();
            }
            return doc.getElementById( id );
        },
        clearTable: function() {
            balls = this.$("balls")
            while (balls.firstChild) {
                balls.removeChild( balls.firstChild );
            }
        },
        addBall: function( ball ) {
            elem = this.d().createElementNS("http://www.w3.org/2000/svg", "use");
            elem.setAttributeNS("http://www.w3.org/1999/xlink", "xlink:href", "#ball");
            elem.setAttribute("x", ball.x);
            elem.setAttribute("y", ball.y);
            elem.setAttribute("fill", mappedColor(ball.color));
            this.$("balls").appendChild(elem);
        },
        addBalls: function(balls) {
            balls.forEach( this.addBall, this )
        },
        request: function(filename, start, frames) {
            var xhr = new XMLHttpRequest();
            var url = "http://localhost:8087/";
            var that = this;

            xhr.open("POST", url, true);
            xhr.setRequestHeader("Content-Type", "application/json");
            xhr.onreadystatechange = function () {
                if (xhr.readyState === 4 && xhr.status === 200) {
                    var json = JSON.parse(xhr.responseText);
                    that.sequence = json;
                    // that.redraw( json.balls );
                }
            };

            var data = JSON.stringify({
                "filename": filename,
                "frames": frames,
                "start": start
            });
            xhr.send(data);
        },
        refresh: function() {
            var filename = $("game_id").value;
            var frames = parseInt($("frames").value);
            var start = parseInt($("start").value);
            this.request(filename, start, frames);
        },
        redraw: function(balls) {
            this.clearTable();
            this.addBalls(balls);
        },
        play: function() {
            if (this.sequence.length > 1) {
                var firstPos = this.sequence[0];

                this.redraw( firstPos.balls );
                this.playNext(1);
            }
        },
        playNext: function(seqIndex) {
            if (seqIndex == this.sequence.length) {
                return;
            }

            var that = this;

            var prevPos = this.sequence[seqIndex-1];
            var prevTimestamp = prevPos.timestamp;

            var nextPos = this.sequence[seqIndex];
            var nextTimestamp = nextPos.timestamp;

            var timeDiff = nextTimestamp - prevTimestamp;

            var prom = new Promise((resolve) => {
                setTimeout(function() {
                    that.redraw( nextPos.balls );
                    resolve();
                }, timeDiff * 1000);
            });

            prom.then(() => {
                that.playNext(seqIndex + 1);
            });
        }
    }
})();

function $(id) {
    return document.getElementById( id )
}

function init() {
    svgTable.frame = top.table;
}
