function helpme()
{
	 var u = new SpeechSynthesisUtterance();
        u.text = 'Welcome to talk to me help. Speak Home to go to home page. Speak refresh to refresh the page. Speak logout to logout from the page.'
        u.lang = 'en-US';
        u.rate = 0.5;
        window.speechSynthesis.speak(u);
        var v = new SpeechSynthesisUtterance();
        v.text =' Speak repeat to listen to the option available. Speak stop to stop listening';
        v.lang = 'en-US';
        v.rate = 0.5;
        window.speechSynthesis.speak(v);
        
}