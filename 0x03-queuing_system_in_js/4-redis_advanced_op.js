import redis from 'redis';

// Create a Redis client
const client = redis.createClient();

// Handle connection events
client.on('connect', () => {
  console.log('Redis client connected to the server');
});
client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err.message}`);
});

// Store hash values using hset
client.hset('ALX', 'Portland', '50', redis.print);
client.hset('ALX', 'Seattle', '80', redis.print);
client.hset('ALX', 'New York', '20', redis.print);
client.hset('ALX', 'Bogota', '20', redis.print);
client.hset('ALX', 'Cali', '40', redis.print);
client.hset('ALX', 'Paris', '2', redis.print);

// Retrieve and display the hash object using hgetall
client.hgetall('ALX', (err, result) => {
  if (err) {
    console.error(`Error retrieving hash: ${err.message}`);
  } else {
    console.log(result);
  }

  // Close the Redis connection after retrieval
  client.quit();
});
