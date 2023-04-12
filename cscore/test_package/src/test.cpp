#include "cscore.h"
#include "fmt/format.h"

int main(int argc, char** argv) {
  CS_Status status = 0;
  std::vector<cs::UsbCameraInfo> cams = cs::EnumerateUsbCameras(&status);
  if (status != 0) {
	  fmt::print("Status code for EnumerateUsbCameras was: {}\n", status);
  }
  else {
	  fmt::print("Avaliable usb cameras:\n");
	  for (const auto& camInfo : cams) {
		  fmt::print("Cam Name: {}\n", camInfo.name);
	  }
  }
  return 0;
}