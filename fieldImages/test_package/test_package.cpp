#include "fields/2024-crescendo.h"
#include "fields/fields.h"
#include <iostream>

int main() {
  static const fields::Field kField = {"2024 Crescendo",
                                       fields::GetResource_2024_crescendo_json,
                                       fields::GetResource_2024_field_png};
  std::cout << kField.getJson() << "\n";
}