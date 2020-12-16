#include "lists.h"

/**
 * list_len - returns the lenght of a list
 * @h: list to get lenght of.
 * Return: the size of the list
 */

size_t list_len(const listint_t *h)
{
	unsigned long int i;

	if (h == NULL)
		return (0);
	for (i = 1; h->next != NULL; i++)
		h = h->next;
	return (i);
}


/**
 * is_palindrome - checks if a list is a palindrome
 * @head: head of list
 * Return: 1 if palindrome or empty, else 0
 */

int is_palindrome(listint_t **head)
{
	size_t len, i, j;
	listint_t *start = *head, *end;

	len = list_len(start);

	if (len == 0 || len == 1 || !head || !start)
		return (1);
	printf("before first loop\n");
	for (i = 0; i < (len / 2); i++, start = start->next)
	{
		printf("before second loop\n");
		end = *head;
		for (j = 0; j < (len - (i) - 1); j++)
		{
			printf("end: %d\n", end->n);
			end = end->next;
		}
		printf("start: %d end: %d\n", start->n, end->n);
		if (start->n != end->n)
			return (0);
	}
	return (1);
}
