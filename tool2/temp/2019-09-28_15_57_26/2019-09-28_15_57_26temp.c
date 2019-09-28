#include <assert.h>
#include <stdlib.h>
void c4(int i);
void c3(int i);
void c1(int i);
void c2(int i);
int main(int argc, char** argv) {
  if (argc != 2) {
    return -1;
  }
  int i =1;

  c1(i);
  c2(i);
  return 0;
}

void c4(int i) {
  assert(i != 42);
}

void c3(int i) {
  c4(i * 7);
}

void c2(int i) {
  c3(i * 3);
}

void c1(int i) {
  c2(i * 2);
}

