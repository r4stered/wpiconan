#include <pathplanner/lib/PathPlanner.h>
#include <pathplanner/lib/PathPlanner.h>
#include <pathplanner/lib/PathPoint.h>

using namespace pathplanner;

int main(int argc, char** argv) {
    PathPlannerTrajectory traj1 = PathPlanner::generatePath(
        PathConstraints(4_mps, 3_mps_sq), 
        PathPoint(frc::Translation2d(1_m, 1_m), frc::Rotation2d(0_deg)), // position, heading
        PathPoint(frc::Translation2d(3_m, 3_m), frc::Rotation2d(45_deg)) // position, heading
    );
    return 0;
}