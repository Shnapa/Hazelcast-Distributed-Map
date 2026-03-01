import hazelcast

print("Connecting to Hazelcast cluster...")
client = hazelcast.HazelcastClient(
    cluster_name="dev",
    cluster_members=["localhost:5701", "localhost:5702", "localhost:5703"]
)
print("Connected!")

dist_map = client.get_map("my-map").blocking()
print("Got distributed map: 'my-map'")

print("Writing 1000 values...")
for i in range(1001):
    dist_map.put(str(i), f"value-{i}")
    print(f"Written: {i} -> value-{i}")

print(f"Total entries in map: {dist_map.size()}")

client.shutdown()
print("Client disconnected")