import importlib
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--module', required=True)
    parser.add_argument('--config', required=True)
    parser.add_argument('--data', default=None)
    args = parser.parse_args()

    mod = importlib.import_module(f"modules.{args.module}")
    mod_func = getattr(mod, args.module)
    mod_func(args.config, args.data)

if __name__ == "__main__":
    main()
