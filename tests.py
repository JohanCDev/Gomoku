#!/usr/bin/env python3
import builtins
from unittest import mock
from src.ParseInput import ParseInput


def run_tests():
    run_parser_tests()


def run_parser_tests():
    test_parser_init()
    test_parser_ask_input()
    test_parser_parse_single_input()
    test_parser_parse_double_input()
    test_parser_parse_long_input()


def test_parser_init():
    parser = ParseInput()
    assert parser.getParsedInput() == [], parser.getInput() == ""


def test_parser_ask_input():
    parser = ParseInput()
    parser.setInput("Input")
    assert parser.getInput() == "Input"


def test_parser_parse_single_input():
    parser = ParseInput()
    parser.setInput("Input")
    assert parser.getParsedInput() == ["Input"]


def test_parser_parse_double_input():
    parser = ParseInput()
    parser.setInput("Input test")
    assert parser.getParsedInput() == ["Input", "test"]


def test_parser_parse_long_input():
    parser = ParseInput()
    parser.setInput('Input test because we need to test it you know I make this '
                    'test and we will know if it works')
    assert parser.getParsedInput() == ["Input", "test", "because", "we", "need", "to", "test", "it", "you", "know",
                                       "I", "make", "this", "test", "and", "we", "will", "know", "if", "it",
                                       "works"]
