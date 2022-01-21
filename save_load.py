import marisa_trie

#相当于列表 marisa_trie.Trie
trie = marisa_trie.Trie([u'key1',u'key2',u'key12'])

# Trie 对象支持保存/加载、pickling/unpickling 和内存映射 I/O。
# 将尝试保存到文件：
trie.save('my_trie.dic')
#加载
trie2 = marisa_trie.Trie()
trie2.load('my_trie.dic')

#判断某个键是否在trie里
print(u'key1'in trie2)    #True
print(u'key20'in trie2)   #False
#返回key的索引
print(trie2[u'key2'])      #1
#根据索引找到key
print(trie2.restore_key(1))    #key2
#找到key所有的前缀
print(trie2.prefixes(u'key12'))     #['key1', 'key12']
#找到所有前缀为key的keys
print(trie2.keys(u'key1'))       #['key1', 'key12']


# Trie objects are picklable:
# import pickle
# data = pickle.dumps(trie2)
# trie3 = pickle.load(data)
