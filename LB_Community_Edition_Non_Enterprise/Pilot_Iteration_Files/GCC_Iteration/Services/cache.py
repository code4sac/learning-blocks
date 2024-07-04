from Pilot_Iteration_Files.GCC_Iteration.Config.RedisConfig import redis_client

def cache_data(key: str, value: str):
    redis_client.set(key, value)

def get_cached_data(key: str) -> str:
    return redis_client.get(key)
