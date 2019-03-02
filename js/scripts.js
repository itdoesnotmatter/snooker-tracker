svgTable = (function(){
    function mappedColor(color) {
        return color;
    }

    return {
        frame: null,
        d: function() {
            return this.frame.document;
        },
        $: function(id) {
            return this.d().getElementById( id );
        },
        clearTable: function() {
            balls = this.$("balls")
            while (balls.firstChild) {
                balls.removeChild( balls.firstChild );
            }
        },
        addBall: function( x, y, color ) {
            ball = this.d().createElementNS("http://www.w3.org/2000/svg", "use");
            ball.setAttributeNS("http://www.w3.org/1999/xlink", "xlink:href", "#ball");
            ball.setAttribute("x", x);
            ball.setAttribute("y", y);
            ball.setAttribute("fill", mappedColor(color));
            this.$("balls").appendChild(ball);
        }
    }
})();

function init() {
    svgTable.frame = top.table;
}
