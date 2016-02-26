import play


ACTIONS_JSON = "${actions_json}"

if __name__ == "__main__":
    args = play.handle_arguments()
    play.play_macro(macro_json=ACTIONS_JSON,
                    action_delay=args.delay / 1000.,
                    repeats=args.repeats,
                    animate_mouse=False)