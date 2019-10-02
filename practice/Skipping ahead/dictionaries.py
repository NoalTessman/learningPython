#dictionaries are just objects in js and Ruby I think
customer = {
    "Name":"john Smith",
    "Age": 30,
    "is_verified":True
}
print(customer["Name"])
customer["Name"] = "Not John Smith"
print(customer["Name"])
