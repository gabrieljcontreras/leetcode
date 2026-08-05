from collections import Counter
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0: 
            return False

        count = Counter(hand)

        for card in sorted(count.keys()):
            if count[card] > 0: 
                num_groups = count[card]

                for i in range(groupSize):
                    target_card = card + i
                    if count[target_card] < num_groups: 
                        return False

                    count[target_card] -= num_groups
        return True

