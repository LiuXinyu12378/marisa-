**MARISA-trie 中的字符串数据可能比标准 Python dict 占用内存少 50 到 100 倍；**

**原始查找速度相当；**

**trie 还提供了快速匹配的高级方法，例如前缀搜索。**



```
我是王蓉，我不是黄蓉
请播放邓紫棋画
请播放美丽的神话
```

### 全匹配

[{'music-album': ['我不是黄蓉']}, {'music-singer': ['王蓉']}, {'music-song': ['我不是黄蓉']}]
[{'music-singer': ['邓紫', '邓紫棋']}]
[{'music-album': ['美丽的神话', '神话']}, {'music-song': ['美丽的神话', '神话']}]

### 最大匹配

[{'music-album': '我不是黄蓉'}, {'music-singer': '王蓉'}, {'music-song': '我不是黄蓉'}]
[{'music-singer': '邓紫棋'}]
[{'music-album': '美丽的神话'}, {'music-song': '美丽的神话'}]
