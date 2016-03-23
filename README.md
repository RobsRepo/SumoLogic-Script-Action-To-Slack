# Posting Messages to Slack with Sumo Logic Script Actions

Before you say: "Hey Rob, you dummy! You can already post to slack with a regular alert in Sumo Logic!" I know. The issue is that some of the clients that I've worked with were actually interested in having some of their data exposed to the Channel but without having the JSON brackets in place. At the time of writing this script, the option to strip these JSON handlebars out was not available with the Sumo Logic service.

# Basic Idea

1.	Download this script onto the machine with the scheduled alert.
2.	Add a Sumo Logic Script Action that points to this script.
3.	Setup a Sumo Logic alert that triggers this script action.

##Visually the flow looks like this:
 ![alt tag](https://github.com/RobsRepo/SumoLogic-Script-Action-To-Slack/blob/master/overview.png)
 
# Prerequisites
1.	You will need Python 2.7
2.	You will need the Slack Python library. Install it using “pip install SlackClient”
3.	A Sumo Logic installed collector.
4.	A Sumo Logic query that you would like to schedule as an alert.

# Setup
1.	Install the prerequisites.
2.	Add the necessary configuration information inside config.properties.
3.	Add the attributes you would like to expose by adding them line by line inside attributesToExpose.txt. These are usually the fields being exposed in your Sumo Logic alert query.
4.	Give executable rights to the shell script: chmod +x postScriptActionToSlack.sh
5.	Create a script action inside a Sumo Logic alert with "postScriptActionToSlack.sh" as the script you would like it to execute.

# Run:
The script action run this script when the alert fires.
However, if you would like to test it, run "python postScriptActionToSlack.py '\<filename\>'"

