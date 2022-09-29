import unittest

# Counts the number of a's in a sentence (e.g., a string)
def count_a(sentence):
	total = 0
	for i in range(len(sentence)):
		if sentence[i] == 'a':
			total += 1
	return total


# Item class
# Describes an item to be sold. Each item has a name, a price, and a stock.
class Item:
	# Constructor.
	def __init__(self, name, price, stock):
		self.name = name
		self.price = price
		self.stock = stock

	# Print
	def __str__(self):
		return ("Item = {}, Price = {}, Stock = {}".format(self.name, self.price, self.stock))

# Warehouse class
# A warehouse stores items and manages them accordingly.
class Warehouse:

	# Constructor
	def __init__(self, items = []):
		self.items = items

	# Prints all the items in the warehouse, one on each line.	
	def print_items(self):
		for item in self.items:
			print(item)
			print("\n")	

	# Adds an item to the warehouse	
	def add_item(self, item):
		self.items.append(item)
		

	# Returns the item in the warehouse with the most stock		
	def get_max_stock(self):
		if len(self.items) == 0:
			return None
		maxitem = self.items[0]
		maxamount = self.items[0].stock
		for item in self.items:
			amount = item.stock
			if amount > maxamount:
				maxamount = amount
				maxitem = item
		return maxitem
		
	
	# Returns the item in the warehouse with the highest price
	def get_max_price(self):
		if len(self.items) == 0:
			return None
		maxitem = self.items[0]
		maxprice = self.items[0].price
		for item in self.items:
			price = item.price
			if price > maxprice:
				maxprice = item.price
				maxitem = item
		return maxitem
			



# Tests
class TestAllMethods(unittest.TestCase):

	# SetUp -- we create a bunch of items for you to use in your tests.
	def setUp(self):
		self.item1 = Item("Beer", 6, 20)
		self.item2 = Item("Cider", 5, 25)
		self.item3 = Item("Water", 1, 100)
		self.item4 = Item("Fanta", 2, 60)
		self.item5 = Item("CocaCola", 3, 40)
		self.warehouse1 = Warehouse([self.item1, self.item2])

	## Check to see whether count_a works
	def test_count_a(self):
		self.assertEqual(count_a("Jack Basner"), 2, "Jack Basner")
		self.assertEqual(count_a("SI 206"), 0, "No A's")
		


	## Check to see whether you can add an item to the warehouse
	def test_add_item(self):
		self.warehouse1.add_item(self.item3)
		self.assertEqual(self.item1 in self.warehouse1.items, True, "Item 1 in Warehouse 1")
		self.assertEqual(self.item3 in self.warehouse1.items, True, "Item 3 in Warehouse 1")
		self.assertEqual(self.item4 in self.warehouse1.items, False, "Item 4 in Warehouse 1")



	## Check to see whether warehouse correctly returns the item with the most stock
	def test_warehouse_max_stocks(self):
		self.warehouse1.add_item(self.item1)
		self.warehouse1.add_item(self.item2)
		self.warehouse1.add_item(self.item3)
		self.warehouse1.add_item(self.item4)
		self.warehouse1.add_item(self.item5)

		
		self.assertEqual(self.warehouse1.get_max_stock(), self.item3, "Max stock is Item 3")


	# Check to see whether the warehouse correctly return the item with the highest price
	def test_warehouse_max_price(self):
		self.warehouse1.add_item(self.item1)
		self.warehouse1.add_item(self.item2)
		self.warehouse1.add_item(self.item3)
		self.warehouse1.add_item(self.item4)
		self.warehouse1.add_item(self.item5)

		self.assertEqual(self.warehouse1.get_max_price(), self.item1, "Max price is Item 1")
		
		

def main():
	unittest.main()

if __name__ == "__main__":
	main()