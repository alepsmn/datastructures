

# def contains_duplicate(nums:list[int])->bool:
#     return len(set(nums)) == len(nums)

# def group_anagrams(strs: list[str]) -> list[list[str]]:
#     dic = defaultdict(list)
#     for s in strs:
#         key = tuple(sorted(s))
#         dic[key].append(s)

#     return [v for k,v in dic.items()]
