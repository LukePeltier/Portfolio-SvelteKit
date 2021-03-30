function getRGBHeatmapColor(val, lowColor, highColor, midColor, useMidVal = true, minVal = 0, midVal = 50, maxVal = 100){
    var lowColorRGB = lowColor.replace(/[^\d,]/g, '').split(',');
    var highColorRGB = highColor.replace(/[^\d,]/g, '').split(',');
    if(!midColor==null){
        var midColorRGB = midColor.replace(/[^\d,]/g, '').split(',');
    }
    if(useMidVal){
        if (val < midVal) {
            var multiplier = (((midVal-minVal) - (value-minVal)) / (midVal-minVal));
            var redVal = Math.floor((lowColorRGB[0] * multiplier) + (midColorRGB[0] * (1 - multiplier)));
            var greenVal = Math.floor((lowColorRGB[1] * multiplier) + (midColorRGB[1] * (1 - multiplier)));
            var blueVal = Math.floor((lowColorRGB[2] * multiplier) + (midColorRGB[2] * (1 - multiplier)));
            var colorString = 'rgb(' + [redVal, greenVal, blueVal].join(',') + ')';
            return colorString;

        } else {
            var multiplier = (((maxVal-midVal) - (tempValue-midVal)) / (maxVal-midVal));
            var redVal = Math.floor((midColorRGB[0] * multiplier) + (highColorRGB[0] * (1 - multiplier)));
            var greenVal = Math.floor((midColorRGB[1] * multiplier) + (highColorRGB[1] * (1 - multiplier)));
            var blueVal = Math.floor((midColorRGB[2] * multiplier) + (highColorRGB[2] * (1 - multiplier)));
            var colorString = 'rgb(' + [redVal, greenVal, blueVal].join(',') + ')';
            return colorString;
        }
    }
    else{
        var multiplier = (((maxVal-minVal) - (value-minVal)) / (maxVal-minVal));
        var redVal = Math.floor((lowColorRGB[0] * multiplier) + (highColorRGB[0] * (1 - multiplier)));
        var greenVal = Math.floor((lowColorRGB[1] * multiplier) + (highColorRGB[1] * (1 - multiplier)));
        var blueVal = Math.floor((lowColorRGB[2] * multiplier) + (highColorRGB[2] * (1 - multiplier)));
        var colorString = 'rgb(' + [redVal, greenVal, blueVal].join(',') + ')';
        return colorString;
    }

}