# devops_list_examples.py

servers = ["web1", "web2", "db1"]

print("Total Servers:", len(servers))

for server in servers:
print(f"Pinging {server}")

pods = ["pod1", "pod2", "pod3"]

for pod in pods:
print(f"Checking status of {pod}")
