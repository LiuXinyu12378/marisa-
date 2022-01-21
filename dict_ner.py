import marisa_trie
import os


class DictionaryNER:
    MatchLongest = 0
    MatchAll = 1
    ne_types = (
                'entertainment_music-album',
                'entertainment_music-song',
                'entertainment_music-singer')
    domains = list(set(ne_type.split('_')[0] for ne_type in ne_types))

    def __init__(self, data_dir):
        self.ne_dict = {}  # domain => [(ne_type1, ne_trie1), (ne_type2, ne_trie2), ...]
        for ne_type in self.ne_types:
            fn = os.path.join(data_dir, f'{ne_type}.dic')
            if not os.path.isfile(fn): continue
            domain, sub_type = ne_type.split('_')
            subtype_dicts = self.ne_dict.get(domain, [])
            subtype_dicts.append((sub_type, marisa_trie.Trie().mmap(fn)))
            self.ne_dict[domain] = subtype_dicts
            print(f'{ne_type} loaded')

    '''
    text: preprocessed text
    dicts: list of tuples, [(ne_type1, ne_trie1), (ne_type2, ne_trie2), ...]
    domains: list of top level domain names
    strategy: MatchLongest(default) or MatchAll
    seg: a list of word begin positions; None indicates match by character, i.e. seg=[0, 1, 2, 3, ..., len(text)]
    @return
    result: dictionary, domain => list of tuples, [(ne_type1, begin1, end1), (ne_type2, begin2, end2), ...]
    '''
    def match(self, text, domains=domains, strategy=MatchLongest, seg=None):  # seg is a list of word begin positions
        if seg is None:
            seg = list(range(len(text)+1))
        result = {}
        for domain in set(domains):
            domain_dicts = self.ne_dict.get(domain, None)
            if not domain_dicts:
                continue

            matches = self.__match_by_dicts(text, seg, domain_dicts, strategy)
            if matches:
                result[domain] = matches
        return result

    '''
    text: preprocessed text
    dicts: list of tuples, [(ne_type1, ne_trie1), (ne_type2, ne_trie2), ...]
    seg: a list of word begin positions
    @return
    matches: list of tuples, [(ne_type1, begin1, end1), (ne_type2, begin2, end2), ...]
    '''
    def __match_by_dicts(self, text, seg, dicts, strategy):
        seg_set = set(seg)
        matches = []  #
        if strategy == DictionaryNER.MatchAll:
            for i in seg[:-1]:
                for ne_type, ne_trie in dicts:
                    for prefix in ne_trie.iter_prefixes(text[i:]):
                        j = i + len(prefix)
                        if j in seg_set:
                            matches.append((ne_type, i, j))

        elif strategy == DictionaryNER.MatchLongest:
            cur_end = 0
            for i in seg[:-1]:
                if i < cur_end:
                    continue
                longest_match_ne_type = None
                longest_match_length = 0
                for ne_type, ne_trie in dicts:
                    for prefix in ne_trie.iter_prefixes(text[i:]):
                        if len(prefix) > longest_match_length:
                            longest_match_length = len(prefix)
                            longest_match_ne_type = ne_type
                if longest_match_length > 0 and (i + longest_match_length) in seg_set:
                    cur_end = i + longest_match_length
                    matches.append((longest_match_ne_type, i, cur_end))
        return matches


if __name__ == '__main__':
    dict_ner = DictionaryNER('dicts.marisa')
    print(dict_ner.domains)
    print(dict_ner.ne_dict)

    print(dict_ner.match("我是王蓉，我不是黄蓉"))