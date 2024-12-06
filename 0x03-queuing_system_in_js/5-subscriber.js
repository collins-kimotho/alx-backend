import redis from 'redis';

// Create a Redis client
const subscriber = redis.createClient();

// Handle connection events
subscriber.on('connect', () => {
  console.log('Redis client connected to the server');
});

subscriber.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err.message}`);
});

// Subscribe to the channel
subscriber.subscribe('ALXchannel');

// Listen for messages on the channel
subscriber.on('message', (channel, message) => {
  console.log(message);

  // If the message is KILL_SERVER, unsubscribe and quit
  if (message === 'KILL_SERVER') {
    subscriber.unsubscribe();
    subscriber.quit();
  }
});
