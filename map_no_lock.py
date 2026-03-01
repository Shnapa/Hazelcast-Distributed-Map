import hazelcast
import time

client = hazelcast.HazelcastClient(
    cluster_members=["localhost:5701", "localhost:5702", "localhost:5703"]
)

map = client.get_map("lock-test").blocking()

map.put_if_absent("key", 0)

start = time.time()

for k in range(10_000):
    value = map.get("key")
    value += 1
    map.put("key", value)

end = time.time()

print(f"Final value: {map.get('key')}")
print(f"Time: {end - start:.2f}s")

client.shutdown()