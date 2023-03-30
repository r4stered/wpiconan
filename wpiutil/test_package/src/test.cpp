#include <wpi/interpolating_map.h>
#include <fmt/format.h>

int main(int argc, char** argv) {

  wpi::interpolating_map<double, double> map;

  map.insert(3, 0);
  map.insert(4, 10);

  if(map[3.5] == 5) {
    return 0;
  }
  else {
    return -1;
  }
}