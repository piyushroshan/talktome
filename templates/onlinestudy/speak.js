<script>
                meSpeak.loadConfig("mespeak_config.json");
                meSpeak.loadVoice("voices/en/en-us.json");
                var t=0;
                var speechArr = [];
                var pauseArr = [];
                var len =0;
                var recurseLoop = 0;
                function speakdata(spokendata) {
                    var looper = new Boolean();
                    looper = true;
                    var posCount = new Number(0);
                    var pauseCount = new Number(0);                 
                    while (looper)
                    {
                        if (spokendata.substring(posCount).indexOf("[") == -1) {
                            speechArr.push(meSpeak.speak (spokendata.substring(posCount)),{ 'rawdata': true });
                            pauseArr.push(0);
                            len++;
                            looper = false;
                        } else {
                            if (posCount == 0) {
                                speechArr.push(meSpeak.speak(spokendata.substring(posCount,spokendata.indexOf("[")-1),{ 'rawdata': true }));
                                pauseArr.push(0);
                                len++;
                            }
                            pauseCount += parseInt(spokendata.substring(posCount).substring(spokendata.substring(posCount).indexOf("[")+1, spokendata.substring(posCount).indexOf("]")))
                            posCount = parseInt(posCount+spokendata.substring(posCount).indexOf("]")+1)
                                if (spokendata.substring(posCount).indexOf("[") != -1) {
                                    var posCount2 = spokendata.substring(posCount).indexOf("[");
                                    speechArr.push(meSpeak.speak(spokendata.substring(posCount,posCount2+posCount),{ 'rawdata': true }));
                                    pauseArr.push(pauseCount*1000);
                                    len++;
                                    posCount = posCount2+posCount
                                    looper = true;
                                } else {
                                    speechArr.push(meSpeak.speak(spokendata.substring(posCount),{ 'rawdata': true }));
                                    pauseArr.push(pauseCount*1000);
                                    len++;
                                    looper = false;
                                    }
                                }
                    }
                    setTimeout(function(){meSpeak.play(speechArr[0],1,playNext)},pauseArr[0]);              
                }

                function playNext() {
  if (++recurseLoop < len) {
    setTimeout(function(){meSpeak.play(speechArr[recurseLoop],1,playNext)},pauseArr[recurseLoop]);
  }
}
                </script>