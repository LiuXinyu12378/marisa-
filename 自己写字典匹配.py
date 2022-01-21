import marisa_trie
import os

class Dict_Ner():
    all_match = 0
    max_match = 1
    def __init__(self,dirpath,match=all_match):
        listdir = os.listdir(dirpath)
        self.match = match
        self.listdir = [dir for dir in listdir if dir.endswith("dic")]
        self.listdic = [ [dir.split("_")[1].replace(".dic",""),marisa_trie.Trie().load(os.path.join(dirpath,dir))] for dir in self.listdir]
        # self.listdic = [ [dir.split("_")[1].replace(".dic",""),marisa_trie.Trie().mmap(os.path.join(dirpath,dir))] for dir in self.listdir]           #不把字典全部加载到内存当中

    def find_entity(self,text):
        entities = []
        for cls,dic in self.listdic:
            entity = {}
            result = self.__find_entity(text,dic,self.match)
            if result:
                entity[cls] = result
                entities.append(entity)
        return entities

    def __find_entity(self,text,dic,match):
        text_len = len(text)
        entities = []
        if match == Dict_Ner.max_match:
            for i in range(text_len):
                _text = text[i:]
                #找到key所有的前缀
                results = dic.prefixes(_text)
                if len(results) > 0:
                    entity = max(results)
                    entities.append(entity)
            if entities:
                return max(entities)
            else:
                return []

        if match == Dict_Ner.all_match:
            for i in range(text_len):
                _text = text[i:]
                #找到key所有的前缀
                results = dic.prefixes(_text)
                if len(results) > 0:
                    entities.extend(results)
            if entities:
                return entities
            else:
                return []

if __name__ == '__main__':
    dict_ner = Dict_Ner('dicts.marisa',1)
    print(dict_ner.find_entity("我是王蓉，我不是黄蓉"))        #[{'music-album': '我不是黄蓉'}, {'music-singer': '王蓉'}, {'music-song': '我不是黄蓉'}]
    print(dict_ner.find_entity("请播放邓紫棋画"))              #[{'music-singer': '邓紫棋'}]
    print(dict_ner.find_entity("请播放美丽的神话"))            #[{'music-album': '美丽的神话'}, {'music-song': '美丽的神话'}]

# [{'music-album': ['我不是黄蓉']}, {'music-singer': ['王蓉']}, {'music-song': ['我不是黄蓉']}]
# [{'music-singer': ['邓紫', '邓紫棋']}]
# [{'music-album': ['美丽的神话', '神话']}, {'music-song': ['美丽的神话', '神话']}]