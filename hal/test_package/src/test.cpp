#include <fmt/core.h>
#include "hal/HAL.h"

int main(int argc, char** argv) {
  fmt::print("Hello World\n");
  fmt::print("{}\n", static_cast<int32_t>(HAL_GetRuntimeType()));
}