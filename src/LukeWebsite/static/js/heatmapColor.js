function getRGBHeatmapColor(val, lowColor, highColor, midColor, transparency=1, useMidVal = true, minVal = 0, midVal = 50, maxVal = 100){
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
            var colorString = 'rgba(' + [redVal, greenVal, blueVal, transparency].join(',') + ')';
            return colorString;

        } else {
            var multiplier = (((maxVal-midVal) - (val-midVal)) / (maxVal-midVal));
            var redVal = Math.floor((midColorRGB[0] * multiplier) + (highColorRGB[0] * (1 - multiplier)));
            var greenVal = Math.floor((midColorRGB[1] * multiplier) + (highColorRGB[1] * (1 - multiplier)));
            var blueVal = Math.floor((midColorRGB[2] * multiplier) + (highColorRGB[2] * (1 - multiplier)));
            var colorString = 'rgba(' + [redVal, greenVal, blueVal, transparency].join(',') + ')';
            return colorString;
        }
    }
    else{
        var multiplier = (((maxVal-minVal) - (val-minVal)) / (maxVal-minVal));
        var redVal = Math.floor((lowColorRGB[0] * multiplier) + (highColorRGB[0] * (1 - multiplier)));
        var greenVal = Math.floor((lowColorRGB[1] * multiplier) + (highColorRGB[1] * (1 - multiplier)));
        var blueVal = Math.floor((lowColorRGB[2] * multiplier) + (highColorRGB[2] * (1 - multiplier)));
        var colorString = 'rgba(' + [redVal, greenVal, blueVal, transparency].join(',') + ')';
        return colorString;
    }

}