from UM.OutputDevice.OutputDevice import OutputDevice


class CrealityOutputDevice(OutputDevice):
    def __init__(self, device_id: str) -> None:
        super().__init__("creality_output_gcode")

        self._pluginId = device_id
        self.setName("Creality Screen Gcode")
        self.setShortDescription("Save as Creality Screen format")
        self.setDescription("Save as Creality Screen format")
        self.setIconName("save")
