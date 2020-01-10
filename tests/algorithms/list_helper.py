def convert_linked_list_to_list(head):
    list, current = [], head

    while current is not None:
        list.append(current.val)

        current = current.next

    return list
