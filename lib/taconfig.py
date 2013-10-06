import json

class Feed:
	pass

class TaConfig():
    def __init__(self, configpath):
        self.feeds = []

        # interpret the config file as json
        with open(configpath) as ff:
            cfg_json = json.load(ff)

        feeds = cfg_json["feeds"]
        for feed in feeds:
            newfeed=Feed()
            newfeed.name = feed["feedname"]
            newfeed.url = feed["feedurl"]
            newfeed.websocket_host = feed["websocket_host"]
            newfeed.websocket_port = feed["websocket_port"]
            self.feeds.append(newfeed)
			
	