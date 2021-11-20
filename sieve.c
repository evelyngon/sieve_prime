#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <math.h>

void sieve(int n, bool *isprime) {
  isprime[0] = isprime[1] = false;
  for (int i=2; i<n; i++)
    isprime[i] = true;

  for (int j=2; j*j<=n; j++) {
    if (isprime[j]) {
      for (int i=j*j; i<=n; i+=j)
        isprime[i] = false;
    }
  }
}

int main(int argc, char **argv) {
  if (argc < 2)
    printf("USAGE:\n\t sieve natural_number");
  else {
    int n = atoi(argv[1]);
    if (n < 2) {
      printf("No primes\n");
      exit(0);
    }

    bool isprime[n+1];
    sieve(n+1, isprime);
    for (int i=0; i<n+1; i++)
      if(isprime[i])
        printf("%d ", i);
    printf("\n");
  }
  return 0;
}
