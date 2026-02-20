# threat instance logs

threat_instance = {
    "title": "Suspicious PowerShell Activity Detected",
    "description": "Multiple endpoints executed obfuscated PowerShell commands attempting to download a remote payload from an unknown external server.",
    "mitre": {
        "T1059.001": "Command and Scripting Interpreter: PowerShell",
        "T1105": "Ingress Tool Transfer",
        "T1027": "Obfuscated Files or Information"
    },
    "log_lines": [
        "powershell.exe -EncodedCommand SQBFAFgA...",
        "Outbound connection to 185.203.119.45 over port 443",
        "File dropped at C:\\Users\\Public\\update.ps1"
    ],
    "confidence": "High",
    "recommendations": [
        "Isolate affected endpoints from the network",
        "Block malicious IP addresses at the firewall",
        "Perform full antivirus and EDR scans",
        "Reset credentials associated with impacted users"
    ],
    "indicators_of_compromise": [
        "185.203.119.45",
        "malicious-update[.]com",
        "C:\\Users\\Public\\update.ps1",
        "SHA256: a3f5c9d8b1e72b4a9c0f7a1234567890abcdef1234567890abcdef1234567890"
    ],
    "tags": [
        "powershell",
        "malware",
        "command-and-control",
        "incident-response"
    ],
    "notes": "Activity observed across three workstations within a 10-minute window. Behavior is consistent with early-stage compromise."
}

print(threat_instance['log_lines'][1])

# fruit dictionary

# fruits = {
#     "apple": "A sweet, crunchy fruit that grows on trees and comes in many varieties.",
#     "banana": "A soft, elongated tropical fruit with a yellow peel and sweet flesh.",
#     "orange": "A round citrus fruit known for its juicy segments and high vitamin C content.",
#     "mango": "A tropical stone fruit with sweet, juicy flesh and a large seed inside."
# }

# print(fruits['apple'])

# fruits['grape'] = 'A small, juicy fruit that grows in bunches.'

# fruits['banana'] = 'A soft, sweet tropical fruit with a yellow peel.'


# del fruits['mango']

# for fruit, description in fruits.items():
#     print(f"{fruit.title()}: {description}")


# people JSON

# people = [
#     {
#         "name": "Josh",
#         "age": 35,
#         "profession": "Cyber Professional",
#         "locations": ["United States", "Thailand", "Japan"],
#         "likes": [
#             "Japanese sweet potato",
#             "cakes",
#             "pizza",
#             "sushi"
#         ]
#     },
#     {
#         "name": "Maya",
#         "age": 32,
#         "profession": "Cyber Professional",
#         "locations": ["United States", "Thailand", "Japan"],
#         "likes": [
#             "Japanese sweet potato",
#             "cakes",
#             "pizza",
#             "sushi"
#         ]
#     },
#     {
#         "name": "Daniel",
#         "age": 30,
#         "profession": "Cyber Professional",
#         "locations": ["United States", "Thailand", "Japan"],
#         "likes": [
#             "Japanese sweet potato",
#             "cakes",
#             "pizza",
#             "sushi"
#         ]
#     },
#     {
#         "name": "Aiko",
#         "age": 40,
#         "profession": "Cyber Professional",
#         "locations": ["United States", "Thailand", "Japan"],
#         "likes": [
#             "Japanese sweet potato",
#             "cakes",
#             "pizza",
#             "sushi"
#         ]
#     }
# ]


# print(people[3]["locations"][1])
