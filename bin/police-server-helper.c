
#include <unistd.h> /* for execv() */
#include <stdio.h> /* for perror() */

#define REAL_PATH "/root/police/bin/police"

int main(int argc, char ** argv)
{
	if (argc != 3) {
		printf("Mussing arguments\n");
		return 1;
	}


	char * argve[4] = { REAL_PATH, "-q", "request", "host" };
	argve[2] = argv[1];
	argve[3] = argv[2];
    execv(REAL_PATH, argve);
    perror("Can't execue main script");
    return 126;
}

