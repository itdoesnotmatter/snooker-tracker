svgTable = (function(){
    debug_seq = [{"balls": [{"color": "yellow", "y": 109.70475354107649, "x": 11.48197435897436}, {"color": "red", "y": -0.5097804532577754, "x": 9.552230769230768}, {"color": "red", "y": 19.371657223796035, "x": 6.754102564102564}, {"color": "pink", "y": 31.91225637393768, "x": 1.5437948717948724}, {"color": "brown", "y": 109.09301699716713, "x": 0.09648717948717789}, {"color": "blue", "y": 67.90275637393768, "x": 0}, {"color": "red", "y": 29.465310198300273, "x": 0.28946153846153744}, {"color": "white", "y": 31.708344192634556, "x": -6.368153846153845}, {"color": "green", "y": 109.09301699716713, "x": -10.99953846153846}, {"color": "red", "y": 15.803194050991493, "x": -26.63046153846154}, {"color": "red", "y": 42.92351416430594, "x": -31.06887179487179}], "game_id": "video/ronnie-masters.mkv", "timestamp": 902}, {"balls": [{"color": "yellow", "y": 109.70475354107649, "x": 11.48197435897436}, {"color": "red", "y": -0.5097804532577754, "x": 9.552230769230768}, {"color": "red", "y": 19.371657223796035, "x": 6.754102564102564}, {"color": "pink", "y": 31.91225637393768, "x": 1.5437948717948724}, {"color": "brown", "y": 109.09301699716713, "x": 0.09648717948717789}, {"color": "blue", "y": 67.90275637393768, "x": 0}, {"color": "red", "y": 29.465310198300273, "x": 0.28946153846153744}, {"color": "pink", "y": 31.606388101983, "x": -6.271666666666665}, {"color": "green", "y": 109.09301699716713, "x": -10.99953846153846}], "game_id": "video/ronnie-masters.mkv", "timestamp": 903}, {"balls": [{"color": "yellow", "y": 109.80670963172804, "x": 11.48197435897436}, {"color": "red", "y": -0.5097804532577754, "x": 9.552230769230768}, {"color": "red", "y": 19.371657223796035, "x": 6.754102564102564}, {"color": "pink", "y": 31.91225637393768, "x": 1.5437948717948724}, {"color": "brown", "y": 109.09301699716713, "x": 0.09648717948717789}, {"color": "blue", "y": 67.90275637393768, "x": 0}, {"color": "red", "y": 29.465310198300273, "x": 0.28946153846153744}, {"color": "white", "y": 31.606388101983, "x": -6.368153846153845}, {"color": "green", "y": 109.09301699716713, "x": -10.99953846153846}, {"color": "green", "y": 72.28686827195467, "x": -31.06887179487179}], "game_id": "video/ronnie-masters.mkv", "timestamp": 904}, {"balls": [{"color": "yellow", "y": 109.70475354107649, "x": 11.48197435897436}, {"color": "red", "y": -0.5097804532577754, "x": 9.552230769230768}, {"color": "red", "y": 19.371657223796035, "x": 6.754102564102564}, {"color": "pink", "y": 31.91225637393768, "x": 1.5437948717948724}, {"color": "brown", "y": 109.09301699716713, "x": 0.09648717948717789}, {"color": "blue", "y": 67.90275637393768, "x": 0}, {"color": "red", "y": 29.465310198300273, "x": 0.28946153846153744}, {"color": "black", "y": 10.399521246458932, "x": 0.09648717948717789}, {"color": "white", "y": 31.606388101983, "x": -6.271666666666665}, {"color": "green", "y": 109.09301699716713, "x": -10.99953846153846}, {"color": "pink", "y": 43.7391628895184, "x": -20.93771794871795}, {"color": "red", "y": 15.803194050991493, "x": -26.63046153846154}, {"color": "red", "y": 42.71960198300283, "x": -31.06887179487179}], "game_id": "video/ronnie-masters.mkv", "timestamp": 905}, {"balls": [{"color": "yellow", "y": 109.70475354107649, "x": 11.48197435897436}, {"color": "red", "y": -0.5097804532577754, "x": 9.552230769230768}, {"color": "red", "y": 19.371657223796035, "x": 6.754102564102564}, {"color": "pink", "y": 31.91225637393768, "x": 1.5437948717948724}, {"color": "brown", "y": 109.09301699716713, "x": 0.09648717948717789}, {"color": "blue", "y": 67.90275637393768, "x": 0}, {"color": "red", "y": 29.465310198300273, "x": 0.28946153846153744}, {"color": "black", "y": 10.399521246458932, "x": 0.09648717948717789}, {"color": "white", "y": 31.606388101983, "x": -6.271666666666665}, {"color": "green", "y": 109.09301699716713, "x": -10.99953846153846}, {"color": "brown", "y": 42.82155807365439, "x": -20.262307692307694}, {"color": "red", "y": 15.803194050991493, "x": -26.63046153846154}, {"color": "red", "y": 42.61764589235126, "x": -31.06887179487179}], "game_id": "video/ronnie-masters.mkv", "timestamp": 906}];

    function mappedColor(color) {
        return color;
    }

    return {
        frame: null,
        paused: false,
        seqIndex: 0,
        sequence: debug_seq,
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
        redraw: function(balls, pos) {
            this.clearTable();
            this.addBalls(balls);
            $("seq_pos").value = pos;
        },
        play: function() {
            if (this.sequence.length > 1) {
                var firstPos = this.sequence[0];

                disablePlayButton();
                player.seekTo(firstPos.timestamp, true);
                player.playVideo();

                this.redraw( firstPos.balls, firstPos.timestamp );
                this.playNext(1);
            }
        },
        playNext: function(seqIndex) {
            if (this.paused) {
                return;
            }
            if (seqIndex == this.sequence.length) {
                player.pauseVideo();
                enablePlayButton();
                return;
            }

            this.seqIndex = seqIndex;

            var that = this;

            var prevPos = this.sequence[seqIndex-1];
            var prevTimestamp = prevPos.timestamp;

            var nextPos = this.sequence[seqIndex];
            var nextTimestamp = nextPos.timestamp;

            var timeDiff = nextTimestamp - prevTimestamp;

            var prom = new Promise((resolve) => {
                setTimeout(function() {
                    that.redraw( nextPos.balls, nextTimestamp );
                    resolve();
                }, timeDiff * 1000);
            });

            prom.then(() => {
                that.playNext(seqIndex + 1);
            });
        },
        pause: function() {
            if (this.paused) {
                this.paused = false;
                player.playVideo();
                this.playNext( this.seqIndex + 1 );
            }
            else {
                this.paused = true;
                player.pauseVideo();
            }
        }
    }
})();

function $(id) {
    return document.getElementById( id )
}

function init() {
    svgTable.frame = top.table;
    loadYTplayer();
}

function loadYTplayer() {
    var tag = document.createElement('script');

    tag.src = "https://www.youtube.com/iframe_api";
    var firstScriptTag = document.getElementsByTagName('script')[0];
    firstScriptTag.parentNode.insertBefore(tag, firstScriptTag);
}

function onYouTubeIframeAPIReady() {
    player = new YT.Player('ytframe', {
        height: '360',
        width: '640',
        videoId: '2241I6gaaB8'
        // events: {
        //     'onReady': onPlayerReady,
        //     'onStateChange': onPlayerStateChange
        // }
    });
}

function disablePlayButton() {
    $("play_button").disabled = "disabled";
}

function enablePlayButton() {
    $("play_button").disabled = "";
}
