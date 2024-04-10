// Copyright (c) FIRST and other WPILib contributors.
// Open Source Software; you can modify and/or share it under the terms of
// the WPILib BSD license file in the root directory of this project.

#include <fmt/format.h>

#include <functional>

#include <Eigen/Eigenvalues>

#include "frc/EigenCore.h"
#include "frc/system/Discretization.h"
#include "frc/system/NumericalIntegration.h"

int main() {
  frc::Matrixd<2, 2> contA{{0, 1}, {0, 0}};
  frc::Matrixd<2, 1> contB{0, 1};

  frc::Vectord<2> x0{1, 1};
  frc::Vectord<1> u{1};
  frc::Matrixd<2, 2> discA;
  frc::Matrixd<2, 1> discB;

  frc::DiscretizeAB<2, 1>(contA, contB, 1_s, &discA, &discB);
  frc::Vectord<2> x1Discrete = discA * x0 + discB * u;

  // We now have pos = vel = accel = 1, which should give us:
  frc::Vectord<2> x1Truth{1.0 * x0(0) + 1.0 * x0(1) + 0.5 * u(0),
                          0.0 * x0(0) + 1.0 * x0(1) + 1.0 * u(0)};

  fmt::print("X1Truth {}\n", x1Truth(1));
  return 0;
}
