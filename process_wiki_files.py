from somajo import SoMaJo
import os
import re
from multiprocessing import Pool, cpu_count

# user settings
INPUT_DIR = "data/dewiki-20220201"
OUTPUT_DIR = "data/dewiki-20220201-clean"
LANGUAGE = "de"
# LANGUAGE = "en"

tokenizer = SoMaJo(f"{LANGUAGE}_CMC")
html_tag_patten = re.compile('<[^<>]+>')


# see https://github.com/tsproisl/SoMaJo/issues/17
def detokenize(tokens):
    """Convert SoMaJo tokens to sentence (str)."""
    result_list = []
    for token in tokens:
        if token.original_spelling is not None:
            result_list.append(token.original_spelling)
        else:
            result_list.append(token.text)

        if token.space_after:
            result_list.append(" ")
    result = "".join(result_list)
    result = result.strip()
    return result


def is_doc_start_line(line):
    return line.startswith('<doc id=')


def is_doc_end_line(line):
    return line.startswith('</doc>')


def get_data_dirs(root_dir):
    return [name for name in os.listdir(root_dir)
            if os.path.isdir(os.path.join(root_dir, name))]


def get_data_files(root_dir):
    return [name for name in os.listdir(root_dir)
            if os.path.isfile(os.path.join(root_dir, name))]


def process_text_line(line):
    # remove HTML taks if still there
    line = re.sub(html_tag_patten, ' ', line)

    sentences = tokenizer.tokenize_text([line])

    result = []

    for s in sentences:
        sentence_string = detokenize(s)
        result.append(sentence_string)

    return result


def process_directory(map_item):
    input_dir, output_file_name = map_item
    print("Creating:", output_file_name)
    with open(os.path.join(OUTPUT_DIR, output_file_name), 'a') as output_file:
        # r_=root, d_=directories, f_=files
        data_files = get_data_files(input_dir)
        for data_file in data_files:
            next_input_file = os.path.join(input_dir, data_file)
            print("Reading file:", next_input_file)

            with open(next_input_file, "r") as input_file:

                skip_next_line = False

                for line in input_file:

                    # drop line with start tag
                    if is_doc_start_line(line):
                        skip_next_line = True
                        continue

                    # drop line with end tag and append blank line
                    if is_doc_end_line(line):
                        output_file.write("\n")
                        continue

                    # skip first line to skip headline
                    if skip_next_line:
                        skip_next_line = False
                        continue

                    # skip empty lines
                    if len(line) <= 1:
                        continue

                    sentences = process_text_line(line)

                    for sentence in sentences:
                        # ignore blank lines and make sure that stuff like "\n" is also ignored:
                        if len(sentence) > 2:
                            output_file.write(f"{sentence}\n")


if __name__ == '__main__':
    # get sub directories with data
    data_dirs = get_data_dirs(INPUT_DIR)

    # create tasks for parallel execution
    task_list = []
    for data_dir in data_dirs:
        call_item = (os.path.join(INPUT_DIR, data_dir), data_dir + ".txt")
        task_list.append(call_item)

    pool_size = cpu_count() * 4
    print("pool_size:", pool_size)

    # execute tasks in parallel
    with Pool(pool_size) as p:
        p.map(process_directory, task_list)

    print("Done!")
