#include "apriltag.h"
#include "tag16h5.h"

int main(int argc, char** argv) {
  apriltag_family_t *tf = NULL;
  tf = tag16h5_create();
  tag16h5_destroy(tf);
  return 0;
}