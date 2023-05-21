from io import BytesIO
from picamera import PiCamera
from PIL import Image
from time import sleep
import gpiozero


class Camera:
    def __init__(self, led_pin):
        self.led = gpiozero.LED(
            led_pin, pin_factory=gpiozero.pins.pigpio.PiGPIOFactory()
        )
        self.camera = PiCamera(
            resolution=(1280, 720),
        )
        self.stream = BytesIO()
        self.camera.start_preview()
        # camera warm-up
        sleep(2)

    def capture(self) -> Image.Image:
        self.led.on()
        self.camera.capture(self.stream, format="jpeg")
        self.led.off()

        return self._image_from_stream()

    def _image_from_stream(self) -> Image.Image:
        self.stream.seek(0)
        return Image.open(self.stream)
