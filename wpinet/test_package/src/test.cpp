#include <wpinet/HttpUtil.h>

int main(int argc, char** argv) {
  wpi::HttpPath path{"http://10.20.53.2:5800/index.html"};
  if(!path.empty()) {
    return 0;
  }
  else {
    return -1;
  }
}