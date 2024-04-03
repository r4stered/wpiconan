#include <cstdlib>
#include <iostream>

#include "wpi/interpolating_map.h"

int main() {
  wpi::interpolating_map<double, double> table;

  table.insert(125, 450);
  table.insert(200, 510);
  table.insert(268, 525);
  table.insert(312, 550);
  table.insert(326, 650);

  printf("Test: %f\n", table[250]);

  return 0;
}