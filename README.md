# smart-redis-storage <sup>v1.0.0</sup>

A lightweight and efficient Redis storage manager for Python applications. Provides simple CRUD (Create, Read, Update, Delete) operations with JSON serialization and hash-based data organization.

---

[![PyPI Downloads](https://static.pepy.tech/badge/smart-redis-storage)](https://pepy.tech/projects/smart-redis-storage)
![GitHub top language](https://img.shields.io/github/languages/top/smartlegionlab/smart-redis-storage)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/smart-redis-storage?label=pypi%20downloads)](https://pypi.org/project/smart-redis-storage/)
[![GitHub release (latest by date)](https://img.shields.io/github/v/release/smartlegionlab/smart-redis-storage)](https://github.com/smartlegionlab/smart-redis-storage/)
[![GitHub](https://img.shields.io/github/license/smartlegionlab/smart-redis-storage)](https://github.com/smartlegionlab/smart-redis-storage/blob/master/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/smart-redis-storage)](https://pypi.org/project/smart-redis-storage)
[![PyPI - Format](https://img.shields.io/pypi/format/smart-redis-storage)](https://pypi.org/project/smart-redis-storage)
[![GitHub Repo stars](https://img.shields.io/github/stars/smartlegionlab/smart-redis-storage?style=social)](https://github.com/smartlegionlab/smart-redis-storage/)
[![GitHub watchers](https://img.shields.io/github/watchers/smartlegionlab/smart-redis-storage?style=social)](https://github.com/smartlegionlab/smart-redis-storage/)
[![GitHub forks](https://img.shields.io/github/forks/smartlegionlab/smart-redis-storage?style=social)](https://github.com/smartlegionlab/smart-redis-storage/)

---

## Features

- **Simple CRUD Operations**: Easy-to-use methods for Create, Read, Update, and Delete operations
- **JSON Serialization**: Automatic serialization and deserialization of Python objects
- **Hash-based Storage**: Organized data storage using Redis hashes with unique keys
- **TTL Support**: Configurable expiration time for stored data
- **Thread-safe**: Built on Redis-py, suitable for multi-threaded applications
- **Flexible Data Structure**: Store multiple key-value pairs under a single unique identifier

---

## ⚠️ Disclaimer

**By using this software, you agree to the full disclaimer terms.**

**Summary:** Software provided "AS IS" without warranty. You assume all risks.

**Full legal disclaimer:** See [DISCLAIMER.md](https://github.com/smartlegionlab/smart-redis-storage/blob/master/DISCLAIMER.md)

---

## Installation

```bash
pip install smart-redis-storage
```

## Requirements

- Python 3.6+
- Redis server
- redis-py library

---

## Quick Start

```python
from smart_redis_storage.redis_storage import RedisStorageManager

# Initialize with default Redis connection (localhost:6379)
redis_storage = RedisStorageManager()

# Store user data
user_id = 123
redis_storage.set_data(
    uniq_key=user_id, 
    key='profile', 
    value={'name': 'John', 'age': 30, 'email': 'john@example.com'}
)

# Retrieve user data
profile = redis_storage.get_data(uniq_key=user_id, key='profile')
print(profile)  # {'name': 'John', 'age': 30, 'email': 'john@example.com'}

# Store with expiration (30 seconds)
redis_storage.set_data(
    uniq_key=user_id,
    key='session_data',
    value={'token': 'abc123', 'last_login': '2026-01-01'},
    expiration=30
)
```

---

## Advanced Usage

### Custom Redis Connection

```python
# Connect to custom Redis instance
redis_storage = RedisStorageManager(
    host='redis-server.com', 
    port=6379, 
    db=1
)
```

### Multiple Data Operations

```python
# Store multiple pieces of data under same unique key
user_id = 456
redis_storage.set_data(user_id, 'preferences', {'theme': 'dark', 'language': 'en'})
redis_storage.set_data(user_id, 'cart', {'items': [1, 2, 3], 'total': 150.0})

# Get all data for a user
all_user_data = redis_storage.get_all_data(user_id)
print(all_user_data)
# {'preferences': {'theme': 'dark', 'language': 'en'}, 'cart': {'items': [1, 2, 3], 'total': 150.0}}

# Update specific data
redis_storage.update_data(user_id, 'preferences', {'theme': 'light', 'language': 'en'})

# Pop data (read and remove)
cart_data = redis_storage.pop_data(user_id, 'cart')
print(cart_data)  # {'items': [1, 2, 3], 'total': 150.0}

# Check remaining TTL
ttl = redis_storage.get_ttl(user_id)
print(f"TTL: {ttl} seconds")
```

### Data Management

```python
# Delete specific key
redis_storage.delete_key(user_id, 'preferences')

# Delete all data for a unique key
redis_storage.delete_all_hash(user_id)

# Check if data exists
data = redis_storage.get_data(user_id, 'nonexistent_key')
print(data)  # None
```

---

## API Reference

### RedisStorageManager Class

#### Constructor
```python
RedisStorageManager(host='localhost', port=6379, db=0)
```

#### Methods

- **set_data(uniq_key, key, value, expiration=None)**  
  Store data with optional expiration (in seconds)

- **get_data(uniq_key, key, pop=False)**  
  Retrieve data. Set `pop=True` to remove after reading

- **get_all_data(uniq_key)**  
  Retrieve all key-value pairs for a unique identifier

- **update_data(uniq_key, key, value, expiration=None)**  
  Update existing data (alias for set_data)

- **pop_data(uniq_key, key)**  
  Retrieve and remove data

- **delete_key(uniq_key, key)**  
  Remove specific key

- **delete_all_hash(uniq_key)**  
  Remove all data for a unique identifier

- **get_ttl(uniq_key)**  
  Get remaining time-to-live in seconds

---

## Use Cases

### Session Management
```python
# Store user session
def store_user_session(user_id, session_data):
    redis_storage.set_data(
        uniq_key=user_id,
        key='session',
        value=session_data,
        expiration=3600  # 1 hour
    )

# Retrieve and validate session
def get_valid_session(user_id):
    session = redis_storage.get_data(user_id, 'session')
    if session and session.get('valid_until') > time.time():
        return session
    return None
```

### Cache Management
```python
# Cache expensive computation results
def get_cached_data(user_id, data_key, compute_function):
    cached = redis_storage.get_data(user_id, data_key)
    if cached is not None:
        return cached
    
    # Compute and cache if not found
    result = compute_function()
    redis_storage.set_data(user_id, data_key, result, expiration=300)
    return result
```

### Multi-tenant Data Isolation
```python
# Different tenants can use the same storage with different unique keys
tenant_a_data = redis_storage.get_all_data('tenant_a')
tenant_b_data = redis_storage.get_all_data('tenant_b')
```

---

## Storage Structure

The library uses Redis hashes with the following pattern:
- Key format: `uniq:{unique_identifier}`
- Field: Your specified key
- Value: JSON-serialized data

Example:
```
uniq:123 (Hash)
  ├── profile → '{"name": "John", "age": 30}'
  ├── session → '{"token": "abc123", "last_login": "2026-01-01"}'
  └── preferences → '{"theme": "dark", "language": "en"}'
```

---

## Error Handling

The library handles Redis connection errors and JSON serialization/deserialization automatically. In case of connection issues, Redis-py will raise appropriate exceptions that you can catch in your application.

```python
try:
    redis_storage.set_data(user_id, 'key', {'data': 'value'})
except redis.ConnectionError as e:
    print(f"Redis connection error: {e}")
except Exception as e:
    print(f"Unexpected error: {e}")
```

---

## Performance Considerations

- Uses Redis hashes for efficient storage of multiple related data
- JSON serialization adds overhead but provides flexibility
- Consider data size and expiration policies for optimal performance
- Batch operations can be implemented by storing multiple keys under same unique identifier

---

## License

*Licensed under [BSD 3-Clause License](LICENSE) • Copyright (©) 2026, [Alexander Suvorov](https://github.com/smartlegionlab)*

---

## Author

**Alexander Suvorov**  
- GitHub: [@smartlegionlab](https://github.com/smartlegionlab)
- Package: [PyPI](https://pypi.org/project/smart-redis-storage/)

---
