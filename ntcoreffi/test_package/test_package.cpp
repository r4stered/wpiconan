#include "networktables/NetworkTable.h"
#include "networktables/NetworkTableInstance.h"

int main() {
  auto inst = nt::NetworkTableInstance::Create();
  auto nt = inst.GetTable("containskey");
  nt->PutNumber("testkey", 5);
  nt::ResetInstance(inst.GetHandle());
  nt::NetworkTableInstance::Destroy(inst);
}