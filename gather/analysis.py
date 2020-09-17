from afinn import Afinn

class analysis_s(Afinn):
    def __init__(self, lang):
        Afinn.__init__(self, language=lang)

    def analyze(self, text):

        obj = {}

        scored_list = []
        good_list = []
        bad_list = []

        for s in text.split('.'):
            for w in self.find_all(s):
                if self._dict[w] > 0:
                    good_list.append(w)
                if self._dict[w] < 0:
                    bad_list.append(w)
            scored_list.append(self.score(s))

        result = (sum(scored_list) / len(scored_list))

        obj["positive_words"] = good_list
        obj["negative_words"] = bad_list
        obj["score"] = str(result)

        if result > 0:
            obj["eval"] = "POSITIVE"
        elif result < 0:
            obj["eval"] = "NEGATIVE"
        else:
            obj["eval"] = "NEUTRAL"

        return obj