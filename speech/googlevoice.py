import pysox
import urllib
import requests

#import logging
#requests_log = logging.getLogger("requests")
#requests_log.setLevel(logging.WARNING)

from subprocess import call

rate = "16000"

headers = {
	"Content-type": "audio/x-flac; rate=" + rate
}

url = "http://www.google.com/speech-api/v1/recognize"

def wav_to_flac(filename, flac_filename, pysox=False):
	if pysox:
		wav = pysox.CSoxStream(filename)
		flac = pysox.CSoxStream(flac_filename, 'w', wav.get_signal())	
		chain = pysox.CEffectsChain(wav, flac)
		chain.flow_effects()
		flac.close()
		print "Used pysox"
	else:
		call(["sox", filename, "-r", rate,"-b", "16", "-c", "1", flac_filename, "vad", "reverse", "vad", "reverse", "lowpass", "-2", "2500" ])

def recognize(filename, lang="en"):
	flac_filename = filename.replace(".wav", ".flac")
	wav_to_flac(filename, flac_filename)

	params = {
		"xjerr": "1",
		"client": "chromium",
		"lang": lang		
	}

	url_with_params = "%s?%s" % (url, urllib.urlencode(params))
	print url_with_params
	r = requests.post(url_with_params, files={'file': open(flac_filename,'rb').read()}, headers=headers)

	json = r.json()
	print json
	if json and len(json["hypotheses"]):
		return json["hypotheses"][0]["utterance"]

	return None
