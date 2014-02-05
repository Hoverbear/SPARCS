// NOTE: This is not written in Python, you will need a C compiler to use this code.

// This code shows the maximum value of a 32-bit integer.

#include <stdio.h>        /* Standard IO. */

int main(void) {
  int number = 0;
  while (number + 1 > number) {
    number++;
  }
  fprintf(stderr, "The max number is: %d, the next number would be: %d\n", number, number+1);
}