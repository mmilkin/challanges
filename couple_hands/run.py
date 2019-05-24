from collections import deque


class Solution(object):
    def min_swaps_couples(self, input):
        """
        :type row: List[int]
        :rtype: int
        """
        row = deque(input)
        swaps = 0
        item = self.get_next(row)
        while item:
            x = row[index - 1]
            y = row[index]

            x_partner = self.find_partner(x)
            y_partner = self.find_partner(y)

            if x == y_partner:
                continue

            # [(0, 2), 1, 3]

            # x = 0
            # y = 2

            # xp = 1
            # yp = 3

            swaps += 1

            index_xp, x_partner_neighbor = self.get_partners_partner(x_partner, row)

            # index_xp = 2
            # index_yp = 3
            # x_partner_neighbor = 3
            # y_partner_neighbor = 1

            if x_partner_neighbor == y_partner:
                # switch xpartner_neighbor with y
                pass
            else:
                index_yp, y_partner_neighbor = self.get_partners_partner(x_partner, row)
                # switch anyway

    def get_next(self, row):
        while row:

        pass


    def find_partner(self, number):
        if number % 2:
            return number - 1
        return number + 1

    def get_partners_partner(self, partner, row):
        partner_index = row.index(partner)
        partner_neighbor = row[partner_index + 1] if partner_index % 2 == 0 else row[partner_index - 1]
        return partner_index, partner_neighbor