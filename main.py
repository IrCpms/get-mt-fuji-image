from datetime import date
from datetime import datetime
from datetime import timedelta
from enum import Enum
from argparse import ArgumentParser
from urllib import request


class location(Enum):
    shimizu = 'shimizu'
    fujinomiya = 'fujinomiya'
    gotenba = 'gotenba'


def calc_date(from_date: date, to_date: date) -> None:
    """
    Args:
        from_date (datetime.date): Start date. 
        to_date (datetime.date): End date.

    Yields:
        datetime.date: Date.

    Example:
        >>> calc_date(date(2021,1,1), date(2021,12,31))
    """

    for day in range((to_date - from_date).days + 1):
        date = from_date + timedelta(day)
        yield date.strftime("%Y%m%d")


def main() -> None:
    parser = ArgumentParser(description='Mt. Fuji Image Downloader.')
    parser.add_argument('location', help='Location')
    parser.add_argument('from_date', help='Start date. ',
                        default=datetime.now().strftime('%Y%m%d'))
    parser.add_argument('to_date', help='End date.',
                        default=datetime.now().strftime('%Y%m%d'))
    parser.add_argument('--from_hour', help='Start Hour.', default=0)
    parser.add_argument('--to_hour', help='End Hour.', default=23)
    args = parser.parse_args()

    # Error handling.
    if args.from_date > args.to_date:
        raise ValueError('from_date is greater than to_date.')

    if not args.location in location.__members__:
        raise TypeError('Invalid location.')

    # String to datetime.
    from_date = datetime.strptime(args.from_date, '%Y%m%d')
    to_date = datetime.strptime(args.to_date, '%Y%m%d')

    # Main process.
    base_url = "https://www.pref.shizuoka.jp/~live/archive/"
    available_hours = range(args.from_hour, args.to_hour + 1)
    for date in calc_date(from_date, to_date):
        for hour in available_hours:
            available_hour = str(hour).zfill(2)
            download_url = f"{base_url}{str(date)}{args.location}/{available_hour}/xl.jpg"

            # Download image.
            save_name = f"{date}_{args.location}_{available_hour}_xl.jpg"
            request.urlretrieve(download_url, save_name)
            print(f"{download_url} -> {save_name}")


if __name__ == '__main__':
    main()
