from fractions import Fraction as frac

def standard_form(m):
    absorb_state = []
    transit_state = []
    for index, row in enumerate(m):
        if row.count(0) == len(m[0]):
            absorb_state.append(index)
        else:
            transit_state.append(index)
    final_state = transit_state + absorb_state

    final = []
    for i, index1 in enumerate(final_state):
        final.append([])
        for index2 in final_state:
            final[i].append(m[index1][index2])
        total = sum(m[index1])
        if total != 0:
            for w in range(len(final_state)):
                final[i][w] = frac(final[i][w], total)

    return final, len(transit_state)