import argparse

# import timeit
# from functools import partial


class WC:
    def __init__(self, files, count_lines, count_words, count_chars, count_bytes):
        self.files = files
        self.count_lines = count_lines
        self.count_words = count_words
        self.count_chars = count_chars
        self.count_bytes = count_bytes

    def count_file(self, file_path):
        with open(file_path, "rb") as file:
            content = file.read()
            utf8_decoded_content = content.decode("utf-8")

            if self.count_lines:
                lines_count = utf8_decoded_content.count("\n")
            else:
                lines_count = None

            if self.count_words:
                words = utf8_decoded_content.split()
                word_count = len(words)
            else:
                word_count = None

            if self.count_chars:
                char_count = len(utf8_decoded_content)
            else:
                char_count = None

            if self.count_bytes:
                byte_count = len(content)
            else:
                byte_count = None

            return lines_count, word_count, char_count, byte_count

    def execute(self):
        for file_path in self.files:
            try:
                lines_count, words_count, chars_count, byte_count = self.count_file(
                    file_path
                )
                output = ""
                if lines_count is not None:
                    output += f"{lines_count}\t"
                if words_count is not None:
                    output += f"{words_count}\t"
                if chars_count is not None:
                    output += f"{chars_count}\t"
                if byte_count is not None:
                    output += f"{byte_count}\t"
                output += file_path
                print(output)
            except FileNotFoundError:
                print(f"wc: {file_path}: No such file or directory")


def main():
    parser = argparse.ArgumentParser(description="wc command replica")
    parser.add_argument("files", metavar="FILE", nargs="+", help="input files")
    parser.add_argument(
        "-l", "--lines", action="store_true", help="print the newline counts"
    )
    parser.add_argument(
        "-w", "--words", action="store_true", help="print the word counts"
    )
    parser.add_argument(
        "-c", "--bytes", action="store_true", help="print the byte counts"
    )
    parser.add_argument(
        "-m", "--chars", action="store_true", help="print the character counts"
    )

    args = parser.parse_args()

    wc = WC(args.files, args.lines, args.words, args.chars, args.bytes)
    wc.execute()


if __name__ == "__main__":
    main()


# def measure_performance():
#     # Create an instance of the WC class with your desired arguments
#     wc = WC(
#         files=["test.txt"],
#         count_lines=True,
#         count_words=True,
#         count_chars=True,
#         count_bytes=True,
#     )

#     # Measure the execution time of the execute() method of the WC class
#     execution_time = timeit.timeit(partial(wc.execute), number=1)
#     print(f"Execution time: {execution_time:.6f} seconds")


# if __name__ == "__main__":
#     measure_performance()
