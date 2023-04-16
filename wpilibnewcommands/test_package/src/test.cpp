#include <frc2/command/CommandPtr.h>

int main(int argc, char** argv) {
  frc2::CommandPtr ptr = frc2::cmd::Print("Hello!\n");
}