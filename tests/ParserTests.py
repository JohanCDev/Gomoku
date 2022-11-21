#!/usr/bin/env python3
from src.ParseInput import ParseInput


def run_parser_tests():
    test_parser_init()
    test_parser_ask_input()
    test_parser_parse_single_input()
    test_parser_parse_double_input()
    test_parser_parse_long_input()


def test_parser_init():
    parser = ParseInput()
    assert parser.get_parsed_input() == [], parser.get_input() == ""


def test_parser_ask_input():
    parser = ParseInput()
    parser.set_input("Input")
    assert parser.get_input() == "Input"


def test_parser_parse_single_input():
    parser = ParseInput()
    parser.set_input("Input")
    assert parser.get_parsed_input() == ["Input"]


def test_parser_parse_double_input():
    parser = ParseInput()
    parser.set_input("Input test")
    assert parser.get_parsed_input() == ["Input", "test"]


def test_parser_parse_long_input():
    parser = ParseInput()
    parser.set_input('Input test because we need to test it you know I make this '
                    'test and we will know if it works')
    assert parser.get_parsed_input() == ["Input", "test", "because", "we", "need", "to", "test", "it", "you", "know",
                                       "I", "make", "this", "test", "and", "we", "will", "know", "if", "it",
                                       "works"]
