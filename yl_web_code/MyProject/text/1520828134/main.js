var soundSensitivity = 1;
var bassOnly = false;
var darkMode = false;
var isKeyboardDrawnActive = false;

window.onload = function() {
    window.wallpaperRegisterAudioListener(wallpaperAudioListener);
};

window.wallpaperPropertyListener = {
    applyUserProperties: function(properties) {
        if(properties.soundsensitivity) {
            soundSensitivity = properties.soundsensitivity.value / 100;
        }
    
        if(properties.bassonly) {
            bassOnly = properties.bassonly.value;
        }

        if(properties.darkmode) {
            darkMode = properties.darkmode.value;
            if(darkMode) {
                document.getElementById("background").style.filter = "invert(100%)";
                if(isKeyboardDrawnActive) {
                    document.getElementById("instrument").style.filter = "invert(100%)";
                }
            } else {
                document.getElementById("background").style.filter = null;
                if(isKeyboardDrawnActive) {
                    document.getElementById("instrument").style.filter = null;
                }
            }
        }
    
        if(properties.instrument.value) {
            document.getElementById("instrument").children[0].style.display = "block";
            var imageFile;
            switch(properties.instrument.value) {
                case 1:
                    imageFile = "bongos.png";
                    isKeyboardDrawnActive = false;
                    break;
                case 2:
                    imageFile = "keyboardReal.png";
                    isKeyboardDrawnActive = false;
                    break;
                case 3:
                    imageFile = "keyboardDrawn.png";
                    isKeyboardDrawnActive = true;
                    break;
                case 4:
                    imageFile = "tambourines.png";
                    isKeyboardDrawnActive = false;
                    break;
            }
            document.getElementById("instrument").children[0].setAttribute("src", "./img/"+imageFile);
            
            if(darkMode && imageFile === "keyboardDrawn.png") {
                document.getElementById("instrument").style.filter = "invert(100%)";
            } else {
                document.getElementById("instrument").style.filter = null;
            }

        } else {
            document.getElementById("instrument").children[0].style.display = "none";
        }

    }
};

function wallpaperAudioListener(audioArray) {
    var i;
    var foundLeft = false;
    var foundRight = false;
    var soundThreshold = 1-(0.5 * soundSensitivity);
    var frequenciesHeard;

    if(bassOnly) {
        frequenciesHeard = 21;
    } else {
        frequenciesHeard = 63;
    }

    i=0;
    while(i<frequenciesHeard && (!foundLeft || !foundRight)) {
        if(audioArray[i] > soundThreshold) {
            foundLeft=true;
        }
        if(audioArray[i+64] > soundThreshold) {
            foundRight=true;
        }
        i++;
    }
	
	var fileName;

	//LEFT
    if(foundLeft) {
        if(darkMode) {
            fileName = "bongoLeftTapDark.png";
        } else {
            fileName = "bongoLeftTap.png";
        }
    } else {
		if(darkMode) {
            fileName = "bongoLeftDark.png";
        } else {
            fileName = "bongoLeft.png";
        }
    }
	document.getElementById("imgLeft").setAttribute("src", "./img/"+fileName);

	//RIGHT
    if(foundRight) {
        if(darkMode) {
            fileName = "bongoRightTapDark.png";
        } else {
            fileName = "bongoRightTap.png";
        }
    } else {
        if(darkMode) {
            fileName = "bongoRightDark.png";
        } else {
            fileName = "bongoRight.png";
        }
    }
	document.getElementById("imgRight").setAttribute("src", "./img/"+fileName);

}