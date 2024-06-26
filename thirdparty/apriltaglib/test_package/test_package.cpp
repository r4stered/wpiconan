// Copyright (c) FIRST and other WPILib contributors.
// Open Source Software; you can modify and/or share it under the terms of
// the WPILib BSD license file in the root directory of this project.

#include <apriltag.h>
#include <tag36h11.h>

int main() {
  apriltag_detector_t *td = apriltag_detector_create();
  apriltag_family_t *tf = tag36h11_create();
  apriltag_detector_add_family(td, tf);
  apriltag_detector_destroy(td);
  tag36h11_destroy(tf);
  return 0;
}
