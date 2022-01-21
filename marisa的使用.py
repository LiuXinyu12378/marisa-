import marisa_trie

#相当于列表 marisa_trie.Trie
trie = marisa_trie.Trie([u'key1',u'key2',u'key12'])
#判断某个键是否在trie里
print(u'key1'in trie)    #True
print(u'key20'in trie)   #False
#返回key的索引
print(trie[u'key2'])      #1
#根据索引找到key
print(trie.restore_key(1))    #key2
#找到key所有的前缀
print(trie.prefixes(u'key12'))     #['key1', 'key12']
#找到所有前缀为key的keys
print(trie.keys(u'key1'))       #['key1', 'key12']



#新建一个marisa_trie.RecordTrie 字典（key，data）
#marisa的字典功能,且带有前置匹配
keys = [u'foo',u'bar',u'foobar',u'foo']
values = [(1,2),(2,1),(3,3),(2,1)]
fmt = "<HH"    #two short integers
trie = marisa_trie.RecordTrie(fmt,zip(keys,values))
#判断key值是否在字典中
print(u'foo' in trie)    #True
print(u'spam' in trie)      #False
#根据key值返回键值，且带有前置匹配
print(trie[u'bar'])       #[(2, 1)]
print(trie[u'foo'])       #[(1, 2), (2, 1)]
print(trie.get(u'bar',123))   #如果找到值，则返回值  [(2, 1)]
print(trie.get(u'BAAR',123))  #如果字典中没有该值，返回设定值  123
#找前缀为fo的所有key值
print(trie.keys(u'fo'))   #['foo', 'foo', 'foobar']
#找前缀为fo的所有键值对值
print(trie.items(u'fo'))    #[('foo', (1, 2)), ('foo', (2, 1)), ('foobar', (3, 3))]


#marisa_trie.BytesTrie     值为二进制的字典
keys = [u'foo', u'bar', u'foobar', u'foo']
values = [b'foo-value', b'bar-value', b'foobar-value', b'foo-value2']
trie = marisa_trie.BytesTrie(zip(keys, values))

print(trie[u'bar'])   #[b'bar-value']

# Trie 对象支持保存/加载、pickling/unpickling 和内存映射 I/O。
# 将尝试保存到文件：
trie.save('my_trie.marisa')







