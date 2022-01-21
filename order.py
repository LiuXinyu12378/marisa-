import marisa_trie

#新建一个marisa_trie.RecordTrie 字典（key，data）
#marisa的字典功能,且带有前置匹配
keys = [u'foo',u'bar',u'foobar',u'foo']
values = [(1,2),(2,1),(3,3),(2,1)]
fmt = "<HH"    #two short integers
#按字母顺序返回结果
# trie = marisa_trie.RecordTrie(fmt, zip(keys,values), order=marisa_trie.LABEL_ORDER)
trie = marisa_trie.RecordTrie(fmt, zip(keys,values), order=marisa_trie.WEIGHT_ORDER)
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


