class Order:
    def __init__(self, id, order_type, operation, price, quantity):
        self.id = id
        self.order_type = order_type  # Buy or Sell
        self.operation = operation  # Add or Remove
        self.price = price
        self.quantity = quantity


class StockExchange:
    def __init__(self):
        self.buy_orders = []  # List of buy orders
        self.sell_orders = []  # List of sell orders

    def add_order(self, order):
        if order.operation == "Remove":
            self.remove_order(order)
            return

        if order.order_type == "Buy":
            self.buy_orders.append(order)
            # Sort descending by price for buy orders
            self.buy_orders.sort(key=lambda x: x.price, reverse=True)
        else:  # Sell
            self.sell_orders.append(order)
            # Sort ascending by price for sell orders
            self.sell_orders.sort(key=lambda x: x.price)

    def remove_order(self, order):
        if order.order_type == "Buy":
            self.buy_orders = [o for o in self.buy_orders
                               if not (o.id == order.id and
                                       o.price == order.price and
                                       o.quantity == order.quantity)]
        else:
            self.sell_orders = [o for o in self.sell_orders
                                if not (o.id == order.id and
                                        o.price == order.price and
                                        o.quantity == order.quantity)]

    def display_best_prices(self):
        print("\nBest Orders:")
        print("Buy orders:")
        for order in self.buy_orders:
            print(f"ID: {order.id}, Price: {order.price}, Quantity: {order.quantity}")

        print("\nSell orders:")
        for order in self.sell_orders:
            print(f"ID: {order.id}, Price: {order.price}, Quantity: {order.quantity}")


# Example usage
def main():
    exchange = StockExchange()

    # Adding orders from the example
    orders = [
        Order("001", "Buy", "Add", 20.00, 100),
        Order("002", "Sell", "Add", 25.00, 200),
        Order("003", "Buy", "Add", 23.00, 50),
        Order("004", "Buy", "Add", 23.00, 70),
        Order("003", "Buy", "Remove", 23.00, 50),
        Order("005", "Sell", "Add", 28.00, 100)
    ]

    for order in orders:
        exchange.add_order(order)

    exchange.display_best_prices()


if __name__ == "__main__":
    main()