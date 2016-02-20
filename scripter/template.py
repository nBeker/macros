import argparse
import play


def handle_arguments():
    parser = argparse.ArgumentParser(description="macro")
    parser.add_argument("-d", "--delay", type=int, help="Delay between actions (milliseconds)",
                          required=False, default=100, dest="delay")
    parser.add_argument("-r", "--repeats", type=int, help="How many times to repeat the macro",
                          required=False, default=1, dest="repeats")

    return parser.parse_args()


ACTIONS_JSON = "${actions_json}"

if __name__ == "__main__":
    args = handle_arguments()
    play.play_macro(macro_json=ACTIONS_JSON,
                    action_delay=args.delay / 1000.,
                    repeats=args.repeats,
                    animate_mouse=False)