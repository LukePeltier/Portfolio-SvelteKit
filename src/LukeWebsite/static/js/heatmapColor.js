function getRGBHeatmapColor(val, lowColor, highColor, midColor, transparency=1, useMidVal = true, minVal = 0, midVal = 50, maxVal = 100){

    var trueTransparency = (transparency+0.2)/(1.2)
    var lowColorRGB = lowColor.replace(/[^\d,]/g, '').split(',');
    var highColorRGB = highColor.replace(/[^\d,]/g, '').split(',');
    var midColorRGB = midColor.replace(/[^\d,]/g, '').split(',');
    for(var i=0; i<3;i++){
        lowColorRGB[i] = parseInt(lowColorRGB[i]);
        midColorRGB[i] = parseInt(midColorRGB[i]);
        highColorRGB[i] = parseInt(highColorRGB[i]);
    }

    val = parseInt(val);

    if(useMidVal){
        if (val < midVal) {
            var multiplier = (((midVal-minVal) - (val-minVal)) / (midVal-minVal));
            var redVal = Math.floor((lowColorRGB[0] * multiplier) + (midColorRGB[0] * (1 - multiplier)));
            var greenVal = Math.floor((lowColorRGB[1] * multiplier) + (midColorRGB[1] * (1 - multiplier)));
            var blueVal = Math.floor((lowColorRGB[2] * multiplier) + (midColorRGB[2] * (1 - multiplier)));
            var colorString = 'rgba(' + [redVal, greenVal, blueVal, trueTransparency].join(',') + ')';
            return colorString;

        } else {
            var multiplier = (((maxVal-midVal) - (val-midVal)) / (maxVal-midVal));
            var redVal = Math.floor((midColorRGB[0] * multiplier) + (highColorRGB[0] * (1 - multiplier)));
            var greenVal = Math.floor((midColorRGB[1] * multiplier) + (highColorRGB[1] * (1 - multiplier)));
            var blueVal = Math.floor((midColorRGB[2] * multiplier) + (highColorRGB[2] * (1 - multiplier)));
            var colorString = 'rgba(' + [redVal, greenVal, blueVal, trueTransparency].join(',') + ')';
            return colorString;
        }
    }
    else{
        var multiplier = (((maxVal-minVal) - (val-minVal)) / (maxVal-minVal));
        var redVal = Math.floor((lowColorRGB[0] * multiplier) + (highColorRGB[0] * (1 - multiplier)));
        var greenVal = Math.floor((lowColorRGB[1] * multiplier) + (highColorRGB[1] * (1 - multiplier)));
        var blueVal = Math.floor((lowColorRGB[2] * multiplier) + (highColorRGB[2] * (1 - multiplier)));
        var colorString = 'rgba(' + [redVal, greenVal, blueVal, trueTransparency].join(',') + ')';
        return colorString;
    }

}

function getRGBHeatmapColorFromHex(val, lowColor, highColor, midColor, transparency=1, useMidVal = true, minVal = 0, midVal = 50, maxVal = 100, noGradient = false){
    var trueTransparency = (transparency+0.2)/(1.2)

    if(noGradient){
        lowGate = (maxVal-minVal)*.45;
        if(val < lowGate){
            return getComputedStyle(document.documentElement).getPropertyValue('--tenmansred');
        }
        highGate = (maxVal-minVal)*.60;
        if(val < highGate){
            return getComputedStyle(document.documentElement).getPropertyValue('--tenmansyellow');
        }
        return getComputedStyle(document.documentElement).getPropertyValue('--tenmansgreen');
    }

    var lowColorRGB = [
        parseInt(lowColor.charAt(1)+''+lowColor.charAt(2), 16),
        parseInt(lowColor.charAt(3)+''+lowColor.charAt(4), 16),
        parseInt(lowColor.charAt(5)+''+lowColor.charAt(6), 16)
    ];

    var highColorRGB = [
        parseInt(highColor.charAt(1)+''+highColor.charAt(2), 16),
        parseInt(highColor.charAt(3)+''+highColor.charAt(4), 16),
        parseInt(highColor.charAt(5)+''+highColor.charAt(6), 16)
    ];

    var midColorRGB = [
        parseInt(midColor.charAt(1)+''+midColor.charAt(2), 16),
        parseInt(midColor.charAt(3)+''+midColor.charAt(4), 16),
        parseInt(midColor.charAt(5)+''+midColor.charAt(6), 16)
    ];

    val = parseInt(val);

    if(useMidVal){
        if (val < midVal) {
            var multiplier = (((midVal-minVal) - (val-minVal)) / (midVal-minVal));
            var redVal = Math.floor((lowColorRGB[0] * multiplier) + (midColorRGB[0] * (1 - multiplier)));
            var greenVal = Math.floor((lowColorRGB[1] * multiplier) + (midColorRGB[1] * (1 - multiplier)));
            var blueVal = Math.floor((lowColorRGB[2] * multiplier) + (midColorRGB[2] * (1 - multiplier)));
            var colorString = 'rgba(' + [redVal, greenVal, blueVal, trueTransparency].join(',') + ')';
            return colorString;

        } else {
            var multiplier = (((maxVal-midVal) - (val-midVal)) / (maxVal-midVal));
            var redVal = Math.floor((midColorRGB[0] * multiplier) + (highColorRGB[0] * (1 - multiplier)));
            var greenVal = Math.floor((midColorRGB[1] * multiplier) + (highColorRGB[1] * (1 - multiplier)));
            var blueVal = Math.floor((midColorRGB[2] * multiplier) + (highColorRGB[2] * (1 - multiplier)));
            var colorString = 'rgba(' + [redVal, greenVal, blueVal, trueTransparency].join(',') + ')';
            return colorString;
        }
    }
    else{
        var multiplier = (((maxVal-minVal) - (val-minVal)) / (maxVal-minVal));
        var redVal = Math.floor((lowColorRGB[0] * multiplier) + (highColorRGB[0] * (1 - multiplier)));
        var greenVal = Math.floor((lowColorRGB[1] * multiplier) + (highColorRGB[1] * (1 - multiplier)));
        var blueVal = Math.floor((lowColorRGB[2] * multiplier) + (highColorRGB[2] * (1 - multiplier)));
        var colorString = 'rgba(' + [redVal, greenVal, blueVal, trueTransparency].join(',') + ')';
        return colorString;
    }
}