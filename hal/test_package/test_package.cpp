#include "hal/HAL.h"
#include <fmt/format.h>

int main() {
  int type = HAL_GetRuntimeType();
  fmt::print("runtime type: {}\n", type);
  return 0;
}