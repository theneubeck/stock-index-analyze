from dataclasses import dataclass, field
from datetime import datetime
from typing import List


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
        shares = amount / price
        point = Point(date=date, price=price, shares=shares)
        self.transactions.append(point)
        self.shares += shares
        self.invested += amount

    @property
    def current_value(self):
        return self.shares * self.transactions[-1].price

    @property
    def total_precentage(self):
        return self.current_value / self.invested

    @property
    def years(self):
        first_year = self.transactions[0].date.year
        last_year = self.transactions[-1].date.year
        return last_year - first_year

    @property
    def yearly(self):
        return (self.current_value / self.invested) ** (1 / self.years)

    @property
    def total(self):
        first_year = self.transactions[0].price
        last_year = self.transactions[-1].price
        return last_year / first_year

    @property
    def total_yearly(self):
        return self.total ** (1 / self.years)

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
