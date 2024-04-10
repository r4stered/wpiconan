// Copyright (c) FIRST and other WPILib contributors.
// Open Source Software; you can modify and/or share it under the terms of
// the WPILib BSD license file in the root directory of this project.

#include <frc/Errors.h>

#include "frc2/command/CommandPtr.h"
#include "frc2/command/CommandScheduler.h"
#include "frc2/command/Commands.h"

using namespace frc2;

int main() {
  int counter = 0;
  CommandPtr movedFrom = cmd::Run([&counter] { counter++; });
  CommandPtr movedTo = std::move(movedFrom);
  return 0;
}
