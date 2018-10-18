
#include <unistd.h> /* for execv() */
#include <stdio.h> /* for perror() */

#define REAL_PATH "/usr/bin/police-client"

int main(int argc, char ** argv)
{
	char ** argve = NULL;
    execv(REAL_PATH, argve);
    perror("Can't execue main script");
    return 126;
}

