#include <photonlib/PhotonUtils.h>
#include <units/length.h>

int main(int argc, char** argv) {
    units::meter_t range = photonlib::PhotonUtils::CalculateDistanceToTarget(2_m, 5_m, 1_deg, units::degree_t{10});
    fmt::print("Range: {}\n", range.value());
    return 0;
}