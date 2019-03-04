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
        request: function(filename, start, frames, process_fps) {
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
                "process_fps": process_fps,
                "start": start
            });
            xhr.send(data);
        },
        loadJSON: function() {
            var xhr = new XMLHttpRequest();
            var file = "js/ding-1fps.json";
            var that = this;

            xhr.open("GET", file, true);
            // xhr.setRequestHeader("Content-Type", "application/json");
            xhr.overrideMimeType("application/json");
            xhr.onreadystatechange = function () {
                if (xhr.readyState === 4 && xhr.status === 200) {
                    var json = JSON.parse(xhr.responseText);
                    that.sequence = json;
                }
            };

            xhr.send(null);
        },
        refresh: function() {
            var filename = $("game_id").value;
            var frames = parseInt($("frames").value);
            var start = parseInt($("start").value);
            var process_fps = parseInt($("process_fps").value);
            this.request(filename, start, frames, process_fps);
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
                // FIXME Hardcoded FPS
                player.seekTo(parseInt(firstPos.timestamp/25), true);
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
            updateTime(nextTimestamp);

            // FIXME Hardcoded FPS
            var timeDiff = (nextTimestamp - prevTimestamp) / 25;

            var prom = new Promise((resolve) => {
                setTimeout(function() {
                    that.redraw( nextPos.balls, nextTimestamp );
                    resolve();
                }, parseInt(timeDiff * 1000));
            });

            prom.then(() => {
                that.playNext(seqIndex + 1);
            });
        },
        pause: function() {
            if (this.paused) {
                this.paused = false;
                currTimestamp = this.sequence[ this.seqIndex ].timestamp;
                player.seekTo(parseInt(currTimestamp/25), true);
                player.playVideo();
                this.playNext( this.seqIndex + 1 );
            }
            else {
                this.paused = true;
                player.pauseVideo();
            }
        },
        setIndexByTimestamp: function(timestamp) {
            var seconds = parseInt(timestamp/25);
            var i = 1;
            var prevTimestamp = this.sequence[0].timestamp;
            var found = false;

            while (!found && i < this.sequence.length) {
                var currTimestamp = this.sequence[i].timestamp;

                if ( currTimestamp < timestamp ) {
                    prevTimestamp = currTimestamp;
                }
                else {
                    found = true;
                }

                i++;
            }

            this.seqIndex = i - 1;
        }
    }
})();

function $(id) {
    return document.getElementById( id )
}

function init() {
    svgTable.frame = top.table;
    loadYTplayer();
    $("seq_pos").onchange = function(e) {
        svgTable.setIndexByTimestamp( e.target.value );
    };
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
        videoId: 'uvmW-BtF1iA'
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

function updatePos() {
    $("seq_pos").value = (parseInt($("minutes").value) * 60 + parseInt($("seconds").value)) * 25;
}

function updateTime(timestamp) {
    $("minutes").value = parseInt( timestamp / 25 / 60 );
    $("seconds").value = parseInt(timestamp / 25) % 60;
}
