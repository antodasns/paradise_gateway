 
var image = document.querySelector('.clear-image');
var appending = document.querySelector('.bg-container');    
var imageCanvas = document.createElement('canvas');
var imageCanvasContext = imageCanvas.getContext('2d');
var lineCanvas = document.createElement('canvas');
var lineCanvasContext = lineCanvas.getContext('2d');
var pointLifetime = 1000;
var points = [];

if (image.complete) {
  start();
} else {
  image.onload = start;
}  

function start() {
            document.addEventListener('mousemove', onMouseMove);
            window.addEventListener('resize', resizeCanvases);
            appending.appendChild(imageCanvas);
            resizeCanvases();
            tick();
        }

        function onMouseMove(event) {
            var scroll = 0;
            if (!$(".search-popup").length) scroll = $(document).scrollTop();
            points.push({
                time: Date.now(),
                x: event.clientX,
                y: event.clientY + scroll
            });
        }

        function resizeCanvases() {
            setTimeout(function() {
                var c = setInterval(function() {
                    if ($(".hero-header canvas").length) {
                        imageCanvas.width = lineCanvas.width = $(".hero-header canvas").parent().width();
                        imageCanvas.height = lineCanvas.height = $(".hero-header canvas").parent().height();
                    }
                }, 1);
                setTimeout(function() {
                    clearInterval(c);
                }, 200);
            }, 2000);
        }

        function tick() {
            points = points.filter(function(point) {
                var age = Date.now() - point.time;
                return age < pointLifetime;
            });
            drawLineCanvas();
            drawImageCanvas();
            requestAnimationFrame(tick);
        }

        function drawLineCanvas() {
            var minimumLineWidth = 25;
            var maximumLineWidth = 75;
            var lineWidthRange = maximumLineWidth - minimumLineWidth;
            var maximumSpeed = 50;
            lineCanvasContext.clearRect(0, 0, lineCanvas.width, lineCanvas.height);
            lineCanvasContext.lineCap = 'round';
            lineCanvasContext.shadowBlur = 20;
            lineCanvasContext.shadowColor = '#000';
            for (var i = 1; i < points.length; i++) {
                var point = points[i];
                var previousPoint = points[i - 1];
                var distance = getDistanceBetween(point, previousPoint);
                var speed = Math.max(0, Math.min(maximumSpeed, distance));
                var percentageLineWidth = (maximumSpeed - speed) / maximumSpeed;
                lineCanvasContext.lineWidth = minimumLineWidth + percentageLineWidth * lineWidthRange;
                var age = Date.now() - point.time;
                var opacity = (pointLifetime - age) / pointLifetime;
                lineCanvasContext.strokeStyle = 'rgba(0, 0, 0, ' + opacity + ')';
                lineCanvasContext.beginPath();
                lineCanvasContext.moveTo(previousPoint.x, previousPoint.y);
                lineCanvasContext.lineTo(point.x, point.y);
                lineCanvasContext.stroke();
            }
        }

        function getDistanceBetween(a, b) {
            return Math.sqrt(Math.pow(a.x - b.x, 2) + Math.pow(a.y - b.y, 2));
        }

        function drawImageCanvas() {
            var top = 0,
                left = 0;
            var width = imageCanvas.width;
            var height = imageCanvas.width / image.naturalWidth * image.naturalHeight;
            if (height < imageCanvas.height) {
                width = imageCanvas.height / image.naturalHeight * image.naturalWidth;
                height = imageCanvas.height;
                left = -(width - imageCanvas.width) / 2;
            } else {
                top = -(height - imageCanvas.height) / 2;
            }
            imageCanvasContext.clearRect(0, 0, imageCanvas.width, imageCanvas.height);
            imageCanvasContext.globalCompositeOperation = 'source-over';
            imageCanvasContext.drawImage(image, left, top, width, height);
            imageCanvasContext.globalCompositeOperation = 'destination-in';
            imageCanvasContext.drawImage(lineCanvas, 0, 0);
        };