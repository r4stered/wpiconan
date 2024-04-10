// Copyright (c) FIRST and other WPILib contributors.
// Open Source Software; you can modify and/or share it under the terms of
// the WPILib BSD license file in the root directory of this project.

#include <fmt/core.h>
#include <networktables/NetworkTableInstance.h>

#include "cameraserver/CameraServer.h"

int main(int argc, char *argv[]) {
  // start NetworkTables
  auto ntinst = nt::NetworkTableInstance::GetDefault();
  ntinst.StartServer();

  auto camera = frc::CameraServer::StartAutomaticCapture();
  return 0;
}
