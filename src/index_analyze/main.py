from datetime import datetime
import sys
from typing import List, Tuple
import pandas as pd
import pandas as pd
from dataclasses import dataclass, field


@dataclass
class Point:
    date: datetime
    price: float
    shares: float

@dataclass
class Investor:
    name: str
    invested: float = field(default=0.0)
    shares: float = field(default=0.0)
    transactions: List[Point] = field(default_factory=list)

    def buy(self, date, price, amount):
        shares = amount/price
        point = Point(date=date, price=price, shares=shares)
        self.transactions.append(point)
        self.shares += shares
        self.invested += amount

    @property
    def current_value(self):
        return self.shares * self.transactions[-1].price

    @property
    def total_precentage(self):
        return self.current_value/self.invested

    @property
    def years(self):
        first_year = self.transactions[0].date.year
        last_year = self.transactions[-1].date.year
        return (last_year - first_year)

    @property
    def yearly(self):
        return (self.current_value/self.invested) ** (1/self.years)

    @property
    def total(self):
        first_year = self.transactions[0].price
        last_year = self.transactions[-1].price
        return last_year/first_year

    @property
    def total_yearly(self):
        return self.total ** (1/self.years)

    def inspect(self):
        return {
            "name": self.name,
            "current": self.current_value,
            "invested": self.invested,
            "shares": self.shares,
            "total_percentage": self.total_precentage,
            "last_price": self.transactions[-1].price,
            "total": self.total,
            "total_yearly": self.total_yearly,
            "years": self.years,
            "yearly": self.yearly,
        }


def parse_input(format="csv"):
    if format == "csv":
        return pd.read_csv(sys.stdin, parse_dates=['Date'], date_format="%b %d, %Y")
    elif format == "csv-curvo":
        return pd.read_csv(sys.stdin, parse_dates=['Date'], date_format="%Y-%m")
    return pd.read_json(sys.stdin)

def run(data):
    investor = Investor("stdin")
    for _, row in data.iterrows():
        investor.buy(row['Date'], row['Close'], 100)
    return investor

def main():
    result = run(parse_input("json"))
    print(result.inspect())

if __name__ == "__main__":
    main()
