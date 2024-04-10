// Copyright (c) FIRST and other WPILib contributors.
// Open Source Software; you can modify and/or share it under the terms of
// the WPILib BSD license file in the root directory of this project.

#include <fmt/format.h>

#include "hal/HAL.h"

int main() {
  int type = HAL_GetRuntimeType();
  fmt::print("runtime type: {}\n", type);
  return 0;
}
