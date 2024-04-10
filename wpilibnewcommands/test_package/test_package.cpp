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