#include <sys/types.h>
#include <unistd.h>
#include <stdio.h>
#include <sys/wait.h>
/**
 * infinite_while - Functions that creates an infinite loop
 *
 * Return: 0 if the loop finish
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
 * main - main
 *
 * Return: 0
 */
int main(void)
{
	pid_t child_pid;
	unsigned int i = 0;
	int wait_status = 0;
	i = 0;
	while (i < 5)
	{
		child_pid = fork();
		if (child_pid != 0)
		{
			return (0);
		}
		printf("Zombie process created, PID: %d\n", child_pid);
		i++;
	}
	return (infinite_while());
}
