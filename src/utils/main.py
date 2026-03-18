import argparse
import logging
import yaml
from redis import Redis

def configure_redis(config_file):
    with open(config_file, 'r') as stream:
        try:
            config = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            logging.error(f"Failed to parse YAML: {exc}")
            return None

    redis = Redis(host=config['redis']['host'], port=config['redis']['port'], db=config['redis']['db'])

    return redis

def main():
    parser = argparse.ArgumentParser(description='Cache Redis Config')
    parser.add_argument('-c', '--config', help='Path to the config file', required=True)
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO)

    redis = configure_redis(args.config)

    if redis is None:
        return 1

    redis.ping()

    return 0

if __name__ == "__main__":
    sys.exit(main())