import sys
import json
import ConfigParser
from slackclient import SlackClient

# Post the message to a Slack channel
def postToSlack(msg):
	config = ConfigParser.RawConfigParser()
	config.readfp(open('config.properties'))

	# Retrieves the Slack channel configuration
	try:
		token = config.get("Slack", "token")
		channel = config.get("Slack", "channel")
		username = config.get("Slack", "username")
		icon_emoji = config.get("Slack", "icon_emoji")

		if(token and channel and msg):
			sc = SlackClient(token)
			sc.api_call(
			    "chat.postMessage", channel=channel, text=msg,
			    username=username, icon_emoji=icon_emoji
			)
	except ConfigParser.NoOptionError as e:
		print "Not Slack configuration to post to"

def constructMessage():
	# Read attributes into set
	attributeSet = set(line.strip() for line in open('attributesToExpose.txt'))
	args = sys.argv
	fileName = args[1] 
	#fileName = "/Applications/Sumo Logic Collector/alerts/0000000006A23483-03-21-22-25-21-27.txt"

	scriptActionFile = open (fileName, "r")
	jsonData = json.loads(scriptActionFile.read())['messages']

	config = ConfigParser.RawConfigParser()
	config.readfp(open('config.properties'))
	messageHeader = config.get("Message", "header")
	messageLimit = int(config.get("Message", "limit"))

	if messageLimit > 10 or messageLimit == 0:
		messageLimit = 10

	outputMessage = messageHeader + "\n"
	messageCounter = 0; # limiting how many sets of data we can create

	# Looping through the JSON data to construct what we are looking for
	for message in jsonData:
		for attribute, value in message.iteritems():
			if attribute in attributeSet:
				outputMessage += attribute + ":\t" + str(value) + "\n"
		messageCounter += 1
		if messageCounter > messageLimit:
			break

	return outputMessage

def main(): 
	msg = constructMessage()
	postToSlack(msg)

main()