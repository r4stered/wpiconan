#include "ntcore.h"
#include <fmt/format.h>

int main(int argc, char** argv) {
  auto myValue = nt::GetEntry(nt::GetDefaultInstance(), "MyValue");
  nt::SetEntryValue(myValue, nt::Value::MakeString("Hello World"));
  fmt::print("{}\n", nt::GetEntryValue(myValue).GetString());
}