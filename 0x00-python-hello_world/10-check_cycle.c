#include "lists.h"

/**
 * check_cycle - checks for a loop in a linked list
 * @list: list to check
 * Return: 1 if there is a loop, 0 if not
 */

int check_cycle(listint_t *list)
{
	listint_t *slow = NULL, *fast = list;
	int i = 0;

	while (fast)
	{
		if (fast == slow)
			return (1);
		fast = fast->next;
		if (i == 0)
			slow = list;
		else if (i % 2 == 0)
			slow = slow->next;
		i++;
	}
	return (0);
}
