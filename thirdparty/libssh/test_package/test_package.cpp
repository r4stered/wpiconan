// Copyright (c) FIRST and other WPILib contributors.
// Open Source Software; you can modify and/or share it under the terms of
// the WPILib BSD license file in the root directory of this project.

#define LIBSSH_STATIC

#include <libssh/libssh.h>

#include <cstdlib>

int main() {
  ssh_session my_ssh_session = ssh_new();
  if (my_ssh_session == NULL)
    std::exit(-1);
  ssh_free(my_ssh_session);
  return 0;
}
