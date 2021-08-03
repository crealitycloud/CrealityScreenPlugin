from . import CrealityScreenPlugin


def getMetaData():
    return{}


def register(app):
    return {"output_device": CrealityScreenPlugin.CrealityOutputDevicePlugin()}
 