#!/usr/bin/env python3
import platform
import resource


def limitMemory(maxsize: int):
    if platform.system() == "Linux":
        soft, hard = resource.getrlimit(resource.RLIMIT_AS)
        resource.setrlimit(resource.RLIMIT_AS, (maxsize, hard))
    elif platform.system() == "Darwin" or platform.system() == "Windows":
        raise OSError("Memory limit unhandled on " + platform.system())
