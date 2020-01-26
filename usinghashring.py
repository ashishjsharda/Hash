from hash_ring import MemcacheRing
mc=MemcacheRing(['127.0.0.1:11212'])
mc.set('hello','world')
print(mc.get('hello'))
