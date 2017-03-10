#!/usr/bin/env python3

import tweepy
import random
from credentials import keys
from freshness import *

class TwitterAPI:
    def __init__(self):
        consumer_key = keys['consumer_key']
        consumer_secret = keys['consumer_secret']
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        access_token = keys['access_token']
        access_token_secret = keys['access_secret']
        auth.set_access_token(access_token, access_token_secret)
        self.api = tweepy.API(auth)

    def tweet(self, message):
        self.api.update_status(status=message)


    def trumpReply(self, new_trump_id, message):
        self.api.update_status(status=message,in_reply_to_status_id=new_trump_id)


    def scrapeTrump(self):
        s = self.api.user_timeline(user_id='@realdonaldtrump',count=1)
        new_trump_id = s.id
        last_log_id = setLtweet(new_trump_id)
        return new_trump_id, last_log_id


def compareIDs():
    new_trump_id, last_log_id = twitter.scrapeTrump()
    if new_trump_id > last_log_id:
        message = insult_generator()
        twitter.trumpReply(new_trump_id, message)
        logLtweet(new_trump_id)
    else:
        pass


def insult_generator():
    column1 = ["artless",
               "bawdy",
               "beslubbering",
               "bootless",
               "churlish",
               "cockered",
               "clouted",
               "craven",
               "currish",
               "dankish",
               "dissembling",
               "droning",
               "errant",
               "fawning",
               "fobbing",
               "froward",
               "frothy",
               "gleeking",
               "goatish",
               "gorbellied",
               "impertinent",
               "infectious",
               "jarring",
               "loggerheaded",
               "lumpish",
               "mammering",
               "mangled",
               "mewling",
               "paunchy",
               "pribbling",
               "puking",
               "puny",
               "qualling",
               "rank",
               "reeky",
               "roguish",
               "ruttish",
               "saucy",
               "spleeny",
               "spongy",
               "surly",
               "tottering",
               "unmuzzled",
               "vain",
               "venomed",
               "villanous",
               "warped",
               "wayward",
               "weedy",
               "yeasty",
               "cullionly",
               "fusty",
               "caluminous",
               "wimpled",
               "burly-boned",
               "misbegotten",
               "odiferous",
               "poisonous",
               "fishified",
               "wart-necked"]
    column2 = ["base-court",
               "bat-fowling",
               "beef-witted",
               "beetle-headed",
               "boil-brained",
               "clapper-clawed",
               "clay-brained",
               "common-kissing",
               "crook-pated",
               "dismal-dreaming",
               "dizzy-eyed",
               "doghearted",
               "dread-bolted",
               "earth-vexing",
               "elf-skinned",
               "fat-kidneyed",
               "fen-sucked",
               "flap-mouthed",
               "fly-bitten",
               "folly-fallen",
               "fool-born",
               "full-gorged",
               "guts-griping",
               "half-faced",
               "hasty-witted",
               "hedge-born",
               "hell-hated",
               "idle-headed",
               "ill-breeding",
               "ill-nurtured",
               "knotty-pated",
               "milk-livered",
               "motley-minded",
               "onion-eyed",
               "plume-plucked",
               "pottle-deep",
               "pox-marked",
               "reeling-ripe",
               "rough-hewn",
               "rude-growing",
               "rump-fed",
               "shard-borne",
               "sheep-biting",
               "spur-galled",
               "swag-bellied",
               "tardy-gaited",
               "tickle-brained",
               "toad-spotted",
               "unchin-snouted",
               "weather-bitten",
               "whoreson",
               "malmsey-nosed",
               "rampallian",
               "lily-livered",
               "scurvy-valiant",
               "brazen-faced",
               "unwash'd",
               "bunch-back'd",
               "leaden-footed",
               "muddy-mettled",
               "pigeon-liver'd",
               "scale-sided"]
    column3 = ["apple-john",
               "baggage",
               "barnacle",
               "bladder",
               "boar-pig",
               "bugbear",
               "bum-bailey",
               "canker-blossom",
               "clack-dish",
               "clotpole",
               "coxcomb",
               "codpiece",
               "death-token",
               "dewberry",
               "flap-dragon",
               "flax-wench",
               "flirt-gill",
               "foot-licker",
               "fustilarian",
               "giglet",
               "gudgeon",
               "haggard",
               "harpy",
               "hedge-pig",
               "horn-beast",
               "hugger-mugger",
               "joithead",
               "lewdster",
               "lout",
               "maggot-pie",
               "malt-worm",
               "mammet",
               "measle",
               "minnow",
               "miscreant",
               "moldwarp",
               "mumble-news",
               "nut-hook",
               "pigeon-egg",
               "pignut",
               "puttock",
               "pumpion",
               "ratsbane",
               "scut",
               "skainsmate",
               "strumpet",
               "varlot",
               "vassal",
               "whey-face",
               "wagtail",
               "knave",
               "blind-worm",
               "poppinjay",
               "scullian",
               "jolt-head",
               "malcontent",
               "devil-monk",
               "toad",
               "rascal",
               "basket-cockle"]
    c1 = random.randint(0, 59)
    c2 = random.randint(0, 61)
    c3 = random.randint(0, 59)

    insult = ".@realdonaldtrump Thou " + column1[c1] + " " + column2[c2] + " " + column3[c3] + "!"
    return insult


if __name__ == "__main__":
    twitter = TwitterAPI()
    compareIDs()
