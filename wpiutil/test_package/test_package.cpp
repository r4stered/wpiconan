// Copyright (c) FIRST and other WPILib contributors.
// Open Source Software; you can modify and/or share it under the terms of
// the WPILib BSD license file in the root directory of this project.

#include <fmt/format.h>

#include "wpi/interpolating_map.h"

int main() {
  wpi::interpolating_map<double, double> table;

  table.insert(125, 450);
  table.insert(200, 510);
  table.insert(268, 525);
  table.insert(312, 550);
  table.insert(326, 650);

  fmt::print("Test: {}\n", table[250]);

  return 0;
}
