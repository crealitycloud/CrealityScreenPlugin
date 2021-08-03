from UM.OutputDevice.OutputDevicePlugin import OutputDevicePlugin
from .CrealityOutputDevice import CrealityOutputDevice

class CrealityScreenPlugin(OutputDevicePlugin):
    def __init__(self):
        super().__init__()

    def start(self):
        self.getOutputDeviceManager().addOutputDevice(
            CrealityOutputDevice(self.getPluginId()))

    def stop(self):
        self.getOutputDeviceManager().removeOutputDevice("creality_output_gcode")