# smart_redis_storage <sup>0.1.0</sup>
Redis storage manager.

***

![GitHub top language](https://img.shields.io/github/languages/top/smartlegionlab/smart_redis_storage)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/smart_redis_storage?label=pypi%20downloads)](https://pypi.org/project/smart_redis_storage/)
[![GitHub release (latest by date)](https://img.shields.io/github/v/release/smartlegionlab/smart_redis_storage)](https://github.com/smartlegionlab/smart_redis_storage/)
[![GitHub](https://img.shields.io/github/license/smartlegionlab/smart_redis_storage)](https://github.com/smartlegionlab/smart_redis_storage/blob/master/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/smart_redis_storage)](https://pypi.org/project/smart_redis_storage)
[![PyPI - Format](https://img.shields.io/pypi/format/smart_redis_storage)](https://pypi.org/project/smart_redis_storage)
[![GitHub Repo stars](https://img.shields.io/github/stars/smartlegionlab/smart_redis_storage?style=social)](https://github.com/smartlegionlab/smart_redis_storage/)
[![GitHub watchers](https://img.shields.io/github/watchers/smartlegionlab/smart_redis_storage?style=social)](https://github.com/smartlegionlab/smart_redis_storage/)
[![GitHub forks](https://img.shields.io/github/forks/smartlegionlab/smart_redis_storage?style=social)](https://github.com/smartlegionlab/smart_redis_storage/)

***

Author and developer: ___A.A Suvorov___

***

## Help:

`pip install smart-redis-storage`

> CRUD (Create, Read, Update, Delete) for Redis.
> Used in a large corporate project in a multi-user CRM (Django) to store intermediate data.
> I used user ids as uniq_key.
> 
> 

```python
from smart_redis_storage.redis_storage import RedisStorageManager

user_id = 1
redis_storage_manager = RedisStorageManager()
redis_storage_manager.set_data(uniq_key=user_id, key='data', value={'id': 1, 'age': 33})
data = redis_storage_manager.get_data(uniq_key=user_id, key='data')
print(data) # {'id': 1, 'age': 33}
print(type(data)) # <class 'dict'>
```

***

## Disclaimer of liability:

    THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
    AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
    IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
    DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
    FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
    DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
    SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
    CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
    OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
    OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

***

## Copyright:
    --------------------------------------------------------
    Licensed under the terms of the BSD 3-Clause License
    (see LICENSE for details).
    Copyright © 2018-2024, A.A Suvorov
    All rights reserved.
    --------------------------------------------------------
