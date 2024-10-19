class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        def justify_line(line, is_last_line=False):
            """Justifies a single line of words."""
            num_words = len(line)
            total_chars = sum(len(word) for word in line)
            spaces_needed = maxWidth - total_chars

            if num_words == 1 or is_last_line:  # Left justify
                return ' '.join(line) + ' ' * (spaces_needed - (num_words - 1))

            spaces_between_words = spaces_needed // (num_words - 1)
            extra_spaces = spaces_needed % (num_words - 1)

            justified_line = line[0]  # Start with the first word
            for i in range(1, num_words):
                spaces = ' ' * (spaces_between_words + (1 if i <= extra_spaces else 0))
                justified_line += spaces + line[i]

            return justified_line

        lines = []
        current_line = []
        current_length = 0

        for word in words:
            # n- 1 spaces required but we have 1 more word so its n
            n = len(current_line)
            if current_length + len(word) + n <= maxWidth:  # Check if word fits
                current_line.append(word)
                current_length += len(word)
            else:
                lines.append(justify_line(current_line))  # Justify the current line
                current_line = [word]  # Start a new line
                current_length = len(word)

        lines.append(justify_line(current_line, is_last_line=True))  # Justify the last line
        return lines