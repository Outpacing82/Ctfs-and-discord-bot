#include <stdio.h>
#include <string.h>

void check_password(char *input) {
  char key[] = {0x1F, 0x3C, 0x2A, 0x55, 0x66, 0x7B, 0x12, 0x10, 0x1E, 0x33};
  char target[] = {0x46, 0x5B, 0x57, 0x3A, 0x03, 0x1F, 0x71, 0x75, 0x65, 0x52};

  for (int i = 0; i < 10; i++) {
    if ((input[i] ^ key[i]) != target[i]) {
      printf("Access Denied\n");
      return;
    }
  }
  printf("Access Granted! The flag is: flag{%s}\n", input);
}

int main() {
  char input[32];
  printf("Enter password: ");
  fgets(input, 32, stdin);
  input[strcspn(input, "\n")] = 0; // remove newline

  if (strlen(input) != 10) {
    printf("Wrong length! The password must be 10 characters long\n");
    return 1;
  }

  check_password(input);
  return 0;
}
