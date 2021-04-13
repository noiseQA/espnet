#!/usr/bin/env python3
# encoding: utf-8

# Copyright 2017 Johns Hopkins University (Shinji Watanabe)
#  Apache 2.0  (http://www.apache.org/licenses/LICENSE-2.0)

import argparse
import codecs
import json
import logging
import re

from espnet.utils.cli_utils import get_commandline_args


def get_parser():
    parser = argparse.ArgumentParser(
        description="convert ASR recognized json to text",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument("json", type=str, help="json files")
    parser.add_argument("base", type=str, help="base name")
    return parser

if __name__ == "__main__":
    args = get_parser().parse_args()

    with codecs.open(args.json, "r", encoding="utf-8") as f:
        j = json.load(f)

    for idx in range(1,len(j["utts"])+1):
        x = args.base + "-" + str(idx)
        try:
            seq = j["utts"][x]["output"][0]["rec_text"]
            seq = seq.replace(u"\u2581", u" ")
            seq = seq.replace("<eos>", "")
            seq = re.sub(' +', ' ',seq).lstrip(" ")
        except:
            seq = ""
        print(seq)
