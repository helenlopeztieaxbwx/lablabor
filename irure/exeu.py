import json_agent

# Example list of list of JSON objects
list_of_lists = [
    [
        {"id": 1, "name": "John"},
        {"id": 2, "name": "Jane"}
    ],
    [
        {"id": 3, "name": "Alice"},
        {"id": 4, "name": "Bob"}
    ]
]

# Flatten the list of list of JSON objects into a single list
flattened_list = json_agent.flatten(list_of_lists)

print(flattened_list)
