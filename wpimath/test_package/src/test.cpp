#include <frc/EigenCore.h>
#include <fmt/format.h>

int main(int argc, char** argv) {
  frc::Matrixd<2,2> mat{frc::Matrixd<2,2>::Zero()};
  fmt::print("Mat(0,0): {}\n", mat(0,0));
}