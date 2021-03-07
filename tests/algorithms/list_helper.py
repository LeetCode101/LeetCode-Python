def convert_linked_list_to_list(head):
    list, current = [], head

    while current:
        list.append(current.val)

        current = current.next

    return list


def convert_circular_linked_list_to_list(head):
    if not head:
        return []

    list, current = [head.val], head.next

    while current and current is not head:
        list.append(current.val)

        current = current.next

    return list
