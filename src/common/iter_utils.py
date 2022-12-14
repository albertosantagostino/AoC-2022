#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def slide(container, nn):
    for idx in range(len(container) - nn + 1):
        yield container[idx:idx + nn], idx