import text_manipulate
import layout_switcher

def main():
	try:
		text_manipulate.manipulator(layout_switcher.switch_layout)
	except Exception as e:
		import ipdb; ipdb.set_trace()
		input()


if __name__ == "__main__":
	main()