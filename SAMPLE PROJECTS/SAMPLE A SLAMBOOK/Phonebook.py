#!/usr/bin/env python3
"""
Phonebook CLI

Simple phonebook application with add/list/search/delete and JSON storage.

Usage:
	python Phonebook.py

Data is persisted to `phonebook.json` in the current working directory when saved.
"""
from __future__ import annotations

import json
import os
from dataclasses import dataclass, asdict, field
from typing import Dict, List


@dataclass
class Contact:
	name: str
	numbers: List[str] = field(default_factory=list)

	def add_number(self, number: str) -> bool:
		number = number.strip()
		if number and number not in self.numbers:
			self.numbers.append(number)
			return True
		return False

	def remove_number(self, number: str) -> bool:
		try:
			self.numbers.remove(number)
			return True
		except ValueError:
			return False


class PhoneBook:
	def __init__(self) -> None:
		self.contacts: Dict[str, Contact] = {}

	def add_contact(self, name: str, number: str) -> None:
		name = name.strip()
		if not name:
			raise ValueError("Name cannot be empty")
		if name in self.contacts:
			self.contacts[name].add_number(number)
		else:
			c = Contact(name=name, numbers=[number.strip()])
			self.contacts[name] = c

	def remove_contact(self, name: str) -> bool:
		if name in self.contacts:
			del self.contacts[name]
			return True
		return False

	def update_contact(self, name: str, new_numbers: List[str]) -> bool:
		if name in self.contacts:
			self.contacts[name].numbers = [n.strip() for n in new_numbers if n.strip()]
			return True
		return False

	def find_contacts(self, query: str) -> List[Contact]:
		q = query.lower().strip()
		if not q:
			return list(self.contacts.values())
		return [c for c in self.contacts.values() if q in c.name.lower() or any(q in n for n in c.numbers)]

	def list_contacts(self) -> List[Contact]:
		return sorted(self.contacts.values(), key=lambda c: c.name.lower())

	def to_dict(self) -> Dict[str, List[str]]:
		return {name: c.numbers for name, c in self.contacts.items()}

	def save_to_file(self, path: str) -> None:
		with open(path, "w", encoding="utf-8") as f:
			json.dump(self.to_dict(), f, indent=2)

	def load_from_file(self, path: str) -> None:
		if not os.path.exists(path):
			return
		with open(path, "r", encoding="utf-8") as f:
			data = json.load(f)
		self.contacts = {name: Contact(name=name, numbers=nums) for name, nums in data.items()}


def main() -> None:
	import argparse

	parser = argparse.ArgumentParser(description="Simple Phonebook CLI")
	parser.add_argument("--db", default="phonebook.json", help="path to phonebook JSON file")
	args = parser.parse_args()

	pb = PhoneBook()
	pb.load_from_file(args.db)

	def menu() -> None:
		print("\nPhonebook — choose an option:")
		print("1) List contacts")
		print("2) Add contact")
		print("3) Search contacts")
		print("4) Remove contact")
		print("5) Save")
		print("6) Load")
		print("7) Exit")

	while True:
		try:
			menu()
			choice = input("> ")
			if choice == "1":
				for c in pb.list_contacts():
					print(f"- {c.name}: {', '.join(c.numbers) if c.numbers else '(no numbers)'}")
			elif choice == "2":
				name = input("Name: ").strip()
				number = input("Number: ").strip()
				try:
					pb.add_contact(name, number)
					print("Saved.")
				except ValueError as e:
					print(e)
			elif choice == "3":
				q = input("Query (name or number): ")
				results = pb.find_contacts(q)
				if not results:
					print("No contacts found.")
				for c in results:
					print(f"- {c.name}: {', '.join(c.numbers)}")
			elif choice == "4":
				name = input("Name to remove: ")
				if pb.remove_contact(name):
					print("Removed.")
				else:
					print("Contact not found.")
			elif choice == "5":
				pb.save_to_file(args.db)
				print(f"Saved to {args.db}")
			elif choice == "6":
				pb.load_from_file(args.db)
				print(f"Loaded from {args.db}")
			elif choice == "7":
				print("Goodbye.")
				break
			else:
				print("Unknown choice")
		except (KeyboardInterrupt, EOFError):
			print("\nGoodbye.")
			break


if __name__ == "__main__":
	main()
