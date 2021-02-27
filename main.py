from configparser import ConfigParser


if __name__ == '__main__':
    cfg = ConfigParser()
    cfg.read('./config/secret.ini')
    cfg.read('./config/config.ini')
    print(cfg.get('main', 'token'))
