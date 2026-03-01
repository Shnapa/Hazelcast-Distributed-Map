import hazelcast
import time

client = hazelcast.HazelcastClient(
    cluster_members=["127.0.0.1:5701"]
)

map = client.get_map("lock-map").blocking()

map.put_if_absent("key", 0)

start = time.time()

for k in range(10_000):
    map.lock("key")
    try:
        value = map.get("key")
        value += 1
        map.put("key", value)
    finally:
        map.unlock("key")

elapsed = time.time() - start

print(f"Done. Final value: {map.get('key')}")
print(f"Time elapsed: {elapsed:.2f}s")

client.shutdown()