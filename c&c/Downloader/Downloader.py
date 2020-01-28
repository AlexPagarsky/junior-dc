import urllib.request
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='data downloader')
    parser.add_argument('url',
                        type=str,
                        help='URL which content will be downloaded')
    args = parser.parse_args()

    # actual code
    path = args.url.split('/')
    urllib.request.urlretrieve(url=args.url, filename=path[-1])
    print("Finished")
