#include "wpigui.h"

int main() {
  wpi::gui::CreateContext();
  wpi::gui::Initialize("Hello World", 1024, 768);
  wpi::gui::Main();
}