#include "izombie.h"


/**
 * infinite_while - loop forever
 *
 *
 * Return: Never
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - spawn zombie processes
 *
 * Return: Never
 */
int main(void)
{
	int idz = 0;
	int i = 0;

	while (i++ < N_ZOMBIES)
	{
		idz = fork();
		if (idz)
			printf("Zombie process created, PID: %d\n", idz);
		else
			return (EXIT_SUCCESS);
	}
	return (infinite_while());
}
