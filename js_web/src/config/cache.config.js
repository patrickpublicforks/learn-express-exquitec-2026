import { createClient } from 'redis';

var RedisClient = createClient({
    url: process.env.REDIS_URL
});

async function connectToRedis() {
  try {
    RedisClient.on('error', (err) => console.log('Redis Client Error', err)); // Mandatory error handling
    await RedisClient.connect();

    return RedisClient;
  } catch (e) {
    console.error(e);
  }
}

connectToRedis();

export default RedisClient;