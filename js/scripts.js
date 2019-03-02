svgTable = (function(){
    function mappedColor(color) {
        return color;
    }

    return {
        frame: null,
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
        request: function(filename) {
            var xhr = new XMLHttpRequest();
            var url = "http://localhost:8087/";
            that = this;
            xhr.open("POST", url, true);
            xhr.setRequestHeader("Content-Type", "application/json");
            xhr.onreadystatechange = function () {
                if (xhr.readyState === 4 && xhr.status === 200) {
                    var json = JSON.parse(xhr.responseText);
                    that.clearTable();
                    that.addBalls( json.balls );
                }
            };
            var data = JSON.stringify({"filename": filename});
            xhr.send(data);
        },
        refresh: function() {
            var filename = $("game_id").value;
            this.request(filename);
        }
    }
})();

function $(id) {
    return document.getElementById( id )
}

function init() {
    svgTable.frame = top.table;
}
