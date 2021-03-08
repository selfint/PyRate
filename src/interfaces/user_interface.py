from typing import TypeVar, List, Optional

from src.interfaces.interface_device import InterfaceDevice
from src.interfaces.exceptions import assert_not_exception_keyword

from gensim import corpora, models, similarities


SupportedInputValueType = TypeVar("SupportedInputValueType", int, str)


class SimilarityChecker:
    def __init__(self, options: List[str]):
        assert len(options) > 0, "must receive at least one option"

        self.options = options
        self.threshold = 0.9

        texts = [[word for word in option.lower().split()] for option in options]
        self.dictionary = corpora.Dictionary(texts)
        corpus = [self.dictionary.doc2bow(text) for text in texts]
        self.lsi = models.LsiModel(corpus, id2word=self.dictionary, num_topics=2)
        self.index = similarities.MatrixSimilarity(self.lsi[corpus])

    def get_most_similar(self, user_input: str) -> Optional[str]:
        """
        Get option that is similar to user input, or None if no option is similar.

        :param user_input: Value user gave to check options against
        :return: Option with the highest similarity score to user user input
        """

        vec_bow = self.dictionary.doc2bow(user_input.lower().split())
        vec_lsi = self.lsi[vec_bow]
        sims = self.index[vec_lsi]
        max_percent = self.threshold
        best_index = None
        for index, percent_fraction in list(enumerate(sims)):
            if percent_fraction * 100 > max_percent:
                max_percent = percent_fraction * 100
                best_index = index

        if best_index is not None:
            return self.options[best_index]
        else:
            return None


class UserInterface:
    def __init__(
        self, stdin: InterfaceDevice, stdout: InterfaceDevice, stderr: InterfaceDevice
    ):
        self._stdin = stdin
        self._stdout = stdout
        self._stderr = stderr

    def get_input(self):
        """Get input from stdin"""
        return self._stdin.get_input()

    def send_output(self, msg: str):
        """Send message to stdout"""

        self._stdout.send_output(msg)

    def send_error(self, msg: str):
        """Send error message to stderr"""

        self._stderr.send_output(msg)

    def get_value(self, value_type: SupportedInputValueType) -> SupportedInputValueType:
        """
        Get a typed value from the user, loops until a valid input is given.

        :param value_type: Type of value to get
        :raises KeywordException - if user utters an exception keyword
        :return: Typed value
        """

        while True:
            value = self._stdin.get_input()
            assert_not_exception_keyword(value)

            try:
                return value_type(value)
            except (TypeError, ValueError):
                self._stderr.send_output(f"not a valid {value_type.__name__} value")

    def get_similar(self, ranked_options: List[List[str]]) -> str:
        """
        Get option that is similar to user input, loops until a similar option is found.

        Iterates through ranked options when comparing, and returns the option
        with the highest similarity score, in the first rank that has an option
        with a similarity score above the threshold.

        :param ranked_options: Options to check against, with index 0 as the first rank to check
        :return: Highest ranked option with a similarity score above the threshold
        """

        checkers = [SimilarityChecker(options) for options in ranked_options]

        while True:
            user_input = self._stdin.get_input()
            assert_not_exception_keyword(user_input)

            for checker in checkers:
                option = checker.get_most_similar(user_input)
                if option is not None:
                    return option

            self._stderr.send_output("didn't understand")
