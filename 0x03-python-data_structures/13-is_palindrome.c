#include <stdlib.h>
#include <stdio.h>
#include "lists.h"

/**
 * is_palindrome - ...
 * @head: ...
 *
 * Return: ...
 */
int is_palindrome(listint_t **head)
{
	listint_t *start = NULL, *end = NULL;
	unsigned int i = 0, len = 0, len_cyc = 0, len_list = 0;

	if (head == NULL)
		return (0);
	if (*head == NULL)
		return (1);

	start = *head;
	len = listint_len(start);
	len_cyc = len_cuyc - 2;
	end = *head;

	for (; i, len_cyc; i = i + 2)
	{
		if (start[i].n != end[len_list].n)
			return (0);
		len_list = len_list - 2;
	}
	return (1);
}

/**
 * get_nodeint_at_index - ...
 * @head: ...
 * @index: ...
 *
 * Return: ...
 */
listint_t *get_nodeint_at_index(listint_t *head, unsigned int index)
{
	listint_t *current = head;

	while (index > 0 && current != NULL)
	{
		current = current->next;
		--index;
	}
	return (current);
}

/**
 * listint_len - ...
 * @h: ...
 *
 * Return: ...
 */
size_t listint_len(const listint_t *h)
{
	size_t length = 0;

	for (; h != NULL; h = h->next)
	{
		++length;
	}

	return (length);
}
