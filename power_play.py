from subprocess import Popen as exec_cmd
from win32api import GetSystemMetrics
from sys import argv

from win32con import SM_CMONITORS as MONITORS_COUNT
from ss import *


COMMAND = r'C:\PROGRA~1\MPC-HC\mpc-hc64.exe "{file_path}" /monitor %d /fullscreen ' % GetSystemMetrics(MONITORS_COUNT)
SUBTITLES = '/sub "{subtitle_path}"'


def fetch_subtitles(input_filenames, config=None, multi=False):
    matches = dict()
    for input_filename in input_filenames:
        for language in config.languages:
            subtitle_path = has_subtitle(input_filename, language, multi)
            if subtitle_path:
                matches[language] = subtitle_path

    if matches:
        print('Found at least one subtitle, skipping download')
        return matches

    print("Subtitles were not found locally, Attempting download from OpenSubtitles")

    to_query = set(itertools.product(input_filenames, config.languages))

    if not to_query:
        return 0
    to_query = sorted(to_query)

    with ThreadPoolExecutor(max_workers=config.parallel_jobs) as executor:
        future_to_movie_and_language = {}
        for movie_filename, language in to_query:
            f = executor.submit(search_and_download, movie_filename,
                                language=language, multi=multi)
            future_to_movie_and_language[f] = (movie_filename, language)

        for future in as_completed(future_to_movie_and_language):
            movie_filename, language = future_to_movie_and_language[future]
            subtitle_filename = future.result()

            if subtitle_filename:
                matches[language] = subtitle_filename

            name = os.path.basename(movie_filename)
    return matches


def has_subtitle(filename, language, multi):
    # list of subtitle extensions obtained from opensubtitles' advanced search page.
    extensions = ['.sub', '.srt', '.ssa', '.smi', '.mpl']
    for extension in extensions:
        subtitle_filename = obtain_subtitle_filename(filename, language, extension, multi)
        if os.path.isfile(subtitle_filename):
            return subtitle_filename


def main(movie_path):
    config_filename = os.path.join(os.path.expanduser('~'), '.ss.ini')
    config = load_configuration(config_filename)

    input_filenames = list(find_movie_files([movie_path], recursive=config.recursive))
    multi = len(config.languages) > 1

    subtitles_argument = ""
    try:
        matches = fetch_subtitles(input_filenames, config=config, multi=multi)
        if matches:
            language, path = matches.popitem()
            print("Using language: '%s'" % language)
            subtitles_argument = SUBTITLES.format(subtitle_path=path)
    except:
        print("Something went wrong while trying to fetch subtitles, continuing without subs..")

    command = COMMAND.format(file_path=movie_path) + subtitles_argument
    print(command)
    exec_cmd(command)


if __name__ == "__main__":
    if len(argv) is not 2:
        print(argv)
        print("<power_play.py> <movie_name>")
    else:
        main(argv[1])