
#include <unistd.h> /* for execv() */
#include <stdio.h> /* for perror() */

#define REAL_PATH "/usr/bin/police-client"

int main(int argc, char ** argv)
{
    execv(REAL_PATH, argv);
    perror("Can't execue main script");
    return 126;
}

