function helpme()
{
	var read=new Array()
	read.push({'text':"Welcome to talk to me help"})
	read.push({'text':"Speak Home to go to home page"})
	read.push({'text':"Speak refresh to refresh the page"})
	read.push({'text':"Speak logout to logout from the page"})
	read.push({'text':"Speak repeat to listen to the option available"})
	read.push({'text':"Speak stop to stop listening"})
	meSpeak.speakMultipart(read);
}