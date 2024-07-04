import redis

# Assuming Redis is running locally on default port 6379
redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)

# Optionally, you can add more configuration here, like connection pooling settings, etc.
