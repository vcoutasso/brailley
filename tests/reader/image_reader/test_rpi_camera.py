from brailley.reader.image_reader.camera_io_device import CameraIODevice
from brailley.reader.image_reader.rpi_camera import RPICamera
from io import BytesIO
from PIL import Image
from unittest.mock import Mock
from unittest import TestCase


class TestRPICamera(TestCase):
    def setUp(self) -> None:
        self.flashMock = Mock()
        self.fakeCamera = FakeCameraDevice()
        self.sut = RPICamera(self.flashMock, camera_io_device=self.fakeCamera, warmup=0)

    def test_init_shouldStartCameraDevicePreview(self):
        self.assertEqual(self.fakeCamera.did_call_start_preview, 1)

    def test_capture_shouldNotStartCameraDevicePreview(self):
        self.sut.capture()

        self.assertEqual(self.fakeCamera.did_call_start_preview, 1)

    def test_capture_shouldCallCameraDeviceCapture(self):
        self.sut.capture()

        self.assertTrue(self.fakeCamera.did_call_capture)

    def test_capture_shouldToggleFlashOn(self):
        self.sut.capture()

        self.flashMock.on.assert_called_once()

    def test_capture_shouldToggleFlashOff(self):
        self.sut.capture()

        self.flashMock.off.assert_called_once()

    def test_capture_shouldReturnCapturedImage(self):
        self.assertEqual(
            self.sut.capture().tobytes(), self.fakeCamera.stub_image.tobytes()
        )


class FakeCameraDevice(CameraIODevice):
    stub_image = Image.new("RGB", (20, 20), color="white")

    did_call_start_preview = 0

    def start_preview(self):
        self.did_call_start_preview += 1

    did_call_capture = False

    def capture(self, stream: BytesIO, **kwargs):
        self.did_call_capture = True
        self.stub_image.save(stream, "jpeg")
