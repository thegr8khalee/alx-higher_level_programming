#include "lists.h"

/**
 * insert_node - ...
 * @head: ...
 * @number: ...
 *
 * Return: ...
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *newNode;

	newNode = malloc(sizeof(listint_t));
	if (newNode == NULL)
		return (NULL);
	newNode->number = number;
	newNode->next = *head;
	*head = newNode;

	return (newNode);
}
