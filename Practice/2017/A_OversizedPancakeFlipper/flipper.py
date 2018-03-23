#!/usr/bin/env python3


# reading input
def parse_input(filename):
    with open(filename, "r") as f:
        test_cases = [case.split(" ") for case in f.readlines()[1:]]
        test_cases = [(pancakes, int(k)) for pancakes, k in test_cases]

    return test_cases


def flip(string, k, i):
    return (string[:i] +
            "".join("+" if char == "-" else "-" for
                    char in string[i:(i+k)]) +
            string[(i+k):])


# actually solve problem
def solve(pancakes, k):
    # Lemma: if an endpoint pancake p is '-', it must be flipped exactly once.
    # pf: if it's '-' it needs flipped an odd number of times, and there is
    # exactly one window (0 through k-1)
    left = 0
    right = len(pancakes)
    side = "left"
    count = 0

    while right - left > k-1:
        if side == "left":
            if pancakes[left] == '-':
                count += 1
                pancakes = flip(pancakes, k, left)
            side = "right"
            left += 1
        elif side == "right":
            if pancakes[right-1] == '-':
                count += 1
                pancakes = flip(pancakes, k, right-k)
                side = "left"
            right -= 1

    if '-' in pancakes:
        return "IMPOSSIBLE"
    else:
        return count


# make this file a runnable script
if __name__ == "__main__":
    from sys import argv as arguments
    from os import path

    if arguments[1] == "-single":
        pancakes = arguments[2]
        k = int(arguments[3])
        result = solve(pancakes, k)
        print("result for {0}, {1}: {2}".format(pancakes, k, result))
    else:
        infname = arguments[1]
        outfname = path.splitext(infname)[0] + ".out"

        test_cases = parse_input(arguments[1])
        results = [solve(pancakes, k) for pancakes, k in test_cases]
        with open(outfname, "w") as f:
            f.write("\n".join(
                "Case #{index}: {result}".format(index=i+1, result=r) for
                i, r in enumerate(results)))

        print("Done processing {0}. Check {1} for results.".format(
            infname, outfname))
