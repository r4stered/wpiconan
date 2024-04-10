// Copyright (c) FIRST and other WPILib contributors.
// Open Source Software; you can modify and/or share it under the terms of
// the WPILib BSD license file in the root directory of this project.

#include <iostream>

#include "fields/2024-crescendo.h"
#include "fields/fields.h"

int main() {
  static const fields::Field kField = {"2024 Crescendo",
                                       fields::GetResource_2024_crescendo_json,
                                       fields::GetResource_2024_field_png};
  std::cout << kField.getJson() << "\n";
}
