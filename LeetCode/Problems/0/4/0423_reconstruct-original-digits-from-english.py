class Solution:
    def originalDigits(self, s: 'str') -> 'str':
        count = Counter(s)

        out = {"0": count["z"], "2": count["w"], "4": count["u"], "6": count["x"], "8": count["g"]}
        out["3"] = count["h"] - out["8"]
        out["5"] = count["f"] - out["4"]
        out["7"] = count["s"] - out["6"]
        out["9"] = count["i"] - out["5"] - out["6"] - out["8"]
        out["1"] = count["n"] - out["7"] - 2 * out["9"]

        return "".join([key * out[key] for key in sorted(out.keys())])
