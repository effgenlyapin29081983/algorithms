from collections import defaultdict

COUNT_QUARTERS = 4
lst = []
organization_count = int(input("Enter count of organizations:\n"))

for i in range(1,organization_count+1):
    organization_name = input(f"Enter name {i} organization:\n")
    for j in range (1,COUNT_QUARTERS + 1):
        organization_profit = float(input(f"Enter profit {j} quarter:\n"))
        lst.append((organization_name,organization_profit))

print(lst)

organizations = defaultdict(float)
for org_name, org_profit in lst:
    organizations[org_name] += org_profit

print(organizations)

avg_profit = sum(organizations.values())/len(organizations)

for org in organizations.items():
    if (org[1]>avg_profit):
        print(f"{org[0]} - is profitable(+)")
    elif (org[1]<avg_profit):
        print(f"{org[0]} - is unprofitable(-)")