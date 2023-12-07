from collections import Counter, defaultdict

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        total = 0
        chars_count = Counter(chars)

        for word in words:
            word_count = defaultdict(int)
            valid = True

            for c in word:
                word_count[c] += 1

                if c not in chars_count or chars_count[c] < word_count[c]:
                    valid = False
                    break

            if valid:
                total += len(word)

        return total


# from collections import Counter

# class Solution:
#     def countCharacters(self, words: List[str], chars: str) -> int:
#         total = 0
#         chars_count = Counter(chars)

#         for word in words:
#             word_count = Counter(word)
#             valid = True

#             for c in word_count:
#                 if c not in chars_count or chars_count[c] < word_count[c]:
#                     valid = False
#                     break

#             if valid:
#                 total += len(word)

#         return total
