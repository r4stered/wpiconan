// Copyright (c) FIRST and other WPILib contributors.
// Open Source Software; you can modify and/or share it under the terms of
// the WPILib BSD license file in the root directory of this project.

#include "networktables/NetworkTable.h"
#include "networktables/NetworkTableInstance.h"

int main() {
  auto inst = nt::NetworkTableInstance::Create();
  auto nt = inst.GetTable("containskey");
  nt->PutNumber("testkey", 5);
  nt::ResetInstance(inst.GetHandle());
  nt::NetworkTableInstance::Destroy(inst);
}
